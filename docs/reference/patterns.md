# Common Patterns

SeedML provides built-in support for common application patterns that help you build robust applications quickly.

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
