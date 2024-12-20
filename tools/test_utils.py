import re
from pathlib import Path
import shutil
import tempfile
from typing import Optional, Dict, Any

def render_component(
    component: str,
    theme: dict,
    darkTheme: Optional[dict] = None,
    props: Optional[Dict[str, Any]] = None
) -> str:
    """
    Simulate rendering a React component with theme tokens.
    Returns the className string that would be applied to the component.
    
    Args:
        component: String containing React component code
        theme: Theme configuration dictionary
        darkTheme: Optional dark mode theme configuration
        props: Optional component props
    
    Returns:
        String of space-separated CSS classes
    """
    # Extract className from component
    class_match = re.search(r'className=\{([^}]+)\}', component)
    if not class_match:
        return ""
        
    # Extract the token path from useThemeTokens call
    token_match = re.search(r'useThemeTokens\("([^"]+)"', component)
    if not token_match:
        # If no useThemeTokens found, return the literal className value
        return class_match.group(1) if class_match else ""
            
    from tools.compile_react_theme import compile_theme_tokens
    
    # Get classes for light theme
    classes = compile_theme_tokens(theme, token_match.group(1))
    
    # Add dark theme classes if provided
    if darkTheme:
        dark_classes = compile_theme_tokens(darkTheme, token_match.group(1), mode="dark")
        if dark_classes:
            classes = f"{classes} {dark_classes}"
            
    return classes

def cleanup_after_test():
    """Clean up any temporary files or state after each test"""
    # Clean up any temporary directories
    temp_dir = Path(tempfile.gettempdir()) / "seedspec-test"
    if temp_dir.exists():
        shutil.rmtree(temp_dir)
