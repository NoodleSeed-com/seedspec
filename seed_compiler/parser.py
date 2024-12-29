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
            # Stricter type validation - must be either a valid type or a model reference
            if field_type not in self.valid_types:
                if not field_type.isidentifier():
                    raise ParseError(f"Invalid field type: {field_type}")
                
            field = {
                'name': field_name,
                'type': field_type,
                'default': None,
                'constraints': {}
            }

            # Parse constraints if present
            if '{' in line:
                constraint_start = line.index('{')
                constraint_end = line.rindex('}')
                constraint_str = line[constraint_start+1:constraint_end]
                
                for constraint in constraint_str.split(','):
                    if ':' in constraint:
                        key, value = constraint.split(':')
                        key = key.strip()
                        value = value.strip()
                        
                        # Convert numeric constraints
                        if key in ('min', 'max'):
                            value = int(value) if field_type == 'num' else value
                        elif key == 'pattern':
                            value = value.strip('"\'')
                            
                        field['constraints'][key] = value
            
            # Handle default value if present
            if len(parts) > 2 and parts[2] == '=':
                if len(parts) < 4:
                    raise ParseError("Missing default value")
                field['default'] = parts[3]
                
            model['fields'].append(field)
            
        except Exception as e:
            raise ParseError(f"Invalid field declaration: {str(e)}")
