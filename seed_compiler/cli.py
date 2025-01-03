import argparse
import sys
import os
from pathlib import Path
from .parser import SeedParser, ParseError
from .generator import Generator

def main(argv=None):
    """Main entry point for the seed compiler CLI"""
    if argv is None:
        argv = sys.argv[1:]
        
    parser = argparse.ArgumentParser(
        description='SeedSpec compiler - Generate React apps from .seed files'
    )
    
    parser.add_argument(
        'input',
        type=str,
        help='Input .seed file'
    )
    
    parser.add_argument(
        '-o', '--output',
        type=str,
        default='output',
        help='Output directory (default: ./output)'
    )
    
    parser.add_argument(
        '-v', '--verbose',
        action='store_true',
        help='Enable verbose output'
    )

    args = parser.parse_args(argv)

    try:
        # Validate input file
        input_path = Path(args.input)
        if not input_path.exists():
            print(f"Error: Input file not found: {args.input}", file=sys.stderr)
            sys.exit(1)
        if not input_path.suffix == '.seed':
            print(f"Warning: Input file does not have .seed extension: {args.input}")

        # Read input file
        if args.verbose:
            print(f"Reading input file: {args.input}")
        with open(input_path) as f:
            seed_content = f.read()

        # Parse spec
        if args.verbose:
            print("Parsing SeedSpec file...")
        parser = SeedParser()
        spec = parser.parse(seed_content)
        
        if args.verbose:
            print("Parsed spec:")
            print(f"- Models: {len(spec['models'])}")
            print(f"- Screens: {len(spec['screens'])}")

        # Create output directory
        output_path = Path(args.output)
        if args.verbose:
            print(f"Generating React app in: {output_path}")
        
        # Generate React app
        generator = Generator()
        generator.generate(spec, str(output_path))

        # Print success message
        print("\nSuccessfully generated React app!")
        print(f"\nTo run the app:")
        print(f"  cd {args.output}")
        print(f"  npm install")
        print(f"  npm start")
        sys.exit(0)

    except Exception as e:
        if isinstance(e, ParseError):
            print("\n🚫 Parse Error:", file=sys.stderr)
            print("\nContext:", file=sys.stderr)
            if e.prev_line:
                print(f"  Line {e.line_num-1}: {e.prev_line}", file=sys.stderr)
            print(f"→ Line {e.line_num}: {e.line_content}", file=sys.stderr)
            if e.next_line:
                print(f"  Line {e.line_num+1}: {e.next_line}", file=sys.stderr)
            print(f"\nDetails: {str(e)}", file=sys.stderr)
            if args.verbose:
                print("\nStack trace:", file=sys.stderr)
                import traceback
                traceback.print_exc()
        else:
            print(f"\n❌ Error: {str(e)}", file=sys.stderr)
            if args.verbose:
                print("\nStack trace:", file=sys.stderr)
                import traceback
                traceback.print_exc()
        sys.exit(1)

if __name__ == '__main__':
    main()
