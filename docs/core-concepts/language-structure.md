# Language Structure

SeedML follows core principles that make it powerful yet approachable:

## Fundamental Principles

### 1. Everything is an Expression
All values and logic are expressions that can be evaluated:

```yaml
app Example {
  # Direct expressions
  value: 1 + 2
  text: "Hello " + name
  
  # Method expressions
  total: items.sum()
  filtered: users.filter(active)
  
  # Conditional expressions
  status: if total > 1000 then "high" else "low"
  
  # Collection expressions
  tags: ["a", "b"].concat(extra_tags)
}
```

### 2. Consistent Type System
Types follow clear, predictable patterns:

```yaml
types {
  # Basic types
  name: string              # Basic type
  age: number              # Numeric type
  active: bool             # Boolean type
  
  # Type modifiers
  optional: string?        # Optional value
  required: string!        # Required value
  validated: string(email) # Validated type
  
  # Collections
  tags: [string]          # List type
  scores: map<id,number>  # Map type
  status: draft->done     # State machine
}
```

### 3. Clear Component Boundaries
Components have specific responsibilities:

```yaml
app MyApp {
  # 1. Configuration
  config {
    name: "My Application"
    version: "1.0.0"
    features: [auth, api]
  }

  # 2. Type Definitions
  types {
    Money: decimal(2) {
      min: 0
      currency: USD
    }
  }

  # 3. Data Models
  entity Order {
    # Properties
    id: uuid
    total: Money
    status: draft->submitted->approved

    # Relationships
    customer: Customer
    items: [OrderItem]

    # Behaviors
    rules { ... }
    compute { ... }
    access { ... }
  }

  # 4. Business Logic
  rules {
    submit_order: {
      when: order.status -> submitted
      require: [
        order.total > 0,
        order.items.length > 0
      ]
      then: [
        notify@customer,
        create@invoice
      ]
    }
  }

  # 5. User Interface
  screens {
    OrderList {
      layout: table
      columns: [id, customer, total, status]
      actions: [create, edit]
    }
  }

  # 6. Integration
  integrate {
    stripe: {
      on: order.submit
      charge: total
      then: approve
    }
  }
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
