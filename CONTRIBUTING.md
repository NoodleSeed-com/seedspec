# Contributing to SeedSpec

Thank you for your interest in contributing to SeedSpec! This document provides guidelines and information for contributors.

## Getting Started

1. Fork the repository
2. Clone your fork
3. Create a new branch for your work
4. Make your changes
5. Submit a pull request

## Development Setup

```bash
# Install from source
git clone https://github.com/seedml/seedml.git
cd seedml
pip install -e .

# Set your API key
export ANTHROPIC_API_KEY='your-api-key'

# Build documentation
mkdocs build
```

## CLI Development

The SeedSpec CLI tool generates applications from specifications:

```bash
# Generate application from spec
seedml myapp.seed

# Show help
seedml --help

# Show version
seedml --version
```

Options:
```bash
--api-key KEY      Anthropic API key (or use ANTHROPIC_API_KEY env var)
--output DIR       Output directory (default: ./generated)
--verbose         Show detailed output
```

## Contribution Areas

We welcome contributions in these areas:

1. Language Design
   - Syntax improvements
   - New features
   - Pattern recognition

2. Compiler Development
   - Parser improvements
   - Code generation
   - Optimization

3. Documentation
   - Examples
   - Tutorials
   - API documentation

4. Tools
   - IDE plugins
   - Development tools

## Code Style

- Follow existing patterns
- Document your changes
- Keep commits focused

## Pull Request Process

1. Update documentation
2. Update CHANGELOG.md
3. Submit PR with clear description

## Questions?

- Open an issue for bugs
- Discussions for features
- Discord for community chat

## License

By contributing, you agree to license your work under our project's license terms.
