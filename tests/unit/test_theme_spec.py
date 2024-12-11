import pytest
from src.themes.spec import ThemeSpec, ColorSpec, TypographySpec, SpacingSpec, BordersSpec, ShadowsSpec

def test_theme_spec_defaults():
    """Test theme spec default values"""
    theme = ThemeSpec()
    
    assert theme.theme == "default"
    assert isinstance(theme.colors, ColorSpec)
    assert isinstance(theme.typography, TypographySpec)
    assert isinstance(theme.spacing, SpacingSpec)
    assert isinstance(theme.borders, BordersSpec)
    assert isinstance(theme.shadows, ShadowsSpec)

def test_color_spec_defaults():
    """Test color spec default values"""
    colors = ColorSpec()
    
    assert colors.primary == "#0066cc"
    assert colors.secondary == "#6c757d"
    assert colors.background == "#ffffff"

def test_typography_spec_defaults():
    """Test typography spec default values"""
    typography = TypographySpec()
    
    assert "Inter" in typography.fontFamily["base"]
    assert "Poppins" in typography.fontFamily["heading"]

def test_theme_spec_overrides():
    """Test theme override functionality"""
    overrides = {
        "colors.primary": "#FF0000",
        "typography.fontSize.base": "16px"
    }
    
    theme = ThemeSpec(overrides=overrides)
    assert theme.overrides == overrides
