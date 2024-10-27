# Language Structure

## Basic Syntax

SeedML uses a clean, hierarchical syntax that is both human-readable and machine-parseable:

```yaml
app [AppName] {
  # Global Configuration
  meta: { ... }
  
  # Data Models
  entity [EntityName] { ... }
  
  # Business Rules
  rules { ... }
  
  # User Interface
  screens { ... }
  
  # Integrations
  integrate { ... }
}
```

## Key Components

### 1. Entities
Define your data models and their relationships:
```yaml
entity User {
  name: string
  email: email
  role: admin/user/guest
  projects: [Project]
}
```

### 2. Rules
Specify business logic and validation:
```yaml
rules {
  createProject: {
    require: role == admin
    validate: name.length > 0
    then: notify@team
  }
}
```

### 3. Screens
Define user interfaces and interactions:
```yaml
screen Dashboard {
  layout: grid(2x2)
  widgets: [
    stats: counter,
    tasks: list,
    alerts: feed
  ]
}
```

### 4. Integrations
Configure external services and APIs:
```yaml
integrate {
  auth: oauth2
  storage: s3
  email: sendgrid
}
```

## Best Practices

1. Use meaningful names that reflect business concepts
2. Keep entities focused and cohesive
3. Group related rules together
4. Design screens around user workflows
5. Follow consistent naming conventions
