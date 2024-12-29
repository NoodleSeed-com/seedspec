# SeedSpec Language Reference

SeedSpec is a minimal language for defining data-driven applications.

## Core Types

- `text`: Text strings
- `num`: Numbers 
- `bool`: True/false values

## Models

Define data structures:

```seed
model Task {
  title text        // Required text field
  done bool = false // Boolean with default
}
```

Each model automatically gets:
- Unique ID field
- CRUD operations (create, read, update, delete)
- Generated UI screen

## Screens 

Reference models to get UI:

```seed
screen Tasks using Task  // Auto-generates CRUD interface
```

That's it! This minimal grammar lets you build working applications with:
- Data modeling
- Basic persistence
- Generated UI
- CRUD operations

Additional features can be added as needed.
