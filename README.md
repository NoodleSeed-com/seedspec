# SeedML

[![Project Status: Initial Development](https://img.shields.io/badge/Project%20Status-Initial%20Development-yellow.svg)]()
[![License](https://img.shields.io/badge/license-Dual%20GPL%2FCommercial-blue.svg)](LICENSE.md)

SeedML is an AI-native programming language that bridges the gap between human intent and production software. It enables rapid application development through declarative specifications that are natural for both humans and AI to read and write.

## Vision

Traditional development requires translating business requirements through multiple technical layers, leading to lost context and increased complexity. SeedML solves this by providing:

1. A natural bridge between human intent and working software
2. Clear, declarative specifications that serve as a single source of truth
3. AI-native design that leverages the power of language models
4. Technology-independent patterns that can target any modern stack

## How It Works

SeedML uses a two-phase transformation approach:

### Phase 1: Intent → SeedML
Convert business requirements into SeedML specifications through:
- Direct human authoring
- AI-assisted generation from natural language
- Collaborative human-AI refinement

```yaml
# Business intent: "Task management system with assignments and priorities"
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
- Current: AI-powered generation using LLMs for maximum flexibility
- Future: Deterministic compilers for reliability and efficiency
- Hybrid: Combine approaches based on needs

The current implementation uses Claude to generate:
- React + TypeScript frontend
- FastAPI + SQLAlchemy backend
- MySQL database
- Docker & Kubernetes deployment
- Complete CI/CD pipeline

## Key Features

- **Natural Expression**: Write specifications in a clear, intent-focused language
- **AI-First Design**: Optimized for both human and AI interaction
- **Smart Defaults**: Production patterns built-in, customizable when needed
- **Single Source**: One specification drives all application layers
- **Tech Independence**: Target any modern technology stack

## Current Status

SeedML is in active development with a focus on:

1. Language Evolution
   - Defining core patterns and qualities
   - Gathering real-world usage feedback
   - Refining the specification format

2. Implementation Strategy
   - Phase 1: LLM-based generation for flexibility
   - Phase 2: Deterministic compilation for reliability
   - Hybrid approaches for optimal results

3. Tooling Development
   - CLI tools for generation
   - IDE integration
   - Development workflows

## Getting Started

1. Install SeedML:
```bash
pip install -e .
export ANTHROPIC_API_KEY='your-api-key'
```

2. Create your specification:
```yaml
app MyApp {
  # Your app specification
}
```

3. Generate your application:
```bash
seedml myapp.seed
```

## Documentation

- [Getting Started](docs/getting-started.md)
- [Core Concepts](docs/core-concepts/)
- [Examples](docs/examples/)
- [Reference](docs/reference/)

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

