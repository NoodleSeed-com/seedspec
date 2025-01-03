import pytest
import os
import tempfile
from seed_compiler.parser import SeedParser
from seed_compiler.generator import Generator

def test_complex_model_relationships():
    """Test integration of parser and generator with complex model relationships"""
    input_text = """
    app BlogSystem "Blog System" {
        model Author {
            name text
            email email
            bio text
        }
        
        model Post {
            title text
            content text
            published bool = false
            author Author
        }
        
        screen Posts using Post
        screen Authors using Author
    }
    """
    
    # Test complete pipeline
    parser = SeedParser()
    spec = parser.parse(input_text)
    
    # Verify parser output for relationships
    assert len(spec['models']) == 2
    post_model = next(m for m in spec['models'] if m['name'] == 'Post')
    author_field = next(f for f in post_model['fields'] if f['name'] == 'author')
    assert author_field['type'] == 'Author'
    
    # Test generator with relationship handling
    with tempfile.TemporaryDirectory() as tmpdir:
        generator = Generator()
        generator.generate(spec, tmpdir)
        
        # Verify model imports and relationships
        with open(os.path.join(tmpdir, 'src/models/Post.js')) as f:
            post_content = f.read()
            assert 'useAuthor' in post_content
            assert 'import { useAuthor }' in post_content
        
        # Verify screen handling of relationships
        with open(os.path.join(tmpdir, 'src/screens/Posts.js')) as f:
            screen_content = f.read()
            # Check reference field rendering
            assert 'Select Author' in screen_content
            assert 'authorItems' in screen_content

def test_advanced_form_handling():
    """Test integration of complex form generation and validation"""
    input_text = """
    app UserSystem "User Management" {
        model User {
            username text
            email email
            age num
            preferences text
            terms bool = false
        }
        
        screen UserProfile using User
    }
    """
    
    parser = SeedParser()
    spec = parser.parse(input_text)
    
    # Verify parser handles all field types
    user_model = spec['models'][0]
    assert len(user_model['fields']) == 5
    assert any(f['type'] == 'email' for f in user_model['fields'])
    assert any(f['type'] == 'num' for f in user_model['fields'])
    
    with tempfile.TemporaryDirectory() as tmpdir:
        generator = Generator()
        generator.generate(spec, tmpdir)
        
        # Verify form generation with different input types
        with open(os.path.join(tmpdir, 'src/screens/UserProfile.js')) as f:
            content = f.read()
            # Check proper input type generation
            assert 'type="email"' in content
            assert 'type="number"' in content
            assert 'type="checkbox"' in content
            # Check form submission handling
            assert 'onSubmit' in content
            assert 'preventDefault' in content
            assert 'FormData' in content

def test_error_and_loading_integration():
    """Test integration of error handling and loading states"""
    input_text = """
    app DataSystem "Data Management" {
        model DataItem {
            name text
            status text
            priority num
        }
        
        screen DataItems using DataItem
    }
    """
    
    parser = SeedParser()
    spec = parser.parse(input_text)
    
    with tempfile.TemporaryDirectory() as tmpdir:
        generator = Generator()
        generator.generate(spec, tmpdir)
        
        # Verify error boundary integration
        with open(os.path.join(tmpdir, 'src/App.js')) as f:
            app_content = f.read()
            assert 'ErrorBoundary' in app_content
            assert '<ErrorBoundary>' in app_content
        
        # Verify screen error and loading handling
        with open(os.path.join(tmpdir, 'src/screens/DataItems.js')) as f:
            screen_content = f.read()
            # Error state handling
            assert 'useState' in screen_content
            assert 'setError' in screen_content
            assert 'catch' in screen_content
            # Loading state handling
            assert 'setLoading' in screen_content
            assert 'disabled={loading}' in screen_content
            assert 'finally {' in screen_content

def test_component_interaction():
    """Test integration of component interactions and state management"""
    input_text = """
    app TaskSystem "Task Management" {
        model Task {
            title text
            description text
            status text = "pending"
            priority num = 1
        }
        
        screen Tasks using Task
    }
    """
    
    parser = SeedParser()
    spec = parser.parse(input_text)
    
    with tempfile.TemporaryDirectory() as tmpdir:
        generator = Generator()
        generator.generate(spec, tmpdir)
        
        # Verify model hooks and state management
        with open(os.path.join(tmpdir, 'src/models/Task.js')) as f:
            model_content = f.read()
            assert 'useState' in model_content
            assert 'localStorage' in model_content
            assert 'useCallback' in model_content
        
        # Verify screen-model interaction
        with open(os.path.join(tmpdir, 'src/screens/Tasks.js')) as f:
            screen_content = f.read()
            # Model hook usage
            assert 'useTask' in screen_content
            assert 'const { items, create, update, remove }' in screen_content
            # State updates
            assert 'useState' in screen_content
            assert 'setEditingId' in screen_content
            # Default value handling
            assert "'pending'" in model_content
            assert '1' in model_content
