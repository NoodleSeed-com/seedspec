import pytest
from pathlib import Path
import json
from tools.compile_react_theme import compile_theme_tokens
from tools.test_utils import render_component, cleanup_after_test

@pytest.fixture(autouse=True)
def setup_teardown():
    """Setup and teardown for each test"""
    yield
    cleanup_after_test()

def test_button_component():
    """Test button component using theme tokens"""
    theme = {
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
        }
    }
    
    component = """
    export function Button({ variant = "primary" }) {
        const classes = useThemeTokens("button.primary");
        return (
            <button className={classes}>
                Click Me
            </button>
        );
    }
    """
    
    rendered = render_component(component, theme=theme)
    classes = compile_theme_tokens(theme, "button.primary")
    
    for class_name in classes.split():
        assert class_name in rendered

def test_dark_mode_component():
    """Test component with dark mode theme tokens"""
    theme = {
        "card": {
            "bg": "white",
            "text": "gray.900",
            "border": "gray.200"
        }
    }
    
    dark_theme = {
        "card": {
            "bg": "gray.800",
            "text": "gray.100",
            "border": "gray.700"
        }
    }
    
    component = """
    export function Card() {
        const classes = useThemeTokens("card");
        return (
            <div className={classes}>
                Card Content
            </div>
        );
    }
    """
    
    rendered = render_component(component, theme=theme, darkTheme=dark_theme)
    light_classes = compile_theme_tokens(theme, "card")
    dark_classes = compile_theme_tokens(dark_theme, "card", mode="dark")
    
    for class_name in light_classes.split():
        assert class_name in rendered
    for class_name in dark_classes.split():
        assert class_name in rendered

def test_responsive_component():
    """Test component with responsive theme tokens"""
    theme = {
        "typography": {
            "heading": {
                "size": {
                    "base": "xl",
                    "sm": "lg",
                    "lg": "2xl"
                },
                "weight": "bold",
                "color": "gray.900"
            }
        }
    }
    
    component = """
    export function Heading() {
        const classes = useThemeTokens("typography.heading");
        return (
            <h1 className={classes}>
                Responsive Heading
            </h1>
        );
    }
    """
    
    rendered = render_component(component, theme=theme)
    classes = compile_theme_tokens(theme, "typography.heading")
    
    for class_name in classes.split():
        assert class_name in rendered

def test_interactive_states():
    """Test component with interactive state theme tokens"""
    theme = {
        "input": {
            "base": {
                "bg": "white",
                "border": "gray.300",
                "focus": {
                    "border": "blue.500",
                    "ring": "blue.500"
                },
                "error": {
                    "border": "red.500",
                    "text": "red.500"
                }
            }
        }
    }
    
    component = """
    export function Input({ error }) {
        const classes = useThemeTokens("input.base");
        return (
            <input 
                type="text"
                className={classes}
                aria-invalid={error}
            />
        );
    }
    """
    
    rendered = render_component(component, theme=theme, props={"error": True})
    classes = compile_theme_tokens(theme, "input.base")
    
    for class_name in classes.split():
        assert class_name in rendered

def test_theme_composition():
    """Test component using composed theme tokens"""
    theme = {
        "button": {
            "base": {
                "px": "4",
                "py": "2",
                "rounded": "md",
                "font": "semibold"
            },
            "primary": {
                "extends": "base",
                "bg": "blue.500",
                "text": "white"
            }
        }
    }
    
    component = """
    export function Button() {
        const classes = useThemeTokens("button.primary");
        return (
            <button className={classes}>
                Composed Button
            </button>
        );
    }
    """
    
    rendered = render_component(component, theme=theme)
    classes = compile_theme_tokens(theme, "button.primary")
    
    for class_name in classes.split():
        assert class_name in rendered
