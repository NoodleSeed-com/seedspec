# Analytics Dashboard Example

```yaml
// Real-time analytics dashboard with location intelligence
app Analytics {
  // Data models
  entity Metric {
    name: string
    value: number
    timestamp: datetime
    category: string
    location?: location    // Optional location data
  }

  entity LocationMetric {
    location: location
    metrics: map<string, number>
    timestamp: datetime
    region: reference
  }

  # Dashboard screen
  screen Dashboard {
    layout: grid(2x2)
    
    // Multiple visualization types
    widgets: [
      {
        type: map
        data: LocationMetric
        view: {
          type: heatmap
          cluster: {
            enabled: true
            threshold: 100
            radius: 50
            colors: gradient
          }
          controls: {
            zoom: true
            pan: true
            search: {
              radius: 10km
              filters: [type, status]
            }
          }
        }
        value: {
          field: metrics.value
          range: last-7-days
          aggregation: sum
        }
      },
      {
        type: region-map
        data: Metric.by(region)
        color: value
        legend: true
        interact: drill_down
      },
      {
        type: line-chart
        data: Metric
        x: timestamp
        y: value
        group: category
        range: last-7-days
      },
      {
        type: cluster-map
        data: EventMetric
        cluster: category
        size: value
        tooltip: details
      }
    ]
    
    // Interactive features 
    features: [
      time-range-selector,
      region-filter,
      category-filter,
      export-data
    ]

    # Real-time updates
    refresh: 5min
    realtime: websocket
  }

  # Location analytics
  analytics {
    spatial: {
      hotspots: {
        method: kernel_density
        threshold: significant
        timeframe: hourly
      },
      patterns: {
        type: movement
        window: 24h
        detect: [clusters, flows]
      }
    }
    
    metrics: {
      density: per_km2
      distribution: by_region
      concentration: gini_index
    }
  }

  # Map controls
  controls {
    view: {
      type: [heat, cluster, region]
      switch: animated
      sync: linked
    },
    
    analysis: {
      tools: [
        area_selection,
        pattern_detection
      ],
      export: [
        geojson,
        csv,
        image
      ]
    }
  }
}
```

This example demonstrates:
- Location-based analytics
- Spatial visualization
- Real-time updates
- Interactive mapping
- Multiple chart types
- Pattern detection
- Integrated dashboard layout
