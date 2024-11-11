# Quick Start Guide

## Prerequisites

1. Install SeedML following the [installation guide](installation.md)
2. Set up your Anthropic API key:
```bash
export ANTHROPIC_API_KEY='your-api-key'
```
3. Set up your Google Maps API key (optional):
```bash
export GOOGLE_MAPS_KEY='your-maps-key'
```

## Your First SeedML App

1. Create a new file `todo.seed`:

```yaml
app TodoList {
  # Core domain model
  entity Task {
    title: string
    done: bool = false
    due?: date
    location?: location    # Optional location
  }
  
  # UI definition
  screen Tasks {
    # List view with location awareness
    list: [title, done, due, location]
    actions: [create, toggle-done]
    
    # Optional map view
    map?: {
      markers: incomplete_tasks
      cluster: true
    }
  }
}
```

2. Generate the application:

```bash
seedml todo.seed
```

This will create a basic application with:
- React + TypeScript frontend (alpha)
- FastAPI backend (alpha)
- MySQL database schema
- Basic API documentation
- Interactive maps (when location fields are used)
- Geocoding support

Note: SeedML is currently in early alpha. Many features are still under development and the generated code should be reviewed carefully before use in production.

Note: Location features require a Google Maps API key. Without the key, the application will still work but location features will be disabled. Features can be enabled later by adding the API key to your environment.

## Next Steps

1. Add more features to your todo app
2. Learn about [Core Concepts](../core-concepts/overview.md)
3. Try the [First Application Tutorial](first-app.md)
