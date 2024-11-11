# Business Rules

SeedML lets you express business logic through simple, intent-focused rules that automatically handle validation, computation, and workflow.

## Core Concepts

### State Management
```yaml
entity Order {
  # Smart state transitions
  states: Draft -> Submitted -> Approved -> Completed {
    Submitted: requires[complete]
    Approved: requires[manager.review] 
    Completed: triggers[invoice.create]
  }
}
```

```yaml
entity Order {
  # Smart validation - handles type checking, required fields
  validate {
    total: positive
    items: not_empty
    customer: verified
  }

  # Automatic computations
  compute {
    subtotal: sum(items.price)
    tax: subtotal * 0.1  
    total: subtotal + tax
  }

  # Intent-focused workflows
  flow submit {
    when: valid           # Implied validation
    then: notify@sales    # Automatic handling
  }
}
```

## Key Features

### 1. Smart Validation
```yaml
validate {
  # Built-in validations with clear intent
  email: valid_email     # Format checking
  age: adult            # Business logic
  stock: available      # External check
}
```

### 2. Computed Properties 
```yaml
compute {
  # Automatic dependency tracking
  full_name: first_name + " " + last_name
  age: today - birthdate
  status: if(balance > 0) "active" else "suspended"
}
```

### 3. Business Workflows
```yaml
flow approve_expense {
  # Focus on business logic, not implementation
  when: [
    amount < policy.limit,
    submitter.manager_approved
  ]
  then: [
    notify@accounting,
    create@payment
  ]
}
```

## Best Practices

1. **Express Intent**
   - Use business terminology
   - Focus on what, not how
   - Let SeedML handle implementation

2. **Smart Defaults**
   - Common validations built-in
   - Standard workflows included
   - Override only when needed

3. **Keep It Simple**
   - One rule per concept
   - Clear dependencies
   - Automatic optimization
