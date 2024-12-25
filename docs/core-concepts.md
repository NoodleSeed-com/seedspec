# Architecture & Design

The Seed Specification Language transforms specifications into working applications through a carefully designed pipeline architecture.

## System Architecture

The Seed Specification Language follows a strict layered architecture pattern where each layer has clear responsibilities and boundaries:

### Layer Dependencies
```ascii
┌─────────────────────────────────────────────────────┐
│                Integration Layer                     │
│  • External services, APIs, webhooks                │
│  • Location services, mapping providers             │
│  • Error handling, rate limiting, security          │
├─────────────────────────────────────────────────────┤
│                Presentation Layer                    │
│  • UI components, layouts, navigation               │
│  • User interactions, forms, validation             │
├─────────────────────────────────────────────────────┤
│                 Security Layer                       │
│  • Roles, permissions, access control               │
│  • Authentication, authorization, audit             │
├─────────────────────────────────────────────────────┤
│                  Logic Layer                         │
│  • Business rules, workflows                        │
│  • Computations, validations                        │
├─────────────────────────────────────────────────────┤
│                  Data Layer                         │
│  • Entities, relationships                          │
│  • CRUD operations, queries                         │
├─────────────────────────────────────────────────────┤
│                Foundation Layer                      │
│  • Types, validation rules                          │
│  • Common patterns, base entities                   │
└─────────────────────────────────────────────────────┘
```

The Seed Specification Language enforces these architectural boundaries:

```ascii
┌─────────────────────────────────────────────────────┐
│                Integration Layer                     │
├─────────────────────────────────────────────────────┤
│                Presentation Layer                    │
├─────────────────────────────────────────────────────┤
│                 Security Layer                       │
├─────────────────────────────────────────────────────┤
│                  Logic Layer                         │
├─────────────────────────────────────────────────────┤
│                  Data Layer                         │
├─────────────────────────────────────────────────────┤
│                Foundation Layer                      │
└─────────────────────────────────────────────────────┘
```

Each layer builds upon lower layers:

1. **Foundation Layer**
   - Type system
   - Validation rules
   - Computed fields

2. **Data Layer**
   - Independent entities
   - Dependent entities
   - Relationships

3. **Logic Layer**
   - Business rules
   - Workflows
   - Computations

4. **Security Layer**
   - Permissions
   - Roles
   - Access control

5. **Presentation Layer**
   - Screens
   - Components
   - Layouts

6. **Integration Layer**
   - External services
   - APIs
   - Events

## Core Components

### 1. Parser & Validator

The validation pipeline ensures specifications are correct before generation:

```python
class Validator:
    def validate_syntax(self, spec):
        """Check YAML syntax and structure"""
        # Verify basic YAML format
        # Check required sections
        # Validate section structure
        
    def validate_semantics(self, spec):
        """Verify semantic correctness"""
        # Check entity relationships
        # Validate type usage
        # Verify rule logic
        
    def resolve_references(self, spec):
        """Resolve all references"""
        # Link entity relationships
        # Resolve type references
        # Connect rule dependencies
```

### 2. Generation Engine

The generation engine handles interaction with Claude:

```python
class Generator:
    def prepare_prompt(self, spec):
        """Transform spec into prompt"""
        # Break into logical chunks
        # Add context and instructions
        # Format for Claude
        
    def generate_code(self, prompt):
        """Generate via Claude API"""
        # Send prompt to Claude
        # Handle response streaming
        # Manage rate limits
        # Retry on failures
        
    def process_response(self, response):
        """Process Claude's response"""
        # Parse response format
        # Extract file content
        # Validate output
```

### 3. Output Processor

The output processor handles file system operations:

```python
class OutputProcessor:
    def create_structure(self):
        """Create directory structure"""
        # Make directories
        # Set up config files
        # Initialize git repo
        
    def write_files(self, files):
        """Write files atomically"""
        # Write to temp location
        # Validate content
        # Move to final location
        
    def setup_project(self):
        """Configure project"""
        # Install dependencies
        # Set up tooling
        # Initialize services
```

