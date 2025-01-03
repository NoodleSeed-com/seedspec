import pytest
import os
import tempfile
from seed_compiler.generator import Generator

@pytest.fixture
def theme_spec():
    return {
        'themes': [{
            'name': 'CustomTheme',
            'extends': 'Default',
            'colors': {
                'primary': 'ocean-blue',
                'secondary': 'forest-green',
                'hover': 'primary.light',
                'active': 'primary.dark'
            },
            'typography': {
                'fonts': {
                    'body': 'sans',
                    'heading': 'sans'
                },
                'weights': {
                    'regular': '400',
                    'bold': '700'
                }
            },
            'spacing': {
                'base': '1',
                'lg': '1.5'
            },
            'radii': {
                'base': '0.25',
                'lg': '0.5'
            }
        }]
    }

@pytest.fixture
def themed_app_spec(theme_spec):
    return {
        'app': {
            'name': 'ThemedTodo',
            'title': 'Themed Todo App',
            'theme': 'CustomTheme'
        },
        'themes': theme_spec['themes'],
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

# Theme Generation Tests
def test_generator_creates_theme_files(themed_app_spec):
    with tempfile.TemporaryDirectory() as tmpdir:
        generator = Generator()
        generator.generate(themed_app_spec, tmpdir)
        
        # Check theme-specific files
        assert os.path.exists(os.path.join(tmpdir, 'src/theme'))
        assert os.path.exists(os.path.join(tmpdir, 'src/theme/theme.js'))
        assert os.path.exists(os.path.join(tmpdir, 'tailwind.config.js'))
        assert os.path.exists(os.path.join(tmpdir, 'src/theme/ThemeProvider.js'))

def test_generator_tailwind_config(themed_app_spec):
    with tempfile.TemporaryDirectory() as tmpdir:
        generator = Generator()
        generator.generate(themed_app_spec, tmpdir)
        
        with open(os.path.join(tmpdir, 'tailwind.config.js')) as f:
            content = f.read()
            # Check Tailwind configuration
            assert 'theme: {' in content
            assert 'extend: {' in content
            assert 'colors: {' in content
            assert 'typography: {' in content
            assert 'spacing: {' in content
            assert 'borderRadius: {' in content
            # Check color values
            assert 'primary:' in content
            assert 'secondary:' in content
            # Check dark mode configuration
            assert 'darkMode:' in content

def test_generator_theme_tokens(themed_app_spec):
    with tempfile.TemporaryDirectory() as tmpdir:
        generator = Generator()
        generator.generate(themed_app_spec, tmpdir)
        
        with open(os.path.join(tmpdir, 'src/theme/theme.js')) as f:
            content = f.read()
            # Check theme token exports
            assert 'export const theme = {' in content
            assert 'colors:' in content
            assert 'typography:' in content
            assert 'spacing:' in content
            assert 'radii:' in content
            # Check color values and modifiers
            assert 'ocean-blue' in content
            assert 'forest-green' in content
            assert 'primary:' in content
            assert 'hover:' in content

def test_generator_theme_provider(themed_app_spec):
    with tempfile.TemporaryDirectory() as tmpdir:
        generator = Generator()
        generator.generate(themed_app_spec, tmpdir)
        
        with open(os.path.join(tmpdir, 'src/theme/ThemeProvider.js')) as f:
            content = f.read()
            # Check theme provider implementation
            assert 'export function ThemeProvider' in content
            assert 'createContext' in content
            assert 'useContext' in content
            assert 'children' in content
            # Check theme switching functionality
            assert 'setTheme' in content
            assert 'useEffect' in content

def test_generator_themed_components(themed_app_spec):
    with tempfile.TemporaryDirectory() as tmpdir:
        generator = Generator()
        generator.generate(themed_app_spec, tmpdir)
        
        with open(os.path.join(tmpdir, 'src/screens/Tasks.js')) as f:
            content = f.read()
            # Check theme class applications
            assert 'className=' in content
            assert 'bg-primary' in content or 'text-primary' in content
            assert 'hover:' in content
            # Check typography classes
            assert 'font-sans' in content
            assert 'font-bold' in content
            # Check spacing/sizing classes
            assert 'p-' in content
            assert 'rounded-' in content

def test_generator_dark_mode_support(themed_app_spec):
    with tempfile.TemporaryDirectory() as tmpdir:
        generator = Generator()
        generator.generate(themed_app_spec, tmpdir)
        
        with open(os.path.join(tmpdir, 'src/theme/ThemeProvider.js')) as f:
            content = f.read()
            # Check dark mode implementation
            assert 'dark:' in content
            assert 'prefers-color-scheme' in content
            assert 'setDarkMode' in content
