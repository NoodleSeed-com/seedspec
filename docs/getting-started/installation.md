# Installing Seed Spec

## Prerequisites

Before installing Seed Spec, ensure you have:
- Python 3.8 or higher
- pip package manager
- Anthropic API key (for Claude access)
- Node.js 16+ (for frontend implementations)
- Docker (optional, for containerized builds)

## Installation

```bash
# Install from source
git clone https://github.com/fahd-noodleseed/seed-spec.git
cd seed-spec
pip install -e .
```

## Configuration

Set your Anthropic API key:
```bash
export ANTHROPIC_API_KEY='your-api-key'
```

## Verify Installation

```bash
# Should show available commands
seedspec --help

# Should show version number
seedspec --version
```

## Current Status

Seed Spec is in early development (v0.1.0). Current features:
- Basic application generation from .seed files
- Cross-compilation to multiple implementations:
  - React + FastAPI stack
  - Vue + Express stack
  - Angular + NestJS stack
- Simple CRUD operations
- Template customization support

Many planned features are still in development.

## Next Steps

- Follow the [Quick Start Guide](quick-start.md)
- Try the [First Application Tutorial](first-app.md)
- Read about [Core Concepts](../core-concepts/overview.md)
