from antlr4 import InputStream, CommonTokenStream, ParseTreeWalker, Token
from antlr4.error.DiagnosticErrorListener import DiagnosticErrorListener
from antlr4.error.ErrorListener import ErrorListener
from typing import Dict, Any, List

__all__ = ['SeedParser', 'ParseError']

class SeedSpecErrorListener(ErrorListener):
    def __init__(self):
        super().__init__()
        self.errors: List[Dict[str, Any]] = []

    def syntaxError(self, recognizer, offendingSymbol, line, column, msg, e):
        error = {
            'line': line,
            'column': column,
            'message': msg,
            'symbol': offendingSymbol.text if offendingSymbol else None,
            'token_type': offendingSymbol.type if offendingSymbol else None
        }
        self.errors.append(error)

class ParseError(Exception):
    """Exception raised for parsing errors"""
    pass

from .SeedSpecLexer import SeedSpecLexer
from .SeedSpecParser import SeedSpecParser
from .SeedSpecVisitor import SeedSpecVisitor

class SeedSpecCustomVisitor(SeedSpecVisitor):
    def visitProgram(self, ctx):
        app = self.visit(ctx.app())
        return app

    def visitApp(self, ctx):
        try:
            print("DEBUG: Visiting app node")
            print(f"DEBUG: ctx attributes: {dir(ctx)}")
            
            if not ctx.name:
                raise ParseError("App name is missing")
            print(f"DEBUG: App name: {ctx.name.text}")
            
            if not ctx.title:
                raise ParseError("App title is missing")
            print(f"DEBUG: App title: {ctx.title.text}")
                
            app_spec = {
                'name': ctx.name.text if ctx.name else None,
                'title': ctx.title.text.strip('"') if ctx.title else None,
                'models': [],
                'screens': []
            }
            
            print("DEBUG: Processing declarations")
            for decl in ctx.declaration():
                print(f"DEBUG: Processing declaration: {decl.getText()}")
                result = self.visit(decl)
                if 'fields' in result:  # It's a model
                    print("DEBUG: Found model declaration")
                    app_spec['models'].append(result)
                else:  # It's a screen
                    print("DEBUG: Found screen declaration")
                    app_spec['screens'].append(result)
                    
            return app_spec
        except AttributeError as e:
            print(f"DEBUG: AttributeError in visitApp: {str(e)}")
            raise ParseError(f"Failed to parse app declaration: {str(e)}")
        except Exception as e:
            print(f"DEBUG: Unexpected error in visitApp: {str(e)}")
            raise

    def visitModel(self, ctx):
        model = {
            'name': ctx.name.text,
            'fields': []
        }
        
        for field_ctx in ctx.field():
            field = self.visit(field_ctx)
            model['fields'].append(field)
            
        return model

    def visitBasicField(self, ctx):
        field = {
            'name': ctx.name.text,
            'type': ctx.type.text
        }
        
        if ctx.role:
            field['role'] = ctx.role.text
            
        if ctx.default:
            # Remove quotes from string defaults
            default_val = ctx.default.text
            if default_val.startswith('"') and default_val.endswith('"'):
                default_val = default_val[1:-1]
            field['default'] = default_val
            
        return field

    def visitScreen(self, ctx):
        return {
            'name': ctx.name.text,
            'model': ctx.modelRef.text
        }

class SeedParser:
    """Parser for the SeedSpec DSL"""
    
    @staticmethod
    def parse(input_text: str) -> Dict[str, Any]:
        """Parse SeedSpec DSL text and return app specification dictionary"""
        try:
            print("\nDEBUG: Starting parse")
            print(f"DEBUG: Input text:\n{input_text}")
            
            # Normalize line endings and ensure consistent whitespace
            input_text = input_text.replace('\r\n', '\n')
            if not input_text.startswith('\n'):
                input_text = '\n' + input_text
            if not input_text.endswith('\n'):
                input_text = input_text + '\n'
            print("DEBUG: Normalized text")
                
            # First pass: tokenize and validate
            input_stream = InputStream(input_text)
            print("DEBUG: Created input stream")
            
            lexer = SeedSpecLexer(input_stream)
            print("DEBUG: Created lexer")
            
            token_stream = CommonTokenStream(lexer)
            print("DEBUG: Created token stream")
            
            try:
                token_stream.fill()  # Force token generation
                print("DEBUG: Filled token stream")
            except Exception as e:
                print(f"DEBUG: Error filling token stream: {str(e)}")
                raise
            
            # Store tokens for error reporting
            tokens = []
            print("\nDEBUG: Processing tokens:")
            for token in token_stream.tokens:
                if token.type != Token.EOF:
                    print(f"DEBUG: Processing token: type={token.type}, text={token.text}")
                    # Skip newlines and whitespace tokens
                    if token.text.strip() == '':
                        continue
                    try:
                        token_name = lexer.symbolicNames[token.type] if token.type > 0 and token.type < len(lexer.symbolicNames) else f"'{token.text}'"
                        print(f"DEBUG: Token name resolved: {token_name}")
                        tokens.append(f"{token.text!r} ({token_name} at {token.line}:{token.column})")
                    except IndexError as e:
                        print(f"DEBUG: IndexError for token type {token.type}: {str(e)}")
                        # Don't raise error for whitespace tokens
                        if token.text.strip() != '':
                            raise ParseError(f"Invalid token type {token.type} for text '{token.text}'") from e
            
            # Second pass: actual parsing
            token_stream.seek(0)  # Reset stream for parsing
            parser = SeedSpecParser(token_stream)
            
            # Configure error handling
            error_listener = SeedSpecErrorListener()
            parser.removeErrorListeners()
            parser.addErrorListener(error_listener)
            
            # Parse and visit
            try:
                tree = parser.program()
                
                if error_listener.errors:
                    error_details = '\n'.join(
                        f"Line {e['line']}, Column {e['column']}: {e['message']}"
                        + (f" (Found: {e['symbol']})" if e['symbol'] else "")
                        for e in error_listener.errors
                    )
                    context = '\n'.join([
                        "Token stream:",
                        *tokens,
                        "\nErrors:",
                        error_details
                    ])
                    raise ParseError(f"Failed to parse SeedSpec:\n{context}")
                
                visitor = SeedSpecCustomVisitor()
                return visitor.visit(tree)
                
            except Exception as e:
                if isinstance(e, ParseError):
                    raise
                
                # Get the line where the error occurred
                error_line = None
                error_token = None
                if hasattr(e, 'token'):
                    error_token = e.token
                    error_line = error_token.line if error_token else None
                
                # Build error context
                context = [
                    "Token stream:",
                    *tokens
                ]
                
                if error_line is not None:
                    lines = input_text.splitlines()
                    if 0 < error_line <= len(lines):
                        context.extend([
                            "\nError context:",
                            f"Line {error_line-1}: {lines[error_line-2] if error_line > 1 else ''}",
                            f"Line {error_line}: {lines[error_line-1]} <-- Error here",
                            f"Line {error_line+1}: {lines[error_line] if error_line < len(lines) else ''}"
                        ])
                
                raise ParseError(f"Failed to parse SeedSpec:\n{chr(10).join(context)}\nError: {str(e)}") from e
                
        except Exception as e:
            if isinstance(e, ParseError):
                raise
            raise ParseError(f"Unexpected error while parsing SeedSpec: {str(e)}") from e
