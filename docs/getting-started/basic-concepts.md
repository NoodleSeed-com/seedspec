# Basic Concepts

The Seed Specification Language (SeedSpec) is built around type-safe, modular concepts that ensure reliability and maintainability.

## Core Structure

```seed
// Import standard library components
import "@stdlib/core"
use { Button, Card } from "@stdlib/components"

app TaskManager {
  // Core domain model with type validation
  entity Task {
    title: string {
      min: 3
      max: 100
    }
    done: boolean
    due: datetime {
      min: now()  // Must be in future
    }
  }
  
  // Type-safe theme definition
  theme MainTheme {
    tokens {
      colors {
        primary: color(#0066cc)
        success: color(green.500)
        error: color(red.500)
      }
      spacing {
        small: size(4px)
        medium: size(8px)
      }
    }
  }
  
  // Strongly typed UI components
  component TaskCard {
    required {
      task: Task
      onComplete: function
    }
    
    styles {
      background: color(white)
      padding: spacing(medium)
      border: {
        width: size(1px)
        style: solid
        color: color(tokens.colors.primary)
      }
    }
  }
}
```

## Type System

### 1. Basic Types

```seed
types {
  // Text with validation
  string {
    min?: number
    max?: number
    pattern?: regex
  }
  
  // Numbers with constraints
  number {
    min?: number
    max?: number
    integer?: boolean
  }
  
  // Dates and times
  datetime {
    min?: datetime
    max?: datetime
    timezone?: string
  }
  
  // Boolean values
  boolean
}
```

### 2. UI-Specific Types

```seed
types {
  // Colors with format validation
  color {
    type: hex | rgb | hsl | token
    value: string
  }
  
  // Sizes with units
  size {
    type: px | rem | em
    value: number
    unit: string
  }
  
  // Typography settings
  font {
    family: string
    size: size
    weight: number
    lineHeight?: number
  }
}
```

## Modules and Components

### 1. Module Structure

```seed
// Explicit imports
import "@stdlib/core"
use { Button, Input } from "@stdlib/components"

// Explicit exports
export {
  TaskCard,
  TaskList
} from "./components"

// Module definition
module Tasks {
  // Components
  component TaskCard {
    // Type-safe props
    required {
      task: Task
      onComplete: function
    }
    
    // Styled variants
    variants {
      default: {
        background: color(white)
        padding: spacing(medium)
      }
      highlighted: {
        background: color(yellow.100)
        padding: spacing(large)
      }
    }
  }
}
```

### 2. Component Schema

```seed
// Define reusable component contract
schema Button {
  required {
    text: string
    onClick: function
  }
  
  optional {
    disabled: boolean
    variant: enum {
      values: ["primary", "secondary"]
    }
  }
}

// Implement component
component Button {
  // Implement required schema
  implements: Button
  
  // Style variants
  variants {
    primary: {
      background: color(tokens.colors.primary)
      text: color(white)
    }
    secondary: {
      background: color(transparent)
      text: color(tokens.colors.primary)
      border: {
        color: color(tokens.colors.primary)
      }
    }
  }
}
```

## Best Practices

1. **Use Strong Typing**
   - Always specify types explicitly
   - Add validation constraints
   - Use schema definitions

2. **Structure Code Clearly**
   - One component per file
   - Group related functionality
   - Use clear module boundaries

3. **Follow Type Patterns**
   - Use consistent type definitions
   - Validate at compile time
   - Handle all edge cases

4. **Write Clear Contracts**
   - Define explicit schemas
   - Document requirements
   - Use descriptive names

5. **Think in Components**
   - Break down into small pieces
   - Make components reusable
   - Define clear interfaces
