import os
from fpdf import FPDF2 as FPDF
import markdown
import re
from bs4 import BeautifulSoup
import unicodedata
from pygments import highlight
from pygments.formatters import HtmlFormatter
from pygments.lexers import get_lexer_by_name, guess_lexer
from datetime import datetime

class RepoToPDF:
    def __init__(self):
        self.pdf = FPDF()
        self.pdf.add_page()
        self.pdf.set_font("Arial", size=12)
        self.current_y = 10
        self.page_width = 190
        
    def add_heading(self, text, level=1):
        sizes = {1: 24, 2: 18, 3: 14, 4: 12}
        self.pdf.set_font("Arial", "B", sizes.get(level, 12))
        self.pdf.cell(0, 10, text, ln=True)
        self.pdf.set_font("Arial", size=12)

    def clean_text(self, text):
        # Remove control characters and normalize unicode
        text = ''.join(char for char in text if unicodedata.category(char)[0] != 'C')
        text = unicodedata.normalize('NFKD', text)
        # Replace problematic characters
        text = text.encode('ascii', 'replace').decode('ascii')
        return text

    def add_text(self, text):
        cleaned_text = self.clean_text(text)
        self.pdf.multi_cell(0, 5, cleaned_text)
        
    def process_code(self, content, language=""):
        try:
            if language:
                lexer = get_lexer_by_name(language)
            else:
                lexer = guess_lexer(content)
            formatted = highlight(content, lexer, HtmlFormatter())
            soup = BeautifulSoup(formatted, 'html.parser')
            return soup.get_text()
        except:
            return content

    def process_markdown(self, content):
        html = markdown.markdown(content)
        soup = BeautifulSoup(html, 'html.parser')
        return soup.get_text()

    def process_file(self, filepath):
        self.add_heading(f"File: {filepath}", 2)
        
        try:
            with open(filepath, 'r', encoding='utf-8') as file:
                content = file.read()

            # Determine file type
            ext = os.path.splitext(filepath)[1].lower()
            
            if ext in ['.md', '.markdown']:
                processed_content = self.process_markdown(content)
            elif ext in ['.py', '.js', '.css', '.html']:
                processed_content = self.process_code(content, ext[1:])
            else:
                processed_content = content

            self.add_text(processed_content)
            self.pdf.add_page()

        except Exception as e:
            self.add_text(f"Error processing file: {str(e)}")

    def process_repository(self, repo_path):
        self.add_heading("Repository Documentation", 1)
        self.add_text(f"Generated on: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
        self.pdf.add_page()

        for root, dirs, files in os.walk(repo_path):
            # Skip .git directory
            if '.git' in dirs:
                dirs.remove('.git')
            
            # Skip virtual environments
            dirs[:] = [d for d in dirs if not d.startswith('venv') and not d.startswith('.env')]
            
            for file in files:
                if file.startswith('.'):
                    continue
                    
                filepath = os.path.join(root, file)
                self.process_file(filepath)

    def save(self, output_path):
        self.pdf.output(output_path)

def main():
    generator = RepoToPDF()
    repo_path = os.getcwd()  # Current directory
    generator.process_repository(repo_path)
    generator.save("repository_documentation.pdf")

if __name__ == "__main__":
    main()
