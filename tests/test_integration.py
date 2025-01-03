import pytest
import os
import tempfile
from seed_compiler.parser import SeedParser
from seed_compiler.generator import Generator
from seed_compiler.stdlib import StdLibManager

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

def test_screen_async_handlers():
    input_text = """
    app Todo "Todo App" {
        model Task {
            title text
            done bool = false
        }
        
        screen Tasks using Task
    }
    """
    
    parser = SeedParser()
    spec = parser.parse(input_text)
    
    with tempfile.TemporaryDirectory() as tmpdir:
        generator = Generator()
        generator.generate(spec, tmpdir)
        
        # Read generated screen file
        with open(os.path.join(tmpdir, 'src/screens/Tasks.js')) as f:
            content = f.read()
            
            # Verify create form has async handler
            assert 'onSubmit={async e =>' in content
            assert 'await create(data);' in content
            
            # Verify edit form has async handler
            assert 'onSubmit={async e =>' in content
            assert 'await update(item.id, data);' in content
            
            # Verify delete has async handler
            assert 'onClick={async () =>' in content
            assert 'await remove(item.id);' in content

def test_theme_end_to_end():
    """Test complete theme system integration from parsing to generation"""
    input_text = """
    import { Default } from "@stdlib/themes"
    
    theme CustomTheme extends Default {
        colors {
            primary: ocean-blue
            secondary: forest-green
            hover: primary.light
        }
        typography {
            fonts: {
                body: sans
            }
        }
    }
    
    app ThemedTodo "Themed Todo App" {
        use theme CustomTheme
        
        model Task {
            title text
            done bool = false
        }
        
        screen Tasks using Task
    }
    """
    
    parser = SeedParser()
    spec = parser.parse(input_text)
    
    with tempfile.TemporaryDirectory() as tmpdir:
        generator = Generator()
        generator.generate(spec, tmpdir)
        
        # Verify theme files
        assert os.path.exists(os.path.join(tmpdir, 'src/theme'))
        assert os.path.exists(os.path.join(tmpdir, 'src/theme/theme.js'))
        assert os.path.exists(os.path.join(tmpdir, 'tailwind.config.js'))
        
        # Verify theme content
        with open(os.path.join(tmpdir, 'src/theme/theme.js')) as f:
            theme_content = f.read()
            assert 'ocean-blue' in theme_content
            assert 'forest-green' in theme_content
            assert 'sans' in theme_content
        
        # Verify Tailwind config
        with open(os.path.join(tmpdir, 'tailwind.config.js')) as f:
            config_content = f.read()
            assert 'primary:' in config_content
            assert 'secondary:' in config_content
            assert 'hover:' in config_content
        
        # Verify theme application in components
        with open(os.path.join(tmpdir, 'src/screens/Tasks.js')) as f:
            screen_content = f.read()
            assert 'className=' in screen_content
            assert 'bg-primary' in screen_content or 'text-primary' in screen_content
            assert 'font-sans' in screen_content

def test_theme_inheritance_chain():
    """Test theme inheritance through multiple levels"""
    input_text = """
    import { Default } from "@stdlib/themes"
    
    theme BaseTheme extends Default {
        colors {
            primary: ocean-blue
        }
    }
    
    theme ExtendedTheme extends BaseTheme {
        colors {
            secondary: forest-green
        }
    }
    
    theme FinalTheme extends ExtendedTheme {
        colors {
            accent: coral-green
        }
    }
    
    app ThemedApp "Themed App" {
        use theme FinalTheme
        
        model Task {
            title text
        }
        
        screen Tasks using Task
    }
    """
    
    parser = SeedParser()
    spec = parser.parse(input_text)
    
    with tempfile.TemporaryDirectory() as tmpdir:
        generator = Generator()
        generator.generate(spec, tmpdir)
        
        with open(os.path.join(tmpdir, 'src/theme/theme.js')) as f:
            content = f.read()
            # Verify inheritance chain
            assert 'ocean-blue' in content  # From BaseTheme
            assert 'forest-green' in content  # From ExtendedTheme
            assert 'coral-green' in content  # From FinalTheme

