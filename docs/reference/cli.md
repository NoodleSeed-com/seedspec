# Command Line Interface

SeedML provides a powerful CLI for managing projects and generating applications.

## Installation

```bash
# Install globally
npm install -g seedml-cli

# Or locally in a project
npm install --save-dev seedml-cli
```

## Basic Commands

### Project Management
```bash
# Create new project
seedml new my-app

# Initialize in existing directory
seedml init

# Add component to project
seedml add entity User
seedml add screen Dashboard
```

### Development
```bash
# Start development server
seedml dev

# Watch for changes
seedml watch

# Run type checking
seedml check
```

### Code Generation
```bash
# Generate full application
seedml generate

# Generate specific components
seedml generate entity User
seedml generate screen Dashboard

# Clean generated files
seedml clean
```

### Testing
```bash
# Run all tests
seedml test

# Run specific tests
seedml test entities
seedml test screens

# Test coverage
seedml test --coverage
```

### Deployment
```bash
# Build for production
seedml build

# Deploy to environment
seedml deploy staging
seedml deploy production

# Show deployment status
seedml status
```

### Development Tools
```bash
# Start interactive console
seedml console

# Analyze project
seedml analyze

# Format code
seedml format

# Validate configuration
seedml validate
```

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
