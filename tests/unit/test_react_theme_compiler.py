import pytest
from pathlib import Path
from tools.compile_react_theme import (
    generate_css, 
    generate_theme_context,
    extract_theme_from_app_spec,
    apply_theme_overrides
)

SAMPLE_APP_SPEC = {
    "ui": {
        "theme": {
            "colors": {
                "primary": "#3b82f6",
                "secondary": "#6366f1",
                "background": "#ffffff",
                "surface": "#f8fafc",
                "text": "#1e293b"
            },
            "typography": {
                "fontFamily": {
                    "base": "Inter, system-ui, sans-serif",
                    "heading": "Inter, system-ui, sans-serif"
                },
                "fontSize": {
                    "base": "1rem",
                    "lg": "1.25rem"
                }
            }
        },
        "overrides": {
            "colors.primary": "#0070f3",
            "typography.fontSize.base": "16px"
        }
    }
}

SAMPLE_THEME_REFERENCE_SPEC = {
    "ui": {
        "theme": "light"
    }
}

def test_generate_css():
    """Test CSS variable generation"""
    theme = extract_theme_from_app_spec(SAMPLE_APP_SPEC)
    css = generate_css(theme)
    css_normalized = "".join(css.split())  # Remove all whitespace
    assert ":root{" in css_normalized
    assert "--colors-primary:#3b82f6;" in css_normalized
    assert "--typography-fontSize-base:1rem;" in css_normalized
    assert "}" in css_normalized

def test_generate_theme_context():
    """Test React context generation"""
    theme = extract_theme_from_app_spec(SAMPLE_APP_SPEC)
    context = generate_theme_context(theme)
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
    css_normalized = "".join(css.split())  # Remove all whitespace
    assert "--typography-fontFamily-base:Inter,sans-serif;" in css_normalized
    assert "--typography-fontFamily-heading-primary:Poppins,sans-serif;" in css_normalized

def test_extract_theme_from_app_spec():
    """Test theme extraction from app specification with inline theme"""
    theme = extract_theme_from_app_spec(SAMPLE_APP_SPEC)
    assert theme["colors"]["primary"] == "#0070f3"  # Overridden value
    assert theme["colors"]["secondary"] == "#6366f1"
    assert theme["colors"]["background"] == "#ffffff"
    assert theme["typography"]["fontSize"]["base"] == "16px"  # Overridden value
    assert theme["typography"]["fontFamily"]["base"] == "Inter, system-ui, sans-serif"

def test_extract_theme_reference():
    """Test theme extraction using theme reference"""
    theme = extract_theme_from_app_spec(SAMPLE_THEME_REFERENCE_SPEC)
    assert theme["colors"]["background"] == "#ffffff"  # From light theme
    assert theme["colors"]["text"] == "#212529"  # From light theme

def test_extract_theme_no_ui():
    """Test theme extraction with no UI section"""
    theme = extract_theme_from_app_spec({})
    assert theme == {}

def test_apply_theme_overrides():
    """Test applying theme overrides"""
    base_theme = {
        "colors": {
            "primary": "#000000",
            "secondary": "#ffffff"
        },
        "typography": {
            "fontSize": {
                "base": "14px",
                "lg": "18px"
            }
        }
    }
    overrides = {
        "colors.primary": "#ff0000",
        "typography.fontSize.base": "16px"
    }
    result = apply_theme_overrides(base_theme, overrides)
    assert result["colors"]["primary"] == "#ff0000"
    assert result["colors"]["secondary"] == "#ffffff"
    assert result["typography"]["fontSize"]["base"] == "16px"
    assert result["typography"]["fontSize"]["lg"] == "18px"
