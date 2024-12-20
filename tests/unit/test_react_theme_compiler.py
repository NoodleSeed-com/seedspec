import pytest
from pathlib import Path
from tools.compile_react_theme import (
    extract_theme_from_app_spec,
    apply_theme_overrides,
    compile_theme_tokens
)

SAMPLE_APP_SPEC = {
    "ui": {
        "theme": {
            "button": {
                "primary": {
                    "bg": "blue.500",
                    "text": "white",
                    "hover": {
                        "bg": "blue.600"
                    },
                    "focus": {
                        "ring": "blue.500"
                    }
                }
            },
            "card": {
                "bg": "white",
                "border": "gray.200",
                "shadow": "sm",
                "hover": {
                    "shadow": "md"
                }
            }
        },
        "overrides": {
            "button.primary.bg": "blue.600",
            "card.shadow": "md"
        }
    }
}

def test_compile_button_tokens():
    """Test compilation of button theme tokens to Tailwind classes"""
    theme = extract_theme_from_app_spec(SAMPLE_APP_SPEC)
    classes = compile_theme_tokens(theme, "button.primary")
    
    assert "bg-blue-600" in classes  # From override
    assert "text-white" in classes
    assert "hover:bg-blue-600" in classes
    assert "focus:ring-blue-500" in classes

def test_compile_card_tokens():
    """Test compilation of card theme tokens to Tailwind classes"""
    theme = extract_theme_from_app_spec(SAMPLE_APP_SPEC)
    classes = compile_theme_tokens(theme, "card")
    
    assert "bg-white" in classes
    assert "border-gray-200" in classes
    assert "shadow-md" in classes  # From override
    assert "hover:shadow-md" in classes

def test_dark_mode_compilation():
    """Test compilation of dark mode theme tokens"""
    theme = {
        "button": {
            "primary": {
                "bg": "blue.400",
                "text": "white",
                "hover": {
                    "bg": "blue.300"
                }
            }
        }
    }
    
    classes = compile_theme_tokens(theme, "button.primary", mode="dark")
    assert "dark:bg-blue-400" in classes
    assert "dark:text-white" in classes
    assert "dark:hover:bg-blue-300" in classes

def test_responsive_compilation():
    """Test compilation of responsive theme tokens"""
    theme = {
        "typography": {
            "heading": {
                "size": {
                    "base": "xl",
                    "sm": "lg",
                    "lg": "2xl"
                }
            }
        }
    }
    
    classes = compile_theme_tokens(theme, "typography.heading")
    assert "text-xl" in classes
    assert "sm:text-lg" in classes
    assert "lg:text-2xl" in classes

def test_state_variants_compilation():
    """Test compilation of state variant theme tokens"""
    theme = {
        "input": {
            "base": {
                "bg": "white",
                "border": "gray.200",
                "focus": {
                    "border": "blue.500",
                    "ring": "blue.500"
                },
                "disabled": {
                    "bg": "gray.100",
                    "border": "gray.200"
                }
            }
        }
    }
    
    classes = compile_theme_tokens(theme, "input.base")
    assert "bg-white" in classes
    assert "border-gray-200" in classes
    assert "focus:border-blue-500" in classes
    assert "focus:ring-blue-500" in classes
    assert "disabled:bg-gray-100" in classes
    assert "disabled:border-gray-200" in classes

def test_theme_inheritance():
    """Test compilation with theme inheritance"""
    base_theme = {
        "button": {
            "primary": {
                "bg": "blue.500",
                "text": "white"
            }
        }
    }
    
    overrides = {
        "button.primary.bg": "indigo.500"
    }
    
    theme = apply_theme_overrides(base_theme, overrides)
    classes = compile_theme_tokens(theme, "button.primary")
    
    assert "bg-indigo-500" in classes  # From override
    assert "text-white" in classes     # From base theme
