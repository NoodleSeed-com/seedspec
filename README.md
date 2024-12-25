# Seed Specification Language

[![Project Status: Prototype](https://img.shields.io/badge/Project%20Status-Prototype-yellow.svg)]()
[![License](https://img.shields.io/badge/license-Dual%20GPL%2FCommercial-blue.svg)](LICENSE.md)

SeedSpec is a minimal, declarative language for rapidly prototyping web applications. Looking ahead, SeedSpec aims to evolve into a comprehensive solution for defining entire end-to-end production business applications, completely declaratively. It will provide built-in functional components and integrations with popular online services, all while maintaining a focus on minimal token usage, readability, and deterministic behavior.

## Quick Example

This example demonstrates a simple task management app with an integrated AI assistant using inline screen definitions.

```seed
import "@stdlib/ai" as ai

app Todo "Task Management App" {
  model Users "Users" {
    name text = "New User"
    email text = ""
    role text = "member"
  }

  model Tasks "Tasks" {
    title text = "New Task"
    done bool = false
    priority num = 3
  }

  data {
    Users "User Data" [
      { name: "John Doe", email: "john@example.com", role: "admin" },
      { name: "Jane Smith", email: "jane@example.com", role: "member" }
    ]

    Tasks "Task Data" [
      { title: "Create mockups", done: false, priority: 1 },
      { title: "Review design", done: true, priority: 2 }
    ]
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
- **Modular Design:** Explicit imports for better organization.
- **Unified Full-Stack Language (Future):** Envisioned to cover everything from UI (fonts, colors, themes) to database schema, business logic, workflows, and integrations, all defined declaratively. These features represent our long-term vision for SeedSpec. While the current prototype focuses on frontend development and core language features, we are actively working towards expanding SeedSpec into a comprehensive solution for building complete business applications.
- **Built-in Integrations (Future):** Will include pre-built components for integrating with popular services like chatbot APIs, maps, calendars, CRMs, and other essential tools for business applications. These features represent our long-term vision for SeedSpec. While the current prototype focuses on frontend development and core language features, we are actively working towards expanding SeedSpec into a comprehensive solution for building complete business applications.

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

Currently, SeedSpec generates React components with TypeScript types, styled components, basic routing, and simple state management. This represents our initial focus on providing a robust frontend prototyping solution. As we progress towards our long-term vision of a unified full-stack language, we will expand SeedSpec's capabilities to include backend generation, database schema definition, and seamless integration with various online services.

## 📚 Documentation

- **[Getting Started](docs/getting-started.md)**
  - [Quick Start](docs/getting-started/quick-start.md)
  - [First Prototype](docs/getting-started/first-prototype.md)

- **[Core Concepts](docs/core-concepts/)**
  - [Basic Types](docs/core-concepts/types.md)
  - [Components](docs/core-concepts/components.md)
  - [Language Structure](docs/core-concepts/language-structure.md)

## 🛠️ Development Status

SeedSpec is currently in the prototype phase, focusing on representing working prototypes with the ability to integrate with online services. While our initial development includes an example integration with Google Cloud services, our goal is to support a wide range of platforms and services in the future. This will enable developers to easily connect their SeedSpec applications to the tools and services they need. The prototype phase allows us to build a solid foundation for SeedSpec's core functionality and gather feedback from early users. This iterative approach ensures that we are on the right path towards achieving our long-term vision.

## 📱 Contact & Support

- **GitHub Issues**: Bug reports & feature requests
- **Discord**: Community chat & support
- **Email**: [info@noodleseed.com](mailto:info@noodleseed.com)

---
