class ParseError(Exception):
    """Custom error for parsing issues"""
    def __init__(self, message, line_num=None, line_content=None, prev_line=None, next_line=None):
        super().__init__(message)
        self.line_num = line_num
        self.line_content = line_content
        self.prev_line = prev_line
        self.next_line = next_line

class SeedParser:
    """Parses .seed files into Python data structures"""
    
    def __init__(self):
        self.valid_types = {'text', 'num', 'bool'}

    def parse(self, input_text: str) -> dict:
        try:
            spec = {
                'models': [],
                'screens': []
            }
            
            lines = input_text.strip().splitlines()
            current_block = None
            
            for line_num, line in enumerate(lines, 1):
                line = line.strip()
                if not line or line.startswith('//'): 
                    continue
                
                try:
                    if line.startswith('model'):
                        current_block = self._parse_model(line)
                        spec['models'].append(current_block)
                    elif line.startswith('screen'):
                        screen = self._parse_screen(line)
                        spec['screens'].append(screen)
                    elif current_block and line != '}':
                        if line.strip():
                            self._parse_field(line, current_block)
                except ParseError as e:
                    # Get context lines
                    prev_line = lines[line_num-2] if line_num > 1 else None
                    next_line = lines[line_num] if line_num < len(lines) else None
                    raise ParseError(
                        str(e),
                        line_num=line_num,
                        line_content=line,
                        prev_line=prev_line,
                        next_line=next_line
                    )
                
            return spec
            
        except Exception as e:
            if isinstance(e, ParseError):
                raise
            raise ParseError(f"Failed to parse spec: {str(e)}")

    def _parse_model(self, line: str) -> dict:
        """Parse model declaration"""
        try:
            parts = line.split()
            if len(parts) < 2:
                raise ParseError("Invalid model declaration")
            
            model_name = parts[1].strip('{').strip()
            if not model_name.isidentifier():
                raise ParseError(f"Invalid model name: {model_name}")
                
            return {'name': model_name, 'fields': []}
            
        except Exception as e:
            raise ParseError(f"Invalid model declaration: {str(e)}")

    def _parse_screen(self, line: str) -> dict:
        """Parse screen declaration"""
        try:
            parts = line.split()
            if len(parts) != 4 or parts[2] != 'using':
                raise ParseError("Invalid screen declaration - expected 'screen Name using Model'")
                
            screen_name = parts[1]
            model_name = parts[3]
            
            if not screen_name.isidentifier():
                raise ParseError(f"Invalid screen name: {screen_name}")
            if not model_name.isidentifier():
                raise ParseError(f"Invalid model reference: {model_name}")
                
            return {
                'name': screen_name,
                'model': model_name
            }
            
        except Exception as e:
            raise ParseError(f"Invalid screen declaration: {str(e)}")

    def _parse_field(self, line: str, model: dict) -> None:
        """Parse model field"""
        try:
            parts = line.split()
            if len(parts) < 2:
                raise ParseError(f"Invalid field declaration in line: '{line}'")
                
            field_name = parts[0]
            field_type = parts[1]
            
            if not field_name.isidentifier():
                raise ParseError(f"Invalid field name '{field_name}' in line: '{line}'")
            
            # Field type can be either a basic type or a model reference
            field = {
                'name': field_name,
                'type': field_type,
                'default': None,
                'is_reference': field_type not in self.valid_types
            }
            
            # Handle default value if present
            if len(parts) > 2:
                if parts[2] != '=':
                    raise ParseError(f"Expected '=' after type, got '{parts[2]}' in line: '{line}'")
                if len(parts) < 4:
                    raise ParseError(f"Missing default value after '=' in line: '{line}'")
                field['default'] = parts[3]
                
                # Handle 'as title' after default value
                if len(parts) > 4:
                    if parts[4:] != ['as', 'title']:
                        raise ParseError(f"Invalid syntax after default value in line: '{line}'")
            # Handle 'as title' without default value        
            elif len(parts) > 2:
                if parts[2:] != ['as', 'title']:
                    raise ParseError(f"Invalid syntax after type in line: '{line}'")
                
            model['fields'].append(field)
            
        except Exception as e:
            if isinstance(e, ParseError):
                raise
            raise ParseError(f"Invalid field declaration in line: '{line}' - {str(e)}")
