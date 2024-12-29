# Examples

Simple examples of SeedSpec applications.

## Basic Task List

```seed
model Task {
  title text
  done bool = false
}

screen Tasks using Task
```

## User Directory

```seed
model User {
  name text
  email text
}

screen Users using User
```

## Product Catalog

```seed
model Product {
  name text
  price num
  inStock bool = true
}

model Category {
  name text
  products [Product]
}

screen Products using Product
screen Categories using Category
```

These examples demonstrate the core features of SeedSpec:
- Basic data modeling
- Simple types
- Model references
- Auto-generated CRUD screens

Status: ✓ Available
