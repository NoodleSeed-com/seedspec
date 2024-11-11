# Basic CRUD Example

The simplest possible SeedML application showing smart defaults in action.

```seedml
app Contacts {
  # Core domain model
  entity Contact {
    name: string      # Required by default
    email: email     # Validated automatically
    phone: phone?    # Optional field
    location: location # Location with geocoding
  }

  # Complete UI with maps
  screen Contacts {
    list: [name, email, phone]  # List view
    map: location               # Map view
  }
}
```

## What You Get

This minimal specification automatically generates:

### Data Layer
- Database schema with proper types and indexes
- Input validation for all fields
- API endpoints for CRUD operations
- Search and filter capabilities

### User Interface
- Responsive list/grid view
- Create and edit forms 
- Search functionality
- Sort and filter options
- Mobile friendly layout

### Features
- Authentication and authorization
- Error handling
- Success messages
- Audit logging
- API documentation

### Map Features
- Interactive map view
- Location picker for editing
- Address autocomplete
- Distance calculations
- Clustering for multiple contacts
- Mobile-friendly controls

All of these features come from smart defaults - no additional configuration needed.

## Progressive Enhancement

When you need customization:

```seedml
app Contacts {
  # Override specific defaults
  entity Contact {
    name: string {
      min: 2,            # Min length
      max: 50,           # Max length
      case: title        # Title case
    }
    email: email         # Keep email defaults
    phone: phone?        # Keep phone defaults
    location: location {
      required: true
      validate: {
        region: service_area
        type: business
      }
    }
  }

  # Customize UI
  screen Contacts {
    # Enhanced list view
    list {
      show: [name, email, location]
      group: region
      sort: distance(current_location)
    }
    
    # Enhanced map view
    map {
      cluster: true
      search: {
        radius: 10km
        filters: [region, type]
      }
      interactions: [
        select: show_details,
        route: get_directions
      ]
    }
  }
}
```

## Key Principles Demonstrated

1. **Minimal Valid Specification**: Express only what's unique about your application
2. **Smart Defaults**: Production patterns included automatically
3. **Progressive Enhancement**: Add complexity only when needed
4. **Intent-Focused**: Express what you want, not how to build it
5. **Location-Aware**: Seamless integration of mapping features
