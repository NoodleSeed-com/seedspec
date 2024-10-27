# SeedML

[![Project Status: Initial Development](https://img.shields.io/badge/Project%20Status-Initial%20Development-yellow.svg)]()
[![License](https://img.shields.io/badge/license-Dual%20GPL%2FCommercial-blue.svg)](LICENSE.md)

SeedML is an AI-native programming language that enables rapid application development through simple, declarative specifications. It's designed to be equally understandable by humans and AI.

## Key Features

- **AI-First Design**: Optimized for LLM generation and modification
- **Smart Defaults**: Common patterns built-in, override when needed
- **Single Source**: One specification describes your entire application
- **Technology Independent**: Target any modern tech stack

## Quick Example

```yaml
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

## Documentation

- [Getting Started](docs/getting-started/)
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

