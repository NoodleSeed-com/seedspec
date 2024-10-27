# Business Application Example

```yaml
# Complete order management system
app OrderSystem {
  # Data Models
  entity Order {
    # Basic fields
    customer: Customer
    items: [OrderItem]
    status: draft->submitted->approved->shipped
    total: money
    
    # Computed fields
    subtotal: sum(items.price)
    tax: subtotal * 0.2
    total: subtotal + tax
    
    # Business rules
    rules {
      submit: {
        require: [
          items.length > 0,
          customer.verified,
          total <= customer.creditLimit
        ]
        then: notify@sales
      }
      
      approve: {
        require: role.manager
        check: items.all(inStock)
        then: [create@invoice, notify@warehouse]
      }
    }
  }

  entity OrderItem {
    product: Product
    quantity: int > 0
    price: money
    total: quantity * price
  }

  # User Interface
  screen Orders {
    list {
      view: table
      show: [id, customer, total, status]
      group: status
      actions: [
        submit if draft,
        approve if submitted and role.manager
      ]
    }
    
    detail {
      layout: split
      left {
        customer: card
        items: editable-table
      }
      right {
        summary: [subtotal, tax, total]
        status: timeline
        actions: panel
      }
    }
  }

  # Integrations
  integrate {
    payment: stripe
    shipping: fedex
    notification: sendgrid
  }
}
```

This example demonstrates:
- Complex data models
- Business rules and validation
- Computed fields
- Multi-step workflows
- Rich UI components
- External integrations
