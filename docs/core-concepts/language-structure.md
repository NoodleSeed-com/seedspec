# Language Structure

SeedML uses a clean, hierarchical syntax designed for both human readability and machine parsing. The language structure follows a logical organization that maps directly to application components.

## Core Structure

Every SeedML application follows this high-level structure:

```yaml
app [AppName] {
  # Configuration
  meta: { ... }
  
  # Data Layer
  entity [EntityName] { ... }
  
  # Business Layer  
  rules { ... }
  
  # Presentation Layer
  screens { ... }
  
  # Integration Layer
  integrate { ... }
}
```

## Key Components

### 1. Meta Configuration
Global application settings and metadata:
```yaml
meta {
  name: "My App"
  version: "1.0"
  description: "App description"
}
```

### 2. Entities
Data models with built-in validation:
```yaml
entity User {
  name: string!     # Required
  email: email      # Validated
  role: admin/user  # Enum
  active: bool = true
}
```

### 3. Business Rules
Logic and workflow definitions:
```yaml
rules {
  createOrder: {
    require: [
      user.verified,
      items.length > 0
    ]
    validate: total > 0
    then: notify@sales
  }
}
```

### 4. Screens
UI components and layouts:
```yaml
screen Dashboard {
  layout: grid(3x2)
  widgets: [
    stats: counter(orders),
    chart: trend(sales),
    tasks: list(pending)
  ]
  actions: [refresh, export]
}
```

### 5. Integrations
External service connections:
```yaml
integrate {
  auth: {
    provider: oauth2
    config: { ... }
  }
  storage: s3
  email: sendgrid
}
```

## Best Practices

1. **Organization**
   - Group related entities together
   - Keep rules close to their entities
   - Structure screens by user workflow

2. **Naming**
   - Use clear, descriptive names
   - Follow consistent conventions
   - Reflect business terminology

3. **Modularity**
   - Break large apps into modules
   - Reuse common patterns
   - Keep components focused

4. **Documentation**
   - Comment complex logic
   - Document business rules
   - Explain custom patterns
