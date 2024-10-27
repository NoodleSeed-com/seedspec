# SeedML Syntax Reference

## Basic Structure

Every SeedML application follows this structure:

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

## Entity Syntax

```yaml
entity [EntityName] {
  # Basic fields
  name: string
  age: number
  active: bool = true
  
  # Field modifiers
  required: string!
  optional: string?
  defaulted: string = "default"
  
  # Complex types
  items: [Item]
  metadata: map<string,any>
  status: draft->submitted->approved
  
  # Validation
  validate: {
    age: positive,
    email: format_valid
  }
  
  # Computed fields
  total: sum(items.price)
  
  # Access control
  access: {
    view: authenticated
    edit: role.admin
  }
}
```

## Screen Syntax

```yaml
screen [ScreenName] {
  # Layout
  layout: grid(3x2)
  
  # Components
  list: {
    columns: [id, name, status]
    actions: [edit, delete]
    features: [search, filter, sort]
  }
  
  form: {
    fields: [name, email, role]
    validate: inline
    submit: save_user
  }
  
  # Navigation
  nav: {
    links: [dashboard, settings]
    breadcrumb: true
  }
}
```

## Rules Syntax

```yaml
rules {
  [RuleName]: {
    # Conditions
    require: [
      user.verified,
      total > 0
    ]
    
    # Validation
    validate: items.length > 0
    
    # Actions
    then: [
      update_status,
      notify@user
    ]
  }
}
```

## Integration Syntax

```yaml
integrate {
  [ServiceName]: {
    # Configuration
    config: {
      url: string
      key: string
    }
    
    # Events
    events: {
      success: [handler1, handler2]
      error: notify@admin
    }
    
    # Features
    features: [
      feature1,
      feature2: config
    ]
  }
}
```

## Meta Configuration

```yaml
meta {
  name: string
  version: string
  description: text
  
  config: {
    theme: string
    locale: string
    features: [string]
  }
}
```

## Best Practices

1. **Organization**
   - Group related entities
   - Keep rules close to entities
   - Organize screens by workflow

2. **Naming**
   - Use clear, descriptive names
   - Follow consistent conventions
   - Use business terminology

3. **Documentation**
   - Comment complex logic
   - Document business rules
   - Explain custom patterns

4. **Structure**
   - Keep files focused
   - Use consistent indentation
   - Break up large files
