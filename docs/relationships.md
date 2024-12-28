# Relationships

Model relationships and references in SeedSpec.

```seed
model Order "Order" {
  customer Customer    // Single reference
  items [Product]     // Array reference
}

model Customer "Customer" {
  name text = "New Customer"
  orders [Order]      // Reverse relationship
}

model Product "Product" {
  name text = "New Product"
  price num = 0
}
```

Status: ✓ Available