def test_theme_dark_mode_integration():
    """Test dark mode integration in themed app"""
    input_text = """
    import { Default, Dark } from "@stdlib/themes"
    
    app ThemedApp "Themed App" {
        use theme Default
        use theme Dark
        
        model Task {
            title text
        }
        
        screen Tasks using Task
    }
    """
    
    parser = SeedParser()
    spec = parser.parse(input_text)
    
    with tempfile.TemporaryDirectory() as tmpdir:
        generator = Generator()
        generator.generate(spec, tmpdir)
        
        # Verify dark mode configuration
        with open(os.path.join(tmpdir, 'tailwind.config.js')) as f:
            config = f.read()
            assert 'darkMode:' in config
        
        # Verify theme provider
        with open(os.path.join(tmpdir, 'src/theme/ThemeProvider.js')) as f:
            provider = f.read()
            assert 'dark:' in provider
            assert 'prefers-color-scheme' in provider
        
        # Verify component dark mode classes
        with open(os.path.join(tmpdir, 'src/screens/Tasks.js')) as f:
            screen = f.read()
            assert 'dark:' in screen

def test_theme_color_resolution():
    """Test color resolution and modifier application"""
    input_text = """
    theme TestTheme "Test Theme" {
        colors {
            primary: ocean-blue
            hover: primary.light
            active: primary.dark
            disabled: primary.pale
        }
    }
    
    app TestApp "Test App" {
        use theme TestTheme
        model Task {
            title text
        }
        screen Tasks using Task
    }
    """
    
    parser = SeedParser()
    spec = parser.parse(input_text)
    
    with tempfile.TemporaryDirectory() as tmpdir:
        generator = Generator()
        generator.generate(spec, tmpdir)
        
        with open(os.path.join(tmpdir, 'src/theme/theme.js')) as f:
            content = f.read()
            base_color = content.split('primary:')[1].split(',')[0].strip()
            hover_color = content.split('hover:')[1].split(',')[0].strip()
            active_color = content.split('active:')[1].split(',')[0].strip()
            disabled_color = content.split('disabled:')[1].split(',')[0].strip()
            
            # Verify colors are different
            assert len({base_color, hover_color, active_color, disabled_color}) == 4

def test_external_theme_and_model_references():
    """Test themes and models defined outside app block"""
    input_text = """
    // Theme defined outside app
    theme CustomTheme "Custom Theme" {
        colors {
            primary: ocean-blue
            secondary: forest-green
        }
    }

    // Model defined outside app
    model Task {
        title text
        done bool = false
    }

    app TestApp "Test Application" {
        // Reference external theme
        use theme CustomTheme
        
        // Reference external model
        screen TaskList using Task
    }
    """
    
    parser = SeedParser()
    spec = parser.parse(input_text)
    
    # Verify theme and model are parsed at root level
    assert 'themes' in spec
    assert 'models' in spec
    assert len(spec['themes']) == 1
    assert len(spec['models']) == 1
    
    # Verify app references are resolved
    assert spec['app']['theme'] == 'CustomTheme'
    assert spec['screens'][0]['model'] == 'Task'
    
    with tempfile.TemporaryDirectory() as tmpdir:
        generator = Generator()
        generator.generate(spec, tmpdir)
        
        # Verify theme is properly applied
        with open(os.path.join(tmpdir, 'src/theme/theme.js')) as f:
            theme_content = f.read()
            assert 'ocean-blue' in theme_content
            assert 'forest-green' in theme_content
        
        # Verify model is properly generated
        with open(os.path.join(tmpdir, 'src/models/Task.js')) as f:
            model_content = f.read()
            assert 'title' in model_content
            assert 'done' in model_content
        
        # Verify screen uses both theme and model
        with open(os.path.join(tmpdir, 'src/screens/TaskList.js')) as f:
            screen_content = f.read()
            # Theme classes
            assert 'bg-primary' in screen_content or 'text-primary' in screen_content
            # Model integration
            assert 'title' in screen_content
            assert 'done' in screen_content