### 4. Location Services

```python
class LocationServices:
    def geocode(self, address):
        """Convert address to coordinates"""
        # Validate address format
        # Call geocoding service
        # Cache results
        
    def reverse_geocode(self, lat, lng):
        """Convert coordinates to address"""
        # Validate coordinates
        # Call reverse geocoding
        # Format response
        
    def validate_region(self, points):
        """Validate geographic region"""
        # Check boundary validity
        # Compute area
        # Verify constraints
```

## Design Principles

### 1. Separation of Concerns

Each component has clear responsibilities:
- **Parser**: Understanding specifications
- **Generator**: Code generation
- **Output**: File system management

### 2. Reliability

Multiple layers ensure reliable operation:
- Validation before generation
- Atomic file operations
- Error recovery
- Output verification

### 3. Extensibility

The system is designed for extension:
- Custom validators
- Template overrides
- Output adapters
- Plugin system

## Implementation Details

### 1. Validation Pipeline

```python
def validate_specification(spec):
    # 1. Basic syntax
    validate_yaml_syntax(spec)
    
    # 2. Schema validation
    validate_against_schema(spec)
    
    # 3. Semantic checks
    validate_semantics(spec)
    
    # 4. Reference resolution
    resolve_all_references(spec)
```

### 2. Generation Process

```python
def generate_application(spec):
    # 1. Prepare context
    context = prepare_generation_context(spec)
    
    # 2. Generate components
    components = []
    for component in spec.components:
        result = generate_component(component, context)
        components.append(result)
        
    # 3. Post-process
    post_process_components(components)
```

```python
# Maps Component Generation
def generate_maps_components(spec):
    # 1. Analyze location usage
    location_fields = find_location_fields(spec)
    
    # 2. Generate components
    for field in location_fields:
        # Generate picker component
        # Generate view component
        # Generate search component
        
    # 3. Generate services
    generate_location_services()
    generate_geocoding_pipeline()
    
    # 4. Setup integration
    configure_maps_provider()
    setup_caching()
```

### 3. File Management

```python
def manage_output(components):
    # 1. Prepare directories
    setup_directory_structure()
    
    # 2. Write files
    with atomic_writer() as writer:
        for component in components:
            writer.write_component(component)
            
    # 3. Verify output
    verify_written_files()
```

```python
def handle_location_data(location):
    # 1. Validation
    validate_coordinates(location)
    
    # 2. Geocoding
    with geocoding_client() as client:
        result = client.geocode(location)
        
    # 3. Data enhancement
    enhance_location_data(result)
    
    # 4. Storage preparation
    prepare_for_storage(result)
```

## Error Handling

The system uses a comprehensive error handling approach:

1. **Validation Errors**
   - Syntax errors
   - Semantic errors
   - Reference errors

2. **Generation Errors**
   - API failures
   - Context limits
   - Invalid output

3. **Output Errors**
   - File system errors
   - Permission issues
   - Verification failures

## Cross-Compilation Architecture

The Seed Specification Language uses a sophisticated cross-compilation pipeline to transform declarative specifications into implementation-specific code:

### Cross-Compiler Components

```ascii
┌─────────────────────────────────────────────────────┐
│              Specification Parser                    │
│  • YAML/JSON parsing                                │
│  • Schema validation                                │
│  • Intermediate representation                      │
├─────────────────────────────────────────────────────┤
│               Template Engine                        │
│  • Implementation-specific templates                │
│  • Component generation                             │
│  • Layout processing                                │
├─────────────────────────────────────────────────────┤
│               Code Generator                         │
│  • Target platform adaptation                       │
│  • Project structure generation                     │
│  • Dependency management                            │
└─────────────────────────────────────────────────────┘
```

The cross-compiler follows these key principles:

