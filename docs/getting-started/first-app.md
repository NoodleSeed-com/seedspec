# Creating Your First App

This guide walks you through creating your first Seed Spec application.

## 1. Basic Structure

Start with a simple task management app:

```javascript
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

## 2. Add Features

Enhance the app with more features:

```javascript
app TaskManager {
  // Expanded task model
  entity Task {
    title: string {
      min: 3
      max: 100
    }
    description: text
    done: bool
    due?: date
    priority: low/medium/high
    tags: [string]
    
    // Relations
    assignee?: User
    project?: Project
  }
  
  // Task list screen
  screen TaskList {
    // Data display
    list: [
      title,
      done,
      due,
      priority,
      assignee
    ]
    
    // Available actions
    actions: [
      create,
      edit,
      complete,
      delete
    ]
    
    // List behavior
    filter: [done, priority]
    sort: [due, priority]
    search: [title, description]
  }
  
  // Task detail screen
  screen TaskDetail {
    // Form fields
    fields: [
      title,
      description,
      due,
      priority,
      assignee
    ]
    
    // Related data
    related: [comments, history]
    
    // Available actions
    actions: [save, complete, delete]
  }
}
```

## 3. Add Business Rules

Define validation and behavior:

```javascript
app TaskManager {
  // Previous code...
  
  rules {
    // Validation rules
    validate {
      title: required
      due: future
      assignee: exists
    }
    
    // Business logic
    on_complete {
      // Update project progress
      update: project.progress
      
      // Notify relevant users
      notify: [assignee, project.owner]
      
      // Archive if needed
      if: project.autoArchive {
        archive: task
      }
    }
    
    // Automation rules
    automate {
      // Auto-assign based on tags
      assign_by_tags {
        when: tags.changed
        then: auto_assign
      }
      
      // Due date reminders
      remind_due {
        when: due - 1.day
        then: notify@assignee
      }
    }
  }
}
```

## Next Steps

1. **Add More Features**
   - User authentication
   - Comments system
   - File attachments
   
2. **Enhance the UI**
   - Custom layouts
   - Rich interactions
   - Mobile views
   
3. **Integrate Services**
   - Email notifications
   - Calendar sync
   - External APIs
