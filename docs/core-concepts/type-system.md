# Type System

SeedML provides a rich type system that balances simplicity with power.

## Basic Types

### Primitive Types
```yaml
string              # Text values
number              # Numeric values
bool                # Boolean values
date                # Date values
time                # Time values
datetime            # Date and time
money               # Monetary values
email               # Email addresses
phone               # Phone numbers
url                 # URLs
```

### Complex Types
```yaml
[Type]              # Lists
Type?               # Optional values
Type!               # Required values
map<Key, Value>     # Key-value pairs
enum(v1,v2,v3)      # Enumerations
```

### Special Types
```yaml
id                  # Unique identifiers
timestamp           # Timestamps with timezone
file                # File references
image               # Image references
geo                 # Geographical coordinates
```

## Type Modifiers

### Nullability
```yaml
name: string!       # Required
phone: string?      # Optional
```

### Validation
```yaml
age: number {
  min: 0
  max: 150
}

email: email {
  domain: company.com
}
```

### Collections
```yaml
tags: [string]
scores: [number]
metadata: map<string, any>
```

## Type Inference

SeedML can infer types in many contexts:

```yaml
entity Product {
  price: 0.00      # Inferred as money
  created: now()    # Inferred as timestamp
  active: true     # Inferred as boolean
}
```

## Custom Types

Define reusable custom types:

```yaml
types {
  Currency: money {
    precision: 2
    positive: true
  }
  
  PhoneNumber: string {
    format: "###-###-####"
    validate: regex
  }
  
  Status: enum(active, inactive, pending)
}
```

## Type Composition

Combine types to create complex structures:

```yaml
entity Order {
  items: [{
    product: Product
    quantity: number > 0
    price: money
  }]
  
  shipping: {
    address: Address
    method: standard/express
    tracking?: string
  }
}
```

## Type Safety

SeedML enforces type safety:

1. Compile-time checking
2. Runtime validation
3. Automatic conversions
4. Type coercion rules

## Benefits

1. Clear Data Modeling
   - Explicit types
   - Self-documenting
   - Validation built-in

2. Better Tooling
   - IDE support
   - Error detection
   - Code completion

3. Runtime Safety
   - Type checking
   - Data validation
   - Error prevention

4. Code Generation
   - Database schemas
   - API contracts
   - UI components
