import os
import subprocess
import fnmatch

def create_pdf(repo_root, output_filename):
    """
    Creates a PDF document from all text-based files in a repository.

    Args:
        repo_root: The root directory of the repository.
        output_filename: The name of the output PDF file.
    """
    print("Starting PDF creation...")
    combined_content = "---\ntitle: Seed Specification Language Documentation\n---\n\n"
    
    # First, process README.md as it contains the overview
    readme_path = os.path.join(repo_root, "README.md")
    if os.path.exists(readme_path):
        print(f"Processing README: {readme_path}")
        with open(readme_path, "r", encoding="utf-8") as f:
            combined_content += f"{f.read()}\n\n"

    # Then process other documentation files
    for root, _, files in os.walk(repo_root):
        files.sort()  # Process files in a consistent order
        for file in files:
            filepath = os.path.join(root, file)
            if should_include_file(filepath) and filepath != readme_path:
                try:
                    print(f"Processing file: {filepath}")
                    with open(filepath, "r", encoding="utf-8") as f:
                        file_content = f.read()
                    # Add a section header for each file
                    relative_path = os.path.relpath(filepath, repo_root)
                    combined_content += f"\n\n# {relative_path}\n\n{file_content}\n\n"
                    combined_content += "\n---\n"  # Add a separator between files
                except UnicodeDecodeError:
                    print(f"Skipping non-UTF-8 encoded file: {filepath}")

    with open("temp.txt", "w", encoding="utf-8") as temp_file:
        temp_file.write(combined_content)

    try:
        subprocess.run(
            [
                "pandoc",
                "temp.txt",
                "-o", output_filename,
                "--from", "markdown+yaml_metadata_block",
                "--pdf-engine=xelatex",
                "-V", "mainfont=DejaVu Sans",
                "-V", "monofont=DejaVu Sans Mono",
                "--highlight-style", "tango",
                "--toc",  # Add table of contents
                "--toc-depth=3",
                "-V", "geometry:margin=1in",
                "-V", "linkcolor:blue",
                "-V", "documentclass=report",
                "--standalone"
            ],
            check=True,
            capture_output=True,
            text=True
        )
        print(f"PDF created successfully: {output_filename}")
    except subprocess.CalledProcessError as e:
        print(f"Error during PDF creation: {e}")
        print(f"Pandoc stdout: {e.stdout}")
        print(f"Pandoc stderr: {e.stderr}")

    os.remove("temp.txt")

def should_include_file(filepath):
    """
    Checks if a file should be included in the PDF based on project relevance.

    Args:
        filepath: The path to the file.

    Returns:
        True if the file should be included, False otherwise.
    """
    # Define patterns for different types of content
    doc_patterns = ["*.md"]  # Documentation files
    source_patterns = [
        "src/*.py",         # Source code
        "src/stdlib/*.seed", # Standard library files
        "examples/*.seed",   # Example Seed files
    ]
    exclude_patterns = [
        "*/__pycache__/*",  # Compiled Python files
        "*/tests/*",        # Test files
        "*/.git/*",         # Git files
        "*/node_modules/*", # Node modules
        "create_pdf.py",    # This script itself
        "temp.txt",         # Temporary file
    ]

    # Check if file should be excluded
    if any(fnmatch.fnmatch(filepath, pattern) for pattern in exclude_patterns):
        return False

    # Include documentation files first
    if any(fnmatch.fnmatch(filepath, pattern) for pattern in doc_patterns):
        return True

    # Then include source code files
    if any(fnmatch.fnmatch(filepath, pattern) for pattern in source_patterns):
        return True

    return False

if __name__ == "__main__":
    repo_root = "."  # Current directory
    output_filename = "seedspec.pdf"
    create_pdf(repo_root, output_filename)
