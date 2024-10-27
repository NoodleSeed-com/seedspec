# SeedML

[![Project Status: Initial Development](https://img.shields.io/badge/Project%20Status-Initial%20Development-yellow.svg)]()
[![License](https://img.shields.io/badge/license-Dual%20GPL%2FCommercial-blue.svg)](LICENSE.md)

> 🚧 **Early Development**: SeedML is currently in initial development. Star the repo to follow our progress!

## What is SeedML?

SeedML is a programming language designed to be generated and modified by AI language models. It enables complete application development through a single, AI-friendly format that both humans and machines can easily understand.

## Key Features

- **AI-Native Design**: Optimized for LLM generation and modification
- **Smart Defaults**: Common patterns built-in, override only when needed  
- **Single Source**: One specification describes your entire application
- **Technology Independent**: Target any modern tech stack

### Quick Example

```yaml
# A complete task management system in SeedML
app TaskManager {
  entity Task {
    title: string
    status: todo->doing->done
    assigned: User?
    priority: low/medium/high
    
    rules {
      assign: {
        then: notify@assigned
      }
    }
  }

  screen TaskBoard {
    layout: kanban(status)
    card: [title, assigned.avatar, priority]
    actions: [assign, move, edit]
  }
}
```

This simple specification automatically generates:
- Complete database schema
- API endpoints with validation
- Interactive UI components
- Business logic implementation
- User notifications
- Access control

## Documentation

- [Language Specification](docs/spec.md)
- [Design Principles](docs/principles.md)
- [Examples](docs/examples/)
- [Pattern Recognition](docs/patterns.md)
- [Type System](docs/types.md)
- [Security Guide](docs/security.md)

## Getting Involved

We're looking for collaborators interested in:
- Language design and specification
- Compiler development
- Developer tools and IDE integration
- Documentation and examples

### How to Contribute
We'll be opening up for contributions soon. In the meantime, feel free to:
1. Star the repository to show your interest
2. Watch for updates as we develop the core specification

## Licensing

SeedML will be available under a dual license:

- [GNU General Public License v3.0](LICENSE-GPL.md) for open source use
- Commercial License for commercial use (coming soon)

The core language specification and parser will be open source, while the compiler and enterprise features will require a commercial license.

## Contact

- Email: [info@noodleseed.com](mailto:info@noodleseed.com)
- Website: [https://noodleseed.com](https://noodleseed.com)

## Coming Soon

- Development roadmap
- Contributor guidelines
- Alpha release timeline

---

Built with ❤️ by Noodle Seed

### Quick Example

```yaml
# A complete task management system in SeedML
app TaskManager {
  entity Task {
    title: string
    status: todo->doing->done
    assigned: User?
    priority: low/medium/high
    
    rules {
      assign: {
        then: notify@assigned
      }
    }
  }

  screen TaskBoard {
    layout: kanban(status)
    card: [title, assigned.avatar, priority]
    actions: [assign, move, edit]
  }
}
```

This simple specification automatically generates:
- Complete database schema
- API endpoints with validation
- Interactive UI components
- Business logic implementation
- User notifications
- Access control

## Core Qualities

SeedML is built on eight fundamental qualities that make it uniquely suited for modern application development:

### 1. LLM-Native Design

**What It Means**
- Designed to be generated and modified by AI language models
- Consistent patterns that map to natural language
- Minimal but unambiguous syntax
- Context-preserving structure

**Why It's Important**
```yaml
# LLMs can easily generate this from natural language:
"Create a task system with priorities and assignments"
↓
app TaskSystem {
  entity Task {
    title: string
    priority: low/medium/high
    assigned: User?
  }
}
```

### 2. Single Source of Truth

**What It Means**
- One file describes the entire application
- All aspects (data, UI, logic, integrations) in one place
- No redundant specifications
- No sync issues between layers

**Why It's Important**
```yaml
# Change in one place affects everything:
entity Order {
  status: draft->submitted->approved  # Defines:
  # - Database schema
  # - State management
  # - UI transitions
  # - API endpoints
  # - Validation rules
  # - Audit logging
}
```

### 3. Semantic Over Syntactic

**What It Means**
- Describes what things are, not how they work
- Business concepts map directly to implementation
- Domain-specific patterns built in
- Intent-based configuration

**Why It's Important**
```yaml
# Business concept straight to implementation:
screen Orders {
  type: kanban     # Instead of detailed layout specs
  group: status    # Instead of complex data transformations
  card: [          # Instead of component configuration
    title,
    assigned.avatar,
    due.countdown
  ]
}
```

### 4. Smart Defaults with Explicit Overrides

**What It Means**
- Common patterns are implicit
- Best practices built in
- Override only when needed
- Progressive complexity

**Why It's Important**
```yaml
# Simple by default, complex when needed:
entity User {
  # Simple case - all best practices included
  name: string

  # Complex case - explicit configuration
  email: string {
    format: custom_email
    validate: matches(@company.com)
    unique: per_tenant
  }
}
```

### 5. Technology Independent

**What It Means**
- Describes what, not how
- Compiles to any modern stack
- Framework agnostic
- Future-proof specifications

**Why It's Important**
```yaml
# Same spec, multiple targets:
app CustomerPortal {
  entity Customer { ... }
  screen Dashboard { ... }
}

# Compiles to:
- React/Vue/Angular frontends
- REST/GraphQL APIs
- SQL/NoSQL databases
- Various cloud platforms
```

### 6. Business-Domain Aligned

**What It Means**
- Matches how business stakeholders think
- Natural mapping to requirements
- Clear connection between spec and functionality
- Domain-driven by default

**Why It's Important**
```yaml
# Business requirements map directly to code:
entity Invoice {
  rules {
    approve: {
      require: [
        total <= customer.credit_limit,
        items.all(in_stock)
      ]
      then: [create@payment, notify@account_manager]
    }
  }
}
```

### 7. Full Stack Coherence

**What It Means**
- All layers work together naturally
- Consistent patterns throughout
- Automatic relationship management
- Built-in integrations

**Why It's Important**
```yaml
# Everything works together automatically:
screen ProductCatalog {
  list: Products       # Implies:
  search: [name, tag]  # - API endpoints
  filter: category     # - Database queries
  sort: -price        # - UI components
  cache: 5min         # - Caching logic
}
```

### 8. Implementation Determinism

**What It Means**
- Same spec always produces same result
- No hidden behaviors
- Predictable outputs
- Consistent across environments

**Why It's Important**
```yaml
# Guaranteed consistent implementation:
entity Order {
  status: draft->submitted->approved
  # Always generates:
  # - Same database schema
  # - Same state transitions
  # - Same validation rules
  # - Same audit trails
}
```

These qualities combine to create a language that is:
- Easy for LLMs to generate
- Simple to maintain
- Quick to modify
- Reliable to implement
- Future-proof
- Business-friendly
- Developer-efficient

## Current Status

- [x] Initial language specification
- [x] Basic syntax documentation
- [ ] Parser implementation
- [ ] Basic compiler
- [ ] Development tools
- [ ] Example applications

## Planned Features

- **Complete Application Specification**: Define everything from data models to UI in one place
- **LLM-Native Design**: Optimized for AI generation and modification
- **Technology Agnostic**: Compile to any modern tech stack
- **Production Ready**: Built-in best practices and security patterns
- **Full Stack**: Covers database, backend, frontend, and integrations

## Examples

Here's a progression of examples showing the expressiveness and simplicity of SeedML.

### Basic CRUD Application

```yaml
# Simple customer management system
app CustomerManager {
  entity Customer {
    # Basic information
    name: string
    email: email
    phone: phone?
    status: active/inactive = active
    
    # Validation rules built-in
    validate: email != null if status == active
  }

  # Generates complete admin interface
  screen Customers {
    list: [name, email, status]
    search: [name, email]
    actions: [create, edit, delete]
  }
}
```

### Business Application with Logic

```yaml
# Order management with business rules
app OrderSystem {
  entity Order {
    # Basic fields with types
    customer: Customer
    items: [
      product: Product,
      quantity: int > 0,
      price: money
    ]
    
    # Computed fields
    subtotal: sum(items.price * items.quantity)
    tax: subtotal * 0.2
    total: subtotal + tax
    
    # State management
    status: draft->submitted->approved->shipped->delivered
    
    # Business rules
    rules {
      submit: {
        require: [
          items.length > 0,
          customer.verified,
          total <= customer.creditLimit
        ]
        then: notify@sales
      }
      
      approve: {
        require: role.manager
        check: items.all(inStock)
        then: [create@invoice, notify@warehouse]
      }
    }
  }

  # UI with business-oriented layout
  screen Orders {
    list {
      view: table
      show: [id, customer, total, status]
      group: status
      actions: [
        submit if draft,
        approve if submitted and role.manager
      ]
    }
    
    detail {
      layout: split
      left {
        customer: card
        items: editable-table
      }
      right {
        summary: [subtotal, tax, total]
        status: timeline
        actions: panel
      }
    }
  }
}
```

### Analytics Dashboard

```yaml
# Real-time analytics dashboard
app Analytics {
  # Data models
  entity Metric {
    name: string
    value: number
    timestamp: datetime
    category: string
  }

  # Dashboard screen
  screen Dashboard {
    layout: grid(2x2)
    
    # Multiple chart types
    widgets: [
      {
        type: line-chart
        data: Metric
        x: timestamp
        y: value
        group: category
        range: last-7-days
      },
      {
        type: counter
        data: Metric
        value: sum(value)
        change: vs_previous_period
      },
      {
        type: bar-chart
        data: Metric
        x: category
        y: sum(value)
      },
      {
        type: table
        data: Metric
        columns: [name, value, timestamp]
        sort: -timestamp
        limit: 10
      }
    ]
    
    # Interactive features
    features: [
      time-range-selector,
      category-filter,
      export-data
    ]
  }
}
```

### Full SaaS Application

```yaml
# Complete SaaS project management tool
app ProjectHub {
  # Core entities
  entity Project {
    basics: [name, description, key: slug]
    dates: [start: date, target: date]
    status: planning->active->completed
    team: [lead: User, members: [User]]
    
    # Access control
    access: {
      view: team.members
      edit: team.lead
      admin: role.manager
    }
  }

  entity Task {
    basics: [title, description]
    planning: [estimate: hours, priority: 1-5]
    tracking: [
      status: todo->doing->review->done,
      assigned: User?,
      reporter: User
    ]
    
    # Computed fields
    blocked: depends.any(status != done)
    overdue: due < today and status != done
  }

  # Business logic
  flows {
    TaskAssignment {
      on: Task.assigned_changed
      do: [
        notify@assigned "New task: ${task.title}",
        notify@task.reporter "Task assigned to ${assigned}"
      ]
    }

    ProjectCompletion {
      on: Project.status -> completed
      require: tasks.all(status == done)
      do: [
        notify@team "Project completed!",
        analytics.track("project_completed")
      ]
    }
  }

  # User interface
  screens {
    ProjectDashboard {
      layout: split
      left {
        projects: {
          type: card-grid
          show: [name, status, progress]
          filter: status != completed
          actions: [create, edit]
        }
      }
      right {
        tasks: {
          type: kanban
          group: status
          show: [title, assigned.avatar, due]
          filter: assigned == current_user
        }
      }
    }

    ProjectDetail {
      layout: tabs
      tabs: {
        Overview {
          layout: split
          left: [
            details: card(basics, dates),
            team: avatars(members)
          ]
          right: [
            metrics: [tasks.done, hours.total],
            activity: timeline(events)
          ]
        }
        
        Tasks {
          type: table
          columns: [title, assigned, due, estimate]
          actions: [create, assign, edit]
        }
      }
    }
  }

  # Integrations
  integrate {
    auth0: {
      domain: ${AUTH0_DOMAIN}
      clients: [web, mobile]
    }

    slack: {
      webhook: ${SLACK_WEBHOOK}
      notify: [task.assigned, project.completed]
    }

    s3: {
      bucket: ${S3_BUCKET}
      access: private
    }
  }
}
```

### Pattern Recognition Example

```yaml
# Implicit patterns are automatically recognized and implemented

# State Machine Pattern
entity Order {
  status: draft->submitted->approved
  # Implies:
  # - Enum type creation
  # - State transition validation
  # - UI status indicators
  # - Audit logging
  # - Event triggers
}

# Data Relationship Pattern
entity Customer {
  orders: [Order]
  # Implies:
  # - Foreign key setup
  # - Cascading deletes
  # - API relationship handling
  # - UI data loading
  # - Form relationships
}

# Smart Defaults Pattern
entity Product {
  name: string        # Required, indexed, min length
  email: email        # Unique, validated, indexed
  price: money        # Non-negative, precision(2)
  created: timestamp  # Auto-set, immutable
}
```

### API Integration Example

```yaml
# External API integration
app WeatherDashboard {
  # External API definition
  api OpenWeather {
    base: "https://api.openweathermap.org/data/2.5"
    key: ${WEATHER_API_KEY}
    
    endpoints {
      current: {
        path: "/weather"
        params: [city: string, units: string]
        cache: 30min
      }
      
      forecast: {
        path: "/forecast"
        params: [city: string, days: int]
        cache: 1h
      }
    }
  }

  # Data models
  entity Location {
    city: string
    country: string
    coords: [lat: float, lon: float]
  }

  # UI components
  screen Weather {
    params: [location: Location]
    
    layout: cards
    
    widgets: [
      {
        type: weather-card
        data: OpenWeather.current(location.city)
        show: [temp, humidity, wind]
      },
      {
        type: forecast-chart
        data: OpenWeather.forecast(location.city)
        range: 5d
      }
    ]
  }
}
```

These examples demonstrate:
1. Progressive complexity
2. Business logic integration
3. UI/UX patterns
4. External service integration
5. Data modeling
6. Access control

## Advanced Concepts

SeedML includes sophisticated features for enterprise and complex applications:

### Multi-Tenant Architecture
- Database/schema/row-level tenant isolation
- Tenant-specific customization capabilities
- Cross-tenant sharing patterns
- Automatic tenant scoping

### Domain-Specific Extensions
- Custom type definitions
- Domain-specific patterns
- Specialized validation rules
- Industry-specific vocabularies

### Time-Based Behaviors
- Business calendar support
- Complex scheduling patterns
- Recurring events
- Temporal rules and constraints

### Versioning and Migration
- Schema versioning
- Automated migrations
- Content versioning
- Version-specific behaviors

### Test Specifications
- Test data generation
- Behavioral testing
- Property-based testing
- Automated test scenarios

### Plugin Architecture
- Extensible plugin system
- Multiple plugin types (UI/logic/data)
- Resource isolation
- Lifecycle hooks

### AI Integration
- Content processing
- Decision support
- Automated generation
- AI-enhanced fields

### Internationalization
- Multi-language support
- Regional variations
- Translatable content
- Locale-aware formatting

## Common Business Patterns

SeedML provides built-in support for common business application patterns:

### 1. CRUD Screens
```yaml
screen Customers {
  # Standard list pattern
  list {
    show: [name, email, status]
    actions: [create, edit]
    search: [name, email]
    filter: status
  }

  # Common detail layout
  detail {
    layout: split
    left: info
    right: [activity, actions]
  }
}
```

### 2. Business Workflows
```yaml
entity Expense {
  # Common workflow status
  status: draft->submitted->approved/rejected

  rules {
    submit: {
      require: [amount > 0, description.valid]
      then: notify@manager
    }
    approve: {
      require: role.manager
      then: [notify@submitter, create@payment]
    }
  }
}
```

### 3. Dashboard Layouts
```yaml
screen Dashboard {
  layout: grid(2x2)  # Common 4-panel layout
  
  widgets: [
    {
      type: counter
      title: "New Customers"
      data: Customer.count(this_month)
      compare: last_month
    },
    {
      type: line
      title: "Sales Trend"
      data: Order.total(by: day)
      range: last_30_days
    }
  ]
}
```

### 4. Form Patterns
```yaml
screen OrderForm {
  form {
    sections: {
      customer: [name!, email!, phone?],
      details: [items: table, notes, shipping]
    }

    validate: {
      email: valid_email,
      total: positive
    }

    actions: [save: draft, submit: if valid]
  }
}
```

### 5. Search and Filter
```yaml
screen ProductCatalog {
  search {
    quick: [name, sku]
    filters: {
      category: select,
      price: range,
      status: multiple
    }
    sort: [name, -created, price]
    results: {
      view: grid/table,
      per_page: 20
    }
  }
}
```

### 6. Simple Reports
```yaml
reports {
  SalesSummary: {
    group: [month, category]
    metrics: [
      orders: count,
      revenue: sum,
      average: mean(order_total)
    ]
    format: table
    export: excel
  }
}
```

### 7. Common Integrations
```yaml
integrate {
  email: {
    templates: {
      welcome: "Welcome to {company}",
      order_confirm: "Order #{id} Confirmed"
    }
  }

  storage: {
    documents: [pdf, doc, max: 10mb],
    images: [jpg, png, resize: thumbnail]
  }
}
```

### 8. Access Control
```yaml
app Portal {
  roles: [admin, manager, user]

  access {
    manager: {
      read: all
      write: [orders, products]
      approve: expenses
    }
    
    user: {
      read: [own_orders, products]
      write: own_profile
    }
  }
}
```

These patterns demonstrate how SeedML makes it easy to implement common business functionality with minimal code while following best practices.

## Smart Defaults and Implicit Features

SeedML drastically reduces specification size through intelligent defaults and contextual understanding. Here's how it works:

### 1. Type-Based Implications

```yaml
# Traditional verbose specification
entity Product {
  id: {
    type: uuid,
    primary: true,
    auto_generate: true,
    indexed: true
  }
  name: {
    type: string,
    min_length: 1,
    max_length: 100,
    required: true,
    indexed: true
  }
  email: {
    type: string,
    format: email,
    unique: true,
    required: true,
    indexed: true,
    validate: regex('^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$')
  }
  price: {
    type: decimal,
    precision: 2,
    min: 0,
    required: true,
    validate: value > 0
  }
  created_at: {
    type: timestamp,
    auto_set: true,
    indexed: true,
    update: false
  }
}

# SeedML equivalent (same functionality)
entity Product {
  name: string      # Implies: required, indexed, min(1), max(100)
  email: email      # Implies: unique, required, indexed, format validation
  price: money      # Implies: decimal(2), min(0), required
  created: timestamp  # Implies: auto_set, indexed, immutable
}
```

### 2. Context-Aware UI Patterns

```yaml
# Traditional verbose UI specification
screen Products {
  layout: {
    type: responsive_grid,
    columns: {
      mobile: 1,
      tablet: 2,
      desktop: 4
    },
    spacing: 16,
    padding: 24
  }
  list: {
    type: data_table,
    pagination: {
      enabled: true,
      per_page: 20,
      controls: true
    },
    sorting: {
      enabled: true,
      default_field: "created",
      default_direction: "desc"
    },
    filtering: {
      enabled: true,
      controls: true
    },
    selection: {
      enabled: true,
      type: "multi"
    }
  }
  actions: {
    placement: "top-right",
    primary: {
      create: {
        type: "button",
        variant: "primary",
        icon: "plus",
        label: "Create Product"
      }
    },
    item: {
      edit: {
        type: "button",
        variant: "secondary",
        icon: "edit"
      },
      delete: {
        type: "button",
        variant: "danger",
        icon: "trash",
        confirm: true
      }
    }
  }
}

# SeedML equivalent (same functionality)
screen Products {
  layout: grid      # Implies: responsive, standard spacing, padding
  list: [name, price, status]  # Implies: pagination, sorting, filtering
  actions: [create, edit, delete]  # Implies: proper placement, styling, confirmation
}
```

### 3. Business Logic Patterns

```yaml
# Traditional verbose business rules
entity Order {
  status_transitions: {
    draft: {
      allowed_next: ["submitted"],
      validation: {
        conditions: [
          "items.length > 0",
          "total > 0",
          "customer != null"
        ]
      },
      before_transition: [
        "validateCustomerCredit",
        "checkInventory"
      ],
      after_transition: [
        "notifyCustomer",
        "notifySales",
        "createAuditLog"
      ]
    }
  },
  validations: {
    total: {
      rules: ["positive", "less_than_credit_limit"],
      messages: {
        positive: "Total must be positive",
        less_than_credit_limit: "Exceeds credit limit"
      }
    }
  }
}

# SeedML equivalent (same functionality)
entity Order {
  status: draft->submitted->approved  # Implies: state machine, validation, audit
  total: money  # Implies: positive, credit limit check
  
  rules {
    submit: {
      require: items.length > 0
      then: notify@customer
    }
  }
}
```

### 4. Smart Integration Patterns

```yaml
# Traditional verbose integration
integrations: {
  stripe: {
    type: "payment_processor",
    config: {
      api_key: "${STRIPE_KEY}",
      webhook_secret: "${STRIPE_WEBHOOK}",
      success_url: "/payment/success",
      cancel_url: "/payment/cancel"
    },
    events: {
      payment_success: {
        handler: "handlePaymentSuccess",
        actions: [
          "updateOrderStatus",
          "sendConfirmationEmail",
          "createInvoice"
        ]
      },
      payment_failure: {
        handler: "handlePaymentFailure",
        actions: [
          "markOrderFailed",
          "notifyCustomer",
          "logError"
        ]
      }
    }
  }
}

# SeedML equivalent (same functionality)
integrate {
  stripe: {
    on: order.submit  # Implies: standard payment flow, success/failure handling
    charge: total     # Implies: amount formatting, currency handling
    then: approve     # Implies: status update, notifications, logging
  }
}
```

### 5. Security and Access Control

```yaml
# Traditional verbose permissions
security: {
  roles: {
    admin: {
      permissions: ["*"],
      resource_access: "all"
    },
    manager: {
      permissions: [
        "read:*",
        "write:orders",
        "write:products",
        "delete:own"
      ],
      resource_access: "department"
    },
    user: {
      permissions: [
        "read:own",
        "write:own"
      ],
      resource_access: "own"
    }
  },
  resource_policies: {
    orders: {
      read: "hasRole('admin') || isOwner() || inDepartment()",
      write: "hasRole('admin') || hasRole('manager')",
      delete: "hasRole('admin')"
    }
  }
}

# SeedML equivalent (same functionality)
app Store {
  roles: [admin, manager, user]  # Implies: standard role hierarchy
  
  entity Order {
    access: {
      view: team        # Implies: role-based + ownership checks
      edit: role.manager
      delete: role.admin
    }
  }
}
```

### Key Principles of Implicit Features

#### Convention Over Configuration
- Common patterns are assumed
- Override only when needed
- Standard best practices built-in

#### Context-Aware Defaults
- Type implies validation
- UI patterns imply layout
- Actions imply permissions

#### Semantic Understanding
- Business concepts map to implementations
- Common patterns are recognized
- Standard flows are automated

#### Progressive Disclosure
- Start simple
- Add complexity only when needed
- Override defaults explicitly

This approach allows SeedML to:
- Reduce specification size by 70-90%
- Maintain full functionality
- Ensure consistency
- Reduce errors
- Speed up development

## Language Structure

### Basic Syntax

```yaml
app [AppName] {
  # 1. Global Configuration
  meta: { ... }
  
  # 2. Data Models
  entity [EntityName] { ... }
  
  # 3. Business Rules
  rules { ... }
  
  # 4. User Interface
  screens { ... }
  
  # 5. Integrations
  integrate { ... }
}
```

### Core Types

```yaml
# Primitive Types
string              # Text values
number              # Numeric values
bool                # Boolean values
date                # Date values
time                # Time values
datetime            # Date and time
money               # Monetary values
email               # Email addresses
phone               # Phone numbers
url                 # URLs

# Complex Types
[Type]              # Lists
Type?               # Optional values
Type!               # Required values
map<Key, Value>     # Key-value pairs
enum(v1,v2,v3)      # Enumerations

# Special Types
id                  # Unique identifiers
timestamp           # Timestamps with timezone
file                # File references
image               # Image references
geo                 # Geographical coordinates
```

## Documentation

- [Language Specification](docs/spec.md)
- [Design Principles](docs/principles.md)
- [Examples](docs/examples/)
- [Pattern Recognition](docs/patterns.md)
- [Type System](docs/types.md)
- [Security Guide](docs/security.md)

## Licensing

SeedML will be available under a dual license:

- [GNU General Public License v3.0](LICENSE-GPL.md) for open source use
- Commercial License for commercial use (coming soon)

The core language specification and parser will be open source, while the compiler and enterprise features will require a commercial license.

## Getting Involved

We're looking for collaborators interested in:
- Language design and specification
- Compiler development
- Developer tools and IDE integration
- Documentation and examples

### How to Contribute
We'll be opening up for contributions soon. In the meantime, feel free to:
1. Star the repository to show your interest
2. Watch for updates as we develop the core specification

## Contact

- Email: [info@noodleseed.com](mailto:info@noodleseed.com)
- Website: [https://noodleseed.com](https://noodleseed.com)

## Coming Soon

- Development roadmap
- Contributor guidelines
- Alpha release timeline

---

Built with ❤️ by Noodle Seed
