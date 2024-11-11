# SaaS Application Example

```yaml
# Multi-tenant SaaS platform
app SaaSPlatform {
  # Tenant configuration
  tenant {
    isolation: schema  # database, schema, or row
    routing: subdomain
    
    customize: {
      branding: {
        logo: image
        colors: theme
        domain: url?
      }
      features: {
        enabled: [module]
        limits: map<feature, limit>
      }
    }
  }

  # Subscription management
  subscription {
    plans: {
      basic: {
        price: 10/month
        limits: {
          users: 5
          storage: 5gb
          api: 1000/day
        }
      }
      
      pro: {
        price: 50/month
        limits: {
          users: 50
          storage: 50gb
          api: 10000/day
        }
      }
      
      enterprise: {
        price: custom
        limits: custom
      }
    }
    
    features: {
      basic: [core, support],
      pro: [api, advanced, priority],
      enterprise: [custom, sla, training]
    }
  }

  # Cross-tenant features
  cross_tenant {
    sharing: {
      content: {
        access: explicit
        audit: true
      }
      
      marketplace: {
        publish: verified
        install: compatible
      }
    }
    
    analytics: {
      usage: aggregate
      trends: anonymous
    }
  }

  # Tenant management
  admin {
    dashboard: {
      metrics: [
        active_tenants,
        total_users,
        storage_used,
        api_usage
      ]
      
      actions: [
        provision,
        suspend,
        migrate,
        backup
      ]
    }
    
    monitoring: {
      health: [status, performance],
      alerts: [limits, errors],
      audit: [access, changes]
    }
  }

  # Tenant-aware entities
  entity Document {
    tenant: Tenant
    sharing: private/shared/public
    
    # Tenant isolation
    access: tenant.users
    storage: tenant.bucket
    audit: tenant.log
  }

  # Tenant-specific UI
  screen Dashboard {
    branding: tenant.theme
    modules: tenant.enabled
    limits: tenant.quotas
    
    widgets: [
      usage: tenant.metrics,
      users: tenant.members,
      activity: tenant.events
    ]
  }
}
```

This example demonstrates:
- Multi-tenant architecture
- Tenant isolation
- Custom branding
- Feature management
- Usage tracking
- Cross-tenant features
