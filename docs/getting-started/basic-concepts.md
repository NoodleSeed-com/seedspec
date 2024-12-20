# Basic Concepts

The Seed Specification Language is built around simple, intuitive concepts that map to common application needs.

## Core Structure

```javascript
// core.seed - Core app definition

app TaskManager {
  // Core domain model
  entity Task {
    title: string
    done: bool
    due?: date
  }
  
  // User interface
  screen TaskList {
    list: [title, done, due]
    actions: [create, complete]
  }
}
```

### 1. Entities

```javascript
entity Task {
  // Fields
  title: string
  done: bool
  due?: date
  
  // Relations
  assignee: User
  project: Project
}
```

### 2. Screens

```javascript
screen TaskList {
  // Data
  list: [title, done, due]
  
  // Actions
  actions: [create, complete]
  
  // Layout
  layout: grid(3)
}
```

### 3. Rules

```javascript
rules {
  // Validation
  validate {
    title: required
    due: future
  }
  
  // Behavior
  on_complete {
    notify: assignee
    update: project.progress
  }
}
```

## Field Types

```javascript
// Available field types

fields {
  // Text
  name: string
  description: text
  email: email
  phone: phone
  
  // Numbers
  age: int
  price: decimal
  rating: float
  
  // Dates
  created: datetime
  due: date
  time: time
  
  // Other
  done: bool
  status: draft/active/done
  tags: [string]
}
```

## Views

```javascript
screens {
  // List view
  list {
    columns: [title, status, due]
    actions: [create, edit, delete]
    filter: status
    sort: due
  }
  
  // Detail view
  detail {
    fields: [title, description, status]
    related: [comments, history]
    actions: [save, archive]
  }
}
```

## Actions

```javascript
actions: [
  create {
    fields: [title, description]
    validate: required
  },
  
  complete {
    confirm: "Mark as done?"
    then: notify@assignee
  }
]
```

## Best Practices

1. **Start Simple**
   - Begin with core entities
   - Add screens for basic operations
   - Layer in rules as needed

2. **Use Clear Names**
   - Choose descriptive entity names
   - Use business terminology
   - Keep field names intuitive

3. **Think in Workflows**
   - Model natural user flows
   - Group related actions
   - Consider the full lifecycle

4. **Stay Consistent**
   - Follow naming conventions
   - Use similar patterns
   - Maintain clear structure
