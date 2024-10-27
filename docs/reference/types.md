# Type System Reference

## Primitive Types

```yaml
# Text Types
string              # Basic text
text                # Long text/rich text
email               # Email addresses with validation
phone               # Phone numbers with formatting
url                 # URLs with validation

# Numeric Types
number              # Generic numbers
int                 # Integers
float               # Floating point
money               # Monetary values with currency

# Date/Time Types
date                # Calendar dates
time                # Time values
datetime            # Combined date and time
timestamp           # System timestamps with TZ

# Other Primitives
bool                # True/false values
color               # Color values with formats
```

## Complex Types

```yaml
# Collections
[Type]              # Lists of values
map<Key,Value>      # Key-value mappings
set<Type>           # Unique value sets

# Optional/Required
Type?               # Optional value
Type!               # Required value (default)
Type = default      # Value with default

# Enumerations
enum(v1,v2,v3)      # Simple enums
status: v1->v2->v3  # State machine enums
```

## Special Types

```yaml
# System Types
id                  # Unique identifiers
uuid                # UUID values
slug                # URL-friendly names
version             # Semantic versions

# File Types
file                # Generic files
image               # Image files
document            # Document files
media               # Audio/video files

# Specialized Types
geo                 # Geographic coordinates
json                # JSON data
xml                 # XML data
markdown            # Markdown content
```

## Type Modifiers

```yaml
# Validation
string {
  min: 1           # Minimum length
  max: 100         # Maximum length
  pattern: regex   # Regex pattern
}

number {
  min: 0          # Minimum value
  max: 999        # Maximum value
  step: 0.01      # Value increments
}

# Formatting
string {
  case: lower     # Case formatting
  trim: true      # Whitespace trimming
  format: email   # Format validation
}

# Advanced
Type {
  # Validation
  required: bool     # Field is required
  unique: bool      # Values must be unique
  min: number       # Minimum value/length
  max: number       # Maximum value/length
  pattern: string   # Regex pattern

  # Storage
  index: bool      # Create database index
  private: bool    # Restrict access
  
  # Behavior  
  immutable: bool  # Cannot change after set
  computed: bool   # Derived from other fields
}
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
