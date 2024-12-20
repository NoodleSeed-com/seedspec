from typing import Dict, Any, Set
import re
from pathlib import Path

class SeedParseError(Exception):
    """Raised when parsing a .seed file fails"""
    pass

def parse_seed_file(file_path: Path, imported_files: Set[Path] = None) -> Dict[str, Any]:
    """Parse a .seed file into a Python dictionary structure
    
    Args:
        file_path: Path to the .seed file
        imported_files: Set of already imported files (prevents circular imports)
        
    Returns:
        Dict containing the parsed structure
        
    Raises:
        SeedParseError: If parsing fails
    """
    try:
        # Initialize import tracking
        if imported_files is None:
            imported_files = set()
            
        # Resolve the full path
        file_path = file_path.resolve()
            
        # Check if file exists
        if not file_path.exists():
            raise SeedParseError("Import file not found")
            
        # Check for circular imports
        if file_path in imported_files:
            raise SeedParseError(f"Circular import detected: {file_path}")
                
        # Add to imported files set
        imported_files.add(file_path)
            
        # Read and process file
        with open(file_path) as f:
            content = f.read()
            
        # Remove comments
        content = re.sub(r'//.*$', '', content, flags=re.MULTILINE)
        
        # Track current context
        result = {}
        current_context = [result]
        current_keys = []
        block_count = 0
        
        # Process each line
        lines = content.split('\n')
        i = 0
        while i < len(lines):
            line = lines[i].strip()
            i += 1
            if not line:
                continue
                
            # Handle imports
            import_match = re.match(r'import\s+"([^"]+)"', line)
            if import_match:
                import_path = import_match.group(1)
                
                # Handle stdlib imports
                if import_path.startswith('src/stdlib/'):
                    import_file = (Path(__file__).parent.parent / import_path).resolve()
                else:
                    # Resolve relative to current file
                    import_file = (file_path.parent / import_path).resolve()
                
                if not import_file.exists():
                    raise SeedParseError(f"Import file not found: {import_file}")
                    
                # Parse imported file and merge results
                imported_data = parse_seed_file(import_file, imported_files)
                result.update(imported_data)
                continue
                
            # Handle block start
            if line.endswith('{'):
                block_count += 1
                key = line.split('{')[0].strip()
                
                if key.startswith(('theme', 'component', 'app')):
                    parts = key.split()
                    if len(parts) < 2:
                        raise SeedParseError(f"Invalid {parts[0]} declaration, missing name")
                    
                    name = parts[1]
                    current_context[-1][name] = {}
                    
                    # Handle theme extension
                    if len(parts) > 2:
                        if parts[2] != "extends":
                            raise SeedParseError(f"Invalid theme syntax, expected 'extends' but got '{parts[2]}'")
                        if len(parts) < 4:
                            raise SeedParseError("Missing base theme name after extends")
                        current_context[-1][name]["extends"] = parts[3]
                    
                    current_context.append(current_context[-1][name])
                    current_keys.append(name)
                else:
                    # Block declarations don't use colons
                    if key.endswith(':'):
                        raise SeedParseError(f"Invalid block declaration: {key}, blocks should not end with colon")
                    current_context[-1][key] = {}
                    current_context.append(current_context[-1][key])
                    current_keys.append(key)
                    
            # Handle block end
            elif line == '}':
                block_count -= 1
                if block_count < 0:
                    raise SeedParseError(f"Unexpected closing brace on line {i}")
                current_context.pop()
                current_keys.pop()
                
            # Handle key-value pairs
            elif ':' in line:
                key, value = line.split(':', 1)
                key = key.strip().rstrip(':')  # Remove any trailing colon
                value = value.strip()
                
                # Validate theme tokens
                if isinstance(current_context[-1], dict) and any(k.startswith('theme ') for k in current_keys):
                    if not isinstance(value, (str, int, float, bool, list)) and not value.startswith('{'):
                        raise ValueError(f"Invalid theme token: {value}")
                
                # Convert value types
                if value.startswith('"') and value.endswith('"'):
                    # Handle quoted strings, including hex colors
                    value = value[1:-1].strip()
                elif value.startswith('#'):
                    # Preserve unquoted hex colors
                    value = value
                elif value.startswith('[') and value.endswith(']'):
                    # Convert string lists to actual lists and strip whitespace
                    value = [v.strip() for v in value[1:-1].split(',')]
                    # Filter out empty strings
                    value = [v for v in value if v]
                elif value.lower() == 'true':
                    value = True
                elif value.lower() == 'false':
                    value = False
                elif value.replace('.','',1).isdigit():
                    value = float(value) if '.' in value else int(value)
                elif not value:  # Handle empty values
                    value = ""

                # Store the value directly without any additional processing
                current_context[-1][key] = value
                
        # Check for unclosed blocks
        if block_count > 0:
            raise SeedParseError(f"Unclosed blocks: missing {block_count} closing braces")
        
        # Validate themes after parsing
        themes_to_process = {}
        for key, value in result.items():
            if key.startswith('theme '):
                theme_name = key.split(' ')[1]
                themes_to_process[theme_name] = value
                del result[key]
        
            # Process and validate themes
            for theme_name, theme_value in themes_to_process.items():
                # Check for required sections in themes before extension
                if 'button' not in theme_value and not ('extends' in theme_value):
                    raise ValueError(f"Missing required theme section: button in theme {theme_name}")
                
                result[theme_name] = theme_value
                
                # Handle theme extension
                if 'extends' in theme_value:
                    base_theme = theme_value['extends']
                    if base_theme not in result:
                        raise ValueError(f"Unknown base theme: {base_theme}")
                
                    # Check for circular extension
                    seen_themes = {theme_name}
                    current = base_theme
                    while current in result and 'extends' in result[current]:
                        if current in seen_themes:
                            raise ValueError("Circular theme extension")
                        seen_themes.add(current)
                        current = result[current]['extends']
                
                    # Deep merge base theme properties
                    base_props = result[base_theme].copy()
                    if 'extends' in base_props:
                        del base_props['extends']  # Don't copy extends property
                    
                    def deep_merge(base: dict, override: dict) -> dict:
                        """Deep merge two dictionaries"""
                        merged = base.copy()
                        for key, value in override.items():
                            if key in merged and isinstance(merged[key], dict) and isinstance(value, dict):
                                merged[key] = deep_merge(merged[key], value)
                            else:
                                merged[key] = value
                        return merged
                    
                    result[theme_name] = deep_merge(base_props, theme_value)
        
        return result
        
    except ValueError as e:
        raise e
    except Exception as e:
        raise SeedParseError(f"Failed to parse {file_path}: {str(e)}")
