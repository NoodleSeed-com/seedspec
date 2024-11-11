# Command Line Interface

SeedML CLI focuses on simplicity with smart defaults. Most commands require minimal configuration.

## Quick Start

```bash
# Generate app from spec (uses all smart defaults)
seedml create myapp.seed

# Run the generated app
cd myapp
seedml run
```

## Essential Commands

```bash
seedml create <spec>     # Generate new app from spec
seedml run              # Run the app locally
seedml deploy           # Deploy to production
seedml test             # Run all tests
```

## Configuration

Configuration uses smart defaults - override only when needed:

```bash
# Environment (optional)
export SEEDML_ENV=dev           # dev/staging/prod
export ANTHROPIC_API_KEY=xxx    # For AI features

# Command options (all optional)
seedml create myapp.seed \
  --stack modern      # Use latest tech stack
  --db postgres      # Override default DB
  --port 3000        # Override default port
```

## Generated Stack

The CLI generates a complete, production-ready application with:

- Modern frontend (React + TypeScript)
- API backend (FastAPI)
- Database (PostgreSQL)
- Authentication
- Testing
- Documentation
- Deployment configs

All components use battle-tested patterns and best practices by default.

## Learn More

- [Quick Start Guide](../getting-started/quick-start.md)
- [Configuration Guide](../reference/config.md) 
- [Deployment Guide](../reference/deploy.md)
