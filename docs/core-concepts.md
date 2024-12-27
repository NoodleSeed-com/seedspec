# Core Concepts

The Seed Specification Language is built on simple but powerful concepts that work together to enable rapid prototyping of web applications.

## Type System

SeedSpec uses a type-safe system to ensure data integrity:

```seed
types {
  // Core data types
  text: {
    min: number
    max: number
    pattern?: regex
  }
  
  num: {
    min?: number
    max?: number
    integer?: boolean
  }

  bool: {}
}
```

## Components

Components are defined with the `component` keyword:

```seed
component Button {
    input {
        label: text
    }
}
```

## Models

Models define the data structure of your application:

```seed
model Users "Users" {
  name text = "New User"
  email text = ""
  role text = "member"
}

model Tasks "Tasks" {
  title text = "New Task"
  done bool = false
  priority num = 3
}
```

## Screens

Screens define the user interface of your application:

```seed
screen TaskList "Task List" {
  use task_card
  data tasks
}

screen UserList "User List" {
  use user_card
  data users
}
```

## Key Features

1. **Optimized for Generation with LLMs**
   - Minimal token usage
   - Clear intent expression
   - Deterministic output

2. **Declarative and Cross-Compilable**
   - Define what, not how
   - Target multiple platforms
   - Consistent output

3. **Easy to Read and Understand**
   - Clean syntax
   - Explicit imports
   - Clear structure

4. **Modular Design**
   - Explicit imports
   - Component reuse
   - Clean organization
# Security

Seed Spec provides comprehensive security features built into the language.

## Core Security Features

### 1. Authentication

```javascript
app SecureApp {
  // Authentication configuration
  auth {
    // Providers
    providers: [
      google {
        clientId: env.GOOGLE_CLIENT_ID
        scopes: [profile, email]
      },
      github {
        clientId: env.GITHUB_CLIENT_ID
        scopes: [user]
      }
    ]
    
    // Session management
    session {
      duration: 24h
      renewal: true
      singleDevice: false
    }
    
    // Two-factor auth
    twoFactor {
      required: true
      methods: [app, sms]
    }
  }
}
```

### 2. Authorization

```javascript
roles {
  // Role definitions
  admin {
    permissions: [all]
  }
  
  manager {
    permissions: [
      users.view,
      users.edit,
      orders.manage
    ]
  }
  
  user {
    permissions: [
      profile.edit,
      orders.create
    ]
  }
}
```

### 3. Data Protection

```javascript
protect {
  // Encryption
  encrypt {
    fields: [ssn, creditCard]
    algorithm: aes-256-gcm
  }
  
  // Data masking
  mask {
    fields: [email, phone]
    pattern: "***-***-**{last4}"
  }
  
  // Access control
  access {
    rules: [
      "user.id = record.userId",
      "user.role = 'admin'"
    ]
  }
}
```

### 4. Audit Logging

```javascript
audit {
  // What to log
  track {
    changes: [create, update, delete]
    access: [view, export]
    auth: [login, logout, failed]
  }
  
  // Log details
  details {
    user: true
    timestamp: true
    location: true
    changes: diff
  }
  
  // Retention
  retain {
    duration: 1y
    backup: true
  }
}
```

## Security Patterns

### 1. Data-Level Security

```javascript
entity Order {
  // Fields
  id: uuid
  total: money
  status: pending/paid/shipped
  
  // Security rules
  security {
    view: ["user.id = userId", "user.role = 'admin'"]
    edit: ["user.role in ['admin', 'manager']"]
    delete: ["user.role = 'admin'"]
  }
  
  // Field-level security
  fields {
    creditCard {
      view: ["user.role = 'admin'"]
      encrypt: true
    }
    
    notes {
      edit: ["user.id = assignedTo"]
    }
  }
}
```

### 2. User Management

```javascript
entity User {
  // Core fields
  id: uuid
  email: email
  password: password
  role: admin/manager/user
  
  // Security features
  security {
    password {
      minLength: 12
      require: [number, special, mixed]
      expire: 90d
    }
    
    lockout {
      attempts: 5
      duration: 15m
    }
    
    mfa {
      required: true
      methods: [app, sms]
    }
  }
}
```

### 3. Location Privacy

```javascript
entity UserLocation {
  // Location data
  location: location
  timestamp: datetime
  accuracy: float
  
  // Privacy rules
  privacy {
    // Precision control
    precision: city
    
    // Access rules
    access {
      exact: ["user.role = 'admin'"]
      approximate: ["user.role = 'manager'"]
    }
    
    // Retention
    retain {
      duration: 30d
      anonymize: true
    }
  }
}
```
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
# Integration

Seed Spec provides powerful integration capabilities to connect with external services and systems.

## Core Integration Patterns

### 1. Smart Authentication

```javascript
app MyApp {
  // OAuth-based authentication
  auth {
    provider: google
    scopes: [profile, email]
    roles: [user, admin]
  }
}
```

