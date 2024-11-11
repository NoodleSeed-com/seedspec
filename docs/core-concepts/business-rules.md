# Business Rules

SeedML provides a powerful system for expressing business logic and validation rules in a clear, declarative way.

## Basic Rules

```yaml
entity Order {
  rules {
    submit: {
      require: [
        items.length > 0,
        total > 0,
        customer.verified
      ]
      then: notify@sales
    }
  }
}
```

## Rule Types

### 1. Validation Rules
```yaml
validate: {
  price: positive,
  stock: available,
  email: format_valid
}
```

### 2. Business Logic
```yaml
rules {
  submit_order: {
    require: [
      items.length > 0,
      total > 0,
      customer.verified
    ]
    then: [
      create@invoice,
      notify@customer
    ]
  }
}
```

### 3. Computed Fields
```yaml
fields {
  subtotal: sum(items.price)
  tax: subtotal * tax_rate
  total: subtotal + tax
}
```

### 4. State Transitions
```yaml
status: draft->submitted->approved {
  submitted: {
    require: complete
    then: notify@manager
  }
  approved: {
    require: role.manager
    then: [create@invoice, notify@customer]
  }
}
```

## Best Practices

1. **Clear Intent**
   - Use descriptive rule names
   - Group related rules
   - Document complex logic

2. **Validation First**
   - Validate early
   - Fail fast
   - Clear error messages

3. **Maintainable Logic**
   - Keep rules focused
   - Avoid complex conditions
   - Use computed fields

4. **Proper Events**
   - Trigger appropriate notifications
   - Update related entities
   - Maintain audit trails
