# Smart Defaults

SeedML reduces boilerplate through intelligent defaults while maintaining flexibility for custom configurations.

## Core Principles

### 1. Convention Over Configuration

SeedML follows established patterns and best practices by default:

```yaml
entity User {
  name: string      # Implies: required, indexed
  email: email      # Implies: unique, validated
  created: timestamp  # Implies: auto-set, immutable
}
```

### 2. Progressive Complexity

Start simple and add complexity only when needed:

```yaml
# Simple case - uses all defaults
entity Product {
  name: string
  price: money
}

# Complex case - custom configuration
entity Product {
  name: string {
    min: 3
    max: 100
    format: title_case
  }
  price: money {
    min: 0
    precision: 2
    currency: USD
  }
}
```

### 3. Contextual Awareness

Defaults change based on context:

```yaml
entity Order {
  status: draft->submitted->approved
  # Implies:
  # - State machine behavior
  # - Status validation
  # - Transition hooks
  # - Audit logging
  # - UI status indicators
}
```

## Common Default Patterns

### 1. Type-Based Defaults

Each type comes with sensible defaults:

- `string`: Required, trimmed, max length
- `email`: Unique, validated format
- `money`: Non-negative, precision(2)
- `date`: Valid range, proper formatting
- `phone`: Format validation, optional
- `location`: Validated coordinates, geocoding, map display
- `region`: Boundary validation, area calculation
- `distance`: Unit conversion, formatting

```yaml
# Location type implications
location: {
  validation: coordinates
  geocoding: automatic
  reverse: on_save
  format: address
}

region: {
  validation: boundary
  calculation: area
  contains: points
}

distance: {
  conversion: automatic
  display: localized
}
```

### 2. UI Patterns

Standard UI components with smart defaults:

```yaml
screen Products {
  list: [name, price]  # Implies:
  # - Pagination
  # - Sorting
  # - Search
  # - Responsive layout
}

# Map components with smart defaults
screen Locations {
  map: [location] # Implies:
  # - Marker clustering
  # - Bounds fitting
  # - Zoom controls
  # - Mobile gestures
  # - Location search
  # - Responsive layout
}

# Progressive map enhancement
map: {
  basic: location        # Single marker
  multiple: [location]   # Clustered markers
  interactive: selector  # Location picker
  advanced: {           # Full features
    cluster: true
    search: radius
    draw: regions
  }
}
```

### 3. Business Logic

Common business patterns are built-in:

```yaml
entity Invoice {
  status: draft->submitted->approved
  # Implies:
  # - State transitions
  # - Validation rules
  # - Notifications
  # - Audit trails
}

entity Store {
  location: location
  # Implies:
  # - Distance calculations
  # - Geocoding pipeline
  # - Region validation
  # - Location indexing
  # - Search optimization
}

# Location-aware rules
rules {
  within_region: true    # Region containment
  distance_calc: auto    # Distance computation
  geo_index: enabled     # Spatial indexing
}
```

### 4. Security

Security best practices by default:

```yaml
entity Document {
  access: role.manager
  # Implies:
  # - Role-based access control
  # - Permission checking
  # - Audit logging
  # - Data filtering
}

location_data {
  access: restricted
  # Implies:
  # - Coordinate precision control
  # - Address masking
  # - Usage tracking
  # - API key management
}
```

## Overriding Defaults

When defaults don't fit, explicit configuration takes precedence:

```yaml
entity CustomProduct {
  # Override string defaults
  name: string {
    required: false
    max: 500
    format: custom_regex("[A-Z].*")
  }
  
  # Override money defaults
  price: money {
    min: -1000  # Allow negative
    precision: 4  # 4 decimal places
  }
  
  # Override timestamp defaults
  created: timestamp {
    auto: false
    mutable: true
  }
}
```

## Benefits

1. Faster Development
   - Less boilerplate code
   - Fewer decisions needed
   - Quick prototyping

2. Consistency
   - Standard patterns
   - Best practices built-in
   - Uniform behavior

3. Maintainability
   - Clear override points
   - Documented defaults
   - Centralized configuration

4. Security
   - Secure by default
   - Best practices enforced
   - Explicit overrides needed
