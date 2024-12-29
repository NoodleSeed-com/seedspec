# Types

SeedSpec has three core types:

- `text`: Text strings
- `num`: Numbers
- `bool`: True/false values

Example usage in a model:

```seed
model Task {
  title text        // Text field
  count num         // Number field
  done bool = false // Boolean with default
}
```

Status: ✓ Available
