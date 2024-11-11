# UI Patterns

SeedML provides a rich set of UI patterns for building consistent, interactive user interfaces.

## Basic Layouts

```yaml
screen Dashboard {
  # Common layout patterns
  layout: grid(3x2)  # Grid layout
  layout: split      # Split view
  layout: tabs       # Tabbed interface
  layout: kanban     # Kanban board
}
```

## Components

### 1. Lists and Tables
```yaml
screen Products {
  list: {
    columns: [name, price, status]
    actions: [edit, delete]
    features: [search, filter, sort]
  }
}
```

### 2. Forms
```yaml
screen OrderForm {
  form: {
    sections: [
      customer: [name!, email!, phone?],
      items: editable_table,
      notes: textarea
    ]
    
    validation: inline
    actions: [save_draft, submit]
  }
}
```

### 3. Cards
```yaml
screen Projects {
  cards: {
    layout: grid
    show: [
      title,
      description.preview,
      status.badge,
      team.avatars
    ]
  }
}
```

## Interaction Patterns

### 1. Actions
```yaml
actions: {
  primary: [create, submit],
  item: [edit, delete],
  batch: [export, archive]
}
```

### 2. Navigation
```yaml
nav: {
  main: [dashboard, orders, customers],
  user: [profile, settings, logout]
}
```

### 3. Feedback
```yaml
feedback: {
  validation: inline,
  messages: toast,
  loading: skeleton
}
```

## Best Practices

1. **Consistency**
   - Use standard patterns
   - Maintain visual hierarchy
   - Follow platform conventions

2. **Responsiveness**
   - Mobile-first design
   - Flexible layouts
   - Adaptive components

3. **Accessibility**
   - Semantic markup
   - Keyboard navigation
   - Screen reader support

4. **Performance**
   - Lazy loading
   - Progressive enhancement
   - Optimized rendering
