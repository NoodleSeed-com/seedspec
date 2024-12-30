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
            in_app_block = False
            brace_stack = []  # Track opening braces and their line numbers
            
            for line_num, line in enumerate(lines, 1):
                line = line.strip()
                if not line or line.startswith('//'): 
                    continue
                
                try:
                    # Track opening braces
                    if '{' in line:
                        brace_stack.append((line_num, line))
                    
                    # Track closing braces
                    if '}' in line:
                        if not brace_stack:
                            raise ParseError("Unexpected closing brace - no matching opening brace found")
                        opening_line_num, opening_line = brace_stack.pop()
                    if line.startswith('app'):
                        # Parse app declaration
                        parts = line.split('"')
                        if len(parts) != 3:
                            raise ParseError("Invalid app declaration - expected 'app Name \"Title\" {'")
                        app_name = parts[0].split()[1]
                        app_title = parts[1]
                        if not app_name.isidentifier():
                            raise ParseError(f"Invalid app name: {app_name}")
                        spec['app'] = {'name': app_name, 'title': app_title}
                        in_app_block = True
                    elif line == '}':
                        if current_block:
                            current_block = None
                        elif in_app_block:
                            in_app_block = False
                        else:
                            context = f"\nOpening brace was at line {opening_line_num}: {opening_line}"
                            raise ParseError(f"Unexpected closing brace at line {line_num}", 
                                          line_num=line_num,
                                          line_content=line,
                                          prev_line=lines[line_num-2] if line_num > 1 else None,
                                          next_line=lines[line_num] if line_num < len(lines) else None)
                    elif line.startswith('model'):
                        if not in_app_block:
                            raise ParseError("Model must be defined inside app block")
                        current_block = self._parse_model(line)
                        spec['models'].append(current_block)
                    elif line.startswith('screen'):
                        if not in_app_block:
                            raise ParseError("Screen must be defined inside app block")
                        screen = self._parse_screen(line)
                        spec['screens'].append(screen)
                    elif current_block and line.strip():
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
            
            if field_type not in self.valid_types and not field_type.isidentifier():
                raise ParseError(f"'{field_type}' is not a valid type")
            
            # Field type can be either a basic type or a model reference
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
                field['default'] = remaining_parts[1].strip('"')  # Remove quotes if present
                
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
