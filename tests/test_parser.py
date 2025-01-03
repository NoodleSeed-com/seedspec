import pytest
from seed_compiler.parser import SeedParser, ParseError

def test_basic_model_parsing():
    parser = SeedParser()
    input_text = """
    app Todo "Todo App" {
        model Task {
            title text
            done bool = false
        }
    }
    """
    
    spec = parser.parse(input_text)
    assert len(spec['models']) == 1
    assert spec['models'][0]['name'] == 'Task'
    assert len(spec['models'][0]['fields']) == 2
    assert spec['models'][0]['fields'][0]['name'] == 'title'
    assert spec['models'][0]['fields'][0]['type'] == 'text'
    assert spec['models'][0]['fields'][1]['default'] == 'false'

def test_basic_screen_parsing():
    parser = SeedParser()
    input_text = """
    app Todo "Todo App" {
        screen Tasks using Task
    }
    """
    
    spec = parser.parse(input_text)
    assert len(spec['screens']) == 1
    assert spec['screens'][0]['name'] == 'Tasks'
    assert spec['screens'][0]['model'] == 'Task'

def test_complete_app_parsing():
    parser = SeedParser()
    input_text = """
    app Todo "Todo App" {
        model Task {
            title text
            done bool = false
        }
        
        screen Tasks using Task
    }
    """
    
    spec = parser.parse(input_text)
    assert len(spec['models']) == 1
    assert len(spec['screens']) == 1

def test_invalid_model():
    parser = SeedParser()
    with pytest.raises(ParseError):
        parser.parse("model")

def test_invalid_screen():
    parser = SeedParser()
    with pytest.raises(ParseError):
        parser.parse("screen Tasks")

def test_missing_model_name():
    parser = SeedParser()
    with pytest.raises(ParseError):
        parser.parse("model {}")

def test_invalid_field_type():
    parser = SeedParser()
    with pytest.raises(ParseError):
        parser.parse("""
        app Todo "Todo App" {
            model Task {
                title invalid_type
            }
        }
        """)

def test_email_field_parsing():
    parser = SeedParser()
    input_text = """
    app UserManager "User Management System" {
        model User {
            name text
            email email
            active bool = true
        }
        
        screen Users using User
    }
    """
    spec = parser.parse(input_text)
    assert spec['models'][0]['fields'][1]['type'] == 'email'
