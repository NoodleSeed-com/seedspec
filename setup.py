from setuptools import setup, find_packages
import os
import subprocess
from distutils.command.build import build
from distutils.command.clean import clean

class AntlrBuild(build):
    def run(self):
        # Generate ANTLR parser files
        grammar_path = os.path.join('seed_compiler', 'SeedSpec.g4')
        output_path = os.path.join('seed_compiler')
        
        # Download ANTLR tool if needed
        antlr_jar = 'antlr-4.13.1-complete.jar'
        if not os.path.exists(antlr_jar):
            subprocess.run([
                'curl',
                '-O',
                f'https://www.antlr.org/download/{antlr_jar}'
            ], check=True)
        
        # Generate parser files
        subprocess.run([
            'java',
            '-jar',
            antlr_jar,
            '-Dlanguage=Python3',
            '-visitor',
            '-o', output_path,
            grammar_path
        ], check=True)
        
        # Run original build
        build.run(self)

class AntlrClean(clean):
    def run(self):
        # Remove generated parser files
        parser_files = [
            'SeedSpecLexer.py',
            'SeedSpecParser.py',
            'SeedSpecVisitor.py',
            'SeedSpec.interp',
            'SeedSpec.tokens'
        ]
        for f in parser_files:
            path = os.path.join('seed_compiler', f)
            if os.path.exists(path):
                os.remove(path)
        
        # Remove ANTLR jar
        if os.path.exists('antlr-4.13.1-complete.jar'):
            os.remove('antlr-4.13.1-complete.jar')
            
        # Run original clean
        clean.run(self)

setup(
    name="seed-compiler",
    version="0.1.0",
    packages=find_packages(),
    install_requires=[
        'jinja2>=3.1.2',
        'antlr4-python3-runtime>=4.13.1',
    ],
    entry_points={
        'console_scripts': [
            'seedc=seed_compiler.cli:main',
        ],
    },
    cmdclass={
        'build': AntlrBuild,
        'clean': AntlrClean,
    }
)
