from typing import Dict, Any, Optional
from dataclasses import dataclass, field
from pathlib import Path
from ..parser import parse_seed_file

def load_default_themes():
    """Load theme definitions from stdlib/themes.seed"""
    themes_file = Path(__file__).parent.parent / "stdlib" / "themes.seed"
    return parse_seed_file(themes_file)

# Load themes at module import
DEFAULT_THEMES = load_default_themes()

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
    fontFamily: Dict[str, str] = field(default_factory=lambda: DEFAULT_THEMES["default"]["typography"]["fontFamily"])
    fontSize: Dict[str, str] = field(default_factory=lambda: DEFAULT_THEMES["default"]["typography"]["fontSize"])
    fontWeight: Dict[str, str] = field(default_factory=lambda: DEFAULT_THEMES["default"]["typography"]["fontWeight"])
    lineHeight: Dict[str, str] = field(default_factory=lambda: DEFAULT_THEMES["default"]["typography"]["lineHeight"])

@dataclass
class SpacingSpec:
    """Spacing specification"""
    xs: str = field(default_factory=lambda: DEFAULT_THEMES["default"]["spacing"]["xs"])
    sm: str = field(default_factory=lambda: DEFAULT_THEMES["default"]["spacing"]["sm"])
    md: str = field(default_factory=lambda: DEFAULT_THEMES["default"]["spacing"]["md"])
    lg: str = field(default_factory=lambda: DEFAULT_THEMES["default"]["spacing"]["lg"])
    xl: str = field(default_factory=lambda: DEFAULT_THEMES["default"]["spacing"]["xl"])
    xxl: str = field(default_factory=lambda: DEFAULT_THEMES["default"]["spacing"]["xxl"])

@dataclass 
class BordersSpec:
    """Borders specification"""
    radius: Dict[str, str] = field(default_factory=lambda: DEFAULT_THEMES["default"]["borders"]["radius"])
    width: Dict[str, str] = field(default_factory=lambda: DEFAULT_THEMES["default"]["borders"]["width"])

@dataclass
class ShadowsSpec:
    """Shadows specification"""
    sm: str = field(default_factory=lambda: DEFAULT_THEMES["default"]["shadows"]["sm"])
    md: str = field(default_factory=lambda: DEFAULT_THEMES["default"]["shadows"]["md"])
    lg: str = field(default_factory=lambda: DEFAULT_THEMES["default"]["shadows"]["lg"])

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
