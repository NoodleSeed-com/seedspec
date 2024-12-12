import pytest
from src.parser import parse_seed_file
from pathlib import Path

def test_theme_spec_parsing():
    """Test parsing theme spec from seed file"""
    theme_spec = parse_seed_file(Path("src/themes/spec.seed"))
    
    assert "ThemeSpec" in theme_spec
    assert "colors" in theme_spec["ThemeSpec"]
    assert "typography" in theme_spec["ThemeSpec"]
    assert "spacing" in theme_spec["ThemeSpec"]

def test_color_spec_defaults():
    """Test color spec default values"""
    theme_spec = parse_seed_file(Path("src/themes/spec.seed"))
    colors = theme_spec["ColorSpec"]
    
    assert colors["primary"] == "#0066cc"
    assert colors["secondary"] == "#6c757d"
    assert colors["background"] == "#ffffff"

def test_typography_spec_defaults():
    """Test typography spec default values"""
    theme_spec = parse_seed_file(Path("src/themes/spec.seed"))
    typography = theme_spec["TypographySpec"]
    
    assert "Inter" in typography["fontFamily"]["base"]
    assert "Poppins" in typography["fontFamily"]["heading"]
