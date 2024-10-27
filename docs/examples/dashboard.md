# Analytics Dashboard Example

```yaml
# Real-time analytics dashboard
app Analytics {
  # Data models
  entity Metric {
    name: string
    value: number
    timestamp: datetime
    category: string
  }

  # Dashboard screen
  screen Dashboard {
    layout: grid(2x2)
    
    # Multiple chart types
    widgets: [
      {
        type: line-chart
        data: Metric
        x: timestamp
        y: value
        group: category
        range: last-7-days
      },
      {
        type: counter
        data: Metric
        value: sum(value)
        change: vs_previous_period
      },
      {
        type: bar-chart
        data: Metric
        x: category
        y: sum(value)
      },
      {
        type: table
        data: Metric
        columns: [name, value, timestamp]
        sort: -timestamp
        limit: 10
      }
    ]
    
    # Interactive features
    features: [
      time-range-selector,
      category-filter,
      export-data
    ]

    # Real-time updates
    refresh: 5min
    realtime: websocket
  }
}
```

This example demonstrates:
- Data visualization
- Real-time updates
- Interactive filtering
- Multiple chart types
- Dashboard layout
