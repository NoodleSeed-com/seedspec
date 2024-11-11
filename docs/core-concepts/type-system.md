# Type System

SeedML's type system combines simplicity with power.

## Core Types

```yaml
# Basic Types
string              # Text
number              # Numbers
bool                # True/False
date                # Dates
time                # Time
datetime            # Date+Time
money               # Currency
email               # Email
phone               # Phone
url                 # URLs

# Complex Types
[Type]              # Lists
Type?               # Optional
Type!               # Required
map<Key,Value>      # Maps
enum(v1,v2)         # Enums

# Special Types
id                  # Unique IDs
timestamp           # Timestamps
file                # Files
image               # Images
geo                 # Location
```

## Type Usage

```yaml
# Validation
age: number {
  min: 0
  max: 150
}

# Collections
tags: [string]
metadata: map<string,any>

# Inference
entity Product {
  price: 0.00      # money
  created: now()    # timestamp
  active: true     # bool
}
```

## Custom & Composite Types

```yaml
# Custom Types
types {
  Currency: money {
    precision: 2
    positive: true
  }
  Status: enum(active, pending)
}

# Composition
entity Order {
  items: [{
    product: Product
    quantity: number > 0
    price: Currency
  }]
  shipping: {
    address: Address
    method: standard/express
  }
}
```

## Benefits

- Type Safety: Compile-time & runtime validation
- Clear Modeling: Self-documenting schemas
- Code Generation: DB, API, UI components
- IDE Support: Completion, validation, docs
