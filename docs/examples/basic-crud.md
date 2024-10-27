# Basic CRUD Application Example

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

This example demonstrates:
- Basic entity definition
- Field types and validation
- Simple UI generation
- Standard CRUD operations
