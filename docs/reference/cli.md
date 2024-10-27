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

## Configuration

The CLI can be configured through:
- Command line flags
- Environment variables
- seedml.config.js file

Example configuration:
```js
// seedml.config.js
module.exports = {
  outDir: './dist',
  target: 'node-16',
  features: ['auth', 'api'],
  env: {
    development: {
      port: 3000
    },
    production: {
      port: 8080
    }
  }
}
```

## Environment Variables

```bash
# Core settings
SEEDML_ENV=development
SEEDML_CONFIG=./config.js
SEEDML_OUTPUT=./dist

# Feature flags
SEEDML_FEATURES=auth,api,storage

# Development
SEEDML_PORT=3000
SEEDML_HOST=localhost
SEEDML_WATCH=true
```

## Best Practices

1. **Project Structure**
   - Use consistent naming
   - Organize by feature
   - Keep configurations clean

2. **Development Workflow**
   - Use watch mode
   - Run tests frequently
   - Validate before deploying

3. **Deployment**
   - Use environment configs
   - Version control configs
   - Monitor deployments

4. **Maintenance**
   - Regular updates
   - Clean generated files
   - Backup configurations
