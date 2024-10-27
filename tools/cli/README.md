# SeedML CLI

Command line tool for generating full-stack applications from SeedML specifications using Claude 3.5 Sonnet.

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
  entity Task {
    title: string!
    description: text
    status: todo->doing->done
  }
  
  screen Tasks {
    list: [title, status]
    actions: [create, edit, delete]
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

- Production-ready code generation
- Consistent patterns and practices
- Complete application structure
- Security best practices
- Modern tech stack

## Requirements

- Python 3.8+
- Anthropic API key
