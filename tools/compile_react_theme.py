#!/usr/bin/env python3
from pathlib import Path
import json
import sys
import argparse
from typing import Dict, Any, List, Optional

def compile_theme_tokens(theme: dict, token_path: str, mode: Optional[str] = None) -> str:
    """Compile theme tokens to Tailwind classes.
    
    Args:
        theme: Theme specification dictionary
        token_path: Dot-separated path to tokens (e.g., "button.primary")
        mode: Optional mode modifier (e.g., "dark")
    
    Returns:
        Space-separated string of Tailwind classes
    """
    def get_nested_value(d: dict, path: str) -> Any:
        """Get value from nested dict using dot notation"""
        keys = path.split('.')
        value = d
        for key in keys:
            if not isinstance(value, dict) or key not in value:
                return None
            value = value[key]
        return value
    
    def token_to_class(key: str, value: str, prefix: str = '') -> str:
        """Convert a single token to a Tailwind class"""
        # Handle special cases
        if key == 'ring':
            return f"{prefix}ring-{value.replace('.', '-')}"
        if key == 'shadow':
            return f"{prefix}shadow-{value}"
            
        # Standard cases
        mappings = {
            'bg': 'bg',
            'text': 'text',
            'border': 'border',
            'size': 'text',
            'color': 'text',
            'px': 'px',
            'py': 'py',
            'rounded': 'rounded',
            'font': 'font',
        }
        
        base = mappings.get(key, key)
        
        # Special value handling
        if isinstance(value, dict):
            # Handle responsive values
                if all(k in ['base', 'sm', 'md', 'lg', 'xl', '2xl'] for k in value.keys()):
                    classes = []
                    base_class = None
                    for breakpoint, val in value.items():
                        mapped_key = mappings.get(key, key)
                        if breakpoint == 'base':
                            base_class = f"{prefix}{mapped_key}-{val}"
                        else:
                            classes.append(f"{breakpoint}:{prefix}{mapped_key}-{val}")
                    # Put base class first, then sorted responsive classes
                    if base_class:
                        classes = [base_class] + sorted(classes)
                    return ' '.join(classes)
        return f"{prefix}{base}-{value.replace('.', '-')}"
    
    def process_tokens(tokens: dict, prefix: str = '') -> List[str]:
        """Process tokens recursively, handling nested structures"""
        classes = []
        
        for key, value in tokens.items():
            if isinstance(value, dict):
                # Handle variant prefixes (hover, focus, etc.)
                variant_prefix = f"{key}:" if key in ['hover', 'focus', 'disabled'] else ''
                # Handle responsive breakpoints
                breakpoint_prefix = f"{key}:" if key in ['sm', 'md', 'lg', 'xl', '2xl'] else ''
                classes.extend(process_tokens(value, f"{prefix}{variant_prefix}{breakpoint_prefix}"))
            else:
                classes.append(token_to_class(key, value, prefix))
                
        return classes
    
    # Get tokens for the specified path
    tokens = get_nested_value(theme, token_path)
    if not tokens:
        return ''
    
    # Process tokens with appropriate mode prefix
    mode_prefix = f"{mode}:" if mode else ''
    classes = process_tokens(tokens, mode_prefix)
    
    return ' '.join(sorted(classes))

# Add project root to Python path
project_root = Path(__file__).parent.parent
sys.path.append(str(project_root))

from src.parser import parse_seed_file

def generate_tailwind_config(theme_spec: dict) -> dict:
    """Generate Tailwind config from theme specification"""
    config = {"theme": {}}
    
    # Map colors with semantic scales
    if "colors" in theme_spec:
        config["theme"]["colors"] = theme_spec["colors"]
    
    # Map typography
    if "fontSize" in theme_spec:
        config["theme"]["fontSize"] = theme_spec["fontSize"]
    if "fontFamily" in theme_spec:
        config["theme"]["fontFamily"] = theme_spec["fontFamily"]
    if "fontWeight" in theme_spec:
        config["theme"]["fontWeight"] = theme_spec["fontWeight"]
    
    # Map spacing and sizing
    if "spacing" in theme_spec:
        config["theme"]["spacing"] = theme_spec["spacing"]
    if "borderRadius" in theme_spec:
        config["theme"]["borderRadius"] = theme_spec["borderRadius"]
    
    # Map screens for responsive design
    if "screens" in theme_spec:
        config["theme"]["screens"] = theme_spec["screens"]
    
    # Configure dark mode
    if "colors" in theme_spec and ("dark" in theme_spec["colors"] or "modes" in theme_spec["colors"]):
        config["darkMode"] = "class"
    
    return config

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
    parser = argparse.ArgumentParser(description='Compile Seed theme to Tailwind config')
    parser.add_argument('spec_file', type=Path, default=Path('examples/app-theme.seed'),
                      help='Input .seed file (default: examples/app-theme.seed)')
    parser.add_argument('--output', type=Path, default=Path('examples/react-theme'),
                      help='Output directory (default: examples/react-theme)')
    
    args = parser.parse_args()
    
    if not args.spec_file.exists():
        print(f"Error: Spec file {args.spec_file} not found")
        sys.exit(1)
    
    # Parse app specification
    app_spec = parse_seed_file(args.spec_file)
    
    # Extract theme configuration
    theme_spec = extract_theme_from_app_spec(app_spec)
    
    # Generate Tailwind config
    config = generate_tailwind_config(theme_spec)
    
    # Create output directory
    args.output.mkdir(parents=True, exist_ok=True)
    
    # Write Tailwind config
    config_file = args.output / "tailwind.config.js"
    config_content = f"module.exports = {json.dumps(config, indent=2)}"
    config_file.write_text(config_content)
    
    print(f"\nGenerated Tailwind config at {config_file}")
    print("\nTo use in your React app:")
    print("1. Install Tailwind CSS")
    print("2. Import the config:")
    print('   // tailwind.config.js')
    print('   module.exports = require("./theme/tailwind.config.js");')
    print("\n3. Use semantic classes in components:")
    print('   <div className="bg-primary-500 hover:bg-primary-600">')
    print('     <h1 className="text-lg font-bold text-gray-900 dark:text-white">')
    print('   </div>')

if __name__ == "__main__":
    main()
