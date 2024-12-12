import pytest
from src.parser import parse_seed_file
from pathlib import Path

def test_theme_spec_parsing():
    """Test parsing theme spec from seed file"""
    theme_spec = parse_seed_file(Path("src/stdlib/themes.seed"))
    
    assert "default" in theme_spec
    assert "colors" in theme_spec["default"]
    assert "typography" in theme_spec["default"]
    assert "spacing" in theme_spec["default"]

def test_color_spec_defaults():
    """Test color spec default values"""
    theme_spec = parse_seed_file(Path("src/stdlib/themes.seed"))
    colors = theme_spec["default"]["colors"]
    
    assert colors["primary"] == "#0066cc"
    assert colors["secondary"] == "#6c757d"
    assert colors["background"] == "#ffffff"

def test_typography_spec_defaults():
    """Test typography spec default values"""
    theme_spec = parse_seed_file(Path("src/stdlib/themes.seed"))
    typography = theme_spec["default"]["typography"]
    
    assert "Inter" in typography["fontFamily"]["base"]
    assert "Inter" in typography["fontFamily"]["heading"]
