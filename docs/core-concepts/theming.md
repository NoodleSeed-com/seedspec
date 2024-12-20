# Component-Based Theming

Seed Spec provides a component-based theming system that uses Tailwind tokens to define styles. Themes are defined in the standard library (`src/stdlib/themes.seed`) and compile to Tailwind utility classes.

## Basic Usage

Define component styles using Tailwind tokens:

```javascript
theme default {
  button {
    primary: {
      bg: "blue.500"          // Uses Tailwind color token
      text: "white"           // Uses Tailwind color token
      hover: {
        bg: "blue.600"        // Uses Tailwind color token
      }
      focus: {
        ring: "blue.500"      // Uses Tailwind color token
      }
    }
  }

  card {
    bg: "white"              // Uses Tailwind color token
    border: "gray.200"       // Uses Tailwind color token
    shadow: "sm"             // Uses Tailwind shadow token
    hover: {
      shadow: "md"           // Uses Tailwind shadow token
    }
  }
}
```

Use the compiled theme tokens in components:

```jsx
function Button() {
  const classes = useThemeTokens("button.primary")
  // Compiles to: "bg-blue-500 text-white hover:bg-blue-600 focus:ring-blue-500"
  return <button className={classes}>Click Me</button>
}

function Card() {
  const classes = useThemeTokens("card")
  // Compiles to: "bg-white border-gray-200 shadow-sm hover:shadow-md"
  return <div className={classes}>Content</div>
}
```

## Component Tokens

Theme tokens are organized by component and variant:

### Button Variants
```javascript
button {
  primary: {
    bg: "blue.500"
    text: "white"
  }
  secondary: {
    bg: "gray.100"
    text: "gray.800"
  }
}
```

### Form Elements
```javascript
input {
  base: {
    bg: "white"
    border: "gray.300"
    focus: {
      border: "blue.500"
      ring: "blue.500"
    }
  }
}
```

### Typography
```javascript
typography {
  heading: {
    color: "gray.900"
    font: "sans"
    weight: "bold"
  }
  body: {
    color: "gray.600"
    font: "sans"
  }
}
```

## Dark Mode

Define dark mode variants using Tailwind tokens:

```javascript
theme dark extends default {
  button {
    primary: {
      bg: "blue.400"
      text: "white"
    }
  }

  card {
    bg: "gray.800"
    border: "gray.700"
  }
}
```

The tokens compile to dark mode classes:
```jsx
function Card() {
  const classes = useThemeTokens("card")
  // Compiles to: "bg-white dark:bg-gray-800 border-gray-200 dark:border-gray-700"
  return <div className={classes}>Content</div>
}
```

## Theme Composition

Themes support token composition and inheritance:

```javascript
theme default {
  // Base tokens can be extended
  button {
    base: {
      px: "4"
      py: "2"
      rounded: "md"
    }
    primary: {
      extends: "base"     // Inherits base tokens
      bg: "blue.500"
      text: "white"
    }
  }
}
```

## Smart Defaults

The theme system provides:
- Component-based organization of design tokens
- Automatic compilation to Tailwind classes
- Theme inheritance and composition
- Dark mode support out of the box
