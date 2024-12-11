from typing import Dict, Any, Optional
from dataclasses import dataclass, field
from ..stdlib.themes.seed import (
    DEFAULT_COLORS,
    DEFAULT_FONT_FAMILIES,
    DEFAULT_FONT_SIZES,
    DEFAULT_FONT_WEIGHTS,
    DEFAULT_LINE_HEIGHTS,
    DEFAULT_SPACING,
    DEFAULT_BORDER_RADIUS,
    DEFAULT_BORDER_WIDTH,
    DEFAULT_SHADOWS
)

@dataclass
class ColorSpec:
    """Color palette specification"""
    primary: str = DEFAULT_COLORS["primary"]
    secondary: str = DEFAULT_COLORS["secondary"]
    background: str = DEFAULT_COLORS["background"]
    surface: str = DEFAULT_COLORS["surface"]
    text: str = DEFAULT_COLORS["text"]
    error: str = DEFAULT_COLORS["error"]
    warning: str = DEFAULT_COLORS["warning"]
    success: str = DEFAULT_COLORS["success"]

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
