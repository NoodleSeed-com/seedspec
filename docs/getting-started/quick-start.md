# Quick Start Guide

Get up and running with Seed Spec quickly.

## 1. Create Your First File

Create a new file `core.seed`:

```javascript
// core.seed - Core domain model

app MyApp {
  // Define your core entities
  entity User {
    name: string
    email: email
    role: admin/user
  }
  
  entity Product {
    name: string
    price: money
    stock: int
  }
  
  // Define your screens
  screen Products {
    list: [name, price, stock]
    actions: [create, edit, delete]
    filter: stock > 0
  }
  
  // Define your rules
  rules {
    validate {
      price: positive
      stock: min(0)
    }
    
    on_low_stock {
      when: stock < 10
      then: notify@admin
    }
  }
}
```

## 2. Run the Generator

```bash
seed generate core.seed
```

## 3. Start the App

```bash
seed start
```

Your app is now running at http://localhost:3000

## Next Steps

1. Add more entities and screens
2. Define business rules
3. Customize the theme
4. Add integrations

See the [Full Guide](first-app.md) for a more detailed walkthrough.
