# Data Binding

Bind data to UI components in SeedSpec.

```seed
screen TaskList "Task List" {
  // Bind entire tasks collection to screen
  data tasks

  // Use task data in component
  use task_card {
    task: tasks.current
  }
}

component task_card "Task Card" {
  input {
    task: Task
  }

  // Bind task properties to UI elements
  text task.title
  checkbox task.done
  number task.priority
}
```

Status: ✓ Available
