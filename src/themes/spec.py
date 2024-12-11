from typing import Dict, Any, Optional
from dataclasses import dataclass

@dataclass
class ThemeSpec:
    """Minimal theme specification that can be defined in Seed specs"""
    theme: str = "default"  # Name of preset theme to use
    overrides: Dict[str, Any] = None  # Optional override values

    def __post_init__(self):
        if self.overrides is None:
            self.overrides = {}

# Example usage in spec:
"""
app MyApp {
  ui {
    theme: "light"  # Use preset theme
    overrides: {
      colors.primary: "#FF0000"  # Override specific values
    }
  }
}
"""
