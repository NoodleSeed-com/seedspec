# Type System

The Seed Specification Language's type system provides strict typing with explicit validation.

## Core Types

```seed
types {
  // Basic Types
  string {
    min?: number        // Minimum length
    max?: number        // Maximum length
    pattern?: regex     // Regex pattern
    format?: email | url | phone  // Format validation
  }
  
  number {
    min?: number        // Minimum value
    max?: number        // Maximum value
    integer?: boolean   // Must be integer
    positive?: boolean  // Must be positive
  }
  
  boolean              // true/false
  
  // Collection Types
  array {
    type: Type         // Array element type
    min?: number       // Minimum length
    max?: number       // Maximum length
    unique?: boolean   // Elements must be unique
  }
  
  map {
    key: Type          // Key type
    value: Type        // Value type
  }
  
  enum {
    values: [string]   // Allowed values
  }
}
```

## UI-Specific Types

```seed
types {
  // Color Values
  color {
    type: hex | rgb | hsl | token
    value: string
  }
  
  // Size Values
  size {
    type: px | rem | em | token
    value: number
    unit?: string
  }
  
  // Spacing Values
  spacing {
    type: size | array
    value: size | [size, size, size, size]
  }
  
  // Typography Values
  font {
    family: string
    size: size
    weight: number | token
    style?: normal | italic
    lineHeight?: number | size
  }
  
  // Border Values
  border {
    width: size
    style: solid | dashed | dotted
    color: color
    radius?: size
  }
}
```

## Type Usage

### 1. Explicit Type Declaration

All values must have explicit types:

```seed
theme MainTheme {
  tokens {
    colors {
      primary: color(#0066cc)
      secondary: color(blue.500)
    }
    
    spacing {
      small: size(4px)
      medium: size(8px)
      large: size(16px)
    }
  }
}
```

### 2. Component Type Validation

Components define required and optional typed properties:

```seed
schema Button {
  required {
    background: color
    text: color
    padding: spacing
  }
  
  optional {
    border: border
    hover: {
      background: color
      text: color
    }
  }
}
```

### 3. Entity Type Validation

Business entities use type validation:

```seed
entity User {
  name: string {
    min: 2
    max: 50
    pattern: "[A-Za-z ]+"
  }
  
  email: string {
    format: email
    unique: true
  }
  
  age: number {
    min: 0
    max: 150
    integer: true
  }
  
  roles: array {
    type: enum {
      values: ["user", "admin", "moderator"]
    }
  }
}
```

## Type Composition

Types can be composed to create complex structures:

```seed
// Custom type definitions
types {
  UserRole: enum {
    values: ["user", "admin", "moderator"]
  }
  
  Address: {
    street: string
    city: string
    country: string
    postal: string {
      pattern: "[0-9]{5}"
    }
  }
}

// Using composed types
entity User {
  profile: {
    name: string
    avatar: string {
      format: url
    }
    address: Address
  }
  
  settings: map {
    key: string
    value: string | number | boolean
  }
  
  permissions: array {
    type: UserRole
    unique: true
  }
}
```

## Benefits

1. **Type Safety**
   - Compile-time validation
   - Runtime type checking
   - No implicit conversions

2. **Clear Contracts**
   - Self-documenting schemas
   - Explicit validation rules
   - IDE support

3. **Error Prevention**
   - Early error detection
   - Clear error messages
   - Validation at parse time

4. **Code Generation**
   - Type-safe APIs
   - Database schemas
   - UI components
   - Form validation
