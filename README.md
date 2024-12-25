# Seed Specification Language

[![Project Status: Prototype](https://img.shields.io/badge/Project%20Status-Prototype-yellow.svg)]()
[![License](https://img.shields.io/badge/license-Dual%20GPL%2FCommercial-blue.svg)](LICENSE.md)

SeedSpec is a minimal, declarative language for rapidly prototyping web applications. Write simple specifications with basic typing and get working UI prototypes with built-in UI/UX best practices.

## Quick Example

```seed
app "Task Management App" {
  model {
    User {
      name text = "New User"
      email text = ""
      role text = "member"
    }

    Task {
      title text = "New Task"
      done bool = false
      priority num = 3
    }
  }
  
  data {
    users: User[] = [
      ["John Doe", "john@example.com", "admin"],
      ["Jane Smith", "jane@example.com", "member"]
    ]

    tasks: Task[] = [
      ["Create mockups", false, 1],
      ["Review design", true, 2]
    ]
  }
  
  component task_card {
    input {
      task: Task
    }
  }
  
  component user_card {
    input {
      user: User
    }
  }
  
  screen {
    TaskList {
      use task_card
      data tasks
    }

    UserList {
      use user_card
      data users
    }
  }
}
```

## 🌟 Key Features

- **Optimized for Generation with LLMs**
- **Deterministic, Declarative and cross compilable** into different target execution and deployment targets.
- **Easy to read and understand** for people.

## 🎯 Type System

Basic types for rapid prototyping:

```seed
// Core types with built-in defaults
type str(min?..max?) = ""      // Empty string default
type num(min?..max?) = 0       // Zero default
type bool = false              // False default

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

In the first phase, SeedSpec is being developed to represent working prototypes that have built-in Google Cloud services.

Later, this language will be extended to other targets and end-to-end deployable applications, not just prototypes.

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
