# Seed Specification Language

[![Project Status: Language Design](https://img.shields.io/badge/Project%20Status-Language%20Design-blue.svg)]()
[![License](https://img.shields.io/badge/license-Dual%20GPL%2FCommercial-blue.svg)](LICENSE.md)
[![Documentation Status](https://img.shields.io/badge/docs-latest-brightgreen.svg)]()

Seed Spec is an AI-native language that generates production-ready applications from simple specifications. Write what you want, get working software.

## Quick Example

## Example Specification

```yaml
app TodoApp {
  # Core domain model
  entity Task {
    title: string
    done: bool = false
  }

  # UI definition (implies standard patterns)
  screen Tasks {
    list: [title, done]    # Will imply search, sort, pagination
    actions: [create, done] # Will imply proper handlers
  }
}
```

This specification will eventually generate a complete application, but the generation tools are still under development.

## 🌟 Key Features

- **AI-First Design**: Optimized for LLM generation and modification
- **Intent-Focused**: Express what you want, not how to build it
- **Smart Defaults**: Production patterns built-in, override only when needed
- **Full Stack**: One specification drives all application layers
- **Tech Independent**: Target any modern technology stack
- **Maps Integration**: Built-in support for location-based features and mapping

## 🎯 Smart Defaults

Seed Spec minimizes boilerplate through intelligent defaults:

- `string` fields imply validation, indexing, and proper UI handling
- `list` screens imply pagination, sorting, and search
- `actions` imply proper handlers, validation, and error handling
- All entities get automatic CRUD operations
- Security best practices are automatically applied
- `location` fields imply geocoding, map rendering, and distance calculations
- `map` screens imply clustering, search radius, and interactive controls

Override defaults only when needed:
```bash
entity User {
  # Override string defaults
  name: string {
    min: 3,
    max: 50
  }
  
  # Use defaults
  email: email  # Implies validation, uniqueness
}

# Maps integration with smart defaults
entity Store {
  location: location  # Implies geocoding, validation, map rendering
}

screen StoreLocator {
  map: [location]     # Implies clustering, search, radius filters
}
```

## 🏗️ Generated Stack

Seed Spec generates a complete, production-ready stack:

### Frontend
- React + TypeScript
- Responsive UI components
- State management
- Form handling
- API integration
- Maps components

### Backend
- FastAPI + SQLAlchemy
- REST endpoints
- Authentication
- Validation
- Error handling

### Infrastructure
- Database migrations
- Docker configuration
- API documentation
- Testing setup

## 📚 Documentation

- **[Getting Started](docs/getting-started.md)**
  - [Introduction](docs/getting-started/introduction.md)
  - [Installation](docs/getting-started/installation.md)
  - [Quick Start](docs/getting-started/quick-start.md)
  - [First Application](docs/getting-started/first-app.md)

- **[Core Concepts](docs/core-concepts/)**
  - [Type System](docs/core-concepts/type-system.md)
  - [Business Rules](docs/core-concepts/business-rules.md)
  - [UI Patterns](docs/core-concepts/ui-patterns.md)
  - [Architecture](docs/core-concepts/architecture.md)

- **[Examples](docs/examples/)**
  - [Basic CRUD](docs/examples/basic-crud.md)
  - [Business App](docs/examples/business-app.md)
  - [Dashboard](docs/examples/dashboard.md)
  - [SaaS](docs/examples/saas.md)

- **[Reference](docs/reference/)**
  - [Types](docs/reference/types.md)
  - [Patterns](docs/reference/patterns.md)
  - [CLI](docs/reference/cli.md)

## 🛠️ Development Status

Seed Spec is in active development (v0.1.0) with a focus on:

1. **Language Evolution**
   - Expanding core patterns
   - Enhancing type system
   - Adding advanced features
   - Improving validation

2. **Generation Pipeline**
   - LLM prompt optimization
   - Code quality improvements
   - Performance tuning
   - Testing automation

3. **Developer Experience**
   - IDE integration
   - Live preview
   - Debug tools
   - Error messages

4. **Enterprise Features**
   - Multi-tenancy
   - Authentication
   - Authorization
   - Audit logging
   - Compliance

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
  Making software development more natural for humans and machines
</div>

