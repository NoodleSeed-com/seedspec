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
                    name = parts[1]
                    current_context[-1][name] = {}
                    current_context.append(current_context[-1][name])
                    current_keys.append(name)
                else:
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
                key = key.strip()
                value = value.strip()
                
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
                
        # Check for unclosed blocks
        if block_count > 0:
            raise SeedParseError(f"Unclosed blocks: missing {block_count} closing braces")
                
        return result
        
    except Exception as e:
        raise SeedParseError(f"Failed to parse {file_path}: {str(e)}")
