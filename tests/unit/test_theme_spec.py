import pytest
from src.parser import parse_seed_file
from pathlib import Path

def test_theme_spec_parsing():
    """Test parsing theme spec from seed file"""
    theme_spec = parse_seed_file(Path("src/stdlib/themes/base.seed"))
    
    assert "base" in theme_spec
    assert "button" in theme_spec["base"]
    assert "typography" in theme_spec["base"]
    assert "card" in theme_spec["base"]

def test_button_spec_defaults():
    """Test button spec default values"""
    theme_spec = parse_seed_file(Path("src/stdlib/themes/base.seed"))
    button = theme_spec["base"]["button"]
    
    assert "primary" in button
    assert button["primary"]["bg"] == "blue.500"
    assert button["primary"]["text"] == "white"

def test_typography_spec_defaults():
    """Test typography spec default values"""
    theme_spec = parse_seed_file(Path("src/stdlib/themes/base.seed"))
    typography = theme_spec["base"]["typography"]
    
    assert "heading" in typography
    assert typography["heading"]["weight"] == "bold"
    assert typography["heading"]["color"] == "gray.900"

def test_theme_inheritance():
    """Test theme inheritance and overrides"""
    theme_spec = parse_seed_file(Path("src/stdlib/themes/dark.seed"))
    
    # Should have dark theme components
    assert "button" in theme_spec["dark"]
    assert "typography" in theme_spec["dark"]
    
    # Should override specific values
    assert theme_spec["dark"]["card"]["bg"] == "gray.800"
    # Should have dark mode text colors
    assert theme_spec["dark"]["typography"]["body"]["color"] == "gray.300"

def test_theme_validation():
    """Test theme structure validation"""
    with pytest.raises(ValueError, match="Missing required theme section: button"):
        parse_seed_file(Path("tests/fixtures/invalid/missing_button.seed"))
    
    with pytest.raises(ValueError, match="Invalid theme token"):
        parse_seed_file(Path("tests/fixtures/invalid/invalid_token.seed"))

def test_multiple_theme_definitions():
    """Test handling multiple theme definitions in one file"""
    theme_spec = parse_seed_file(Path("tests/fixtures/imports/theme.seed"))
    
    assert "light" in theme_spec
    assert "dark" in theme_spec
    assert theme_spec["light"]["button"]["primary"]["bg"] != theme_spec["dark"]["button"]["primary"]["bg"]

def test_theme_extends():
    """Test theme extension mechanism"""
    theme_spec = parse_seed_file(Path("tests/fixtures/custom_theme.seed"))
    
    # Should extend base theme
    assert "button" in theme_spec["custom"]
    # Should override specific values
    assert theme_spec["custom"]["button"]["primary"]["bg"] == "indigo.500"

def test_nested_theme_properties():
    """Test deeply nested theme properties"""
    theme_spec = parse_seed_file(Path("src/stdlib/themes/base.seed"))
    
    assert "button" in theme_spec["base"]
    assert "primary" in theme_spec["base"]["button"]
    assert "hover" in theme_spec["base"]["button"]["primary"]
    assert isinstance(theme_spec["base"]["button"]["primary"]["hover"], dict)

def test_theme_variants():
    """Test theme variant definitions"""
    theme_spec = parse_seed_file(Path("src/stdlib/themes/base.seed"))
    
    assert "button" in theme_spec["base"]
    assert "primary" in theme_spec["base"]["button"]
    assert "secondary" in theme_spec["base"]["button"]

def test_component_states():
    """Test component state definitions"""
    theme_spec = parse_seed_file(Path("src/stdlib/themes/base.seed"))
    
    button = theme_spec["base"]["button"]["primary"]
    assert "hover" in button
    assert "focus" in button

def test_responsive_values():
    """Test responsive value definitions"""
    theme_spec = parse_seed_file(Path("src/stdlib/themes/base.seed"))
    
    heading = theme_spec["base"]["typography"]["heading"]
    assert "size" in heading
    assert isinstance(heading["size"], dict)
    assert "base" in heading["size"]
    assert "sm" in heading["size"]
    assert "lg" in heading["size"]

def test_theme_composition():
    """Test theme composition from multiple sources"""
    base = parse_seed_file(Path("src/stdlib/themes/base.seed"))
    custom = parse_seed_file(Path("tests/fixtures/custom_theme.seed"))
    
    # Verify custom theme properly composes with base
    assert "button" in custom["custom"]
    assert "typography" in custom["custom"]
    # Check override behavior
    assert custom["custom"]["button"]["primary"]["bg"] != base["base"]["button"]["primary"]["bg"]

def test_invalid_theme_composition():
    """Test invalid theme composition scenarios"""
    with pytest.raises(ValueError, match="Circular theme extension"):
        parse_seed_file(Path("tests/fixtures/invalid/circular_extend.seed"))
    
    with pytest.raises(ValueError, match="Unknown base theme"):
        parse_seed_file(Path("tests/fixtures/invalid/unknown_base.seed"))
