# Seed Specification Language

[![Project Status: Prototype](https://img.shields.io/badge/Project%20Status-Prototype-yellow.svg)]()
[![License](https://img.shields.io/badge/license-Dual%20GPL%2FCommercial-blue.svg)](LICENSE.md)

SeedSpec is a minimal, declarative language for rapidly prototyping web applications. Looking ahead, SeedSpec aims to evolve into a comprehensive solution for defining entire end-to-end production business applications, completely declaratively. It will provide built-in functional components and integrations with popular online services, all while maintaining a focus on minimal token usage, readability, and deterministic behavior.

## Quick Example

This example demonstrates a simple task management app with an integrated AI assistant using inline screen definitions.

```seed
import "@stdlib/ai" as ai

app Todo "Task Management App" {
  model User "User" {
    name text = "New User"
    email text = ""
    role text = "member"
  }

  model Task "Task" {
    title text = "New Task"
    done bool = false
    priority num = 3
  }

  data {
    User "User Data" [
      { name: "John Doe", email: "john@example.com", role: "admin" },
      { name: "Jane Smith", email: "jane@example.com", role: "member" }
    ]

    Task "Task Data" [
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

**Language Feature Status**

| Feature Category | Feature | Status | Description |
|-----------------|---------|---------|-------------|
| Data Modeling | [Models](docs/models.md) | ✓ Available | Define data structures with typed fields |
| | [Types](docs/types.md) | ✓ Available | Basic types (text, num, bool) with constraints |
| | [Relationships](docs/relationships.md) | ✓ Available | Model relationships and references |
| | [Default Values](docs/default-values.md) | ✓ Available | Specify default field values |
| UI Components | [Components](docs/components.md) | ✓ Available | Define reusable UI components |
| | [Screens](docs/screens.md) | ✓ Available | Define application screens/pages |
| | [Data Binding](docs/data-binding.md) | ✓ Available | Bind data to UI components |
| | [External Components](docs/external-components.md) | ✓ Available | Use components from external libraries |
| | [Layout System](docs/layout-system.md) | 🚧 In Development | Define component positioning and structure |
| | [Styling](docs/styling.md) | 🚧 In Development | Define component appearance and themes |
| | [Event Handling](docs/event-handling.md) | 🚧 In Development | Handle user interactions and events |
| | [Forms](docs/forms.md) | 🚧 In Development | Form validation and submission |
| Business Logic | [Actions](docs/actions.md) | 🚧 In Development | Define data mutations and operations |
| | [Validation Rules](docs/validation-rules.md) | 🚧 In Development | Custom data validation logic |
| | [Workflows](docs/workflows.md) | 🚧 In Development | Multi-step business processes |
| | [State Management](docs/state-management.md) | 🚧 In Development | Application state handling |
| Integration | [Imports](docs/imports.md) | ✓ Available | Import external libraries and files |
| | [API Integration](docs/api-integration.md) | 🚧 In Development | Connect to backend services |
| | [Authentication](docs/authentication.md) | 🚧 In Development | User authentication and authorization |
| | [External Services](docs/external-services.md) | 🚧 In Development | Integration with third-party services |

## 🌟 Key Features

- **Optimized for Generation with LLMs.**
- **Deterministic, Declarative and Cross Compilable** into different target execution and deployment targets.
- **Easy to Read and Understand** for people.
- **Modular Design:** Explicit imports for better organization.
- **Unified Full-Stack Language (Future):** Covers everything from UI (fonts, colors, themes) to database schema, business logic, workflows, and integrations, all defined declaratively. These features represent our long-term vision for SeedSpec. While the current prototype focuses on frontend development and core language features, we are actively working towards expanding SeedSpec into a comprehensive solution for building complete business applications.
- **Built-in Integrations (Future):** Includes pre-built components for integrating with popular services like chatbot APIs, maps, calendars, CRMs, and other essential tools for business applications. These features represent our long-term vision for SeedSpec. While the current prototype focuses on frontend development and core language features, we are actively working towards expanding SeedSpec into a comprehensive solution for building complete business applications.

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
