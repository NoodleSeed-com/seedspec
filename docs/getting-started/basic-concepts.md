# Basic Concepts

Learn the core concepts of SeedML development.

## Application Structure

SeedML applications can be organized in multiple files using the `extend` keyword:

```yaml
# core.seed - Core app definition
app MyApp {
  # Data models
  entity Task {
    title: string
    done: bool
  }
}

# ui.seed - UI components
extend MyApp {
  # Theme configuration
  ui {
    theme: "light"  # Use built-in theme
  }

  # Screens
  screen Tasks {
    list: [title, done]
    actions: [create, complete]
  }
}
```

Every SeedML application has these main parts:

### 1. Data Models (Entities)

Define your data structure:

```yaml
entity Task {
  title: string           # Text fields
  done: bool = false      # Boolean with default
  due: date              # Date field
  assigned: User         # Reference another entity
  items: [Item]          # Simple list
}
```

### 2. User Interface (Screens)

Define your views:

```yaml
screen TaskList {
  # List view
  list: [title, done, due]
  actions: [create, edit, delete]
}

screen TaskForm {
  # Form view  
  form: [title, due, assigned]
  actions: [save]
}
```

### 3. Business Rules

Define basic validation and logic:

```yaml
rules {
  # Validation
  validate: due > today
  require: title != null

  # Simple actions
  then: notify_assigned
}
```

## Key Principles

### 1. Keep It Simple
- Focus on core features
- Use basic types
- Minimal configuration

### 2. Smart Defaults
- Common patterns built-in
- Sensible behaviors
- Easy to get started

### 3. Full Stack
- One specification
- Generates complete app
- Ready to run

## Basic Types

```yaml
# Available field types
string              # Text
number              # Numbers
bool                # True/False
date                # Dates
[Type]              # Lists
Reference           # Entity references
```

## Common Patterns

### 1. Fields
```yaml
fields {
  required: string         # Required field
  optional: string?        # Optional field
  default: bool = false    # Default value
}
```

### 2. Views
```yaml
screens {
  list: [field1, field2]   # List view
  form: [field1, field2]   # Form view
}
```

### 3. Actions
```yaml
actions: [
  create,                  # Create new
  edit,                    # Edit existing
  delete                   # Delete item
]
```

## Next Steps

1. Try the [Quick Start Guide](quick-start.md)
2. Build your [First Application](first-app.md)
3. See [Examples](../examples/basic-crud.md)
