# Type System Reference

## Core Types

```yaml
# Simplified primitive types
types {
  string              # Text values
  number              # Numeric values
  bool                # True/false values 
  date                # Simple dates
}

# Common domain types
types {
  email               # Email addresses
  phone               # Phone numbers  
  money               # Currency values
}

# Simple collections
[Type]                # Lists of values
Type                  # References to entities

# Optional/Required modifiers
Type?                 # Optional value
Type = default        # Default value
```

## Basic Validation

```yaml
# Simple validation rules
string {
  required: bool     # Field is required
  unique: bool      # Values must be unique
  min: number       # Minimum length
  max: number       # Maximum length
}

number {
  min: number       # Minimum value
  max: number       # Maximum value
}

# Format validation
email: string       # Validates email format
phone: string       # Validates phone format
money: number       # Validates currency format
```

## Type Inference

SeedML automatically infers types in many contexts:

```yaml
entity Product {
  price: 0.00      # Inferred: money
  created: now()    # Inferred: timestamp
  active: true     # Inferred: boolean
  tags: []         # Inferred: [string]
}
```

## Custom Types

Define reusable custom types:

```yaml
types {
  # Simple custom type
  Currency: money {
    precision: 2
    positive: true
  }
  
  # Complex custom type
  Address: {
    street: string!
    city: string!
    state: enum(...)
    zip: string {
      pattern: "\\d{5}"
    }
  }
  
  # Enum type
  Status: enum(
    active: "Active",
    inactive: "Inactive",
    pending: "Pending Review"
  )
}
```

## Type Composition

Build complex types through composition:

```yaml
entity Order {
  # Nested structure
  shipping: {
    address: Address
    method: ShippingMethod
    tracking?: string
  }
  
  # List of complex items
  items: [{
    product: Product
    quantity: int > 0
    price: Currency
  }]
}
```

## Best Practices

1. **Type Selection**
   - Use specific types over generic ones
   - Consider validation requirements
   - Think about UI rendering
   - Plan for future needs

2. **Validation**
   - Add constraints appropriately
   - Use built-in validations
   - Create reusable types
   - Document custom types

3. **Performance**
   - Consider database implications
   - Plan indexes carefully
   - Use appropriate list types
   - Monitor complex types

4. **Maintenance**
   - Document custom types
   - Use consistent patterns
   - Plan for versioning
   - Consider migrations

## Basic Structure

Every SeedML application follows this structure:

```yaml
app [AppName] {
  # Global Configuration
  meta: { ... }
  
  # Data Models
  entity [EntityName] { ... }
  
  # Business Rules
  rules { ... }
  
  # User Interface
  screens { ... }
  
  # Integrations
  integrate { ... }
}
```

## Entity Syntax

```yaml
entity [EntityName] {
  # Basic fields
  name: string
  age: number
  active: bool = true
  
  # Field modifiers
  required: string!
  optional: string?
  defaulted: string = "default"
  
  # Complex types
  items: [Item]
  metadata: map<string,any>
  status: draft->submitted->approved
}
```
