# Type System

The Seed Specification Language's type system combines simplicity with power.

## Core Types

```yaml
// Basic Types
string              // Text
number              // Numbers
bool                // True/False
date                // Dates
time                // Time
datetime            // Date+Time
money               // Currency
email               // Email
phone               // Phone
url                 // URLs

// Complex Types
[Type]              // Lists
Type?               // Optional
Type!               // Required
map<Key,Value>      // Maps
enum(v1,v2)         // Enums

// Special Types
id                  // Unique IDs
timestamp           // Timestamps
file                // Files
image               // Images

// Location Types
location            // Geographic coordinates with address
place               // Place details with metadata
region              // Geographic boundary
distance            // Distance with units
```

## Type Usage

```yaml
// Validation
age: number {
  min: 0
  max: 150
}

// Collections
tags: [string]
metadata: map<string,any>

// Inference
entity Product {
  price: 0.00      // money
  created: now()    // timestamp
  active: true     // bool
}
```

## Location Type System

```yaml
# Location Types
location {
  lat: number        # Latitude
  lng: number        # Longitude
  address?: string   # Optional formatted address
  placeId?: string   # Optional place identifier
}

place {
  location: location
  name: string
  type: string
  metadata: map<string, any>
}

region {
  type: circle/polygon/bounds
  center?: location   # For circle
  radius?: distance   # For circle
  points?: [location] # For polygon
  bounds?: {          # For bounds
    ne: location
    sw: location
  }
}

distance {
  value: number
  unit: km/mi/m
}

# Location Validation
location {
  within: region          # Must be within region
  near: location, radius  # Must be near point
  type: business/postal   # Place type constraints
}

# Location Formatting
location {
  format: full/short     # Address format
  components: [street, city, country]
  language: string       # Localization
}

# Usage Examples
stores: [location]           # List of locations
coverage: region            # Service area
distance: number as km      # Distance in kilometers

entity Store {
  location: location {
    within: service_area
    type: commercial
  }
  compute {
    distance: from(user.location)
    nearby: stores.within(5km)
    region: coverage_area()
  }
}
```

## Custom & Composite Types

```yaml
# Custom Types
types {
  Currency: money {
    precision: 2
    positive: true
  }
  Status: enum(active, pending)
}

# Composition
entity Order {
  items: [{
    product: Product
    quantity: number > 0
    price: Currency
  }]
  shipping: {
    address: Address
    method: standard/express
  }
}
```

## Benefits

- Type Safety: Compile-time & runtime validation
- Clear Modeling: Self-documenting schemas
- Code Generation: DB, API, UI components
- IDE Support: Completion, validation, docs
