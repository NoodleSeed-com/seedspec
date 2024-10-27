# SeedML

[![Project Status: Initial Development](https://img.shields.io/badge/Project%20Status-Initial%20Development-yellow.svg)]()
[![License](https://img.shields.io/badge/license-Dual%20GPL%2FCommercial-blue.svg)](LICENSE.md)
[![Python Version](https://img.shields.io/badge/python-3.8%2B-blue.svg)]()
[![Documentation Status](https://img.shields.io/badge/docs-latest-brightgreen.svg)]()

SeedML is an AI-native programming language that bridges the gap between human intent and production software. It enables rapid application development through declarative specifications that are natural for both humans and AI to read and write.

## 🚀 Quick Start

```bash
# Install SeedML
pip install -e .
export ANTHROPIC_API_KEY='your-api-key'

# Create a simple app
cat > app.seed << EOF
app TodoApp {
  entity Task {
    title: string!
    done: bool = false
  }
  screen Tasks {
    list: [title, done]
    actions: [create, toggle-done]
  }
}
EOF

# Generate the application
seedml generate app.seed
```

## 🌟 Key Features

- **Natural Expression**: Write specifications in a clear, intent-focused language
- **AI-First Design**: Optimized for both human and AI interaction
- **Smart Defaults**: Production patterns built-in, customizable when needed
- **Single Source**: One specification drives all application layers
- **Tech Independence**: Target any modern technology stack

## 🏗️ Generated Stack

SeedML currently generates a modern, production-ready stack:

- **Frontend**: React + TypeScript
  - Material UI components
  - Redux state management
  - React Router navigation
  - Form validation
  - API integration

- **Backend**: FastAPI + SQLAlchemy
  - REST API endpoints
  - Database models
  - Authentication
  - Validation
  - Error handling

- **Database**: MySQL
  - Schema migrations
  - Indexes
  - Relationships
  - Constraints

- **DevOps**:
  - Docker containers
  - Kubernetes manifests
  - CI/CD pipelines
  - Monitoring setup

## 📚 Documentation

- **[Getting Started](getting-started.md)**
  - [Introduction](getting-started/introduction.md)
  - [Installation](getting-started/installation.md)
  - [Quick Start](getting-started/quick-start.md)
  - [First Application](getting-started/first-app.md)

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

SeedML is in active development (v0.1.0) with a focus on:

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

