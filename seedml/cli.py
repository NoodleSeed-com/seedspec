#!/usr/bin/env python3

from .generator import SeedMLGenerator
import argparse
import os
import sys

def main():
    parser = argparse.ArgumentParser(description='Generate full-stack application from SeedML specification')
    parser.add_argument('seed_file', help='Path to the .seed file')
    parser.add_argument('--api-key', help='Anthropic API key', default=os.getenv('ANTHROPIC_API_KEY'))
    
    args = parser.parse_args()
    
    if not args.api_key:
        print("Error: Anthropic API key not provided. Set ANTHROPIC_API_KEY environment variable or use --api-key")
        sys.exit(1)
    
    generator = SeedMLGenerator(args.api_key)
    generator.generate_application(args.seed_file)
    
    print(f"Application generated successfully!")

if __name__ == '__main__':
    main()
