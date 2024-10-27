# Installing SeedML

## Prerequisites

Before installing SeedML, ensure you have:
- Python 3.8 or higher
- pip package manager
- Anthropic API key (for Claude access)

## Installation

```bash
# Install from source
git clone https://github.com/seedml/seedml.git
cd seedml
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
seedml --help

# Should show version number
seedml --version
```

## Current Status

SeedML is in early development (v0.1.0). Current features:
- Basic application generation from .seed files
- React + FastAPI stack generation
- Simple CRUD operations

Many planned features are still in development.

## Next Steps

- Follow the [Quick Start Guide](quick-start.md)
- Try the [First Application Tutorial](first-app.md)
- Read about [Core Concepts](../core-concepts/overview.md)
