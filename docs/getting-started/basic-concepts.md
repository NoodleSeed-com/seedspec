# Basic Concepts

Learn the fundamental concepts of SeedML development.

## Application Structure

SeedML applications follow a layered architecture:

### 1. Foundation Layer

The base of every application:

```yaml
# Type definitions
types {
  Email: string { format: email }
  Status: active/inactive
}

# Base validation
validate {
  email: format_valid
  status: in_enum
}
```

### 2. Data Layer

Independent and dependent entities:

```yaml
# Base entity (no dependencies)
entity User {
  name: string!
  email: Email
  status: Status = active
}

# Dependent entity
entity Order {
  customer: User!
  items: [OrderItem]
}
```

### 3. Logic Layer

Business rules and computations:

```yaml
rules {
  create_user: {
    validate: email != null
    then: send_welcome_email
  }
  
  submit_order: {
    require: [
      items.length > 0,
      customer.verified
    ]
  }
}
```

### 4. Security Layer

Permissions and roles:

```yaml
permissions {
  manage_users: {
    entity: User
    actions: [create, update]
  }
}

roles {
  admin: [all]
  manager: [manage_users]
}
```

### 5. Presentation Layer

UI components and screens:

```yaml
screen UserList {
  list: [name, email, status]
  actions: [create, edit]
}
```

### 6. Integration Layer

External services and APIs:

```yaml
integrate {
  email: sendgrid
  payment: stripe
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
