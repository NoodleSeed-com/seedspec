# Intent-Focused Language Structure

The Seed Specification Language lets you express what you want to build, not how to build it.

## Core Principles

### 1. Express Intent, Not Implementation

```yaml
// Just describe what you want
app TodoList {
  // Core data
  entity Task {
    title: string
    done: bool
    due?: date
  }
  
  // User interface
  screen Tasks {
    list: [title, done, due]
    actions: [create, complete]
  }
}

// SeedML infers the rest:
// - Database schema
// - API endpoints
// - UI components
// - Business logic
// - Validation
// - Error handling
```

### 2. Progressive Complexity

Start simple, add detail only when needed:

```yaml
// Minimal version
entity User {
  name: string
  email: email
}

// Add validation when needed
entity User {
  name: string {
    min: 2
    max: 50
  }
  email: email {
    unique: true
    domain: company.com
  }
}

// Add behavior when needed
entity User {
  name: string
  email: email
  
  rules {
    on_create: send_welcome_email
    on_delete: archive_data
  }
  
  compute {
    full_name: name + " " + surname
    age: birthday.years_since()
  }
}
```

### 3. Smart Composition

Combine patterns to express complex intent:

```yaml
app OrderSystem {
  // Core domain
  entity Order {
    status: draft->submitted->approved
    items: [OrderItem]
    total: money
  }

  // Business rules
  rules {
    submit: {
      require: [
        items.length > 0,
        total > 0
      ]
      then: notify@customer
    }
  }

  // User interface
  screen Orders {
    list: [id, customer, total, status]
    actions: [create, submit, approve]
  }

  // Integration
  integrate {
    payment: stripe {
      on: order.submit
      charge: total
    }
  }
}
```

## Key Components

### 1. Domain Model
Define your core business entities:

```yaml
entity Product {
  name: string
  price: money
  category: electronics/books/clothing
  
  # Relations
  vendor: Vendor
  reviews: [Review]
}
```

### 2. Business Rules
Express logic and workflows:

```yaml
rules {
  approve_order: {
    when: status -> approved
    require: [
      total < 10000,
      items.all(in_stock)
    ]
    then: [
      notify@customer,
      update@inventory
    ]
  }
}
```

### 3. User Interface
Define screens and interactions:

```yaml
screen Products {
  # Layout
  layout: grid(3)
  
  # Data display
  show: [image, name, price]
  
  # User actions
  actions: [
    create: button,
    edit: menu,
    delete: confirm
  ]
  
  # Behavior
  search: [name, category]
  sort: price
  filter: category
}
```

### 4. Integration
Connect external services:

```yaml
integrate {
  # Authentication
  auth: {
    provider: google
    roles: [user, admin]
  }
  
  # Storage
  files: s3 {
    bucket: uploads
    types: [image, pdf]
  }
  
  # Notifications
  notify: {
    email: sendgrid
    sms: twilio
  }
}
```

## Best Practices

1. **Start Simple**
   - Begin with core entities
   - Add complexity gradually
   - Let defaults work for you

2. **Focus on Intent**
   - Describe what, not how
   - Use business terminology
   - Express natural workflows

3. **Leverage Patterns**
   - Use built-in components
   - Combine existing patterns
   - Stay consistent

4. **Think in Domains**
   - Model business concepts
   - Group related features
   - Maintain boundaries
