# Integration Examples

```yaml
# Complete integration example
app IntegratedSystem {
  # Authentication integration
  auth {
    provider: auth0 {
      domain: ${AUTH0_DOMAIN}
      clients: [web, mobile]
      social: [google, github]
    }
    
    mfa: {
      required: role.admin
      methods: [app, sms]
    }
  }

  # Payment processing
  payments {
    stripe {
      webhooks: {
        success: [approve@order, notify@customer],
        failure: [mark@failed, notify@support]
      }
      
      methods: {
        card: {
          enabled: true
          save: customer.consent
        }
        ach: role.business
      }
    }
  }

  # Communication services
  communicate {
    email: sendgrid {
      templates: {
        welcome: "d-123...",
        receipt: "d-456...",
        alert: "d-789..."
      }
      track: [open, click]
    }
    
    sms: twilio {
      verify: true
      marketing: consent
    }
    
    push: firebase {
      apps: [ios, android]
      topics: [news, alerts]
    }
  }

  # Storage services
  storage {
    files: s3 {
      bucket: ${S3_BUCKET}
      public: images/*
      private: documents/*
    }
    
    cache: redis {
      ttl: 1h
      invalidate: [user.*, product.*]
    }
    
    search: elasticsearch {
      indexes: [products, orders]
      replicas: 2
    }
  }

  # External APIs
  apis {
    weather: {
      url: "https://api.weather.com"
      key: ${WEATHER_KEY}
      cache: 30min
    }
    
    shipping: {
      fedex: {
        account: ${FEDEX_ACCOUNT}
        methods: [ground, express]
      }
      ups: {
        account: ${UPS_ACCOUNT}
        methods: [standard, next-day]
      }
    }
  }

  # Integration rules
  rules {
    new_order: {
      then: [
        charge@stripe,
        create@invoice,
        notify@customer,
        track@analytics
      ]
    }
    
    file_upload: {
      validate: [size, type]
      then: [
        store@s3,
        scan@antivirus,
        index@search
      ]
    }
  }
}
```

This example demonstrates:
- Authentication integration
- Payment processing
- Email and SMS
- File storage
- API connections
- Event handling
