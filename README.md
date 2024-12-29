# SeedSpec Language

SeedSpec is a minimal, declarative language for defining data-driven applications.

## Quick Start

1. Install:
   ```bash
   pip install -e .
   ```

2. Create app.seed:
   ```seed
   model Task {
       title text
       done bool = false
   }

   screen Tasks using Task
   ```

3. Generate app:
   ```bash
   seedc app.seed -o my-app
   ```

4. Run app:
   ```bash
   cd my-app
   npm install
   npm start
   ```

## Example

```seed
model Task {
  title text
  done bool = false
}

screen Tasks using Task
```

## Core Features

Currently Implemented:
- **Models** - Define data with 3 basic types:
  - text
  - num
  - bool
- **Screens** - Auto-generated CRUD interfaces
- **Data Binding** - Basic model-screen binding via 'using' keyword
- **Title Fields** - Designate display fields with 'as title'

## Documentation

See the [docs](docs/) directory for detailed documentation.

## Status

SeedSpec is currently in early prototype phase with minimal features:
- Basic React app generation with Tailwind CSS
- Simple CRUD operations
- Form inputs mapped to model types
- Basic routing

## Contact

- GitHub Issues: Bug reports & feature requests
- Email: info@noodleseed.com

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
| Data Modeling | Basic Models | ✓ Implemented | Define data structures with 3 basic types (text, num, bool) |
|              | Title Fields | ✓ Implemented | Designate display fields with 'as title' |
|              | Types | ⚡ Basic | Only text, num, and bool supported |
|              | Default Values | 🚧 Planned | Specify default field values |
|              | Relationships | 🚧 Planned | Model relationships and references |
| UI Components | Basic Screens | ✓ Implemented | Simple screens with model binding |
|              | CRUD Operations | ✓ Implemented | Auto-generated create, read, update, delete |
|              | Data Binding | ⚡ Basic | Simple model-to-screen binding via 'using' |
|              | Components | 🚧 Planned | Define reusable UI components |
|              | External Components | 🚧 Planned | Use components from external libraries |
|              | Layout System | 🚧 Planned | Define component positioning |
|              | Styling | ⚡ Basic | Basic Tailwind CSS integration |
| Business Logic | Actions | 🚧 Planned | Custom data operations |
|              | Validation | 🚧 Planned | Data validation rules |
|              | Workflows | 🚧 Planned | Multi-step processes |
| Integration | Imports | 🚧 Planned | Import external resources |
|            | API Integration | 🚧 Planned | Connect to backend services |
|            | Authentication | 🚧 Planned | User auth and authorization |

Status Key:
- ✓ Implemented: Feature is complete and working
- ⚡ Basic: Minimal implementation available
- 🚧 Planned: Feature is designed but not yet implemented

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
