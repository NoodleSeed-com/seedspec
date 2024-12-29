# Data Binding

SeedSpec automatically binds model data to screens.

```seed
model Task {
  title text
  done bool = false
}

screen Tasks using Task  // Data automatically bound to UI
```

The screen gets:
- List view of all tasks
- Form for creating/editing tasks
- Delete confirmation

Status: ✓ Available
