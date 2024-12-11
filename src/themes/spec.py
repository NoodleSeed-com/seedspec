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
    primary: str = field(default_factory=lambda: DEFAULT_THEMES["default"]["colors"]["primary"])
    secondary: str = field(default_factory=lambda: DEFAULT_THEMES["default"]["colors"]["secondary"])
    background: str = field(default_factory=lambda: DEFAULT_THEMES["default"]["colors"]["background"])
    surface: str = field(default_factory=lambda: DEFAULT_THEMES["default"]["colors"]["surface"])
    text: str = field(default_factory=lambda: DEFAULT_THEMES["default"]["colors"]["text"])
    error: str = field(default_factory=lambda: DEFAULT_THEMES["default"]["colors"]["error"])
    warning: str = field(default_factory=lambda: DEFAULT_THEMES["default"]["colors"]["warning"])
    success: str = field(default_factory=lambda: DEFAULT_THEMES["default"]["colors"]["success"])

@dataclass
class TypographySpec:
    """Typography specification"""
    fontFamily: Dict[str, str] = field(default_factory=lambda: DEFAULT_FONT_FAMILIES)
    fontSize: Dict[str, str] = field(default_factory=lambda: DEFAULT_FONT_SIZES)
    fontWeight: Dict[str, str] = field(default_factory=lambda: DEFAULT_FONT_WEIGHTS)
    lineHeight: Dict[str, str] = field(default_factory=lambda: DEFAULT_LINE_HEIGHTS)

@dataclass
class SpacingSpec:
    """Spacing specification"""
    xs: str = DEFAULT_SPACING["xs"]
    sm: str = DEFAULT_SPACING["sm"]
    md: str = DEFAULT_SPACING["md"]
    lg: str = DEFAULT_SPACING["lg"]
    xl: str = DEFAULT_SPACING["xl"]
    xxl: str = DEFAULT_SPACING["xxl"]

@dataclass 
class BordersSpec:
    """Borders specification"""
    radius: Dict[str, str] = field(default_factory=lambda: DEFAULT_BORDER_RADIUS)
    width: Dict[str, str] = field(default_factory=lambda: DEFAULT_BORDER_WIDTH)

@dataclass
class ShadowsSpec:
    """Shadows specification"""
    sm: str = DEFAULT_SHADOWS["sm"]
    md: str = DEFAULT_SHADOWS["md"]
    lg: str = DEFAULT_SHADOWS["lg"]

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
