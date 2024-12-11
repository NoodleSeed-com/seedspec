from typing import Dict, Any, Optional
from dataclasses import dataclass, field

@dataclass
class ColorSpec:
    """Color palette specification"""
    primary: str = "#0066cc"
    secondary: str = "#6c757d" 
    background: str = "#ffffff"
    surface: str = "#f8f9fa"
    text: str = "#212529"
    error: str = "#dc3545"
    warning: str = "#ffc107"
    success: str = "#28a745"

@dataclass
class TypographySpec:
    """Typography specification"""
    fontFamily: Dict[str, str] = field(default_factory=lambda: {
        "base": "Inter, system-ui, sans-serif",
        "heading": "Poppins, sans-serif"
    })
    fontSize: Dict[str, str] = field(default_factory=lambda: {
        "xs": "0.75rem",
        "sm": "0.875rem", 
        "base": "1rem",
        "lg": "1.125rem",
        "xl": "1.25rem"
    })
    fontWeight: Dict[str, str] = field(default_factory=lambda: {
        "normal": "400",
        "medium": "500",
        "bold": "700"
    })
    lineHeight: Dict[str, str] = field(default_factory=lambda: {
        "tight": "1.25",
        "normal": "1.5", 
        "relaxed": "1.75"
    })

@dataclass
class SpacingSpec:
    """Spacing specification"""
    xs: str = "0.25rem"
    sm: str = "0.5rem"
    md: str = "1rem"
    lg: str = "1.5rem"
    xl: str = "2rem"
    xxl: str = "3rem"

@dataclass 
class BordersSpec:
    """Borders specification"""
    radius: Dict[str, str] = field(default_factory=lambda: {
        "sm": "0.25rem",
        "md": "0.5rem",
        "lg": "1rem",
        "full": "9999px"
    })
    width: Dict[str, str] = field(default_factory=lambda: {
        "thin": "1px",
        "medium": "2px",
        "thick": "4px"
    })

@dataclass
class ShadowsSpec:
    """Shadows specification"""
    sm: str = "0 1px 2px rgba(0,0,0,0.05)"
    md: str = "0 4px 6px rgba(0,0,0,0.1)"
    lg: str = "0 10px 15px rgba(0,0,0,0.1)"

@dataclass
class ThemeSpec:
    """Complete theme specification that can be defined in Seed specs"""
    theme: str = "default"  # Name of preset theme to use
    colors: ColorSpec = field(default_factory=ColorSpec)
    typography: TypographySpec = field(default_factory=TypographySpec)
    spacing: SpacingSpec = field(default_factory=SpacingSpec)
    borders: BordersSpec = field(default_factory=BordersSpec)
    shadows: ShadowsSpec = field(default_factory=ShadowsSpec)
    overrides: Dict[str, Any] = field(default_factory=dict)  # Optional override values

    def __post_init__(self):
        if self.overrides is None:
            self.overrides = {}

# Example usage in spec:
"""
app MyApp {
  ui {
    theme: "light"  # Use preset theme
    overrides: {
      colors.primary: "#FF0000",  # Override specific values
      typography.fontSize.base: "16px",
      spacing.md: "1.25rem"
    }
  }
}
"""
