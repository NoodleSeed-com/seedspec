# Integration

Seed Spec provides powerful integration capabilities to connect with external services and systems.

## Core Integration Patterns

### 1. Smart Authentication

```javascript
app MyApp {
  // OAuth-based authentication
  auth {
    provider: google
    scopes: [profile, email]
    roles: [user, admin]
  }
}
```

### 2. Data Integration

```javascript
storage {
  // File storage
  files {
    provider: s3
    bucket: uploads
    types: [image, pdf]
  }
  
  // Database
  database {
    provider: postgres
    replicas: 2
    backup: daily
  }
}
```

### 3. Service Communication

```javascript
services {
  // REST APIs
  api {
    stripe {
      type: rest
      base: "https://api.stripe.com/v1"
      auth: bearer
    }
    
    weather {
      type: rest
      base: "https://api.weather.com"
      auth: apikey
    }
  }
  
  // Message queues
  queue {
    orders {
      type: sqs
      fifo: true
    }
    
    notifications {
      type: rabbitmq
      durable: true
    }
  }
}
```

### 4. Location Services

```javascript
location {
  // Geocoding
  geocoding {
    provider: google
    cache: true
  }
  
  // Routing
  routing {
    provider: mapbox
    mode: [driving, walking]
  }
}
```

### 5. Event Handling

```javascript
events {
  // Webhooks
  webhooks {
    stripe {
      endpoint: "/webhooks/stripe"
      events: [payment.success, refund]
    }
  }
  
  // Real-time
  realtime {
    provider: pusher
    channels: [orders, chat]
  }
}
```

### 6. Maps Integration

```javascript
maps {
  // Map provider
  provider: mapbox
  
  // Features
  features {
    search: true
    routing: true
    clustering: true
  }
  
  // Styling
  style: streets-v11
  controls: [zoom, fullscreen]
}
```

## Best Practices

### 1. Role-Based Access

```javascript
// Location-based Integration
integrate {
  // Map provider configuration
  maps {
    provider: google
    apiKey: env.GOOGLE_MAPS_KEY
  }
  
  // Location services
  location {
    // Geocoding service
    geocoding {
      provider: google
      cache: true
      rateLimit: 100
    }
    
    // Distance calculations
    distance {
      provider: google
      mode: [driving, walking]
      units: metric
    }
  }
  
  // Access control
  access {
    // Role-based rules
    rules {
      admin: [all]
      manager: [view, edit]
      user: [view]
    }
    
    // Location-based rules
    location {
      required: true
      maxDistance: 100
      unit: kilometers
    }
  }
}
