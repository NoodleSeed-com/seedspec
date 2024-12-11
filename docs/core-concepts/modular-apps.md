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
