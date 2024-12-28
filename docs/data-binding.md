# Data Binding

SeedSpec uses a declarative approach to data binding. Data is defined in `data` blocks and can be bound to UI components. Screens can automatically generate UI elements based on the data model.

## Defining Data

Datasets are defined within the top-level `data` block. To minimize token usage, SeedSpec allows for a flexible syntax when defining data instances within a dataset. The order of fields in the `data` block is significant and corresponds to the order of fields in the model definition.

**Syntax:**

```seed
data {
    DataSetName: Model[] [
        { value1, value2, fieldName: value3, value4 } // Mixed implicit and explicit
    ]
}
```

**Rules:**

1. **Significant Order:** The order of values corresponds to the order of fields in the model definition.
2. **Required Fields First:** Values for required fields must be provided first, in their order of definition.
3. **Implicit Mapping:** Values for required fields can be provided without explicitly naming the fields.
4. **Optional Field Names:** Field names are only required when deviating from the significant order or when skipping optional fields.
5. **Mixed Syntax:** A mix of implicit and explicit field mapping is allowed within the same data definition.
6. **Skipping Optional Fields:** Use commas without values to skip optional fields while maintaining significant order.

**Example:**

```seed
model Todo {
    title text as title      // Required
    completed bool = false  // Required
    dueDate date?           // Optional
    priority num?           // Optional
    category text?          // Optional
    notes text?             // Optional
}

data {
    Todos: Todo[] [
        { "Buy groceries", true, category: "Shopping", notes: "Remember the milk!" }, // Implicit for title and completed, explicit for category and notes
        { "Walk the dog", false, 2023-12-24, priority: 2 }, // Implicit for title, completed, dueDate, explicit for priority
        { "Pay bills", , , 1, "Finance" } // Implicit for title, skipping completed and dueDate, explicit for priority and category
    ]
}
```

## Implicit Screen Generation and Model Inference

When a `screen` is named after a dataset (e.g., `screen Todos`), and that dataset is explicitly typed in the `data` block, the screen automatically:

1. **Infers the associated model:** In the example above, `screen Todos` would infer that it's working with the `Todo` model.
2. **Generates a default CRUD interface:** The screen will provide UI elements for creating, reading, updating, and deleting instances of the associated model.

**Example:**

```seed
screen Todos // Implicitly uses the 'Todo' model and generates a CRUD interface
```

This eliminates the need for manual data binding in many cases, making development faster and more efficient. You can still customize the screen by adding elements within the `screen` definition, which will override or augment the default behavior.

Status: ✓ Available
