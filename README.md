# Seed Specification Language

[![Project Status: Prototype](https://img.shields.io/badge/Project%20Status-Prototype-yellow.svg)]()
[![License](https://img.shields.io/badge/license-Dual%20GPL%2FCommercial-blue.svg)](LICENSE.md)

SeedSpec is a minimal, declarative language for rapidly prototyping web applications. Write simple specifications with basic typing and get working UI prototypes with built-in UI/UX best practices.

## Quick Example

```seed
app todo {
  model {
    Task {
      title "Task Title" text(3..100)
      done "Completed" bool
      priority "Priority Level" num(1..5)
    }
  }
  
  data {
    // Positional style - matches field sequence
    tasks: Task[] = [
      ["Create mockups", false, 1],
      ["Review design", true, 2]
    ]
    
    // Explicit style - when field clarity preferred
    featured: Task[] = [
      {
        title: "Important Task",
        done: false,
        priority: 5
      }
    ]
  }
  
  component task_card {
    input { task Task }
    style {
      // Only override built-in defaults when needed
      surface accent
      spacing.lg
    }
  }
  
  screen {
    TaskList {
      use task_card
      data tasks
    }
  }
  
  // Minimal theme overrides - rest uses built-in defaults
  styles {
    brand: colors.indigo.600
    radius: 0
  }
}
```

## 🌟 Key Features

- **Simple Types**: Basic str, num, bool with minimal validation
- **UI Components**: Easy component definitions with props and styling
- **Basic Theming**: Simple color and spacing tokens
- **Quick Prototypes**: Generate working React components fast

## 🎯 Type System

Basic types for rapid prototyping:

```seed
// Core types
type str(min?..max?)
type num(min?..max?)
type bool

// Simple component
comp button {
  in { text str }
  style {
    bg primary
    pad med
  }
}
```

## 🏗️ Generated Output

Creates React components with:
- TypeScript types
- Styled components
- Basic routing
- Simple state management

## 📚 Documentation

- **[Getting Started](docs/getting-started.md)**
  - [Quick Start](docs/getting-started/quick-start.md)
  - [First Prototype](docs/getting-started/first-prototype.md)

- **[Core Concepts](docs/core-concepts/)**
  - [Basic Types](docs/core-concepts/types.md)
  - [Components](docs/core-concepts/components.md)
  - [Theming](docs/core-concepts/theming.md)

## 🛠️ Development Status

SeedSpec is focused on prototyping with:

1. **Basic Types**
   - Simple validation
   - Clear errors

2. **UI Components**
   - React components
   - Basic styling
   - Simple props

3. **Developer Experience**
   - Fast iteration
   - Easy to learn
   - Quick results

## 📱 Contact & Support

- **GitHub Issues**: Bug reports & feature requests
- **Discord**: Community chat & support
- **Email**: info@noodleseed.com

---

<div align="center">
  Built with ❤️ by <a href="https://noodleseed.com">Noodle Seed</a>
  <br>
  Making prototyping faster and easier
</div>