1. **Clean Separation**
   - Parser independent of implementation
   - Template system isolation
   - Generator modularity

2. **Implementation Support**
   - Multiple frontend frameworks (React, Vue, Angular)
   - Backend technology options
   - Database flexibility

3. **Template Organization**
   - Component templates
   - Layout patterns
   - Style definitions
   - Configuration templates

### Cross-Compilation Process

```python
class CrossCompiler:
    def compile(self, spec):
        """Transform spec to implementation"""
        # 1. Parse and validate
        ir = self.parser.parse(spec)
        
        # 2. Load templates
        templates = self.template_engine.load()
        
        # 3. Generate code
        self.generator.generate(ir, templates)
```

## Future Directions

### 1. Near-term Improvements

- **Deterministic Generation**
  - Local generation options
  - Template-based generation
  - Hybrid approaches

- **Enhanced Validation**
  - Deep semantic analysis
  - Cross-reference checking
  - Custom rule validation

### 2. UI Patterns & Components

```yaml
# Standard Screen Types
screen List {
  list: [field1, field2]        # Fields to display
  actions: [create, edit]       # Basic actions
}

screen Form {
  form: [field1, field2]        # Form fields
  actions: [save, cancel]       # Form actions
}

screen Detail {
  content: [field1, field2]     # Content fields
  actions: [edit, delete]       # Item actions
}

screen Dashboard {
  summary: [metric1, metric2]   # Key metrics
  lists: [recent, popular]      # Data lists
}

# Layout Patterns
screen OrderDetail {
  layout: split
  left: [customer, items]
  right: [summary, actions]
}

# Built-in Features
features: {
  search: true        # Search functionality
  sort: true         # Column sorting
  pagination: true   # Page navigation
}
```

### 3. Research Areas

- **Prompt Engineering**
  - Context optimization
  - Output consistency
  - Token efficiency

- **Code Quality**
  - Style consistency
  - Best practice enforcement
  - Security patterns

- **Location Optimization**
  - Smart geocoding caching
  - Efficient region calculations
  - Clustering algorithms
  - Distance matrix optimization

### 3. Tooling

- **Development Tools**
  - IDE integration
  - Live preview
  - Debug tools

- **Deployment**
  - CI/CD integration
  - Container support
  - Cloud deployment

## Contributing

The architecture is designed for contribution in these areas:

1. **Core Components**
   - Validators
   - Generators
   - Processors

2. **Extensions**
   - Templates
   - Plugins
   - Tools

3. **Documentation**
   - Examples
   - Tutorials
   - Reference
# Architecture

SeedML generates scalable architectures through intent-focused patterns that automatically implement proven practices.

## Core Concepts

```yaml
app ScalableApp {
  # Declare architecture needs
  architecture {
    style: microservices    # Application pattern
    scale: auto             # Infrastructure
    regions: [us, eu]       # Distribution
    resilience: high        # Reliability
  }

  # Intent-focused services
  service Orders {
    type: core          # Service classification
    scale: high         # Resource allocation
    storage: dedicated  # Data patterns
  }
}
```

## Key Features

### 1. Application Patterns
```yaml
architecture {
  # Smart architectural choices
  style: microservices
  patterns: [
    cqrs,              # Command/Query
    event_sourcing,    # State management
    api_gateway        # Access control
  ]
}
```

### 2. Scalability
```yaml
scale {
  # Automatic scaling
  compute: auto       # Resources
  storage: replicated # Data
  cache: distributed  # Performance
  
  limits: {
    cpu: 80%         # Thresholds
    memory: 70%      # Monitoring
  }
}
```

### 3. Resilience
```yaml
resilience {
  # Built-in reliability
  failover: automatic    # Recovery
  backup: continuous     # Data protection
  monitoring: complete   # Observability
  
  sla: {
    uptime: 99.9%       # Availability
    latency: 100ms      # Performance
  }
}
```

