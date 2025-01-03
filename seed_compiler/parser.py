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
        self.valid_types = {'text', 'num', 'bool', 'email'}

    def parse(self, input_text: str) -> dict:
        try:
            spec = {
                'models': [],
                'screens': []
            }
            
            lines = input_text.strip().splitlines()
            block_stack = []  # Track block hierarchy (app, model, etc)
            brace_stack = []  # Track opening braces and their line numbers
            
            for line_num, line in enumerate(lines, 1):
                # Remove inline comments and strip whitespace
                line = line.split('//')[0].strip()
                if not line:
                    continue
                
                try:
                    # Track opening braces and block types
                    if '{' in line:
                        brace_stack.append((line_num, line))
                        if line.startswith('app'):
                            # Parse app declaration
                            parts = line.split('"')
                            if len(parts) != 3:
                                raise ParseError("Invalid app declaration - expected 'app Name \"Title\" {'")
                            app_name = parts[0].split()[1]
                            app_title = parts[1]
                            if not app_name.isidentifier():
                                raise ParseError(f"Invalid app name: {app_name}")
                            if not app_title.strip():
                                raise ParseError("App title cannot be empty")
                            if app_name in spec.get('models', []) or app_name in spec.get('screens', []):
                                raise ParseError(f"Duplicate name: {app_name}")
                            spec['app'] = {'name': app_name, 'title': app_title}
                            block_stack.append('app')
                        elif line.startswith('model'):
                            if 'app' not in block_stack:
                                raise ParseError("Model must be defined inside app block")
                            model = self._parse_model(line)
                            if any(m['name'] == model['name'] for m in spec['models']):
                                raise ParseError(f"Duplicate model name: {model['name']}")
                            spec['models'].append(model)
                            block_stack.append('model')
                    
                    # Track closing braces
                    elif line == '}':
                        if not brace_stack:
                            raise ParseError("Unexpected closing brace - no matching opening brace found")
                        opening_line_num, opening_line = brace_stack.pop()
                        if block_stack:
                            block_stack.pop()
                    
                    # Handle screen declarations
                    elif line.startswith('screen'):
                        if 'app' not in block_stack:
                            raise ParseError("Screen must be defined inside app block")
                        screen = self._parse_screen(line)
                        if any(s['name'] == screen['name'] for s in spec['screens']):
                            raise ParseError(f"Duplicate screen name: {screen['name']}")
                        spec['screens'].append(screen)
                    
                    # Handle model fields
                    elif block_stack and block_stack[-1] == 'model' and line.strip():
                        current_model = spec['models'][-1]
                        self._parse_field(line, current_model)
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
                
            # Check for unclosed braces at end of parsing
            if brace_stack:
                last_brace = brace_stack[-1]
                raise ParseError(f"Unclosed brace from line {last_brace[0]}: {last_brace[1]}")
            
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
                raise ParseError(f"Field declaration must have at least a name and type")
                
            field_name = parts[0]
            field_type = parts[1]
            
            if not field_name.isidentifier():
                raise ParseError(f"'{field_name}' is not a valid field name")
            
            # Check if type is a basic type or a valid model reference
            if field_type not in self.valid_types:
                # For model references, only allow simple identifiers without underscores
                if not field_type.isidentifier() or '_' in field_type:
                    raise ParseError(f"'{field_type}' is not a valid type")
            
            field = {
                'name': field_name,
                'type': field_type,
                'default': None,
                'is_reference': field_type not in self.valid_types
            }
            
            # Handle 'as title' syntax first
            remaining_parts = parts[2:]
            if remaining_parts and remaining_parts[0:2] == ['as', 'title']:
                field['is_title'] = True
                remaining_parts = remaining_parts[2:]
            
            # Then handle default value if present
            if remaining_parts:
                if remaining_parts[0] != '=':
                    raise ParseError(f"Expected '=' for default value, got '{remaining_parts[0]}'")
                if len(remaining_parts) < 2:
                    raise ParseError(f"Missing value after '='")
                default_value = remaining_parts[1].strip('"')  # Remove quotes if present
                
                # Validate default value based on field type
                if field_type == 'bool':
                    if default_value.lower() not in ['true', 'false']:
                        raise ParseError(f"Invalid default value for bool field: {default_value}")
                    field['default'] = default_value.lower()
                elif field_type == 'num':
                    try:
                        float(default_value)
                        field['default'] = default_value
                    except ValueError:
                        raise ParseError(f"Invalid default value for num field: {default_value}")
                else:
                    field['default'] = default_value
                
                # Check for any invalid tokens after default value
                if len(remaining_parts) > 2:
                    unexpected_tokens = ' '.join(remaining_parts[2:])
                    raise ParseError(f"Unexpected tokens after default value: '{unexpected_tokens}'")
                
            model['fields'].append(field)
            
        except Exception as e:
            if isinstance(e, ParseError):
                raise
            context = f"\nIn model '{model.get('name', 'unknown')}'\nParsing field: {line}"
            raise ParseError(f"{str(e)}{context}")
