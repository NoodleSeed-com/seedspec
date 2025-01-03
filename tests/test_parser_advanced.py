import pytest
from seed_compiler.parser import SeedParser, ParseError

def test_invalid_app_declaration():
    """Test various invalid app declarations"""
    parser = SeedParser()
    
    # Missing quotes
    with pytest.raises(ParseError) as e:
        parser.parse("app Todo Todo App {}")
    assert "Invalid app declaration" in str(e.value)
    
    # Missing title
    with pytest.raises(ParseError) as e:
        parser.parse('app Todo "" {}')
    
    # Invalid app name
    with pytest.raises(ParseError) as e:
        parser.parse('app "Todo" "Todo App" {}')
    assert "Invalid app name" in str(e.value)

def test_nested_model_references():
    """Test nested model references"""
    parser = SeedParser()
    input_text = """
    app ProjectManager "Project Management" {
        model User {
            name text
            email email
        }
        
        model Task {
            title text
            assignee User
        }
        
        model Project {
            name text
            owner User
            mainTask Task
        }
        
        screen Projects using Project
    }
    """
    spec = parser.parse(input_text)
    
    # Verify Project model has both User and Task references
    project_model = next(m for m in spec['models'] if m['name'] == 'Project')
    owner_field = next(f for f in project_model['fields'] if f['name'] == 'owner')
    task_field = next(f for f in project_model['fields'] if f['name'] == 'mainTask')
    
    assert owner_field['type'] == 'User'
    assert owner_field['is_reference'] == True
    assert task_field['type'] == 'Task'
    assert task_field['is_reference'] == True

def test_duplicate_names():
    """Test duplicate model and screen names"""
    parser = SeedParser()
    
    # Duplicate model names
    with pytest.raises(ParseError) as e:
        parser.parse("""
        app Todo "Todo App" {
            model Task {
                title text
            }
            model Task {
                name text
            }
        }
        """)
    assert "Duplicate model name" in str(e.value)
    
    # Duplicate screen names
    with pytest.raises(ParseError) as e:
        parser.parse("""
        app Todo "Todo App" {
            model Task {
                title text
            }
            screen Tasks using Task
            screen Tasks using Task
        }
        """)
    assert "Duplicate screen name" in str(e.value)

def test_title_field_syntax():
    """Test 'as title' field syntax"""
    parser = SeedParser()
    input_text = """
    app Todo "Todo App" {
        model Task {
            title text as title
            description text
        }
    }
    """
    spec = parser.parse(input_text)
    
    task_model = spec['models'][0]
    title_field = next(f for f in task_model['fields'] if f['name'] == 'title')
    desc_field = next(f for f in task_model['fields'] if f['name'] == 'description')
    
    assert title_field.get('is_title') == True
    assert desc_field.get('is_title') is None

def test_invalid_default_values():
    """Test invalid default values for different types"""
    parser = SeedParser()
    
    # String for bool
    with pytest.raises(ParseError) as e:
        parser.parse("""
        app Todo "Todo App" {
            model Task {
                done bool = "invalid"
            }
        }
        """)
    assert "Invalid default value" in str(e.value)
    
    # Bool for number
    with pytest.raises(ParseError) as e:
        parser.parse("""
        app Todo "Todo App" {
            model Task {
                priority num = true
            }
        }
        """)
    assert "Invalid default value" in str(e.value)

def test_unclosed_braces():
    """Test unclosed braces detection"""
    parser = SeedParser()
    
    with pytest.raises(ParseError) as e:
        parser.parse("""
        app Todo "Todo App" {
            model Task {
                title text
            
        """)
    assert "Unclosed brace" in str(e.value)

def test_comments():
    """Test comment handling"""
    parser = SeedParser()
    input_text = """
    app Todo "Todo App" {
        // User model for authentication
        model User {
            name text  // User's full name
            email email  // Contact email
        }
        
        model Task {
            title text
            // Assigned user reference
            assignee User
        }
    }
    """
    spec = parser.parse(input_text)
    
    # Verify comments are ignored and don't affect parsing
    assert len(spec['models']) == 2
    user_model = next(m for m in spec['models'] if m['name'] == 'User')
    assert len(user_model['fields']) == 2
