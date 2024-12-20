# Security

Seed Spec provides comprehensive security features built into the language.

## Core Security Features

### 1. Authentication

```javascript
app SecureApp {
  // Authentication configuration
  auth {
    // Providers
    providers: [
      google {
        clientId: env.GOOGLE_CLIENT_ID
        scopes: [profile, email]
      },
      github {
        clientId: env.GITHUB_CLIENT_ID
        scopes: [user]
      }
    ]
    
    // Session management
    session {
      duration: 24h
      renewal: true
      singleDevice: false
    }
    
    // Two-factor auth
    twoFactor {
      required: true
      methods: [app, sms]
    }
  }
}
```

### 2. Authorization

```javascript
roles {
  // Role definitions
  admin {
    permissions: [all]
  }
  
  manager {
    permissions: [
      users.view,
      users.edit,
      orders.manage
    ]
  }
  
  user {
    permissions: [
      profile.edit,
      orders.create
    ]
  }
}
```

### 3. Data Protection

```javascript
protect {
  // Encryption
  encrypt {
    fields: [ssn, creditCard]
    algorithm: aes-256-gcm
  }
  
  // Data masking
  mask {
    fields: [email, phone]
    pattern: "***-***-**{last4}"
  }
  
  // Access control
  access {
    rules: [
      "user.id = record.userId",
      "user.role = 'admin'"
    ]
  }
}
```

### 4. Audit Logging

```javascript
audit {
  // What to log
  track {
    changes: [create, update, delete]
    access: [view, export]
    auth: [login, logout, failed]
  }
  
  // Log details
  details {
    user: true
    timestamp: true
    location: true
    changes: diff
  }
  
  // Retention
  retain {
    duration: 1y
    backup: true
  }
}
```

## Security Patterns

### 1. Data-Level Security

```javascript
entity Order {
  // Fields
  id: uuid
  total: money
  status: pending/paid/shipped
  
  // Security rules
  security {
    view: ["user.id = userId", "user.role = 'admin'"]
    edit: ["user.role in ['admin', 'manager']"]
    delete: ["user.role = 'admin'"]
  }
  
  // Field-level security
  fields {
    creditCard {
      view: ["user.role = 'admin'"]
      encrypt: true
    }
    
    notes {
      edit: ["user.id = assignedTo"]
    }
  }
}
```

### 2. User Management

```javascript
entity User {
  // Core fields
  id: uuid
  email: email
  password: password
  role: admin/manager/user
  
  // Security features
  security {
    password {
      minLength: 12
      require: [number, special, mixed]
      expire: 90d
    }
    
    lockout {
      attempts: 5
      duration: 15m
    }
    
    mfa {
      required: true
      methods: [app, sms]
    }
  }
}
```

### 3. Location Privacy

```javascript
entity UserLocation {
  // Location data
  location: location
  timestamp: datetime
  accuracy: float
  
  // Privacy rules
  privacy {
    // Precision control
    precision: city
    
    // Access rules
    access {
      exact: ["user.role = 'admin'"]
      approximate: ["user.role = 'manager'"]
    }
    
    // Retention
    retain {
      duration: 30d
      anonymize: true
    }
  }
}
