# Quick Start Guide

Get up and running with SeedML in minutes.

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
seedml generate todo.seed
```

3. Run your app:

```bash
cd todo-app
seedml run
```

Visit `http://localhost:3000` to see your running application!

## Key Concepts Demonstrated

- Entity definition with fields
- Basic types and defaults
- Simple UI generation
- CRUD operations

## Next Steps

1. Add more features to your todo app:
   - User authentication
   - Categories/tags
   - Due date reminders

2. Learn about:
   - [Core Concepts](../core-concepts/overview.md)
   - [Type System](../core-concepts/type-system.md)
   - [UI Patterns](../core-concepts/ui-patterns.md)

3. Try the [First Application Tutorial](first-app.md)
