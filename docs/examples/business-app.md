# Business Application Example

```yaml
# Complete order management system
app OrderSystem {
  # Customer entity definition
  entity Customer {
    # Basic information
    name: string!
    email: email!
    phone: phone?
    status: active/inactive = active
    
    # Financial & verification
    verified: boolean = false
    creditLimit: money = 1000.00
    
    # Validation rules
    validate: {
      email: required if status == active
      creditLimit: positive
    }
    
    # Customer verification process
    rules {
      verify: {
        require: [
          email != null,
          status == active
        ]
        then: [
          set(verified, true),
          notify@customer
        ]
      }
    }
  }

  # Product entity definition
  entity Product {
    name: string!
    description: text
    price: money!
    inStock: boolean = true
    stockQuantity: int > 0
    
    validate: {
      price: positive
      stockQuantity: positive
    }
  }

  # Order entity definition
  entity Order {
    # Basic fields
    customer: Customer!
    items: [OrderItem]
    status: draft->submitted->approved->shipped
    
    # Computed fields
    subtotal: sum(items.total)
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
        check: items.all(product.inStock)
        then: [
          create@invoice,
          notify@warehouse
        ]
      }

      ship: {
        require: status == approved
        then: [
          update@inventory,
          notify@customer,
          notify@shipping
        ]
      }
    }
  }

  entity OrderItem {
    product: Product!
    quantity: int > 0
    price: money!
    total: quantity * price

    validate: {
      quantity: <= product.stockQuantity
      price: == product.price
    }
  }

  entity Invoice {
    order: Order!
    issueDate: datetime = now()
    dueDate: datetime = issueDate + 30.days
    status: pending/paid/overdue = pending
    amount: money = order.total
  }

  # User Interface
  screen Orders {
    list {
      view: table
      show: [id, customer.name, total, status]
      group: status
      actions: [
        submit if draft,
        approve if submitted and role.manager,
        ship if approved
      ]
    }
    
    detail {
      layout: split
      left {
        customer: card {
          show: [name, email, creditLimit, verified]
        }
        items: editable-table {
          columns: [product.name, quantity, price, total]
          validate: onEdit
        }
      }
      right {
        summary: [subtotal, tax, total]
        status: timeline
        actions: panel
      }
    }
  }

  screen Customers {
    list {
      view: table
      show: [name, email, status, verified, creditLimit]
      actions: [create, edit, verify]
    }
    
    detail {
      layout: tabs
      info: [name, email, phone, status]
      orders: related-list(Order)
      invoices: related-list(Invoice)
    }
  }

  screen Products {
    list {
      view: table
      show: [name, price, inStock, stockQuantity]
      actions: [create, edit]
    }
  }

  # Integrations
  integrate {
    payment: stripe {
      apiKey: env.STRIPE_KEY
      webhook: /webhooks/stripe
    }
    shipping: fedex {
      account: env.FEDEX_ACCOUNT
      endpoint: env.FEDEX_API_URL
    }
    notification: sendgrid {
      templates: {
        order_confirm: "d-123456",
        shipping_update: "d-789012"
      }
    }
  }
}
```

This example demonstrates:
- Complete entity definitions with relationships
- Comprehensive business rules and validation
- Computed fields and dependencies
- Multi-step workflows with proper states
- Rich UI components and layouts
- Detailed external integrations
- Role-based permissions
- Inventory management
