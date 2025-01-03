# Types

SeedSpec has four core types:

- `text`: Text strings
- `num`: Numbers
- `bool`: True/false values
- `email`: Email addresses

Example usage in a model:

```seed
model User {
  name text         // Text field
  count num         // Number field
  done bool = false // Boolean with default
  email email       // Email field
}
```

Status: ✓ Available
