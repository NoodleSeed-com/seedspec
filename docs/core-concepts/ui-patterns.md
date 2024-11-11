# UI Patterns

SeedML generates complete user interfaces from simple, intent-focused patterns that automatically implement best practices.

## Core Concepts

```yaml
screen Orders {
  # Smart list with built-in features
  list orders {
    show: [date, customer, total, status]
    actions: [view, edit]      # Standard handlers
    features: [search, filter] # Common patterns
  }

  # Intent-focused forms
  form new_order {
    fields: [
      customer: select,    # Smart field types
      items: table,        # Complex components
      notes: text         # Simple inputs
    ]
    actions: [save, submit]
  }
}
```

## Key Features

### 1. Smart Lists
```yaml
list products {
  # Automatic features based on data
  show: [name, price, stock]  # Proper formatting
  group: category            # Built-in grouping
  sort: [-created_at]        # Default sorting
}
```

### 2. Intent-Based Forms
```yaml
form user {
  # Smart field handling
  fields: [
    email,           # Validation included
    password,        # Security built-in
    role: select     # UI components chosen
  ]
  layout: sections   # Responsive design
}
```

### 3. Navigation Patterns
```yaml
nav {
  # Complete navigation structure
  main: [dashboard, orders, customers]
  user: [profile, settings]
  mobile: bottom_tabs
}
```

## Best Practices

1. **Express Intent**
   - Focus on business needs
   - Use clear patterns
   - Trust smart defaults

2. **User Experience**
   - Consistent interfaces
   - Responsive design
   - Accessibility built-in

3. **Performance**
   - Automatic optimization
   - Smart loading
   - Efficient updates
