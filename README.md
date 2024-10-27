# SeedML

[![Project Status: Initial Development](https://img.shields.io/badge/Project%20Status-Initial%20Development-yellow.svg)]()
[![License](https://img.shields.io/badge/license-Dual%20GPL%2FCommercial-blue.svg)](LICENSE.md)

SeedML is an AI-native programming language that bridges natural language requirements and production-ready applications. It enables rapid application development through simple, declarative specifications that are equally understandable by humans and AI.

## How It Works

SeedML follows a two-phase transformation process:

### Phase 1: Natural Language → SeedML
Convert business requirements into SeedML specifications:
- Write SeedML directly (human)
- Generate from natural language using AI
- Hybrid approach (human + AI)

```yaml
# Example SeedML specification
app TaskManager {
  entity Task {
    title: string
    status: todo->doing->done
    assigned: User?
    priority: low/medium/high
  }

  screen TaskBoard {
    layout: kanban(status)
    card: [title, assigned.avatar, priority]
    actions: [assign, move, edit]
  }
}
```

### Phase 2: SeedML → Implementation
Transform SeedML into production applications:
- Currently: AI-powered generation using LLMs
- Future: Deterministic compilation
- Hybrid approaches possible

The current implementation uses Claude to generate:
- React + TypeScript frontend
- FastAPI + SQLAlchemy backend
- MySQL database
- Complete DevOps setup

## Key Features

- **Natural Language Friendly**: Optimized for both human and AI authoring
- **AI-First Design**: Works seamlessly with language models
- **Smart Defaults**: Common patterns built-in, override when needed
- **Single Source**: One specification describes your entire application
- **Technology Independent**: Target any modern tech stack

## Documentation

- [Getting Started](docs/getting-started/)
- [Core Concepts](docs/core-concepts/)
- [Examples](docs/examples/)
- [Reference](docs/reference/)

## Current Status

SeedML is in early development. The language specification is evolving based on real-world usage and feedback. Current focus:

- Phase 1: Using LLMs for flexible code generation
- Establishing core language patterns and qualities
- Building initial tooling and documentation
- Gathering community feedback

Future plans include:
- Deterministic compilers for reliability and efficiency
- Enhanced IDE tooling
- Expanded pattern library
- Enterprise features

## Contributing

See [CONTRIBUTING.md](CONTRIBUTING.md) for how to get involved.

## License

- Open Source: [GNU GPL v3.0](LICENSE-GPL.md)
- Commercial License: Coming soon

## Contact

- Website: https://noodleseed.com
- Email: info@noodleseed.com

---

Built with ❤️ by Noodle Seed