def test_multiple_external_references():
    """Test multiple themes and models defined outside app"""
    input_text = """
    // Multiple themes
    theme LightTheme "Light Theme" {
        colors {
            primary: ocean-blue
            background: white
        }
    }

    theme DarkTheme "Dark Theme" {
        colors {
            primary: ocean-blue.light
            background: midnight-black
        }
    }

    // Multiple models
    model User {
        name text
        email email
    }

    model Task {
        title text
        assignee User
        done bool = false
    }

    app TestApp "Test Application" {
        // Reference themes
        use theme LightTheme
        use theme DarkTheme
        
        // Reference models
        screen Users using User
        screen Tasks using Task
    }
    """
    
    parser = SeedParser()
    spec = parser.parse(input_text)
    
    # Verify multiple themes and models are parsed
    assert len(spec['themes']) == 2
    assert len(spec['models']) == 2
    
    with tempfile.TemporaryDirectory() as tmpdir:
        generator = Generator()
        generator.generate(spec, tmpdir)
        
        # Verify both themes are available
        with open(os.path.join(tmpdir, 'src/theme/theme.js')) as f:
            theme_content = f.read()
            assert 'ocean-blue' in theme_content
            assert 'midnight-black' in theme_content
        
        # Verify both models are generated
        assert os.path.exists(os.path.join(tmpdir, 'src/models/User.js'))
        assert os.path.exists(os.path.join(tmpdir, 'src/models/Task.js'))
        
        # Verify model relationship
        with open(os.path.join(tmpdir, 'src/models/Task.js')) as f:
            task_content = f.read()
            assert 'assignee' in task_content
            assert 'User' in task_content
        
        # Verify screens use correct themes and models
        assert os.path.exists(os.path.join(tmpdir, 'src/screens/Users.js'))
        assert os.path.exists(os.path.join(tmpdir, 'src/screens/Tasks.js'))

def test_themed_todo_example():
    """Test the themed todo example specifically"""
    input_text = """
    import { Default } from "@stdlib/themes"

    theme TodoTheme extends Default {
        colors {
            primary: ocean-blue
            secondary: forest-green
            
            // Status colors derived from nature
            success: emerald-green
            warning: california-gold
        }
    }

    model Todo {
        title text as title
        done bool = false
        dueDate date?
    }

    app TodoApp "Todo List" {
        use theme TodoTheme

        data {
            Todos: Todo[] [
                { title: "Complete project proposal", dueDate: 2024-01-15 },
                { title: "Weekly team meeting", dueDate: 2024-01-10, done: true }
            ]
        }

        screen TodoList using Todo
    }
    """
    
    parser = SeedParser()
    spec = parser.parse(input_text)
    
    with tempfile.TemporaryDirectory() as tmpdir:
        generator = Generator()
        generator.generate(spec, tmpdir)
        
        # Verify theme inheritance and color resolution
        with open(os.path.join(tmpdir, 'src/theme/theme.js')) as f:
            theme_content = f.read()
            # Check custom colors
            assert 'ocean-blue' in theme_content
            assert 'forest-green' in theme_content
            assert 'emerald-green' in theme_content
            assert 'california-gold' in theme_content
            # Check inherited properties are preserved
            assert 'background' in theme_content
            assert 'text' in theme_content
        
        # Verify Tailwind config includes all theme colors
        with open(os.path.join(tmpdir, 'tailwind.config.js')) as f:
            config_content = f.read()
            assert 'primary:' in config_content
            assert 'secondary:' in config_content
            assert 'success:' in config_content
            assert 'warning:' in config_content
        
        # Verify theme application in todo list component
        with open(os.path.join(tmpdir, 'src/screens/TodoList.js')) as f:
            screen_content = f.read()
            # Check theme classes
            assert 'bg-primary' in screen_content or 'text-primary' in screen_content
            assert 'text-success' in screen_content or 'bg-success' in screen_content
            assert 'text-warning' in screen_content or 'bg-warning' in screen_content
            # Check todo functionality
            assert 'title' in screen_content
            assert 'done' in screen_content
            assert 'dueDate' in screen_content
            # Check data integration
            assert 'Todos' in screen_content
            assert 'useState' in screen_content
            assert 'onChange' in screen_content
        
        # Verify model integration with theme
        with open(os.path.join(tmpdir, 'src/models/Todo.js')) as f:
            model_content = f.read()
            assert 'title' in model_content
            assert 'done' in model_content
            assert 'dueDate' in model_content
            assert 'useState' in model_content
