# Integration Examples

This guide shows how to integrate external services using SeedML's simplified patterns.

## Basic Integration

```seedml
app Store {
  # Simple integrations
  integrate {
    auth: google        # Basic auth
    email: sendgrid     # Email service
    storage: s3         # File storage
  }

  # Use integrations naturally
  entity Order {
    status: Draft -> Paid -> Shipped
    attachment: file    # Uses storage

    rules {
      create: {
        then: notify@customer  # Uses email
      }
    }
  }
}
```

## Common Patterns

### 1. Authentication
```seedml
integrate {
  auth: {
    provider: google    # Single provider
    redirect: "/home"   # After login
  }
}
```

### 2. File Storage 
```seedml
integrate {
  storage: {
    provider: s3
    bucket: "app-files"  # Single bucket
  }
}
```

### 3. Email Service
```seedml
integrate {
  email: {
    provider: sendgrid
    from: "app@example.com"
  }
}
```

## Best Practices

1. **Keep It Simple**
   - Use single providers
   - Minimal configuration
   - Default behaviors

2. **Security First**
   - Environment variables for keys
   - HTTPS connections
   - Basic access control

3. **Handle Errors**
   - Basic retry logic
   - Simple error states
   - Clear messages

## Smart Defaults

Every integration includes:
- Basic error handling
- Simple retry logic
- Standard logging
- Essential security
