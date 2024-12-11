# Theming

Seed Spec provides a simple hierarchical theming system.

## Basic Usage

```yaml
app MyApp {
  ui {
    theme: "light"  # Use built-in light theme
  }
}
```

## Theme Hierarchy

Themes inherit from parent themes:
```ascii
           ┌─────────┐
           │ default │ Base theme
           └────┬────┘
                │
        ┌───────┴───────┐
        │               │
    ┌───┴───┐       ┌───┴───┐
    │ light │       │ dark  │
    └───────┘       └───────┘
```

## Theme Overrides

Override specific values while keeping other defaults:

```yaml
app MyApp {
  ui {
    theme: "light"
    overrides: {
      colors.primary: "#0066cc"
    }
  }
}
```

## Smart Defaults

The theme system follows Seed's smart defaults principle:
- Built-in themes provide production-ready styling
- Override only what needs to be different
- Maintain consistent visual patterns
