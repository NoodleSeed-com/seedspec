# UI Patterns

SeedML generates complete user interfaces from simple, intent-focused patterns that automatically implement best practices.

## Core Concepts

```yaml
screen Orders {
  # Smart list with built-in features
  list orders {
    show: [date, customer, total, status]
    actions: [view, edit]      # Standard handlers
    features: [search, filter] # Common patterns
  }

  # Intent-focused forms
  form new_order {
    fields: [
      customer: select,    # Smart field types
      items: table,        # Complex components
      notes: text         # Simple inputs
    ]
    actions: [save, submit]
  }
}
```

## Key Features

### 1. Smart Lists
```yaml
list products {
  # Automatic features based on data
  show: [name, price, stock]  # Proper formatting
  group: category            # Built-in grouping
  sort: [-created_at]        # Default sorting
}
```

### 2. Intent-Based Forms
```yaml
form user {
  # Smart field handling
  fields: [
    email,           # Validation included
    password,        # Security built-in
    role: select     # UI components chosen
  ]
  layout: sections   # Responsive design
}
```

### 3. Navigation Patterns
```yaml
nav {
  # Complete navigation structure
  main: [dashboard, orders, customers]
  user: [profile, settings]
  mobile: bottom_tabs
}
```

### 4. Map Components
```yaml
# Interactive maps with smart defaults
map location_picker {
  view: {
    type: interactive    # Map type
    center: auto        # Smart centering
    zoom: dynamic       # Context-aware zoom
  }
  features: [
    search,            # Location search
    draw,              # Area selection
    cluster            # Smart clustering
  ]
}

# Advanced mapping patterns
screen StoreLocator {
  map: {
    data: Store.active
    cluster: true      # Auto clustering
    radius: 10km       # Search radius
    filters: category  # Data filtering
  }
  sidebar: store_list  # Linked components
}
```

### 4. Dashboard Patterns
```yaml
dashboard {
  # Smart layout with automatic responsiveness
  layout: grid(2x2)
  widgets: [
    sales.summary,    # Automatic data binding
    tasks.kanban,     # Built-in visualizations 
    alerts.feed,      # Real-time updates
    metrics.chart     # Interactive graphs
  ]
}
```

### 5. Map Patterns
```yaml
map {
  # Smart map components
  view: {
    type: interactive    # Map type
    center: location     # Initial center
    zoom: 12            # Initial zoom
    fit: markers        # Auto-fit to data
  }
  
  data: {
    markers: [Store]    # Data binding
    cluster: true       # Auto clustering
    regions: [Zone]     # Area overlays
  }
  
  controls: {
    position: top_left         # Control placement
    features: [
      search,                  # Location search
      filter,                  # Data filtering
      draw                     # Region drawing
    ]
  }
  
  interaction: {
    select: single/multiple    # Selection mode
    hover: show_info          # Hover behavior
    click: show_details       # Click handling
  }
}

# Example Usage
screen StoreLocator {
  layout: split
  map: {
    view: location_picker
    data: Store.active
    features: [
      search: address,
      radius: 10km,
      filters: category
    ]
  }
  
  sidebar: {
    list: selected_stores
    actions: [directions, share]
  }
}
```

## Best Practices

1. **Express Intent**
   - Focus on business needs
   - Use clear patterns
   - Trust smart defaults

2. **User Experience**
   - Consistent interfaces
   - Responsive design
   - Accessibility built-in

3. **Performance**
   - Automatic optimization
   - Smart loading
   - Efficient updates

4. **Map Experience**
   - Mobile-responsive controls
   - Progressive loading
   - Smart clustering
   - Gesture support
   - Accessibility features