### 4. Distribution
```yaml
regions {
  # Global deployment
  primary: us-east
  replicas: [eu, asia]
  
  routing: {
    strategy: latency    # Smart routing
    failover: nearest    # Reliability
  }
}
```

## Best Practices

1. **Cloud Native**
   - Container based
   - Auto scaling
   - Service mesh

2. **Reliability First**
   - High availability
   - Disaster recovery
   - Performance monitoring

3. **Future Ready**
   - Modular design
   - Easy scaling
   - Tech flexibility
# Modular App Specifications

The Seed language supports splitting app definitions across multiple files using the `extend` keyword. This enables better organization, team collaboration, and reuse of components.

## Basic Usage

```yaml
# core.seed - Core app definition
app MyApp {
  entity User {
    name: string
    email: email
  }
}

# ui.seed - UI components 
extend MyApp {
  screen Users {
    list: [name, email]
    actions: [create, edit]
  }
}

# rules.seed - Business rules
extend MyApp {
  rules {
    validateEmail: {
      when: email.changed
      validate: email.format
    }
  }
}
```

## Key Benefits

1. **Separation of Concerns**
   - Split specifications by feature
   - Organize by team responsibility 
   - Maintain focus in each file

2. **Team Collaboration**
   - UI team works on screens
   - Backend team handles data model
   - Rules team manages business logic

3. **Reusability**
   - Share common components
   - Create feature libraries
   - Mix and match modules

## File Organization

Recommended file organization:

```
myapp/
  ├── core.seed      # Core app definition
  ├── ui/
  │   ├── admin.seed    # Admin screens
  │   └── public.seed   # Public screens  
  ├── rules/
  │   ├── auth.seed     # Auth rules
  │   └── billing.seed  # Billing rules
  └── api/
      └── external.seed # External APIs
```

## Loading Order

Files are loaded in this order:

1. Core app definition (`app` keyword)
2. Extensions (`extend` keyword) in alphabetical order
3. Feature modules
4. Component libraries
5. Integration modules

## Validation

The system ensures:

1. **Consistency**
   - No conflicting definitions
   - Valid references
   - Complete dependencies

2. **Uniqueness**
   - No duplicate entities
   - Unique component names
   - Distinct rule names

3. **Dependencies**
   - Core app exists
   - Required modules present
   - Valid references

## Best Practices

1. **File Naming**
   - Use descriptive names
   - Group related files
   - Follow consistent patterns

2. **Module Size**
   - Keep files focused
   - Split large modules
   - Group related features

3. **Dependencies**
   - Minimize coupling
   - Clear dependencies
   - Explicit imports
# Core Concepts

SeedML is built on simple but powerful concepts that work together:

## [Modular Apps](modular-apps.md)

Split app definitions across multiple files for better organization and team collaboration. See [Modular Apps](modular-apps.md) for details.

## Key Ideas

```javascript
// Everything in one place
app TodoList {
  // Data model
  entity Task {
    title: string
    done: bool
  }

  // Business rules
  rules {
    complete {
      validate: !done
      then: done = true
    }
  }

  // User interface
  screen Tasks {
    list: [title, done]
    actions: [create, complete]
  }
}
```

## Core Features

1. **Smart Defaults**
   - Production patterns built-in
   - Override only when needed
   - Progressive enhancement

2. **Clear Intent**
   - Express what you want
   - Not how to build it
   - Natural language

3. **Full Stack**
   - One specification
   - Complete application
   - Modern tech stack

## Learn More

1. [Type System](type-system.md)
   - Basic types
   - Validation
   - Relationships

2. [Business Rules](business-rules.md)
   - Simple validation
   - Clear workflows
   - Computed fields

3. [UI Patterns](ui-patterns.md)
   - Standard layouts
   - Common components
   - Best practices

4. [Theming](theming.md)
   - Hierarchical themes
   - Simple overrides
   - Visual consistency
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
