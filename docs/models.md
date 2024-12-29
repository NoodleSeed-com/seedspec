# Models

Models define data structures in SeedSpec using basic types. Each model automatically gets CRUD operations.

## Basic Types

- `text`: Text strings
- `num`: Numbers
- `bool`: True/false values

## Defining Models

```seed
model Task {
  title text      // Required text field
  done bool       // Required boolean
  count num       // Required number
  notes text?     // Optional text field
}
```

Each model automatically gets:
- Unique ID field
- Title field (first text field)
- Basic CRUD operations

## Example

```seed
model Product {
  name text       // First text field becomes title
  price num
  inStock bool
  description text?
}
```

Status: ✓ Available
