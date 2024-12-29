class ParseError(Exception):
    """Custom error for parsing issues"""
    pass

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
            
            current_block = None
            for line_num, line in enumerate(input_text.strip().splitlines(), 1):
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
                    raise ParseError(f"Line {line_num}: {str(e)}")
                
            return spec
            
        except Exception as e:
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
                raise ParseError("Invalid field declaration")
                
            field_name = parts[0]
            field_type = parts[1]
            
            if not field_name.isidentifier():
                raise ParseError(f"Invalid field name: {field_name}")
            # Allow both basic types and model references
            if field_type not in self.valid_types and not field_type.isidentifier():
                raise ParseError(f"Invalid field type: {field_type}")
                
            field = {
                'name': field_name,
                'type': field_type,
                'default': None
            }
            
            # Handle default value if present
            if len(parts) > 2 and parts[2] == '=':
                if len(parts) < 4:
                    raise ParseError("Missing default value")
                field['default'] = parts[3]
                
            model['fields'].append(field)
            
        except Exception as e:
            raise ParseError(f"Invalid field declaration: {str(e)}")
