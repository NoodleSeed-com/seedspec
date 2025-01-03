# SeedSpec Theming System Implementation Plan

## Overview

This document outlines the implementation plan for adding a robust theming system to SeedSpec that aligns with the framework's core goals:
- Optimized for Generation with LLMs
- Deterministic and Declarative
- Easy to Read and Understand
- Modular Design with explicit imports

## Development Status

### Parser
- [ ] Theme block syntax parsing
- [ ] Theme extension/inheritance parsing
- [ ] Theme import parsing
- [ ] Theme validation rules
- [ ] Integration with existing parser

### Generator
- [ ] Tailwind config generation from theme
- [ ] Theme tokens file generation
- [ ] Component styles generation
- [ ] Theme provider integration
- [ ] Dark mode support

### Standard Library
- [ ] Default light theme implementation
- [ ] Default dark theme implementation
- [ ] Theme extension utilities
- [ ] Theme type definitions

### LLM Integration
- [ ] Theme generation from prompts
- [ ] Theme extension from prompts
- [ ] Color scheme generation
- [ ] Component style generation

### Testing
- [x] Parser unit tests
  - Theme block structure parsing
  - Theme extension/inheritance
  - Color reference resolution
  - Color modifier application
  - Theme validation rules
  - Theme import parsing
  - Theme usage in apps
- [x] Generator unit tests
  - Tailwind config generation
  - Theme token generation
  - Component style generation
  - Dark mode configuration
  - Theme provider generation
  - Themed component generation
- [x] Integration tests
  - End-to-end theme application
  - Theme inheritance chain
  - Dark mode integration
  - Color resolution and modifiers
  - Theme switching capabilities
  - Component theme application
- [x] Theme validation tests
  - Color scheme validation
  - Typography validation
  - Spacing/sizing validation
  - Theme inheritance validation
  - Color modifier validation
- [x] LLM generation tests
  - Theme generation from prompts
  - Color scheme generation
  - Prompt color extraction
  - Theme modification validation
  - Theme extension validation

### Documentation
- [ ] Theme specification docs
- [ ] Theme development guide
- [ ] Standard library theme docs
- [ ] LLM theme generation docs

Current Status: 🚧 Planning Phase
Next Steps: Begin implementation of theme parsing and basic Tailwind integration

## 1. Standard Library Themes (@stdlib/themes)

### Default Light Theme
```seed
// @stdlib/themes/default.seed
theme Default "SeedSpec Default Theme" {
  metadata {
    version: "1.0.0"
    description: "Default light theme optimized for readability and accessibility"
  }

  colors {
    // Base colors with semantic meaning
    primary: ocean-blue
    secondary: forest-green
    background: white
    text: black
    
    // Status colors
    success: emerald-green
    error: ruby-red
    warning: california-gold
    info: mediterranean-blue
    
    // Interaction states
    hover: primary.light
    active: primary.dark
    disabled: slate-gray
    selected: primary.pale
    
    // Feedback states
    valid: success
    invalid: error
    pending: info
    
    // Structural elements
    border: slate-gray.light
    divider: slate-gray.pale
    shadow: black.transparent
    overlay: black.transparent
    
    // Content hierarchy
    heading: text.dark
    body: text
    caption: text.light
    placeholder: text.pale
    
    // Interactive elements
    link: primary
    linkVisited: primary.dark
    button: primary
    buttonText: white
    
    // Form elements
    input: white
    inputBorder: border
    inputFocus: primary
    inputPlaceholder: placeholder
    
    // Navigation
    nav: background.dark
    navText: text.light
    navActive: primary
    
    // Emphasis
    highlight: sunset-yellow.pale
    accent: coral-green
    
    // Surfaces
    card: white
    modal: white
    tooltip: text.dark
    
    // System
    focus: primary
    selection: primary.pale
  }

  typography {
    fonts: {
      body: sans
      heading: sans
      mono: mono
    }
    
    weights: {
      light: 300
      regular: 400
      medium: 500
      bold: 700
    }
    
    sizes: {
      xs: 0.75
      sm: 0.875
      base: 1
      lg: 1.125
      xl: 1.25
      "2xl": 1.5
      "3xl": 1.875
      "4xl": 2.25
    }
    
    lineHeights: {
      tight: 1.25
      base: 1.5
      loose: 1.75
    }
  }

  spacing {
    xs: 0.25
    sm: 0.5
    base: 1
    lg: 1.5
    xl: 2
    "2xl": 3
    "3xl": 4
  }

  radii {
    none: 0
    sm: 0.125
    base: 0.25
    lg: 0.5
    full: 9999
  }
}
```

