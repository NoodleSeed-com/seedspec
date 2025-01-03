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
- [ ] Parser unit tests
- [ ] Generator unit tests
- [ ] Integration tests
- [ ] Theme validation tests
- [ ] LLM generation tests

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
    primary: "#4F46E5"  // Indigo
    secondary: "#10B981" // Emerald
    neutral: {
      50: "#F9FAFB"
      100: "#F3F4F6"
      900: "#111827"
    }
    semantic: {
      success: "#10B981"
      error: "#EF4444"
      warning: "#F59E0B"
    }
  }

  typography {
    fonts: {
      sans: "system-ui, -apple-system, sans-serif"
      mono: "ui-monospace, monospace"
    }
    sizes: {
      base: "1rem"
      lg: "1.125rem"
      xl: "1.25rem"
    }
  }

  components {
    button: {
      base: "rounded-md font-medium transition-colors"
      primary: "bg-primary text-white hover:bg-primary/90"
      secondary: "bg-secondary text-white hover:bg-secondary/90"
    }
    input: {
      base: "rounded-md border border-neutral-200"
      focus: "ring-2 ring-primary/50"
    }
    card: {
      base: "bg-white rounded-lg shadow-sm p-4"
    }
  }
}
```

### Default Dark Theme
```seed
// @stdlib/themes/dark.seed
theme Dark "SeedSpec Dark Theme" {
  metadata {
    version: "1.0.0"
    description: "Default dark theme with reduced eye strain"
  }

  colors {
    primary: "#818CF8"   // Lighter indigo
    secondary: "#34D399" // Lighter emerald
    neutral: {
      50: "#18181B"
      100: "#27272A"
      900: "#FAFAFA"
    }
    semantic: {
      success: "#34D399"
      error: "#F87171"
      warning: "#FBBF24"
    }
  }
  // Inherits other properties from Default theme
}
```

## 2. Theme Extension Syntax

```seed
// custom-theme.seed
import { Default } from "@stdlib/themes"

theme Corporate extends Default {
  metadata {
    version: "1.0.0"
    description: "Corporate brand theme"
  }

  colors {
    primary: "#0047AB"   // Corporate blue
    secondary: "#50C878" // Corporate green
  }
  // Inherits other properties from Default theme
}
```

## 3. LLM-Optimized Theme Generation

Themes can be generated from natural language descriptions:

```seed
// Example LLM prompt: "Generate a modern, professional theme with blue and gray tones"
theme ModernPro {
  metadata {
    version: "1.0.0"
    description: "Modern professional theme with blue and gray accents"
    generated: true
    prompt: "Modern professional theme with blue and gray tones"
  }

  colors {
    primary: "#2563EB"
    secondary: "#64748B"
    // ... LLM generates complete color palette
  }

  // ... LLM generates complete theme
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
            'components': self.parse_components()
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
                    'colors': theme['colors'],
                    'typography': theme['typography']
                }
            }
        }
        # Write config

    def generate_theme_tokens(self, theme):
        """Generate theme.js with design tokens"""
        # Generate JavaScript theme tokens

    def generate_component_styles(self, theme):
        """Generate component-specific styles"""
        # Generate component style utilities
```

### c. Standard Library Integration

```python
class StdLibManager:
    def get_standard_theme(self, theme_name):
        """Load standard library theme"""
        if theme_name == 'Default':
            return self.load_theme('@stdlib/themes/default.seed')
        elif theme_name == 'Dark':
            return self.load_theme('@stdlib/themes/dark.seed')
```

### d. LLM Theme Generation (seed_compiler/llm_theme_generator.py)

```python
class LLMThemeGenerator:
    def generate_theme(self, prompt):
        """Generate theme based on natural language prompt"""
        # Use LLM to generate complete theme specification
        return {
            'metadata': {
                'generated': True,
                'prompt': prompt
            },
            # ... generated theme properties
        }

    def extend_theme(self, base_theme, prompt):
        """Extend existing theme based on prompt"""
        # Use LLM to generate theme extensions
```

## 5. Usage in Apps

```seed
import { Dark } from "@stdlib/themes"
import { Corporate } from "./themes/corporate.seed"

app MyApp "My Application" {
  // Use standard dark theme
  use theme Dark

  // Or use custom theme
  use theme Corporate

  // Or generate theme with LLM
  use theme generate "Modern professional theme with blue accents"

  // Rest of app specification
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
- Maintains SeedSpec's declarative nature
- Leverages LLMs for theme generation
- Provides standard themes out of the box
- Enables easy theme customization and extension
- Keeps the syntax simple and readable
- Supports modular theme development
- Generates optimized output for React/Tailwind

The system is designed to be both powerful for advanced users who want to create custom themes from scratch, and accessible for users who prefer to use standard themes or LLM-generated themes with minimal configuration.

## Reference Files

To implement this theming system, an LLM should analyze these key files from the project:

### Core Files
- `seed_compiler/parser.py` - To understand how to parse seed files and add theme parsing
- `seed_compiler/generator.py` - To understand how to generate React/Tailwind output and add theme generation
- `seed_compiler/templates/Screen.js.tmpl` - To understand current component templating and styling
- `seed_compiler/templates/App.js.tmpl` - To understand app-level structure and where theme provider should be added

### Example Files
- `examples/todo.seed` - To understand current seed file structure and where theme syntax fits
- `examples/expenses.seed` - Another example of seed file structure

### Documentation
- `docs/styling.md` - Current styling documentation
- `docs/components.md` - To understand component system for theme integration
- `docs/concepts-and-structure.md` - To understand overall architecture

### Test Files
- `tests/test_parser.py` - To understand current parsing tests and add theme parsing tests
- `tests/test_generator.py` - To understand current generation tests and add theme generation tests
- `tests/test_integration.py` - To understand end-to-end testing

These files provide the necessary context for:
1. Current parsing and generation system
2. Component templating and styling approach
