# Examples

This document provides examples of SeedSpec applications.

## Basic CRUD Example

The simplest possible SeedSpec application demonstrating core concepts.

```seed
app Contacts "Contact Management" {
  model Contact "Contact" {
    name text = "New Contact"
    email text = ""
  }

  screen ContactList "Contact List" {
    data contacts
  }
}
```

This example demonstrates a basic application that implements a `Contact` model and a `ContactList` screen.

## Business Application Example

A more complex SeedSpec application demonstrating a business application.

```seed
app OrderSystem "Order Management" {
  model Customer "Customer" {
    name text = "New Customer"
  }

  model Product "Product" {
    name text = "New Product"
    price num = 0
  }

  model Order "Order" {
    customer Customer
    items [Product]
  }

  screen OrderList "Order List" {
    data orders
  }
}
```

This example demonstrates a more complex application that implements `Customer`, `Product`, and `Order` models, along with an `OrderList` screen.

## Analytics Dashboard Example

A SeedSpec application demonstrating a dashboard with data visualization.

```seed
app Analytics "Analytics Dashboard" {
  model Metric "Metric" {
    name text = "New Metric"
    value num = 0
  }

  screen Dashboard "Dashboard" {
    data metrics
  }
}
```

This example demonstrates a basic dashboard application that implements a `Metric` model and a `Dashboard` screen.

## Integration Examples

A SeedSpec application demonstrating integration with external services.

```seed
app Store "Store App" {
  model Product "Product" {
    name text = "New Product"
  }

  screen ProductList "Product List" {
    data products
  }
}
```

This example demonstrates a basic application that implements a `Product` model and a `ProductList` screen.

## SaaS Application Example

A SeedSpec application demonstrating a multi-tenant SaaS platform.

```seed
app SaaSPlatform "SaaS Platform" {
  model Tenant "Tenant" {
    name text = "New Tenant"
  }

  model User "User" {
    name text = "New User"
    tenant Tenant
  }

  screen TenantList "Tenant List" {
    data tenants
  }
}
```

This example demonstrates a basic SaaS application that implements `Tenant` and `User` models, along with a `TenantList` screen.
