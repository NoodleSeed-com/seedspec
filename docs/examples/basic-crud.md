# Basic CRUD Application Example

```yaml
# Simple customer management system
app CustomerManager {
  entity Customer {
    # Clear required vs optional
    name: string!       # Required
    email: email!      # Required, validated
    phone: phone?      # Optional
    status: active/inactive = active  # Enum with default
  }

  screen Customers {
    list: [name, email, status]
    actions: [create, edit, delete]
    features: [search, filter, sort]  # Standard features
  }
}
```

This example demonstrates:
- Basic entity definition
- Field types and validation
- Simple UI generation
- Standard CRUD operations
