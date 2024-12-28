# Examples

This document provides examples of SeedSpec applications demonstrating the latest language features.

## 1. Basic CRUD with Implicit Actions and Screens

This example demonstrates the simplest possible SeedSpec application using a single model and its implicit CRUD screen.

```seed
app Contacts "Contact Management" {
  model Contact {
    name text as title // 'name' is the title field for display
    email text?       // 'email' is optional
  }

  data {
    Contacts: Contact[] [
      { "John Doe", email: "john.doe@example.com" }, // Implicit mapping for 'name'
      { "Jane Smith", email: "jane.smith@example.com" } // Implicit mapping for 'name'
    ]
  }

  screen Contacts // Implicitly uses the 'Contact' model and provides a CRUD interface
}
```

**Explanation:**

*   The `Contact` model has an implicit `id` field and two other fields: `name` (required) and `email` (optional).
*   The `name` field is designated as the title field using `as title`.
*   The `Contacts` dataset is explicitly typed as an array of `Contact` objects.
*   The data instances use implicit mapping for the required `name` field, relying on significant order.
*   The `screen Contacts` line automatically generates a CRUD screen for managing `Contact` instances because the screen name matches the dataset name.

## 2. Enhanced Todo App with Category Options

This example demonstrates a more comprehensive Todo app using the latest SeedSpec features, including predefined category options using the default identifier naming convention.

```seed
app TodoApp "Todo App" {
  model Todo {
    title text as title
    completed bool = false
    dueDate date?
    priority num?
    category in [Work, Personal, Shopping] = Personal // Category with predefined options and default value
    notes text?
  }

  data {
    Todos: Todo[] [
        { "Buy groceries", false, 2023-12-25, priority: 1, category: Shopping, notes: "Remember the milk!" }, // Mixed implicit and explicit
        { "Walk the dog", true, 2023-12-24, priority: 2, category: Personal } // Mixed implicit and explicit
    ]
  }

  screen Todos // Implicitly uses the 'Todo' model and provides a CRUD interface
}
```

**Explanation:**

*   The `Todo` model now defines a `category` field with a set of predefined options: Work, Personal, and Shopping. The language will automatically generate the display names "Work", "Personal", and "Shopping" for these options.
*   The `category` field also has a default value of `Personal`.
*   The `Todos` dataset is explicitly typed.
*   The data instances use a mix of implicit and explicit field mapping.
*   The `screen Todos` line automatically generates a CRUD screen for managing `Todo` instances. The UI for the `category` field will likely be a dropdown or a set of radio buttons, allowing the user to select one of the predefined options.

## 3. Product Management App

This example demonstrates a slightly more complex application with multiple models and custom actions.

```seed
app ProductManager "Product Management App" {
  model Category {
    name text as title
  }

  model Product {
    name text as title
    description text?
    price num
    category Category?
  }

  data {
    Categories: Category[] [
      { "Electronics" }, // Implicit mapping for 'name'
      { "Books" }        // Implicit mapping for 'name'
    ]
    Products: Product[] [
      { "Laptop", , 1200, category: Categories[0] }, // Implicit for name and price, explicit for category, skipping description
      { "Mouse", , 25, category: Categories[0] }, // Implicit for name and price, explicit for category, skipping description
      { "SeedSpec Guide", , 99, category: Categories[1] } // Implicit for name and price, explicit for category, skipping description
    ]
  }

  screen Categories
  screen Products

  action AddProduct(name: text, description: text?, price: num, category: Category?) {
    create Product { name: name, description: description, price: price, category: category }
  }
}
```

**Explanation:**

*   This app has two models: `Category` and `Product`.
*   The `Product` model demonstrates a relationship with the `Category` model.
*   The `Categories` and `Products` datasets are explicitly typed.
*   The data instances use a mix of implicit and explicit field mapping, leveraging significant order and skipping optional fields where possible.
*   The `screen Categories` and `screen Products` lines automatically generate CRUD screens for managing `Category` and `Product` instances.
*   The `AddProduct` action demonstrates how to define a custom action for creating a new product. This action could be used, for example, in a custom form within the `Products` screen.

These examples demonstrate the power and conciseness of the SeedSpec language, showcasing its ability to rapidly prototype data-driven applications with minimal code.
