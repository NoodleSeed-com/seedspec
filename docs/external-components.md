# External Components

Use components from external libraries in SeedSpec.

```seed
import "@stdlib/ai" as ai

screen TaskList "Task List" {
  // Use external AI chatbot component
  use ai.Chatbot {
    systemPrompt: "You are a helpful assistant..."
    ui: {
      mode: "modal"
      trigger: "button"
    }
  }

  // Use external chart component
  use charts.LineChart {
    data: taskMetrics
    xAxis: "date"
    yAxis: "completed"
  }
}

// Import multiple components
import "@stdlib/ui" {
  Button,
  Card,
  Table
}

screen Dashboard {
  use Button {
    label: "Refresh"
  }
  use Table {
    data: users
  }
}
```

Status: ✓ Available
