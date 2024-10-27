# Quick Start Guide

## Prerequisites

1. Install SeedML following the [installation guide](installation.md)
2. Set up your Anthropic API key:
```bash
export ANTHROPIC_API_KEY='your-api-key'
```

## Your First SeedML App

1. Create a new file `todo.seed`:

```yaml
app TodoList {
  entity Task {
    title: string
    done: bool = false
    due?: date
  }

  screen Tasks {
    list: [title, done, due]
    actions: [create, toggle-done]
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

Note: SeedML is currently in early alpha. Many features are still under development and the generated code should be reviewed carefully before use in production.

## Next Steps

1. Add more features to your todo app
2. Learn about [Core Concepts](../core-concepts/overview.md)
3. Try the [First Application Tutorial](first-app.md)
