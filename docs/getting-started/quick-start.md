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

This will create a complete application with:
- React + TypeScript frontend
- FastAPI backend 
- MySQL database
- Testing suite
- API documentation

Note: This is an alpha release with basic functionality. More features coming soon.

## Next Steps

1. Add more features to your todo app
2. Learn about [Core Concepts](../core-concepts/overview.md)
3. Try the [First Application Tutorial](first-app.md)
