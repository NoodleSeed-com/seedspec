# Application Patterns

SeedML provides built-in patterns organized by architectural layer.

## 1. Foundation Patterns

```yaml
# Type patterns
types {
  Email: string { format: email }
  Money: number { precision: 2 }
  Status: enum(active, inactive)
}

# Validation patterns
validate {
  required: field != null
  format: matches(pattern)
  range: between(min, max)
}
```

## 2. Data Patterns

```yaml
# Entity patterns
entity Base {
  id: uuid
  created: timestamp
  updated: timestamp
}

# Relationship patterns
relationships {
  one_to_many: [parent->children]
  many_to_many: [products<->categories]
}
```

## 3. Logic Patterns

```yaml
# Business rule patterns
rules {
  validation: require(condition)
  workflow: state->next_state
  computation: derived = formula
}
```

## 4. Security Patterns

```yaml
# Permission patterns
permissions {
  entity_level: {
    entity: Type
    actions: [create, read, update]
  }
}

# Role patterns
roles {
  hierarchical: [admin->manager->user]
  functional: [billing, support, sales]
}
```

## 5. Presentation Patterns

```yaml
# UI patterns
screens {
  layouts: [list, detail, dashboard]
  components: [table, form, chart]
  navigation: [menu, tabs, breadcrumbs]
}
```

## 6. Integration Patterns

```yaml
# External service patterns
integrate {
  apis: [rest, graphql]
  events: [webhook, queue]
  sync: [batch, realtime]
}
```

## CRUD Operations

```yaml
# Basic CRUD pattern
entity Product {
  name: string
  price: money
  status: active/inactive = active
}

screen Products {
  list: [name, price, status]
  search: [name, status]
  actions: [create, edit, delete]
}
```

## Workflow Management

```yaml
# State machine workflow
entity Order {
  status: draft->submitted->approved->shipped
  
  rules {
    submit: {
      require: [items.valid, total > 0]
      then: notify@manager
    }
    approve: {
      require: role.manager
      then: [create@invoice, notify@customer]
    }
  }
}
```

## Dashboard Layouts

```yaml
screen Dashboard {
  layout: grid(2x2)
  
  widgets: [
    {
      type: counter
      data: Orders.count(today)
      compare: yesterday
    },
    {
      type: chart
      data: Sales.by(month)
      range: last_6_months
    }
  ]
}
```

## Form Handling

```yaml
screen OrderForm {
  form: {
    sections: [
      customer: [name!, email!, phone?],
      items: editable_table,
      notes: textarea
    ]
    
    validation: inline
    actions: [save_draft, submit]
  }
}
```

## Search and Filter

```yaml
screen Products {
  search: {
    quick: [name, sku]
    filters: {
      category: select,
      price: range,
      status: multiple
    }
    sort: [name, -created]
  }
}
```

## Access Control

```yaml
app Portal {
  roles: [admin, manager, user]
  
  entity Document {
    access: {
      view: authenticated
      edit: role.manager
      delete: role.admin
    }
  }
}
```

## Integration Patterns

```yaml
integrate {
  # Event-driven integration
  stripe: {
    on: payment.success
    then: [approve@order, notify@customer]
  }

  # API integration
  weather: {
    url: "https://api.weather.com"
    cache: 30min
    retry: 3
  }
}
```

## Multi-tenant Patterns

```yaml
app SaaS {
  tenant {
    isolation: schema  # or: database, row
    routing: subdomain
    
    customize: {
      branding: true
      fields: true
    }
  }

  entity Document {
    tenant: Tenant
    access: tenant.users
  }
}
```

## Best Practices

1. **Pattern Selection**
   - Use built-in patterns when possible
   - Customize only when needed
   - Maintain consistency across app

2. **Pattern Composition**
   - Combine patterns effectively
   - Keep patterns focused
   - Document custom patterns

3. **Pattern Evolution**
   - Start simple
   - Add complexity gradually
   - Refactor when needed
