import os
import sys
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from antlr4 import InputStream, CommonTokenStream, Token
from seed_compiler.SeedSpecLexer import SeedSpecLexer
from seed_compiler.antlr_parser import SeedParser

def test_file(filename):
    print(f"\nTesting {filename}:")
    print("-" * 50)
    
    # Read the seed file
    with open(filename, 'r') as f:
        content = f.read()
    print('Input content:', repr(content))

    # Create input stream and lexer
    input_stream = InputStream(content)
    lexer = SeedSpecLexer(input_stream)
    token_stream = CommonTokenStream(lexer)
    token_stream.fill()

    # Print all tokens
    print('\nTokens:')
    for token in token_stream.tokens:
        if token.type != Token.EOF:
            try:
                token_name = lexer.symbolicNames[token.type] if token.type > 0 and token.type < len(lexer.symbolicNames) else f"'{token.text}'"
                print(f'{token.text!r} ({token_name} at {token.line}:{token.column})')
            except IndexError:
                print(f'{token.text!r} (Unknown token type {token.type} at {token.line}:{token.column})')

    # Try parsing the content
    try:
        result = SeedParser.parse(content)
        print('\nParsing successful!')
        print('App name:', result['name'])
        print('App title:', result['title'])
        print('Models:', [model['name'] for model in result['models']])
        print('Screens:', [screen['name'] for screen in result['screens']])
    except Exception as e:
        print('\nError:', str(e))

# Test both files
test_file('examples/expenses.seed')
test_file('examples/todo.seed')