### Default Dark Theme
```seed
// @stdlib/themes/dark.seed
theme Dark extends Default {
  metadata {
    version: "1.0.0"
    description: "Default dark theme with reduced eye strain"
  }

  colors {
    // Invert main colors
    background: midnight-black
    text: pearl-white
    
    // Adjust color intensities
    primary: ocean-blue.light
    secondary: forest-green.light
    
    // Adjust surfaces
    card: background.light
    modal: background.light
    
    // Adjust states
    hover: primary.pale
    selected: primary.dark
  }
}
```

## 2. Theme Extension Example

```seed
import { Default } from "@stdlib/themes"

theme Corporate extends Default {
  colors {
    primary: california-blue
    secondary: forest-green
    accent: coral-green
    
    // Use modifiers
    hover: primary.light
    active: primary.dark
    
    // Direct hex for exact brand color
    brand: "#FF5733"
  }
}
```

## 3. LLM-Optimized Theme Generation

Themes can be generated from natural language descriptions:

```seed
// Example: "Generate a modern tech startup theme with ocean vibes"
theme ModernTech extends Default {
  colors {
    primary: ocean-blue
    secondary: coral-green
    accent: mediterranean-blue
    background: slate-gray.light
  }
}
```

## 4. Implementation Steps

### a. Parser Updates (seed_compiler/parser.py)

```python
class ThemeParser:
    def parse_theme(self, theme_spec):
        """Parse theme specification"""
        return {
            'metadata': self.parse_metadata(),
            'colors': self.parse_colors(),
            'typography': self.parse_typography(),
            'spacing': self.parse_spacing(),
            'radii': self.parse_radii()
        }

    def parse_theme_extension(self, base_theme, extensions):
        """Handle theme inheritance"""
        return self.merge_themes(base_theme, extensions)
```

### b. Generator Updates (seed_compiler/generator.py)

```python
class ThemeGenerator:
    def generate_theme_files(self, theme, output_dir):
        """Generate theme-related files"""
        self.generate_tailwind_config(theme)
        self.generate_theme_tokens(theme)
        self.generate_component_styles(theme)

    def generate_tailwind_config(self, theme):
        """Generate tailwind.config.js with theme tokens"""
        config = {
            'theme': {
                'extend': {
                    'colors': self.transform_colors(theme.colors),
                    'typography': theme.typography,
                    'spacing': theme.spacing,
                    'borderRadius': theme.radii
                }
            }
        }
        return config

    def transform_colors(self, colors):
        """Transform semantic color names to actual values"""
        return self.resolve_color_references(colors)

    def generate_theme_tokens(self, theme):
        """Generate theme.js with design tokens"""
        tokens = {
            'colors': self.transform_colors(theme.colors),
            'typography': theme.typography,
            'spacing': theme.spacing,
            'radii': theme.radii
        }
        return tokens

    def generate_component_styles(self, theme):
        """Generate component-specific styles"""
        styles = self.generate_component_classes(theme)
        return styles
```

### c. Standard Library Integration

