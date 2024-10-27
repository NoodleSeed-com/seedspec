# Advanced SeedML Patterns

This guide covers advanced patterns and techniques for building sophisticated applications with SeedML.

## Multi-Tenant Architecture

```yaml
app MultiTenantSaaS {
  # Tenant configuration
  tenant {
    isolation: schema  # or: database, row
    routing: subdomain
    customization: {
      branding: true
      fields: true
    }
  }

  # Tenant-aware entity
  entity Document {
    tenant: Tenant
    name: string
    content: text
    
    access: tenant.users
  }
}
```

## Complex Workflows

```yaml
app ApprovalSystem {
  # State machine with parallel tracks
  entity Request {
    status: {
      main: draft->submitted->approved,
      finance: pending->reviewed->cleared,
      legal: waiting->checked->signed
    }
    
    rules {
      approve: {
        require: [
          finance.cleared,
          legal.signed,
          role.manager
        ]
      }
    }
  }
}
```

## Plugin Architecture

```yaml
app PluggableSystem {
  # Plugin system
  plugins {
    types: [ui, logic, data]
    isolation: process
    permissions: restricted
  }

  # Plugin hooks
  hooks {
    beforeCreate: [validate, enrich]
    afterUpdate: [notify, sync]
    onError: [log, retry]
  }
}
```

## Event Sourcing

```yaml
app EventSourced {
  # Event definitions
  events {
    OrderCreated: {
      order_id: id
      items: [Product]
      total: money
    }
    
    OrderShipped: {
      order_id: id
      tracking: string
      carrier: enum
    }
  }

  # Event handlers
  handlers {
    OrderCreated: [
      createInvoice,
      notifyCustomer,
      updateInventory
    ]
  }
}
```

## AI Integration

```yaml
app AIEnhanced {
  # AI field types
  entity Content {
    text: ai.text {
      analyze: sentiment
      extract: [topics, entities]
      suggest: tags
    }
    
    image: ai.image {
      detect: [objects, faces, text]
      moderate: inappropriate
      enhance: quality
    }
  }

  # AI-powered rules
  rules {
    categorize: {
      using: ai.classifier
      model: content-type
      threshold: 0.8
    }
  }
}
```

## Time-Based Patterns

```yaml
app TimeAware {
  # Scheduling
  schedule {
    daily: [
      cleanupTemp,
      updateStats
    ]
    weekly: generateReport
    custom: "0 9 * * 1-5"  # Cron
  }

  # Temporal rules
  entity Contract {
    valid: daterange
    
    rules {
      approve: {
        require: within@businessHours
        deadline: 2@businessDays
      }
    }
  }
}
```

## Best Practices

1. **Plugin Design**
   - Use clear interfaces
   - Implement security boundaries
   - Handle failures gracefully
   - Version plugin APIs

2. **Event Sourcing**
   - Keep events immutable
   - Use meaningful event names
   - Include all relevant data
   - Handle idempotency

3. **AI Integration**
   - Set confidence thresholds
   - Handle AI failures
   - Respect privacy concerns
   - Monitor AI performance

4. **Time Management**
   - Consider timezones
   - Handle business calendars
   - Plan for failures
   - Monitor long-running tasks
