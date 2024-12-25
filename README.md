# Seed Specification Language

[![Project Status: Prototype](https://img.shields.io/badge/Project%20Status-Prototype-yellow.svg)]()
[![License](https://img.shields.io/badge/license-Dual%20GPL%2FCommercial-blue.svg)](LICENSE.md)

SeedSpec is a minimal, declarative language for rapidly prototyping web applications. Write simple specifications with basic typing and get working UI prototypes with built-in UI/UX best practices.

## Quick Example

This example demonstrates a simple task management app with an integrated AI assistant using inline screen definitions.

```seed
import "@stdlib/ai" as ai

app Todo "Task Management App" {
  model User "User" {
    User {
      name text = "New User"
      email text = ""
      role text = "member"
    }
  }

  model Tasks "Tasks" {
    Task {
      title text = "New Task"
      done bool = false
      priority num = 3
    }
  }

  data {
    data Users "User Data" {
      use User
      data [
        { name: "John Doe", email: "john@example.com", role: "admin" },
        { name: "Jane Smith", email: "jane@example.com", role: "member" }
      ]
    }

    data Tasks "Task Data" {
      use Tasks
      data [
        { title: "Create mockups", done: false, priority: 1 },
        { title: "Review design", done: true, priority: 2 }
      ]
    }
  }

  component task_card "Task Card Component" {
    input {
      task: Task
    }
  }

  component user_card "User Card Component" {
    input {
      user: User
    }
  }

  // Define the TaskList screen inline
  screen TaskList "Task List" {
    use task_card
    use ai.Chatbot {
      systemPrompt: "You are a helpful assistant that helps users manage their tasks. You can ask the user for more details about their tasks, suggest deadlines, and help them prioritize their work. You can also answer general questions and provide helpful tips."
      ui: {
        mode: "modal"
        trigger: "button"
      }
    }
    data tasks
  }

  // Define the UserList screen inline
  screen UserList "User List" {
    use user_card
    data users
  }
}
```

**New Feature:** You can now define screens inline within the `app` block using the `screen` keyword followed by the screen name, an optional display name (in quotes), and the screen definition within curly braces. This example also demonstrates how to integrate pre-built components from external libraries, such as the `Chatbot` component from `@stdlib/ai`, and configure them directly within the screen definition.

## 🌟 Key Features

- **Optimized for Generation with LLMs**
- **Deterministic, Declarative and cross compilable** into different target execution and deployment targets.
- **Easy to read and understand** for people.
- **Modular Design** with explicit imports.

## 🎯 Type System

SeedSpec uses a type-safe system to ensure data integrity.

```seed
types {
  // Core data types
  text: {
    min: number
    max: number
    pattern?: regex
  }
  
  num: {
    min?: number
    max?: number
    integer?: boolean
  }

  bool: {}
}
```

## Components

Components are defined with the `component` keyword:

```seed
component Button {
    input {
        label: text
    }
}
```

## Imports

```seed
// Import from standard library
import "@stdlib/core"

// Import a specific file
import "./components"
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
  - [Language Structure](docs/core-concepts/language-structure.md)

## 🛠️ Development Status

In the first phase, SeedSpec is being developed to represent working prototypes that have built-in Google Cloud services.

Later, this language will be extended to other targets and end-to-end deployable applications, not just prototypes.

## 📱 Contact & Support

- **GitHub Issues**: Bug reports & feature requests
- **Discord**: Community chat & support
- **Email**: [info@noodleseed.com](mailto:info@noodleseed.com)

---
