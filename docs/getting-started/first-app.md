# Building Your First Application

This tutorial walks through creating a complete task management application with SeedML.

## 1. Project Setup

Create a new directory and file:

```bash
mkdir task-manager
cd task-manager
touch app.seed
```

## 2. Basic Structure

Add this initial structure to `app.seed`:

```yaml
app TaskManager {
  # We'll add components here
}
```

## 3. Adding Data Models

Expand your app with data models:

```yaml
app TaskManager {
  entity Task {
    title: string!
    description: text
    status: todo->doing->done
    priority: low/medium/high = medium
    due?: date
    assigned?: User
  }

  entity User {
    name: string!
    email: email!
    role: member/admin = member
  }
}
```

## 4. Creating Screens

Add user interface screens:

```yaml
app TaskManager {
  # ... previous code ...

  screen TaskBoard {
    list: [title, assigned, priority, due]
    view: kanban(status)
    actions: [create, edit, assign]
    search: [title, assigned]
  }

  screen TaskDetail {
    layout: split
    left: [title, description, status]
    right: [assigned, due, priority]
    actions: [save, delete]
  }
}
```

## 5. Adding Business Rules

Implement task management logic:

```yaml
app TaskManager {
  # ... previous code ...

  rules {
    assign_task: {
      require: role.member
      validate: assigned != null
      then: notify@assigned
    }

    complete_task: {
      require: [
        status == doing,
        assigned == current_user
      ]
      then: [
        update_status(done),
        notify@created_by
      ]
    }
  }
}
```

## 6. Running Your App

Generate and run the application:

```bash
seedml generate app.seed
cd task-manager-app
seedml run
```

## What You've Learned

- Basic SeedML project structure
- Entity definition and relationships
- Screen layouts and components
- Business rules and validation
- Application generation and deployment

## Next Steps

1. Add more features:
   - Comments on tasks
   - File attachments
   - Time tracking
   - Reports

2. Learn about:
   - [Advanced Patterns](../reference/patterns.md)
   - [Integration](../core-concepts/integration.md)
   - [Security](../core-concepts/security.md)
