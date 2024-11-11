# Integration Example

Shows how SeedML simplifies external service integration through intent-focused patterns.

## Basic Integration

```seedml
app Store {
  # Declare integration needs - everything else is automatic
  integrate {
    auth: auth0          # Authentication
    payment: stripe      # Payments
    email: sendgrid      # Email
    storage: s3          # Files
  }

  # Use integrations through simple intent
  entity Order {
    customer: Customer
    items: [OrderItem]
    status: Draft -> Paid -> Shipped

    rules {
      pay: {
        # Intent-focused payment processing
        requires: items.length > 0
        then: charge@stripe      # Automatic payment flow
      }

      ship: {
        requires: status.paid
        then: [
          notify@customer,       # Automatic email
          track@shipping        # Automatic tracking
        ]
      }
    }
  }
}
```

## Smart Features

Every integration includes:
- Authentication flow
- Error handling
- Rate limiting
- Retry logic
- Logging
- Monitoring

## Advanced Integration

```seedml
app Enterprise {
  # 1. Authentication
  auth {
    provider: oauth2 {
      sources: [google, github]   # Multiple providers
      features: [mfa, sso]       # Security features
    }
  }

  # 2. Storage
  storage {
    files: s3 {
      public: images/*          # Public access
      private: documents/*      # Secure storage
    }
    
    cache: redis {
      ttl: 1h                  # Caching
      invalidate: smart        # Auto invalidation
    }
  }

  # 3. Communication
  notify {
    email: {
      provider: sendgrid
      templates: {
        welcome: "welcome-user"    # Email templates
        order: "order-confirm"
      }
    }
    
    push: {
      provider: firebase
      topics: [news, alerts]      # Push notifications
    }
  }

  # 4. Event Handling
  events {
    'order.created': [
      charge@payment,              # Process payment
      notify@customer,             # Send confirmation
      track@analytics             # Record event
    ]

    'file.uploaded': {
      then: [
        scan@antivirus,           # Security scan
        index@search,             # Make searchable
        notify@owner              # Confirm upload
      ]
      retry: 3                    # Auto retry
    }
  }
}
```

## Event-Based Integration

```seedml
app EventDriven {
  # Define event flows
  events {
    # Simple event flow
    'user.signup': [
      create@account,            # Create account
      send@welcome,             # Welcome email
      notify@sales             # Sales notification
    ]

    # Complex event flow
    'order.submit': {
      validate: [               # Pre-conditions
        stock.available,
        payment.valid
      ]
      then: [                  # Actions
        process@payment,
        update@inventory,
        send@confirmation
      ]
      catch: [                 # Error handling
        notify@support,
        refund@payment
      ]
    }
  }
}
```

## Key Integration Patterns

### 1. Authentication
```seedml
auth {
  type: oauth2                # Auth type
  providers: [google, github] # Providers
  features: [mfa, sso]       # Security
}
```

### 2. Storage
```seedml
storage {
  files: s3                  # File storage
  cache: redis              # Caching
  search: elastic           # Search
}
```

### 3. Communication
```seedml
notify {
  email: sendgrid           # Email
  sms: twilio              # SMS
  push: firebase           # Push
}
```

### 4. Payments
```seedml
payments {
  processor: stripe         # Payment
  methods: [card, bank]    # Methods
  webhooks: auto           # Callbacks
}
```

## Smart Default Features

Every integration automatically includes:

### Security
- Credential management
- Token handling
- Access control
- Audit logging

### Reliability
- Error handling
- Rate limiting
- Circuit breaking
- Retry logic

### Monitoring
- Health checks
- Performance metrics
- Error tracking
- Usage analytics

### Development
- Local testing
- Mock responses
- Debug logging
- API documentation

## Best Practices

1. **Express Intent**
   - Focus on what, not how
   - Use business terminology
   - Let defaults handle details

2. **Handle Failures**
   - Every integration can fail
   - Default retry logic
   - Clear error states

3. **Stay Secure**
   - Credentials in env vars
   - Encrypted connections
   - Access control

4. **Monitor Everything**
   - Health checks
   - Performance metrics
   - Usage tracking

## Key Benefits

1. **Simpler Integration**
   - Minimal configuration
   - Standard patterns
   - Best practices built-in

2. **Better Reliability**
   - Automatic retries
   - Error handling
   - Circuit breakers

3. **Easier Maintenance**
   - Clear intent
   - Consistent patterns
   - Built-in monitoring
