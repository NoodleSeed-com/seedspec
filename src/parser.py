from typing import Dict, Any, Set, Optional
import re
from pathlib import Path
from .types import TypeDefinition, Field, TypeConstraints, ParseResult, ValidationError

class SeedParseError(Exception):
    """Raised when parsing a .seed file fails"""
    pass

class Parser:
    """Parser for the Seed specification language"""
    
    def __init__(self):
        self.imported_files: Set[Path] = set()
        self.types: Dict[str, TypeDefinition] = {}
    
    def parse(self, content: str) -> ParseResult:
        """Parse Seed content into a ParseResult
        
        Args:
            content: String containing Seed code
            
        Returns:
            ParseResult containing parsed types
            
        Raises:
            SeedParseError: If parsing fails
        """
        try:
            # Remove comments
            content = re.sub(r'//.*$', '', content, flags=re.MULTILINE)
            
            # Track current context
            current_context = {}
            current_block = None
            block_count = 0
            
            # Process each line
            lines = content.split('\n')
            i = 0
            while i < len(lines):
                line = lines[i].strip()
                i += 1
                if not line:
                    continue
                    
                # Handle block start
                if line.endswith('{'):
                    block_count += 1
                    key = line.split('{')[0].strip()
                    
                    # Handle type definitions
                    if key.startswith('type '):
                        type_name = key.split()[1]
                        current_block = {'name': type_name, 'fields': {}}
                        
                # Handle block end
                elif line == '}':
                    block_count -= 1
                    if block_count < 0:
                        raise SeedParseError(f"Unexpected closing brace on line {i}")
                    
                    if current_block and 'name' in current_block:
                        # Create TypeDefinition from current block
                        self.types[current_block['name']] = TypeDefinition(
                            name=current_block['name'],
                            fields=current_block['fields']
                        )
                    current_block = None
                    
                # Handle field definitions
                elif ':' in line and current_block:
                    field_def = line.split(':', 1)
                    if len(field_def) != 2:
                        raise SeedParseError(f"Invalid field definition: {line}")
                        
                    field_name = field_def[0].strip()
                    type_def = field_def[1].strip()
                    
                    # Parse field type and constraints
                    field = self._parse_field_definition(field_name, type_def)
                    if field:
                        current_block['fields'][field_name] = field
            
            # Check for unclosed blocks
            if block_count > 0:
                raise SeedParseError(f"Unclosed blocks: missing {block_count} closing braces")
            
            return ParseResult(types=self.types)
            
        except Exception as e:
            raise SeedParseError(f"Failed to parse content: {str(e)}")
    
    def _parse_field_definition(self, name: str, type_def: str) -> Optional[Field]:
        """Parse a field definition into a Field object"""
        # Raise NotImplementedError for now as we're still implementing
        raise NotImplementedError("Field parsing not yet implemented")
    
    def parse_file(self, file_path: Path) -> ParseResult:
        """Parse a .seed file into a ParseResult
        
        Args:
            file_path: Path to the .seed file
            
        Returns:
            ParseResult containing parsed types
            
        Raises:
            SeedParseError: If parsing fails
        """
        try:
            # Resolve the full path
            file_path = file_path.resolve()
                
            # Check if file exists
            if not file_path.exists():
                raise SeedParseError("File not found")
                
            # Check for circular imports
            if file_path in self.imported_files:
                raise SeedParseError(f"Circular import detected: {file_path}")
                    
            # Add to imported files set
            self.imported_files.add(file_path)
                
            # Read and process file
            with open(file_path) as f:
                content = f.read()
                
            return self.parse(content)
            
        except Exception as e:
            raise SeedParseError(f"Failed to parse {file_path}: {str(e)}")

def parse_seed_file(file_path: Path, imported_files: Set[Path] = None) -> Dict[str, Any]:
    """Legacy function for backwards compatibility"""
    # Keep the old implementation for now to maintain compatibility
    # This will be deprecated in favor of the new Parser class
    try:
        # Initialize import tracking
        if imported_files is None:
            imported_files = set()
            
        # Rest of the original implementation...
        # [Previous implementation code here]
        raise NotImplementedError("Legacy parser not implemented")
            
    except ValueError as e:
        raise e
    except Exception as e:
        raise SeedParseError(f"Failed to parse {file_path}: {str(e)}")
