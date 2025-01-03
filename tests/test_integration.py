import pytest
import os
import tempfile
from seed_compiler.parser import SeedParser
from seed_compiler.generator import Generator

def test_end_to_end():
    # Test input
    input_text = """
    app Todo "Todo App" {
        model Task {
            title text
            done bool = false
        }
        
        screen Tasks using Task
    }
    """
    
    # Parse
    parser = SeedParser()
    spec = parser.parse(input_text)
    
    # Generate
    with tempfile.TemporaryDirectory() as tmpdir:
        generator = Generator()
        generator.generate(spec, tmpdir)
        
        # Verify output structure
        assert os.path.exists(os.path.join(tmpdir, 'src'))
        assert os.path.exists(os.path.join(tmpdir, 'package.json'))
        assert os.path.exists(os.path.join(tmpdir, 'src/App.js'))
        assert os.path.exists(os.path.join(tmpdir, 'src/models/Task.js'))
        assert os.path.exists(os.path.join(tmpdir, 'src/screens/Tasks.js'))

def test_multiple_models():
    input_text = """
    app ProjectManager "Project Management System" {
        model User {
            name text
            email email
        }
        
        model Task {
            title text
            assignee User
        }
        
        screen Users using User
        screen Tasks using Task
    }
    """
    
    parser = SeedParser()
    spec = parser.parse(input_text)
    
    with tempfile.TemporaryDirectory() as tmpdir:
        generator = Generator()
        generator.generate(spec, tmpdir)
        
        # Verify model references are handled
        with open(os.path.join(tmpdir, 'src/models/Task.js')) as f:
            content = f.read()
            assert 'assignee' in content
            assert 'User' in content
