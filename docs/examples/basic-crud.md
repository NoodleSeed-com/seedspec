# Basic CRUD Example

This example shows how a minimal specification generates a complete customer management system with rich features.

```yaml
app CustomerManager {
  # Core domain model - everything else is automatic
  entity Customer {
    name: string      # Implies required, validation
    email: email      # Implies unique, format validation  
    status: active/inactive = active
  }
}
```

Generated Features:
- Complete React frontend with:
  - List view with search, sort, filter
  - Create/edit forms with validation
  - Delete confirmation
  - Responsive design
  - Loading states
  - Error handling

- Full REST API backend with:
  - CRUD endpoints
  - Input validation
  - Error handling
  - Database schema
  - API documentation

- Standard patterns included:
  - Pagination
  - Field validation
  - Audit logging
  - API security
  - Database indexes

The minimal specification focuses on business intent while SeedML adds all the necessary implementation details automatically.

Override defaults only when needed:
```yaml
entity Customer {
  name: string {     # Override string defaults
    min: 2,
    max: 50
  }
  email: email      # Use smart defaults
}
```
