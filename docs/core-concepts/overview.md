# Core Concepts

SeedML is built on simple but powerful concepts that work together:

## Modular Specifications

Apps can be defined across multiple files:

```yaml
# app.seed - Core app definition
app TodoList {
  # Data model
  entity Task {
    title: string
    done: bool
  }
}

# ui.seed - UI components
extend TodoList {
  # User interface
  screen Tasks {
    list: [title, done]
    actions: [create, complete]
  }
}
```

## Key Ideas

```yaml
# Everything in one place
app TodoList {
  # Data model
  entity Task {
    title: string
    done: bool
  }

  # Business rules
  rules {
    complete: {
      validate: !done
      then: done = true
    }
  }

  # User interface
  screen Tasks {
    list: [title, done]
    actions: [create, complete]
  }
}
```

## Core Features

1. **Smart Defaults**
   - Production patterns built-in
   - Override only when needed
   - Progressive enhancement

2. **Clear Intent**
   - Express what you want
   - Not how to build it
   - Natural language

3. **Full Stack**
   - One specification
   - Complete application
   - Modern tech stack

## Learn More

1. [Type System](type-system.md)
   - Basic types
   - Validation
   - Relationships

2. [Business Rules](business-rules.md)
   - Simple validation
   - Clear workflows
   - Computed fields

3. [UI Patterns](ui-patterns.md)
   - Standard layouts
   - Common components
   - Best practices

4. [Theming](theming.md)
   - Hierarchical themes
   - Simple overrides
   - Visual consistency