### 2. Data Integration

```javascript
storage {
  // File storage
  files {
    provider: s3
    bucket: uploads
    types: [image, pdf]
  }
  
  // Database
  database {
    provider: postgres
    replicas: 2
    backup: daily
  }
}
```

### 3. Service Communication

```javascript
services {
  // REST APIs
  api {
    stripe {
      type: rest
      base: "https://api.stripe.com/v1"
      auth: bearer
    }
    
    weather {
      type: rest
      base: "https://api.weather.com"
      auth: apikey
    }
  }
  
  // Message queues
  queue {
    orders {
      type: sqs
      fifo: true
    }
    
    notifications {
      type: rabbitmq
      durable: true
    }
  }
}
```

### 4. Location Services

```javascript
location {
  // Geocoding
  geocoding {
    provider: google
    cache: true
  }
  
  // Routing
  routing {
    provider: mapbox
    mode: [driving, walking]
  }
}
```

### 5. Event Handling

```javascript
events {
  // Webhooks
  webhooks {
    stripe {
      endpoint: "/webhooks/stripe"
      events: [payment.success, refund]
    }
  }
  
  // Real-time
  realtime {
    provider: pusher
    channels: [orders, chat]
  }
}
```

### 6. Maps Integration

```javascript
maps {
  // Map provider
  provider: mapbox
  
  // Features
  features {
    search: true
    routing: true
    clustering: true
  }
  
  // Styling
  style: streets-v11
  controls: [zoom, fullscreen]
}
```

## Best Practices

### 1. Role-Based Access

```javascript
// Location-based Integration
integrate {
  // Map provider configuration
  maps {
    provider: google
    apiKey: env.GOOGLE_MAPS_KEY
  }
  
  // Location services
  location {
    // Geocoding service
    geocoding {
      provider: google
      cache: true
      rateLimit: 100
    }
    
    // Distance calculations
    distance {
      provider: google
      mode: [driving, walking]
      units: metric
    }
  }
  
  // Access control
  access {
    // Role-based rules
    rules {
      admin: [all]
      manager: [view, edit]
      user: [view]
    }
    
    // Location-based rules
    location {
      required: true
      maxDistance: 100
      unit: kilometers
    }
  }
}
```
# Business Rules

The Seed Specification Language provides a simplified approach to business rules focused on common use cases and rapid prototyping.

## Core Concepts

### 1. Basic Validation
```javascript
entity User {
  email: email
  password: string
  
  rules {
    validate {
      email: required,
      password: length >= 8
    }
  }
}
```

### 2. Simple State Transitions
```javascript
entity Task {
  status: string = "todo"
  
  rules {
    start {
      validate: status == "todo"
      then: updateStatus("in-progress")
    }
    
    complete {
      validate: status == "in-progress"
      then: updateStatus("done")
    }
  }
}
```

### 3. Basic Computations
```javascript
entity Invoice {
  items: [InvoiceItem]
  
  rules {
    calculate {
      then: [
        updateSubtotal(sum(items.amount)),
        updateTotal(subtotal + tax)
      ]
    }
  }
}
```

## Common Patterns

### 1. Field Validation
```javascript
entity Product {
  rules {
    validate {
      name: required,
      price: positive,
      stock: minimum(0)
    }
  }
}
```

### 2. Cross-field Validation
```javascript
entity Booking {
  rules {
    validate {
      endDate: after(startDate),
      capacity: lessThan(maxCapacity)
    }
  }
}
```

### 3. Simple Workflows
```javascript
entity Leave {
  status: string = "requested"
  
  rules {
    approve {
      validate: status == "requested"
      then: [
        updateStatus("approved"),
        notifyEmployee
      ]
    }
    
    reject {
      validate: status == "requested"
      then: [
        updateStatus("rejected"),
        notifyEmployee
      ]
    }
  }
}
```

## Best Practices

### 1. Keep Validations Simple
```javascript
// DO - Use simple validations
entity Order {
  rules {
    submit {
      validate: [
        items.length > 0,
        total > 0
      ]
    }
  }
}
```

### 2. Use Clear State Transitions
```javascript
// DO - Simple state changes
entity Task {
  rules {
    complete {
      validate: status == "active"
      then: updateStatus("completed")
    }
  }
}
```

### 3. Minimize Complexity
- Focus on common use cases
- Avoid complex validation chains
- Keep workflows linear
- Use simple state machines

### 4. Prefer Convention
- Use standard validation patterns
- Follow common state transitions
- Apply consistent naming
- Leverage built-in behaviors

## Key Benefits

1. **Rapid Development**
   - Quick to implement
   - Easy to understand
   - Fast to modify

2. **Reduced Errors**
   - Simple validation
   - Clear state flow
   - Standard patterns

3. **Better Maintenance**
   - Less complexity
   - Standard approaches
