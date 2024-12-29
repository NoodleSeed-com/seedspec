# Seed Specification Language

[![Project Status: Prototype](https://img.shields.io/badge/Project%20Status-Prototype-yellow.svg)]()
[![License](https://img.shields.io/badge/license-Dual%20GPL%2FCommercial-blue.svg)](LICENSE.md)

SeedSpec is a minimal, declarative language for rapidly prototyping web applications. Looking ahead, SeedSpec aims to evolve into a comprehensive solution for defining entire end-to-end production business applications, completely declaratively. It will provide built-in functional components and integrations with popular online services, all while maintaining a focus on minimal token usage, readability, and deterministic behavior.

## Quick Example

This example demonstrates a simple task management app using implicit CRUD operations and an implicit CRUD screen.

```seed
app Todo "Task Management App" {
  model Todo {
    title text as title
    completed bool = false
    dueDate date?
    priority num?
    category text?
    notes text?
  }

  data {
    Todos: Todo[] [
        { title: "Buy groceries", completed: false, dueDate: 2023-12-25, priority: 1, category: "Shopping", notes: "Remember the milk!" },
        { title: "Walk the dog", completed: true, dueDate: 2023-12-24, priority: 2, category: "Chores", notes: "Take the long route" }
    ]
  }

  screen Todos // Implicitly uses the 'Todo' model because of the 'Todos' dataset
}
```

**Language Feature Status**

| Feature Category | Feature | Status | Description |
|-----------------|---------|---------|-------------|
| Data Modeling | [Models](docs/models.md)          | ✓ Available | Define data structures with typed fields, required/optional properties, implicit/explicit IDs, and title fields |
|              | [Types](docs/types.md)            | ✓ Available | Basic types (text, num, bool) with constraints                                                                   |
|              | [Relationships](docs/relationships.md) | ✓ Available | Model relationships and references                                                                               |
|              | [Default Values](docs/default-values.md) | ✓ Available | Specify default field values                                                                                    |
|              | Implicit CRUD Actions             | ✓ Available | `create`, `update`, and `delete` actions are implicitly available for each model                                  |
| UI Components | [Components](docs/components.md)    | ✓ Available | Define reusable UI components                                                                                   |
|              | [Screens](docs/screens.md)        | ✓ Available | Define application screens/pages                                                                                |
|              | Implicit CRUD Screens           | ✓ Available | A CRUD screen is implicitly available for each model and can be explicitly requested or customized               |
|              | [Data Binding](docs/data-binding.md) | ✓ Available | Bind data to UI components                                                                                      |
|              | [External Components](docs/external-components.md) | ✓ Available | Use components from external libraries                                                                            |
|              | [Layout System](docs/layout-system.md) | 🚧 In Development | Define component positioning and structure                                                                        |
|              | [Styling](docs/styling.md)        | 🚧 In Development | Define component appearance and themes                                                                             |
|              | [Event Handling](docs/event-handling.md) | 🚧 In Development | Handle user interactions and events                                                                              |
|              | [Forms](docs/forms.md)            | 🚧 In Development | Form validation and submission (now largely handled implicitly)                                                   |
| Business Logic | [Actions](docs/actions.md)        | ✓ Available | Define custom data mutations and operations (CRUD operations are implicitly available)                           |
|              | [Validation Rules](docs/validation-rules.md) | 🚧 In Development | Custom data validation logic                                                                                    |
|              | [Workflows](docs/workflows.md)    | 🚧 In Development | Multi-step business processes                                                                                   |
|              | [State Management](docs/state-management.md) | 🚧 In Development | Application state handling                                                                                       |
| Integration | [Imports](docs/imports.md) | ✓ Available | Import external libraries and files |
| | [API Integration](docs/api-integration.md) | 🚧 In Development | Connect to backend services |
| | [Authentication](docs/authentication.md) | 🚧 In Development | User authentication and authorization |
| | [External Services](docs/external-services.md) | 🚧 In Development | Integration with third-party services |

## 🌟 Key Features

- **Optimized for Generation with LLMs.**
- **Deterministic and Declarative** into different target execution and deployment targets.
- **Easy to Read and Understand** for people.
- **Modular Design:** Explicit imports for better organization.
- **Implicit CRUD Operations:** Automatically generated `create`, `update`, and `delete` actions for all models.
- **Implicit Screen Generation:** Automatically generated CRUD screens for all models.
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
component Button "Button Component" {
    input {
        label: text
        onClick: action
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
