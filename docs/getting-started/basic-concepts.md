# Basic Concepts

Learn the fundamental concepts of SeedML development.

## Core Components

### 1. Applications

Every SeedML project starts with an app definition:

```yaml
app MyApp {
  # App components go here
}
```

### 2. Entities

Entities define your data models:

```yaml
entity User {
  name: string
  email: email
  active: bool = true
}
```

### 3. Screens

Screens define your user interface:

```yaml
screen UserList {
  list: [name, email, active]
  actions: [create, edit]
}
```

### 4. Rules

Rules define business logic:

```yaml
rules {
  create_user: {
    validate: email != null
    then: send_welcome_email
  }
}
```

## Key Principles

### 1. Declarative Syntax
- Describe what, not how
- Focus on business concepts
- Let SeedML handle implementation

### 2. Smart Defaults
- Common patterns built-in
- Override only when needed
- Progressive complexity

### 3. Full Stack
- One specification
- Generates all layers
- Consistent behavior

## Common Patterns

### 1. Field Types
```yaml
fields {
  required: string!
  optional: string?
  withDefault: string = "default"
  validated: email
  enumerated: red/green/blue
}
```

### 2. Relationships
```yaml
entity Order {
  customer: Customer  # Single
  items: [Product]   # Multiple
  assigned?: User    # Optional
}
```

### 3. Actions
```yaml
actions {
  simple: doThing
  withParams: doThing(param)
  conditional: doThing if condition
  chained: [first, second, third]
}
```

## Next Steps

1. Try the [Quick Start Guide](quick-start.md)
2. Build your [First Application](first-app.md)
3. Explore [Core Concepts](../core-concepts/overview.md)
