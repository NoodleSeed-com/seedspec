# Seed Specification Language

[![Project Status: Language Design](https://img.shields.io/badge/Project%20Status-Language%20Design-blue.svg)]()
[![License](https://img.shields.io/badge/license-Dual%20GPL%2FCommercial-blue.svg)](LICENSE.md)
[![Documentation Status](https://img.shields.io/badge/docs-latest-brightgreen.svg)]()

SeedSpec is a type-safe, AI-native language that generates production-ready applications from clear specifications. Write what you want with strong typing, get working software.

## Quick Example

```seed
// Import standard library
import "@stdlib/core"
use { Button, Card } from "@stdlib/components"

// Core application
app TodoApp {
  // Type-safe domain model
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
  
  // Strongly typed theme
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
  
  // Component with schema validation
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
  
  // Type-safe screen definition
  screen Tasks {
    layout: grid(3)
    components: [TaskCard]
    actions: [
      create: {
        validate: [
          task.title.length > 0,
          task.due > now()
        ]
      }
    ]
  }
}
```

## 🌟 Key Features

- **Type Safety First**: Catch errors at compile time with explicit types and validation
- **Clear Module System**: Explicit imports/exports and module boundaries
- **Component Schemas**: Define reusable contracts for components
- **Smart Defaults**: Production patterns built-in, override when needed
- **Full Stack**: One specification drives all application layers
- **Tech Independent**: Target any modern technology stack
- **Standard Library**: Rich set of pre-built, type-safe components and themes

## 🎯 Type System

SeedSpec enforces type safety through explicit type declarations:

```seed
types {
  // Basic types with validation
  string {
    min?: number
    max?: number
    pattern?: regex
  }
  
  // UI-specific types
  color {
    type: hex | rgb | hsl | token
    value: string
  }
  
  // Component schemas
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
}
```

## 🏗️ Generated Stack

SeedSpec generates a complete, type-safe stack:

### Frontend
- React + TypeScript
- Type-safe components
- Strongly typed state management
- Validated forms
- Type-safe API integration

### Backend
- FastAPI + SQLAlchemy
- Type-safe endpoints
- Schema validation
- Error handling
- Database type safety

### Infrastructure
- Type-safe migrations
- Configuration validation
- API type definitions
- Test type coverage

## 📚 Documentation

- **[Getting Started](docs/getting-started.md)**
  - [Introduction](docs/getting-started/introduction.md)
  - [Installation](docs/getting-started/installation.md)
  - [Quick Start](docs/getting-started/quick-start.md)
  - [First Application](docs/getting-started/first-app.md)

- **[Core Concepts](docs/core-concepts/)**
  - [Type System](docs/core-concepts/type-system.md)
  - [Language Structure](docs/core-concepts/language-structure.md)
  - [Business Rules](docs/core-concepts/business-rules.md)
  - [Architecture](docs/core-concepts/architecture.md)

- **[Examples](docs/examples/)**
  - [Basic CRUD](docs/examples/basic-crud.md)
  - [Business App](docs/examples/business-app.md)
  - [Dashboard](docs/examples/dashboard.md)
  - [SaaS](docs/examples/saas.md)

## 🛠️ Development Status

SeedSpec is in active development (v0.1.0) with a focus on:

1. **Type System**
   - Strong type checking
   - Compile-time validation
   - Clear error messages
   - IDE integration

2. **Module System**
   - Explicit imports/exports
   - Clear boundaries
   - Dependency management
   - Version control

3. **Developer Experience**
   - Type-aware IDE support
   - Real-time validation
   - Debug tools
   - Error tracing

4. **Enterprise Features**
   - Type-safe multi-tenancy
   - Authentication schemas
   - Authorization rules
   - Audit logging
   - Compliance validation

## 🤝 Contributing

We welcome contributions! See [CONTRIBUTING.md](CONTRIBUTING.md) for:
- Development setup
- Coding standards
- Pull request process
- Issue guidelines

## 📄 License

- **Open Source**: [GNU GPL v3.0](LICENSE-GPL.md)
  - Free for personal and open source use
  - Modifications must be shared
  - Commercial use requires license

- **Commercial License**
  - Coming soon
  - Priority support
  - Private modifications
  - Enterprise features

## 📱 Contact & Support

- **Website**: https://noodleseed.com
- **Documentation**: https://docs.noodleseed.com
- **GitHub Issues**: Bug reports & feature requests
- **Discord**: Community chat & support
- **Email**: info@noodleseed.com
- **Twitter**: [@noodleseed](https://twitter.com/noodleseed)

## 🙏 Acknowledgments

Special thanks to:
- Anthropic for Claude API access
- Our open source contributors
- Early adopters and testers

---

<div align="center">
  Built with ❤️ by <a href="https://noodleseed.com">Noodle Seed</a>
  <br>
  Making software development more type-safe and maintainable
</div>
