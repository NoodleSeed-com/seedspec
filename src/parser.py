from typing import Dict, Any
import re
from pathlib import Path

class SeedParseError(Exception):
    """Raised when parsing a .seed file fails"""
    pass

def parse_seed_file(file_path: Path) -> Dict[str, Any]:
    """Parse a .seed file into a Python dictionary structure
    
    Args:
        file_path: Path to the .seed file
        
    Returns:
        Dict containing the parsed theme structure
        
    Raises:
        SeedParseError: If parsing fails
    """
    try:
        with open(file_path) as f:
            content = f.read()
            
        # Remove comments
        content = re.sub(r'#.*$', '', content, flags=re.MULTILINE)
        
        # Track current context for nested structures
        result = {}
        current_context = [result]
        current_keys = []
        block_count = 0  # Track opening/closing blocks
        
        # Process each non-empty line
        for line_num, line in enumerate(content.split('\n'), 1):
            line = line.strip()
            if not line:
                continue
                
            # Handle block start
            if line.endswith('{'):
                block_count += 1
                key = line.split('{')[0].strip()
                if key.startswith('theme'):
                    # Handle theme declaration
                    parts = key.split()
                    theme_name = parts[1]
                    current_context[-1][theme_name] = {}
                    current_context.append(current_context[-1][theme_name])
                    current_keys.append(theme_name)
                else:
                    # Handle regular block
                    current_context[-1][key] = {}
                    current_context.append(current_context[-1][key])
                    current_keys.append(key)
                    
            # Handle block end
            elif line == '}':
                block_count -= 1
                if block_count < 0:
                    raise SeedParseError(f"Unexpected closing brace on line {line_num}")
                current_context.pop()
                current_keys.pop()
                
            # Handle key-value pairs
            elif ':' in line:
                key, value = line.split(':', 1)
                key = key.strip()
                value = value.strip().strip(',')  # Remove trailing commas too
                
                # Convert value types
                if value.startswith('"') and value.endswith('"'):
                    value = value[1:-1].strip()  # Strip quotes and whitespace
                elif value.lower() == 'true':
                    value = True
                elif value.lower() == 'false':
                    value = False
                elif value.replace('.','',1).isdigit():
                    value = float(value) if '.' in value else int(value)
                elif not value:  # Handle empty values
                    value = ""
                    
                current_context[-1][key] = value
                
        # Check for unclosed blocks
        if block_count > 0:
            raise SeedParseError(f"Unclosed blocks: missing {block_count} closing braces")
                
        # Check for unclosed blocks
        if block_count > 0:
            raise SeedParseError(f"Unclosed blocks: missing {block_count} closing braces")
                
        return result
        
    except Exception as e:
        raise SeedParseError(f"Failed to parse {file_path}: {str(e)}")
