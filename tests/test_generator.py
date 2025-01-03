import pytest
import os
import tempfile
from seed_compiler.generator import Generator

@pytest.fixture
def basic_spec():
    return {
        'app': {'name': 'Todo', 'title': 'Todo App'},
        'models': [{
            'name': 'Task',
            'fields': [
                {'name': 'title', 'type': 'text'},
                {'name': 'done', 'type': 'bool', 'default': 'false'}
            ]
        }],
        'screens': [{
            'name': 'Tasks',
            'model': 'Task'
        }]
    }

@pytest.fixture
def email_spec():
    return {
        'app': {'name': 'UserManager', 'title': 'User Management System'},
        'models': [{
            'name': 'User',
            'fields': [
                {'name': 'name', 'type': 'text'},
                {'name': 'email', 'type': 'email'},
                {'name': 'active', 'type': 'bool', 'default': 'true'}
            ]
        }],
        'screens': [{
            'name': 'Users',
            'model': 'User'
        }]
    }

def test_generator_creates_files(basic_spec):
    with tempfile.TemporaryDirectory() as tmpdir:
        generator = Generator()
        generator.generate(basic_spec, tmpdir)
        
        # Check directory structure
        assert os.path.exists(os.path.join(tmpdir, 'src'))
        assert os.path.exists(os.path.join(tmpdir, 'src/models'))
        assert os.path.exists(os.path.join(tmpdir, 'src/screens'))
        
        # Check generated files
        assert os.path.exists(os.path.join(tmpdir, 'src/App.js'))
        assert os.path.exists(os.path.join(tmpdir, 'src/models/Task.js'))
        assert os.path.exists(os.path.join(tmpdir, 'src/screens/Tasks.js'))
        assert os.path.exists(os.path.join(tmpdir, 'package.json'))

def test_generator_model_content(basic_spec):
    with tempfile.TemporaryDirectory() as tmpdir:
        generator = Generator()
        generator.generate(basic_spec, tmpdir)
        
        with open(os.path.join(tmpdir, 'src/models/Task.js')) as f:
            content = f.read()
            assert 'export function useTask()' in content
            assert 'const [items, setItems] = useState(() => {' in content
            assert 'localStorage.getItem' in content
            assert 'create' in content
            assert 'update' in content
            assert 'remove' in content

def test_generator_screen_content(basic_spec, email_spec):
    with tempfile.TemporaryDirectory() as tmpdir:
        generator = Generator()
        generator.generate(basic_spec, tmpdir)
        
        with open(os.path.join(tmpdir, 'src/screens/Tasks.js')) as f:
            content = f.read()
            assert 'export function Tasks()' in content
            assert 'const { items, create, update, remove }' in content
            assert '<form' in content
            assert 'title' in content
            assert 'done' in content

        # Test email input type generation
        generator.generate(email_spec, tmpdir)
        with open(os.path.join(tmpdir, 'src/screens/Users.js')) as f:
            content = f.read()
            assert 'type="email"' in content

def test_generator_package_json(basic_spec):
    with tempfile.TemporaryDirectory() as tmpdir:
        generator = Generator()
        generator.generate(basic_spec, tmpdir)
        
        with open(os.path.join(tmpdir, 'package.json')) as f:
            content = f.read()
            assert '"react"' in content
            assert '"react-dom"' in content
            assert '"react-router-dom"' in content
