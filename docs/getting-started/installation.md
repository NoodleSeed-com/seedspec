# Installing SeedML

## Prerequisites

Before installing SeedML, ensure you have:
- Python 3.8 or higher
- pip package manager
- Anthropic API key (for Claude access)

## Installation

### 1. From Source (Current Method)

```bash
# Clone the repository
git clone https://github.com/seedml/seedml.git
cd seedml

# Install dependencies
pip install anthropic

# Install SeedML in development mode
pip install -e .
```

### 2. Verify Installation

```bash
# Set your Anthropic API key
export ANTHROPIC_API_KEY='your-api-key'

# Test the CLI
seedml --help
```

## Next Steps

- Follow the [Quick Start Guide](quick-start.md)
- Try the [First Application Tutorial](first-app.md)
- Read about [Core Concepts](../core-concepts/overview.md)
