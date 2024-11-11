# Business Application Example

A complete order management system showing how intent-focused patterns scale to larger applications.

```seedml
app OrderSystem {
  # 1. Domain Model
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

  # Dependent entities
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
        error: {
          items.length: "Order must contain at least one item"
          customer.verified: "Customer must be verified before placing orders"
          creditLimit: "Order total exceeds customer credit limit"
        }
        then: notify@sales
      }
      
      approve: {
        require: role.manager
        check: items.all(product.inStock)
        error: {
          role: "Only managers can approve orders"
          stock: "Some items are out of stock"
        }
        then: [
          create@invoice,
          notify@warehouse
        ]
      }

      ship: {
        require: status == approved
        error: {
          status: "Order must be approved before shipping"
        }
        then: [
          update@inventory,
          notify@customer,
          notify@shipping
        ]
      }
    }
  }

  entity Invoice {
    order: Order!
    issueDate: datetime = now()
    dueDate: datetime = issueDate + 30.days
    status: pending/paid/overdue = pending
    amount: money = order.total
  }

  # Permissions (now can reference known entities)
  permissions {
    # Customer-related permissions
    view_all_customers: {
      entity: Customer
      access: read
      filter: all
    }
    view_active_customers: {
      entity: Customer
      access: read
      filter: status == active
    }
    set_credit_limits: {
      entity: Customer
      access: [read, update]
      fields: [creditLimit]
      validate: {
        creditLimit: <= 50000
      }
    }

    # Order-related permissions
    create_orders: {
      entity: Order
      access: create
      fields: [customer, items]
    }
    view_own_orders: {
      entity: Order
      access: read
      filter: created_by == current_user
    }
    view_customer_orders: {
      entity: Order
      access: read
      filter: customer.id == current_user.id
    }
    approve_orders: {
      entity: Order
      access: [read, update]
      filter: status == submitted
      allow: [approve]
    }
    submit_orders: {
      entity: Order
      access: [read, update]
      filter: created_by == current_user
      allow: [submit]
    }

    # Product-related permissions
    manage_products: {
      entity: Product
      access: [create, read, update]
      filter: all
    }
  }

  # Roles now reference permissions
  roles {
    admin: {
      permissions: [all]
    }
    
    manager: {
      permissions: [
        view_all_customers,
        approve_orders,
        manage_products,
        set_credit_limits
      ]
    }
    
    sales: {
      permissions: [
        view_active_customers,
        create_orders,
        submit_orders,
        view_own_orders
      ]
    }
    
    customer: {
      permissions: [
        view_customer_orders,
        create_orders
      ]
    }
  }
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
        error: {
          items.length: "Order must contain at least one item"
          customer.verified: "Customer must be verified before placing orders"
          creditLimit: "Order total exceeds customer credit limit"
        }
        then: notify@sales
      }
      
      approve: {
        require: role.manager
        check: items.all(product.inStock)
        error: {
          role: "Only managers can approve orders"
          stock: "Some items are out of stock"
        }
        then: [
          create@invoice,
          notify@warehouse
        ]
      }

      ship: {
        require: status == approved
        error: {
          status: "Order must be approved before shipping"
        }
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

  # UI Screens (reference entities and roles)
  screen Products {
    list {
      view: table
      show: [name, price, inStock, stockQuantity]
      actions: [create, edit]
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

  # External integrations (last since they may reference entities and actions)
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
