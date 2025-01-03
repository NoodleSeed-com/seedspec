import pytest
import os
import tempfile
import json
from seed_compiler.parser import SeedParser
from seed_compiler.generator import Generator

def test_complex_relationships():
    """Test complex model relationships and references"""
    input_text = """
    app ProjectManager "Project Management System" {
        model User {
            name text
            email email
            role text = "member"
        }
        
        model Team {
            name text as title
            leader User
            active bool = true
        }
        
        model Project {
            title text as title
            description text
            owner User
            team Team
            status text = "planning"
        }
        
        model Task {
            title text as title
            description text
            project Project
            assignee User
            reviewer User
            priority num = 1
        }
        
        screen Users using User
        screen Teams using Team
        screen Projects using Project
        screen Tasks using Task
    }
    """
    
    parser = SeedParser()
    spec = parser.parse(input_text)
    
    with tempfile.TemporaryDirectory() as tmpdir:
        generator = Generator()
        generator.generate(spec, tmpdir)
        
        # Check model files are generated
        assert os.path.exists(os.path.join(tmpdir, 'src/models/User.js'))
        assert os.path.exists(os.path.join(tmpdir, 'src/models/Team.js'))
        assert os.path.exists(os.path.join(tmpdir, 'src/models/Project.js'))
        assert os.path.exists(os.path.join(tmpdir, 'src/models/Task.js'))
        
        # Check Task model handles multiple User references
        with open(os.path.join(tmpdir, 'src/models/Task.js')) as f:
            content = f.read()
            assert 'assignee' in content
            assert 'reviewer' in content
            assert 'useUser' in content  # Should import User model hook
            
        # Check Project model handles both User and Team references
        with open(os.path.join(tmpdir, 'src/models/Project.js')) as f:
            content = f.read()
            assert 'owner' in content
            assert 'team' in content
            assert 'useUser' in content
            assert 'useTeam' in content

def test_circular_references():
    """Test handling of circular model references"""
    input_text = """
    app CircularTest "Circular Reference Test" {
        model Department {
            name text
            head Employee
        }
        
        model Employee {
            name text
            department Department
            supervisor Employee
        }
        
        screen Departments using Department
        screen Employees using Employee
    }
    """
    
    parser = SeedParser()
    spec = parser.parse(input_text)
    
    with tempfile.TemporaryDirectory() as tmpdir:
        generator = Generator()
        generator.generate(spec, tmpdir)
        
        # Check circular references are handled
        with open(os.path.join(tmpdir, 'src/models/Employee.js')) as f:
            content = f.read()
            assert 'department' in content
            assert 'supervisor' in content
            assert 'useDepartment' in content
            assert 'useEmployee' in content
            assert 'circular' in content.lower()  # Should have circular reference handling

def test_data_persistence():
    """Test data persistence and relationships"""
    input_text = """
    app Notes "Note Taking App" {
        model Category {
            name text as title
            description text
        }
        
        model Note {
            title text as title
            content text
            category Category
            tags text
            created num
            updated num
        }
        
        screen Categories using Category
        screen Notes using Note
    }
    """
    
    parser = SeedParser()
    spec = parser.parse(input_text)
    
    with tempfile.TemporaryDirectory() as tmpdir:
        generator = Generator()
        generator.generate(spec, tmpdir)
        
        # Check Note model handles persistence
        with open(os.path.join(tmpdir, 'src/models/Note.js')) as f:
            content = f.read()
            assert 'localStorage' in content
            assert 'JSON.parse' in content
            assert 'JSON.stringify' in content
            assert 'created' in content
            assert 'updated' in content
            assert 'Date.now()' in content

def test_validation_rules():
    """Test field validation rules"""
    input_text = """
    app Validation "Validation Testing" {
        model User {
            username text
            email email
            age num
            role text = "user"
            active bool = true
        }
        
        screen Users using User
    }
    """
    
    parser = SeedParser()
    spec = parser.parse(input_text)
    
    with tempfile.TemporaryDirectory() as tmpdir:
        generator = Generator()
        generator.generate(spec, tmpdir)
        
        # Check validation in screen component
        with open(os.path.join(tmpdir, 'src/screens/Users.js')) as f:
            content = f.read()
            assert 'required' in content
            assert 'pattern' in content  # Email validation
            assert 'min' in content  # Number validation
            assert 'validate' in content
            assert 'error' in content

def test_error_boundaries():
    """Test error boundary generation"""
    input_text = """
    app ErrorTest "Error Boundary Testing" {
        model Item {
            name text
            quantity num
        }
        
        screen Items using Item
    }
    """
    
    parser = SeedParser()
    spec = parser.parse(input_text)
    
    with tempfile.TemporaryDirectory() as tmpdir:
        generator = Generator()
        generator.generate(spec, tmpdir)
        
        # Check for error boundary component
        assert os.path.exists(os.path.join(tmpdir, 'src/components/ErrorBoundary.js'))
        
        # Check error boundary usage
        with open(os.path.join(tmpdir, 'src/App.js')) as f:
            content = f.read()
            assert 'ErrorBoundary' in content
            assert 'catch' in content
            assert 'error' in content
            assert 'fallback' in content

def test_loading_states():
    """Test loading state handling"""
    input_text = """
    app LoadingTest "Loading State Test" {
        model Post {
            title text
            content text
            published bool = false
        }
        
        screen Posts using Post
    }
    """
    
    parser = SeedParser()
    spec = parser.parse(input_text)
    
    with tempfile.TemporaryDirectory() as tmpdir:
        generator = Generator()
        generator.generate(spec, tmpdir)
        
        # Check loading states in screen component
        with open(os.path.join(tmpdir, 'src/screens/Posts.js')) as f:
            content = f.read()
            assert 'loading' in content
            assert 'isLoading' in content
            assert 'useState' in content
            assert 'disabled' in content
            assert 'spinner' in content.lower()
