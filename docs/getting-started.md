# Getting Started with SeedML

## Installation

```bash
npm install -g seedml
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

- Read the [Core Concepts](core-concepts/overview.md)
- Try the [Examples](examples/basic-crud.md)
- Learn about [Patterns](reference/patterns.md)
