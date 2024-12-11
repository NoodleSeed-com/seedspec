#!/usr/bin/env python3
from pathlib import Path
import json
import sys
import argparse
from src.parser import parse_seed_file

def generate_css(theme_spec: dict) -> str:
    """Generate CSS variables from theme spec"""
    css = [":root {"]
    
    def flatten(obj, prefix=""):
        for key, value in obj.items():
            if isinstance(value, dict):
                flatten(value, f"{prefix}{key}-")
            else:
                css.append(f"  --{prefix}{key}: {value};")
    
    flatten(theme_spec)
    css.append("}")
    
    return "\n".join(css)

def generate_theme_context(theme_spec: dict) -> str:
    """Generate React theme context"""
    return f"""import {{ createContext, useContext, ReactNode }} from 'react';

export const theme = {json.dumps(theme_spec, indent=2)} as const;

export type Theme = typeof theme;

const ThemeContext = createContext<Theme>(theme);

export function ThemeProvider({{ children }}: {{ children: ReactNode }}) {{
  return (
    <ThemeContext.Provider value={{theme}}>
      {{children}}
    </ThemeContext.Provider>
  );
}}

export function useTheme() {{
  return useContext(ThemeContext);
}}
"""

def main():
    parser = argparse.ArgumentParser(description='Compile Seed theme to React')
    parser.add_argument('theme_file', type=Path, help='Input theme.seed file')
    parser.add_argument('--theme', type=str, help='Theme name to compile')
    parser.add_argument('--output', type=Path, default=Path('src/theme'),
                      help='Output directory (default: src/theme)')
    
    args = parser.parse_args()
    
    if not args.theme_file.exists():
        print(f"Error: Theme file {args.theme_file} not found")
        sys.exit(1)
    
    # Parse theme file
    theme_spec = parse_seed_file(args.theme_file)
    
    # Use specified theme or first theme found
    theme_name = args.theme
    if not theme_name:
        theme_name = next(iter(theme_spec))
        print(f"No theme specified, using: {theme_name}")
    
    if theme_name not in theme_spec:
        print(f"Error: Theme '{theme_name}' not found in {args.theme_file}")
        print(f"Available themes: {', '.join(theme_spec.keys())}")
        sys.exit(1)
    
    # Create output directory
    args.output.mkdir(parents=True, exist_ok=True)
    
    # Generate CSS
    css = generate_css(theme_spec[theme_name])
    css_file = args.output / "theme.css"
    css_file.write_text(css)
    
    # Generate Theme Context
    context = generate_theme_context(theme_spec[theme_name])
    context_file = args.output / "ThemeContext.tsx"
    context_file.write_text(context)
    
    print(f"\nGenerated theme files in {args.output}/")
    print(f"- {css_file}")
    print(f"- {context_file}")
    
    print("\nTo use in your React app:")
    print("1. Import the theme provider:")
    print('   import { ThemeProvider } from "./theme/ThemeContext";')
    print('   import "./theme/theme.css";')
    print("\n2. Wrap your app:")
    print("   <ThemeProvider>")
    print("     <App />")
    print("   </ThemeProvider>")

if __name__ == "__main__":
    main()
