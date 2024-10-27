# Command Line Interface

SeedML provides a CLI tool for generating applications from specifications.

## Installation

```bash
# Install from source
git clone https://github.com/seedml/seedml.git
cd seedml
pip install -e .

# Set your API key
export ANTHROPIC_API_KEY='your-api-key'
```

## Basic Usage

```bash
# Generate application from spec
seedml myapp.seed

# Show help
seedml --help

# Show version
seedml --version
```

## Options

```bash
--api-key KEY      Anthropic API key (or use ANTHROPIC_API_KEY env var)
--output DIR       Output directory (default: ./generated)
--verbose         Show detailed output
```

Note: This is an alpha release with basic functionality. More features coming soon.
