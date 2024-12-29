# Relationships

Basic model references in SeedSpec.

```seed
model Task {
  title text
  assignee User     // Single reference
}

model User {
  name text
  tasks [Task]     // Array reference
}
```

Status: ✓ Available
