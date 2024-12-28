# Screens

Define application screens/pages in SeedSpec.

```seed
screen TaskList "Task List" {
  use task_card
  use ai.Chatbot {
    systemPrompt: "You are a helpful assistant..."
    ui: {
      mode: "modal"
      trigger: "button"
    }
  }
  data tasks
}

screen UserList "User List" {
  use user_card
  data users
}

screen Dashboard "Dashboard" {
  use metrics_chart
  use activity_feed
  data {
    metrics
    activities
  }
}
```

Status: ✓ Available
