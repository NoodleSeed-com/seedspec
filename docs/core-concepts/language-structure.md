# Seed Specification Language Structure

The Seed Specification Language (Seed Spec) provides a type-safe, modular way to define consistent design systems and applications.

## Formal Grammar

The following EBNF (Extended Backus-Naur Form) grammar defines the core structure of the Seed Specification Language:

```ebnf
PROGRAM = { IMPORT_STATEMENT } APP_STATEMENT ;

IMPORT_STATEMENT = 
    "import" STRING |
    "use" "{" IDENTIFIER_LIST "}" "from" (STRING | IDENTIFIER) ;

IDENTIFIER_LIST = IDENTIFIER { "," IDENTIFIER } ;

APP_STATEMENT =
    "app" IDENTIFIER "{" 
        [ THEME_BLOCK ]
        [ MODEL_BLOCK ] 
        [ DATA_BLOCK ]
        [ COMPONENT_BLOCKS ]
        [ SCREEN_BLOCK ] 
    "}" ;

THEME_BLOCK = 

TYPE_REF =
    "text" | "num" | "bool" ;

DATA_BLOCK =
    "data" "{" { DATA_DECL } "}" ;

DATA_DECL =
    IDENTIFIER ":" IDENTIFIER "[]" "=" JSON_ARRAY ;

JSON_ARRAY =
    "[" [ JSON_OBJECT { "," JSON_OBJECT } ] "]" ;

JSON_OBJECT =
    "{" [ JSON_FIELD { "," JSON_FIELD } ] "}" ;

JSON_FIELD =
    STRING ":" JSON_VALUE ;

JSON_VALUE =
    STRING | NUMBER | "true" | "false" | "null" | JSON_ARRAY | JSON_OBJECT ;

COMPONENT_BLOCKS =
    { COMPONENT_BLOCK } ;

COMPONENT_BLOCK =
    "component" IDENTIFIER "{" [ INPUT_BLOCK ] "}" ;

INPUT_BLOCK =
    "input" "{" IDENTIFIER ":" IDENTIFIER "}" ;

SCREEN_BLOCK =
    "screen" "{" { SCREEN_ELEMENT } "}" ;

SCREEN_ELEMENT =
    IDENTIFIER "{" "use" IDENTIFIER "data" IDENTIFIER "}" ;

LITERAL = STRING | NUMBER | "true" | "false" ;
STRING  = "\"" { ANY_CHAR_NO_QUOTE } "\"" ;
NUMBER  = DIGIT { DIGIT } [ "." DIGIT { DIGIT } ] ;
IDENTIFIER = LETTER { LETTER | DIGIT | "_" } ;
LETTER = "A" | "B" | "C" | ... | "Z" | "a" | "b" | "c" | ... | "z" ;
DIGIT = "0" | "1" | "2" | "3" | "4" | "5" | "6" | "7" | "8" | "9" ;
ANY_CHAR_NO_QUOTE = ? any character except double quote ? ;
```


## Core Principles

### 1. Type Safety First

All values must have explicit types to prevent ambiguity and catch errors early:

```seed
app TodoApp {
  theme MainTheme {
    tokens {
      colors {
        primary: color(#0066cc)      // Explicit color type
        secondary: color(blue.500)    // Color token reference
      }
      
      spacing {
        small: size(4px)             // Explicit size type
        medium: size(8px)
        large: size(16px)
      }
    }
  }
}
```

### 2. Modular Design

Clear module system with explicit imports and exports:

```seed
// Import from standard library
import "@stdlib/core"

// Use specific exports
use { colors, spacing } from theme

// Export your own components
export {
  Button,
  Card
} from "./components"
```

### 3. Component-Based Structure

Components are first-class citizens with schema validation:

```seed
// Define component schema
schema Button {
  required {
    background: color
    text: color
  }
  optional {
    padding: spacing
    border: border
  }
}

// Implement component
component Button {
  variants {
    primary: {
      background: color(blue.500)
      text: color(white)
      padding: spacing(4)
    }
    
    secondary: {
      background: color(gray.100)
      text: color(gray.900)
      padding: spacing(4)
    }
  }
}
```

## Key Components

### 1. Type System

Built-in types ensure values are valid:

```seed
types {
  // Core data types
  string: {
    min: number
    max: number
    pattern?: regex
  }
  
  number: {
    min?: number
    max?: number
    integer?: boolean
  }
  
  // UI specific types
  color: hex | token        // #fff or blue.500
  size: px | rem | token    // 16px or 1rem or sm
  spacing: size | array     // 16px or [16px, 32px]
  
  // Complex types
  entity: {
    fields: [Field]
    rules?: [Rule]
  }
  
  screen: {
    layout: grid | list
    components: [Component]
  }
}
```

### 2. Design System

Reusable design tokens with explicit types:

```seed
app MyApp {
  theme MainTheme {
    // Color palette
    tokens {
      colors {
        primary: color(#0066cc)
        secondary: color(#666666)
        success: color(green.500)
        error: color(red.500)
      }
      
      // Typography scale
      typography {
        body: {
          size: size(16px)
          lineHeight: size(1.5)
          family: font("Inter")
        }
        heading: {
          size: size(24px)
          lineHeight: size(1.2)
          family: font("Inter")
          weight: number(600)
        }
      }
    }
  }
  
  // Business entities
  entity User {
    name: string {
      min: 2
      max: 50
    }
    email: email {
      unique: true
    }
  }
  
  // UI screens
  screen UserList {
    layout: grid(3)
    components: [
      UserCard,
      Pagination
    ]
    actions: [create, edit, delete]
  }
}
```

### 3. Components

Reusable UI components with variants:

```seed
component Button {
  // Base styles
  base {
    padding: spacing(4)
    border: none
    borderRadius: size(4px)
  }
  
  // Variants
  variants {
    primary: {
      background: color(tokens.colors.primary)
      text: color(white)
    }
    secondary: {
      background: color(transparent)
      text: color(tokens.colors.primary)
      border: {
        width: size(1px)
        style: solid
        color: color(tokens.colors.primary)
      }
    }
  }
  
  // States
  states {
    hover: {
      opacity: number(0.9)
    }
    disabled: {
      opacity: number(0.5)
      cursor: not-allowed
    }
  }
}
```

## Best Practices

1. **Use Types Consistently**
   - Always specify value types
   - Use token references when possible
   - Validate values at parse time

2. **Structure Modules Clearly**
   - One component per file
   - Group related tokens
   - Use explicit imports/exports

3. **Follow Component Patterns**
   - Define clear schemas
   - Use consistent variant names
   - Handle all states

4. **Maintain Application Structure**
   - Separate concerns (entities, UI, themes)
   - Use consistent naming
   - Follow domain-driven design principles