```python
class StdLibManager:
    def get_standard_theme(self, theme_name):
        """Load standard library theme"""
        themes = {
            'Default': self.load_theme('@stdlib/themes/default.seed'),
            'Dark': self.load_theme('@stdlib/themes/dark.seed')
        }
        return themes.get(theme_name)

    def resolve_color(self, color_name):
        """Resolve semantic color name to actual value"""
        # Basic colors
        basic_colors = {
            'red': '#EF4444',
            'blue': '#3B82F6',
            'green': '#10B981',
            'yellow': '#F59E0B',
            'purple': '#8B5CF6',
            'orange': '#F97316'
        }
        
        # Geographic colors
        geographic_colors = {
            'california-blue': '#0077BE',
            'mediterranean-blue': '#1A5F7A',
            'california-gold': '#FDB515'
        }
        
        # Natural colors
        natural_colors = {
            'coral-green': '#84B082',
            'forest-green': '#228B22',
            'ocean-blue': '#00A0B0',
            'sunset-yellow': '#FAD6A5',
            'midnight-black': '#141414',
            'pearl-white': '#F5F5F1'
        }
        
        # Material colors
        material_colors = {
            'slate-gray': '#708090',
            'ruby-red': '#E0115F',
            'emerald-green': '#50C878'
        }
        
        # Combine all color maps
        all_colors = {
            **basic_colors,
            **geographic_colors,
            **natural_colors,
            **material_colors
        }
        
        # Handle modifiers (light, dark, pale, bright)
        if '.' in color_name:
            base, modifier = color_name.split('.')
            if base in all_colors:
                return self.apply_modifier(all_colors[base], modifier)
                
        # Handle direct hex values
        if color_name.startswith('#'):
            return color_name
            
        return all_colors.get(color_name)
```

### d. LLM Theme Generation (seed_compiler/llm_theme_generator.py)

```python
class LLMThemeGenerator:
    def generate_theme(self, prompt):
        """Generate theme based on natural language prompt"""
        return {
            'metadata': {
                'generated': True,
                'prompt': prompt
            },
            'colors': self.generate_color_scheme(prompt),
            'typography': self.generate_typography(prompt),
            'spacing': self.generate_spacing(prompt),
            'radii': self.generate_radii(prompt)
        }

    def generate_color_scheme(self, prompt):
        """Generate semantic color choices based on prompt"""
        return self.analyze_prompt_for_colors(prompt)
```

## 5. Usage in Apps

```seed
import { Dark } from "@stdlib/themes"

app MyApp "My Application" {
  // Use standard dark theme
  use theme Dark

  // Or use custom theme
  use theme Corporate

  // Or generate theme with LLM
  use theme generate "Modern professional theme"
}
```

## 6. Theme Development Workflow

1. Start with standard library themes (@stdlib/themes/default.seed or @stdlib/themes/dark.seed)
2. Use LLM to generate custom themes based on natural language descriptions
3. Fine-tune generated themes manually if needed
4. Create theme variations through extension
5. Share themes via npm packages

## Benefits

This implementation:
- Supports intuitive basic colors (red, blue, green)
- Provides rich descriptive colors (california-blue, coral-green)
- Allows color modifiers (light, dark, pale, bright)
- Enables direct hex values for brand precision
- Maps naturally to human language for LLM generation
- Maintains simplicity while offering designer flexibility

The system creates a natural bridge between human color perception, designer needs, and technical implementation through an expressive yet simple naming system.

## Reference Files

### Core Files
- `seed_compiler/parser.py` - Theme parsing implementation
- `seed_compiler/generator.py` - Theme generation and Tailwind integration
- `seed_compiler/templates/Screen.js.tmpl` - Component templating and styling
- `seed_compiler/templates/App.js.tmpl` - App-level theme provider integration

### Example Files
- `examples/todo.seed` - Basic theme usage example
- `examples/themed-todo.seed` - Advanced theme customization example

### Documentation
- `docs/styling.md` - Theme system usage guide
- `docs/components.md` - Component theming guide
- `docs/concepts-and-structure.md` - Theme architecture overview

### Test Files
- `tests/test_parser.py` - Theme parsing tests
- `tests/test_generator.py` - Theme generation tests
- `tests/test_integration.py` - End-to-end theme tests
