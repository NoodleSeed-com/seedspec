# Command Line Interface

SeedML provides a CLI tool for generating layered full-stack applications from specifications.

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

## Generated Stack

The CLI generates a complete application with:
- React + TypeScript frontend
- FastAPI backend 
- MySQL database
- Full testing suite
- API documentation

## Features

- Layered architecture generation
  - Foundation layer (types, validation)
  - Data layer (entities, relationships) 
  - Logic layer (rules, workflows)
  - Security layer (permissions, roles)
  - Presentation layer (UI, components)
  - Integration layer (external services)

- Production-ready code generation
  - Consistent patterns per layer
  - Cross-layer validation
  - Layer-specific best practices
  - Modern tech stack
  - Complete testing per layer

Note: This is an alpha release with basic functionality. More features coming soon.
