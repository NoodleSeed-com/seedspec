# UI Patterns

SeedML provides simple, consistent UI patterns for rapid application development.

## Basic Screen Types

```yaml
# List Screen
screen List {
  list: [field1, field2]        # Fields to display
  actions: [create, edit]       # Basic actions
}

# Form Screen
screen Form {
  form: [field1, field2]        # Form fields
  actions: [save, cancel]       # Form actions
}

# Detail Screen
screen Detail {
  content: [field1, field2]     # Content fields
  actions: [edit, delete]       # Item actions
}

# Dashboard Screen
screen Dashboard {
  summary: [metric1, metric2]   # Key metrics
  lists: [recent, popular]      # Data lists
}
```

## Key Features

### 1. Simple Layouts
```yaml
# Single column layout (default)
screen UserList {
  list: [name, email]
}

# Split layout
screen OrderDetail {
  layout: split
  left: [customer, items]
  right: [summary, actions]
}
```

### 2. Standard Actions
```yaml
# Common actions included
actions: [
  create,              # Create new
  edit,               # Edit existing
  delete,             # Delete item
  save,               # Save changes
  cancel              # Cancel form
]
```

### 3. Built-in Features
```yaml
# Automatic features
features: {
  search: true        # Search functionality
  sort: true         # Column sorting
  pagination: true   # Page navigation
}
```

## Best Practices

1. **Keep It Simple**
   - Use standard layouts
   - Stick to common patterns
   - Avoid complex customization

2. **Consistent Experience**
   - Standard action names
   - Common feature set
   - Familiar patterns

3. **Rapid Development**
   - Minimal configuration
   - Smart defaults
   - Quick prototyping
