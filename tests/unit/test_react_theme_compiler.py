import pytest
from pathlib import Path
from tools.compile_react_theme import generate_css, generate_theme_context

SAMPLE_THEME = {
    "colors": {
        "primary": "#3b82f6",
        "secondary": "#6366f1"
    },
    "typography": {
        "fontSize": {
            "base": "1rem",
            "lg": "1.25rem"
        }
    }
}

def test_generate_css():
    """Test CSS variable generation"""
    css = generate_css(SAMPLE_THEME)
    assert ":root {" in css
    assert "--colors-primary: #3b82f6;" in css.replace(" ", "")
    assert "--typography-fontSize-base: 1rem;" in css.replace(" ", "")
    assert "}" in css

def test_generate_theme_context():
    """Test React context generation"""
    context = generate_theme_context(SAMPLE_THEME)
    assert "import { createContext, useContext, ReactNode } from 'react';" in context
    assert "export const theme =" in context
    assert '"colors": {' in context
    assert '"primary": "#3b82f6"' in context
    assert "export function ThemeProvider" in context
    assert "export function useTheme()" in context

def test_css_generation_empty_theme():
    """Test CSS generation with empty theme"""
    css = generate_css({})
    assert css == ":root {\n}"

def test_theme_context_generation_empty_theme():
    """Test context generation with empty theme"""
    context = generate_theme_context({})
    assert "export const theme = {} as const;" in context

def test_css_generation_nested_properties():
    """Test CSS generation with deeply nested properties"""
    theme = {
        "typography": {
            "fontFamily": {
                "base": "Inter, sans-serif",
                "heading": {
                    "primary": "Poppins, sans-serif"
                }
            }
        }
    }
    css = generate_css(theme)
    assert "--typography-fontFamily-base: Inter, sans-serif;" in css.replace(" ", "")
    assert "--typography-fontFamily-heading-primary: Poppins, sans-serif;" in css.replace(" ", "")
