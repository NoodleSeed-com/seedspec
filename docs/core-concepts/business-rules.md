# Business Rules

SeedML provides a simplified approach to business rules focused on common use cases and rapid prototyping.

## Core Concepts

### 1. Basic Validation
```yaml
entity User {
  email: email
  password: string
  
  rules {
    validate: {
      email: required,
      password: length >= 8
    }
  }
}
```

### 2. Simple State Transitions
```yaml
entity Task {
  status: string = "todo"
  
  rules {
    start: {
      validate: status == "todo"
      then: updateStatus("in-progress")
    }
    
    complete: {
      validate: status == "in-progress"
      then: updateStatus("done")
    }
  }
}
```

### 3. Basic Computations
```yaml
entity Invoice {
  items: [InvoiceItem]
  
  rules {
    calculate: {
      then: [
        updateSubtotal(sum(items.amount)),
        updateTotal(subtotal + tax)
      ]
    }
  }
}
```

## Common Patterns

### 1. Field Validation
```yaml
entity Product {
  rules {
    validate: {
      name: required,
      price: positive,
      stock: minimum(0)
    }
  }
}
```

### 2. Cross-field Validation
```yaml
entity Booking {
  rules {
    validate: {
      endDate: after(startDate),
      capacity: lessThan(maxCapacity)
    }
  }
}
```

### 3. Simple Workflows
```yaml
entity Leave {
  status: string = "requested"
  
  rules {
    approve: {
      validate: status == "requested"
      then: [
        updateStatus("approved"),
        notifyEmployee
      ]
    }
    
    reject: {
      validate: status == "requested"
      then: [
        updateStatus("rejected"),
        notifyEmployee
      ]
    }
  }
}
```

## Best Practices

### 1. Keep Validations Simple
```yaml
# DO - Use simple validations
entity Order {
  rules {
    submit: {
      validate: [
        items.length > 0,
        total > 0
      ]
    }
  }
}
```

### 2. Use Clear State Transitions
```yaml
# DO - Simple state changes
entity Task {
  rules {
    complete: {
      validate: status == "active"
      then: updateStatus("completed")
    }
  }
}
```

### 3. Minimize Complexity
- Focus on common use cases
- Avoid complex validation chains
- Keep workflows linear
- Use simple state machines

### 4. Prefer Convention
- Use standard validation patterns
- Follow common state transitions
- Apply consistent naming
- Leverage built-in behaviors

## Key Benefits

1. **Rapid Development**
   - Quick to implement
   - Easy to understand
   - Fast to modify

2. **Reduced Errors**
   - Simple validation
   - Clear state flow
   - Standard patterns

3. **Better Maintenance**
   - Less complexity
   - Standard approaches
   - Clear intent
