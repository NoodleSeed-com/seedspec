# Getting Started with SeedML

## Installation

```bash
pip install -e .
```

## Quick Start

1. Create a new project:
```bash
seedml new my-app
cd my-app
```

2. Edit your app.seed file:
```yaml
app MyApp {
  entity User {
    name: string
    email: email
    active: bool = true
  }

  screen Users {
    list: [name, email, active]
    actions: [create, edit]
  }
}
```

3. Generate and run:
```bash
seedml generate
seedml run
```

## Next Steps

- Read the [Core Concepts](./core-concepts/overview.md)
- Try the [Examples](./examples/basic-crud.md)
- Learn about [Patterns](./reference/patterns.md)

## Learning Path

1. Start Here:
   - [Quick Start Guide](./quick-start.md)
   - [First Application](./first-app.md)

2. Core Concepts:
   - [Architecture](../core-concepts/architecture.md)
   - [Type System](../core-concepts/type-system.md)
   - [Business Rules](../core-concepts/business-rules.md)
   - [UI Patterns](../core-concepts/ui-patterns.md)

3. Examples:
   - [Basic CRUD](../examples/basic-crud.md)
   - [Business App](../examples/business-app.md)
   - [Dashboard](../examples/dashboard.md)
   - [SaaS](../examples/saas.md)

4. Reference:
   - [Types](../reference/types.md)
   - [Patterns](../reference/patterns.md)
   - [CLI](../reference/cli.md)
