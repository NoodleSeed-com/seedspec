# Command Line Interface

SeedML CLI focuses on simplicity with smart defaults. Most commands require minimal configuration.

## Quick Start

```bash
// Generate app from spec (uses all smart defaults)
seedml create myapp.seed

// Run the generated app
cd myapp
seedml run
```

## Essential Commands

```bash
seedml create <spec>     # Generate new app from spec(s)
seedml extend <app>      # Add components to existing app
seedml run              # Run the app locally
seedml deploy           # Deploy to production
seedml test             # Run all tests
```

## Location Commands

```bash
seedml geocode <file>    # Batch geocode addresses
seedml regions verify    # Verify region definitions
seedml maps cache clear  # Clear geocoding cache
seedml maps config test  # Test maps configuration
```

## Maps Configuration

Configure maps features through command line options or environment variables:

```bash
// Provider Selection
--maps-provider google|mapbox|osm  // Select maps provider
--maps-version latest|legacy       // API version

// Geocoding Options
--geocoding-cache true|false       // Enable caching
--geocoding-precision high|normal  // Coordinate precision
--geocoding-regions [codes]        // Restrict to regions

// Performance
--maps-clustering auto|manual      // Clustering strategy
--maps-cache-size 100MB           // Cache size limit
--maps-rate-limit 100/min         // API rate limit
```

## Configuration

Configuration uses smart defaults - override only when needed:

```bash
// Environment (optional)
export SEEDML_ENV=dev              // dev/staging/prod
export ANTHROPIC_API_KEY=xxx       // For AI features
export GOOGLE_MAPS_KEY=xxx         // For maps features
export MAPS_CACHE_DIR=./cache      // For geocoding cache

// Command options (all optional)
seedml create myapp.seed \
  --stack modern                   // Use latest tech stack
  --db postgres                    // Override default DB
  --port 3000                      // Override default port
  --maps-provider google           // Maps provider
  --geocoding-strategy cached      // Geocoding approach
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
- Maps components and services
- Geocoding pipeline
- Location caching system

All components use battle-tested patterns and best practices by default.

## Learn More

- [Quick Start Guide](../getting-started/quick-start.md)
- [Configuration Guide](../reference/config.md) 
- [Deployment Guide](../reference/deploy.md)
