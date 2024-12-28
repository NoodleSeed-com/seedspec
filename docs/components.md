# Components

Define reusable UI components in SeedSpec.

```seed
component task_card "Task Card Component" {
  input {
    task: Task
  }
}

component user_card "User Card Component" {
  input {
    user: User
  }
}

component Button "Button Component" {
  input {
    label: text
    onClick: action
  }
}
```

Status: ✓ Available
