# Screens

Screens provide a UI for working with models. Each screen automatically gets CRUD (Create, Read, Update, Delete) operations.

## Basic Usage

Link a screen to a model:

```seed
screen Tasks using Task
```

This generates a UI for:
- Viewing all tasks
- Creating new tasks  
- Editing existing tasks
- Deleting tasks

## Example

```seed
model Task {
  title text
  done bool = false
}

screen Tasks using Task  // Auto-generates CRUD interface
```

Status: ✓ Available
