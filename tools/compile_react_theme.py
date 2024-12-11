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

def extract_theme_from_app_spec(spec: dict) -> dict:
    """Extract theme configuration from app specification"""
    if 'ui' not in spec:
        return {}
        
    ui_config = spec['ui']
    
    # Case 1: Direct theme definition
    if 'theme' in ui_config and isinstance(ui_config['theme'], dict):
        theme_spec = ui_config['theme']
        
    # Case 2: Theme reference
    elif 'theme' in ui_config and isinstance(ui_config['theme'], str):
        theme_name = ui_config['theme']
        theme_spec = load_predefined_theme(theme_name)
    else:
        theme_spec = load_predefined_theme('default')
    
    # Apply any overrides
    if 'overrides' in ui_config:
        theme_spec = apply_theme_overrides(theme_spec, ui_config['overrides'])
        
    return theme_spec

def load_predefined_theme(theme_name: str) -> dict:
    """Load a predefined theme from stdlib"""
    themes_file = Path(__file__).parent.parent / "src" / "stdlib" / "themes.seed"
    themes = parse_seed_file(themes_file)
    return themes.get(theme_name, themes['default'])

def apply_theme_overrides(theme_spec: dict, overrides: dict) -> dict:
    """Apply theme overrides to base theme"""
    from copy import deepcopy
    result = deepcopy(theme_spec)
    
    for path, value in overrides.items():
        keys = path.split('.')
        target = result
        for key in keys[:-1]:
            target = target.setdefault(key, {})
        target[keys[-1]] = value
        
    return result

def main():
    parser = argparse.ArgumentParser(description='Compile Seed theme to React')
    parser.add_argument('spec_file', type=Path, help='Input .seed file')
    parser.add_argument('--output', type=Path, default=Path('src/theme'),
                      help='Output directory (default: src/theme)')
    
    args = parser.parse_args()
    
    if not args.spec_file.exists():
        print(f"Error: Spec file {args.spec_file} not found")
        sys.exit(1)
    
    # Parse app specification
    app_spec = parse_seed_file(args.spec_file)
    
    # Extract theme configuration
    theme_spec = extract_theme_from_app_spec(app_spec)
    
    # Create output directory
    args.output.mkdir(parents=True, exist_ok=True)
    
    # Generate CSS
    css = generate_css(theme_spec)
    css_file = args.output / "theme.css"
    css_file.write_text(css)
    
    # Generate Theme Context
    context = generate_theme_context(theme_spec)
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
