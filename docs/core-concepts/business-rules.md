# Business Rules

SeedML lets you express business logic through simple, intent-focused rules that automatically handle validation, computation, and workflow.

## Core Concepts

### State Management
```yaml
entity Order {
  # Smart state transitions
  states: Draft -> Submitted -> Approved -> Completed {
    Submitted: requires[complete]
    Approved: requires[manager.review] 
    Completed: triggers[invoice.create]
  }
}
```

```yaml
entity Order {
  # Smart validation - handles type checking, required fields
  validate {
    total: positive
    items: not_empty
    customer: verified
  }

  # Automatic computations
  compute {
    subtotal: sum(items.price)
    tax: subtotal * 0.1  
    total: subtotal + tax
  }

  # Intent-focused workflows
  flow submit {
    when: valid           # Implied validation
    then: notify@sales    # Automatic handling
  }
}
```

## Key Features

### 1. Smart Validation
```yaml
validate {
  # Built-in validations with clear intent
  email: valid_email     # Format checking
  age: adult            # Business logic
  stock: available      # External check
}
```

### 2. Computed Properties 
```yaml
compute {
  # Automatic dependency tracking
  full_name: first_name + " " + last_name
  age: today - birthdate
  status: if(balance > 0) "active" else "suspended"

  # Location-based computations
  distance: from(warehouse)        # Distance calc
  coverage: area(service_region)   # Area calc
  nearest: closest(Store, 5)       # Proximity
  density: stores_per_km2         # Density calc
  
  # Advanced computations
  route: {
    optimal_path: [stops]         # Route planning
    eta: with_traffic            # Arrival time
    alternatives: top(3)         # Alternative routes
  }
  
  territory: {
    coverage: region_union       # Combined areas
    overlap: region_intersect    # Shared areas
    gaps: region_difference     # Uncovered areas
  }
}
```

### 3. Business Workflows
```yaml
flow approve_expense {
  # Focus on business logic, not implementation
  when: [
    amount < policy.limit,
    submitter.manager_approved
  ]
  then: [
    notify@accounting,
    create@payment
  ]
}

flow assign_delivery {
  # Location-aware workflow
  when: [
    driver.within(50km, pickup),
    route.duration <= shift_remaining,
    vehicle.capacity >= package.size
  ]
  
  compute: {
    route: optimal_path([pickup, dropoff]),
    eta: route.duration + now(),
    cost: route.distance * rate
  }
  
  then: [
    notify@driver(route),
    update@customer(eta),
    track@analytics(assignment)
  ]
}

flow optimize_territory {
  # Territory management workflow
  when: coverage.gaps > threshold
  
  analyze: {
    density: customers_per_area,
    workload: orders_per_week,
    travel: average_distance
  }
  
  propose: {
    changes: balance_territories,
    impact: simulate_changes,
    timing: transition_plan
  }
  
  then: [
    notify@managers,
    schedule@updates,
    track@changes
  ]
}
```

## Best Practices

1. **Express Intent**
   - Use business terminology
   - Focus on what, not how
   - Let SeedML handle implementation

2. **Smart Defaults**
   - Common validations built-in
   - Standard workflows included
   - Override only when needed

3. **Keep It Simple**
   - One rule per concept
   - Clear dependencies
   - Automatic optimization

4. **Location Rules Best Practices**
   - Validation
     • Use appropriate precision
     • Consider timezone impacts
     • Handle edge cases
     • Validate accessibility

   - Computation
     • Cache distance calculations
     • Optimize bulk operations
     • Use appropriate indices
     • Handle async calculations

   - Workflows
     • Consider mobile scenarios
     • Handle offline cases
     • Manage battery impact
     • Process location batches

   - Performance
     • Smart geocoding cache
     • Efficient region checks
     • Batch distance matrices
     • Progressive loading
