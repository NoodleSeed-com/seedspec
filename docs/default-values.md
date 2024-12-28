# Default Values

Specify default field values in SeedSpec models.

```seed
model User "User" {
  name text = "New User"        // Default name
  email text = ""              // Empty default
  role text = "member"         // Default role
  active bool = true          // Default boolean
  score num = 0              // Default number
}

model Product "Product" {
  name text = "New Product"    // Default product name
  price num = 9.99           // Default price
  inStock bool = true        // Default availability
  category text = "general"  // Default category
}
```

Status: ✓ Available
