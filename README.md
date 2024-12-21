# Seed Specification Language

[![Project Status: Language Design](https://img.shields.io/badge/Project%20Status-Language%20Design-blue.svg)]()
[![License](https://img.shields.io/badge/license-Dual%20GPL%2FCommercial-blue.svg)](LICENSE.md)
[![Documentation Status](https://img.shields.io/badge/docs-latest-brightgreen.svg)]()

SeedSpec is a token-efficient, declarative language optimized for LLM generation that produces full-stack business applications from clear specifications. Write what you want with strong typing, get working software.

## Quick Example

```seed
mod todo {
  use { @core, @ui }
  
  // Domain model
  data {
    Task {
      title str(3..100)
      done bool
      due @future
    }
  }
  
  // Business process
  flow TaskFlow {
    new -> active: assign
    active -> done: complete
    * -> archived: archive
  }
  
  // UI components
  comp task_card {
    in { task Task, done fn }
    style {
      bg white
      pad med
      border @primary
    }
  }
  
  // Screens
  ui {
    TaskList {
      layout grid(3)
      show task_card
      acts { create, done }
      rules {
        create needs title
        done when all done
      }
    }
  }
  
  // Theme
  theme {
    colors {
      primary #0066cc
      success @green.5
      error @red.5
    }
    space {
      sm 4
      med 8
    }
  }
}
```

## 🌟 Key Features

- **Token Efficient**: Optimized syntax for LLM generation while maintaining readability
- **Pure Declarative**: Clear separation of what vs how across all features
- **Full Stack**: Complete coverage from UI to database, workflows, and agents
- **Smart Defaults**: Production patterns built-in with context-aware inference
- **Type Safety**: Catch errors at compile time with explicit types and validation
- **Tech Independent**: Target any modern technology stack
- **Standard Library**: Rich set of pre-built components, themes, and patterns

## 🎯 Type System

SeedSpec uses a token-efficient type system with smart inference:

```seed
// Core types
type str(min?..max?) {
  match?: regex
  format?: @email|@url
}

type num(min?..max?) {
  int?: bool
  pos?: bool
}

// UI types 
type color = hex|rgb|@token
type size = px|rem|@token

// Components
comp btn {
  in { txt str, click fn }
  opt { disabled bool }
  var { pri, sec }
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
