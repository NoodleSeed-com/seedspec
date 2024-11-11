import os
import markdown
from weasyprint import HTML, CSS
from bs4 import BeautifulSoup

def convert_md_to_pdf(output_filename='documentation.pdf'):
    # Initialize empty string to store all content
    all_content = ""
    
    # First add README
    if os.path.exists('README.md'):
        with open('README.md', 'r', encoding='utf-8') as f:
            all_content += f.read() + "\n\n"
    
    # Walk through docs directory
    for root, dirs, files in os.walk('docs'):
        for file in files:
            if file.endswith('.md'):
                file_path = os.path.join(root, file)
                with open(file_path, 'r', encoding='utf-8') as f:
                    # Add a header with the file path
                    all_content += f"\n\n## {file_path}\n\n"
                    all_content += f.read() + "\n\n"
                    all_content += "---\n\n"  # Add separator between files
    
    # Convert markdown to HTML
    html = markdown.markdown(all_content)
    
    # Add some basic styling
    css = CSS(string='''
        body { 
            font-family: Arial, sans-serif;
            line-height: 1.6;
            margin: 40px;
        }
        h1 { color: #2c3e50; }
        h2 { color: #34495e; }
        code { 
            background: #f8f9fa;
            padding: 2px 5px;
            border-radius: 3px;
        }
        pre {
            background: #f8f9fa;
            padding: 15px;
            border-radius: 5px;
        }
        hr {
            margin: 30px 0;
            border: none;
            border-top: 1px solid #ddd;
        }
    ''')
    
    # Create PDF
    HTML(string=html).write_pdf(output_filename, stylesheets=[css])
    
    print(f"PDF created successfully: {output_filename}")

if __name__ == "__main__":
    try:
        convert_md_to_pdf()
    except Exception as e:
        print(f"Error creating PDF: {str(e)}")
