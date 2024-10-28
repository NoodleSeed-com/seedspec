# SeedML CLI

Command line tool for generating layered full-stack applications from SeedML specifications using Claude 3.5 Sonnet.

## Installation

```bash
pip install -e .
```

## Usage

1. Set your Anthropic API key:
```bash
export ANTHROPIC_API_KEY='your-api-key'
```

2. Create a .seed file:
```yaml
app TodoApp {
  # Foundation layer
  types {
    TaskStatus: enum(todo, doing, done)
  }

  # Data layer
  entity Task {
    title: string!
    description: text
    status: TaskStatus = todo
    assigned_to?: User
  }

  # Logic layer
  rules {
    start_task: {
      require: status == todo
      then: [set_status(doing), notify@assigned]
    }
    complete_task: {
      require: status == doing
      then: [set_status(done), notify@creator]
    }
  }

  # Security layer
  permissions {
    manage_tasks: {
      entity: Task
      actions: [create, update]
      filter: assigned_to == current_user
    }
  }
  
  # Presentation layer
  screen Tasks {
    list: [title, status, assigned_to]
    actions: [
      create,
      start if todo,
      complete if doing
    ]
  }

  # Integration layer
  integrate {
    notification: sendgrid {
      templates: {
        task_assigned: "t-123",
        task_completed: "t-456"
      }
    }
  }
}
```

3. Generate the application:
```bash
seedml todo.seed
```

This will create a complete application with:
- React frontend
- FastAPI backend
- MySQL database
- Full testing suite
- Documentation

## Features

- Layered architecture generation
  - Foundation layer (types, validation)
  - Data layer (entities, relationships)
  - Logic layer (rules, workflows)
  - Security layer (permissions, roles)
  - Presentation layer (UI, components)
  - Integration layer (external services)

- Production-ready code generation
  - Consistent patterns per layer
  - Cross-layer validation
  - Layer-specific best practices
  - Modern tech stack
  - Complete testing per layer

## Requirements

- Python 3.8+
- Anthropic API key
