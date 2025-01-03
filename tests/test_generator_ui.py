import pytest
import os
import tempfile
import json
from seed_compiler.generator import Generator

@pytest.fixture
def form_spec():
    return {
        'app': {'name': 'Forms', 'title': 'Form Testing'},
        'models': [{
            'name': 'User',
            'fields': [
                {'name': 'name', 'type': 'text', 'is_title': True},
                {'name': 'email', 'type': 'email'},
                {'name': 'age', 'type': 'num'},
                {'name': 'active', 'type': 'bool', 'default': 'true'}
            ]
        }],
        'screens': [{
            'name': 'Users',
            'model': 'User'
        }]
    }

def test_form_field_types(form_spec):
    """Test that form fields are generated with correct input types"""
    with tempfile.TemporaryDirectory() as tmpdir:
        generator = Generator()
        generator.generate(form_spec, tmpdir)
        
        with open(os.path.join(tmpdir, 'src/screens/Users.js')) as f:
            content = f.read()
            
            # Check input types
            assert 'type="text"' in content  # For name field
            assert 'type="email"' in content  # For email field
            assert 'type="number"' in content  # For age field
            assert 'type="checkbox"' in content  # For active field

def test_form_default_values(form_spec):
    """Test that form fields have correct default values"""
    with tempfile.TemporaryDirectory() as tmpdir:
        generator = Generator()
        generator.generate(form_spec, tmpdir)
        
        with open(os.path.join(tmpdir, 'src/screens/Users.js')) as f:
            content = f.read()
            
            # Check default values using regex to allow for whitespace variations
            import re
            assert re.search(r'defaultValue\s*=\s*{\s*true\s*}', content)  # For active field
            assert re.search(r'defaultValue\s*=\s*{\s*null\s*}', content)  # For fields without defaults

def test_form_validation(form_spec):
    """Test that form validation is generated"""
    with tempfile.TemporaryDirectory() as tmpdir:
        generator = Generator()
        generator.generate(form_spec, tmpdir)
        
        with open(os.path.join(tmpdir, 'src/screens/Users.js')) as f:
            content = f.read()
            
            # Check for required fields
            assert 'required' in content
            
            # Check for email validation
            assert 'type="email"' in content
            assert 'pattern=' in content  # Email pattern validation
            
            # Check for number validation
            assert 'min=' in content
            assert 'step=' in content

def test_crud_operations(form_spec):
    """Test that CRUD operations are properly generated"""
    with tempfile.TemporaryDirectory() as tmpdir:
        generator = Generator()
        generator.generate(form_spec, tmpdir)
        
        with open(os.path.join(tmpdir, 'src/screens/Users.js')) as f:
            content = f.read()
            
            # Test for create capability
            assert 'create(' in content  # Function call exists
            assert '<form' in content    # Form element exists
            
            # Test for read capability
            assert 'items.map(' in content  # Iterating over items
            assert '{item.' in content      # Displaying item properties
            
            # Test for update capability
            assert 'update(' in content     # Update function call exists
            assert 'edit' in content.lower() # Some form of edit UI exists
            
            # Test for delete capability
            assert 'remove(' in content     # Delete function call exists
            assert 'delete' in content.lower() # Some form of delete UI exists
            
            # Test for state management
            assert 'useState(' in content   # State management exists
            
            # Test for form handling
            assert 'preventDefault()' in content  # Form submission handling
            assert 'FormData(' in content        # Form data processing

def test_error_handling(form_spec):
    """Test that error handling is generated"""
    with tempfile.TemporaryDirectory() as tmpdir:
        generator = Generator()
        generator.generate(form_spec, tmpdir)
        
        with open(os.path.join(tmpdir, 'src/screens/Users.js')) as f:
            content = f.read()
            
            # Check for error state and display
            assert 'error' in content.lower()
            assert 'catch' in content
            assert 'try' in content
            
            # Check for validation error handling
            assert 'invalid' in content.lower()
            assert 'message' in content.lower()

def test_loading_states(form_spec):
    """Test that loading states are generated"""
    with tempfile.TemporaryDirectory() as tmpdir:
        generator = Generator()
        generator.generate(form_spec, tmpdir)
        
        with open(os.path.join(tmpdir, 'src/screens/Users.js')) as f:
            content = f.read()
            
            # Check for loading states
            assert 'loading' in content.lower()
            assert 'disabled=' in content
            assert 'useState' in content
