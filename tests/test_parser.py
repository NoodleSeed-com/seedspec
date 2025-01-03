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

# Theme Parsing Tests
def test_basic_theme_parsing():
    parser = SeedParser()
    input_text = """
    theme TestTheme "Test Theme" {
        colors {
            primary: ocean-blue
            secondary: forest-green
        }
    }
    """
    spec = parser.parse(input_text)
    assert 'themes' in spec
    assert spec['themes'][0]['name'] == 'TestTheme'
    assert 'colors' in spec['themes'][0]
    assert spec['themes'][0]['colors']['primary'] == 'ocean-blue'

def test_theme_inheritance():
    parser = SeedParser()
    input_text = """
    import { Default } from "@stdlib/themes"
    
    theme CustomTheme extends Default {
        colors {
            primary: california-blue
        }
    }
    """
    spec = parser.parse(input_text)
    assert spec['themes'][0]['extends'] == 'Default'
    assert spec['themes'][0]['colors']['primary'] == 'california-blue'

def test_complete_theme_structure():
    parser = SeedParser()
    input_text = """
    theme CompleteTheme "Complete Theme" {
        metadata {
            version: "1.0.0"
            description: "A complete theme"
        }
        colors {
            primary: ocean-blue
            secondary: forest-green
        }
        typography {
            fonts: {
                body: sans
                heading: sans
            }
            weights: {
                regular: 400
                bold: 700
            }
        }
        spacing {
            base: 1
            lg: 1.5
        }
        radii {
            base: 0.25
            lg: 0.5
        }
    }
    """
    spec = parser.parse(input_text)
    theme = spec['themes'][0]
    assert 'metadata' in theme
    assert 'colors' in theme
    assert 'typography' in theme
    assert 'spacing' in theme
    assert 'radii' in theme
    assert theme['metadata']['version'] == '1.0.0'
    assert 'fonts' in theme['typography']
    assert theme['spacing']['base'] == '1'

def test_theme_color_modifiers():
    parser = SeedParser()
    input_text = """
    theme ModifierTheme "Theme with Color Modifiers" {
        colors {
            primary: ocean-blue
            hover: primary.light
            active: primary.dark
            disabled: primary.pale
        }
    }
    """
    spec = parser.parse(input_text)
    colors = spec['themes'][0]['colors']
    assert colors['hover'] == 'primary.light'
    assert colors['active'] == 'primary.dark'
    assert colors['disabled'] == 'primary.pale'

def test_theme_validation():
    parser = SeedParser()
    with pytest.raises(ParseError):
        parser.parse("""
        theme InvalidTheme "Invalid Theme" {
            colors {
                primary: nonexistent-color
                invalid.modifier: blue
            }
        }
        """)

def test_theme_in_app():
    parser = SeedParser()
    input_text = """
    import { Default } from "@stdlib/themes"
    
    theme CustomTheme extends Default {
        colors {
            primary: ocean-blue
        }
    }
    
    app ThemedApp "Themed Application" {
        use theme CustomTheme
        
        model Task {
            title text
            done bool = false
        }
    }
    """
    spec = parser.parse(input_text)
    assert 'themes' in spec
    assert spec['app']['theme'] == 'CustomTheme'
