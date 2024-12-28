# Models

Models define data structures with typed fields in SeedSpec. Each model automatically gets implicit `create`, `update`, and `delete` actions for basic CRUD operations.

## Defining Models

```seed
model Todo {
    title text as title // Title field for display
    completed bool = false // Required field with default value
    dueDate date? // Optional field
    priority num? // Optional field
    category text? // Optional field
    notes text? // Optional field
}
```

*   Each model implicitly has an `id` field, which is a unique identifier.
*   Alternatively, you can designate a specific field as the ID using the `as id` syntax:

```seed
model Product {
    productCode text as id // 'productCode' is designated as the ID field
    name text as title
    price num
}
```

## Field Properties

*   **Required/Optional:** Fields are required by default. Use the `?` symbol after the type to make a field optional.
*   **Title Field:** Use `as title` to designate a field as the main title field for display purposes in UI components.
*   **Default Values:** You can specify default values for fields using the `=` operator.

## Display Names

Models and their fields can have display names that are used in UI components. Display names can be automatically generated or explicitly defined.

### Automatic Display Name Generation

If a display name is not explicitly provided, SeedSpec will automatically generate one based on the field name. This is done by splitting the field name at each uppercase letter and inserting a space. For example:

*   `userName` becomes "User Name"
*   `emailAddress` becomes "Email Address"
*   `manufacturerID` becomes "Manufacturer ID"

### Explicitly Defining Display Names

You can explicitly define a display name for a field by including it in double quotes after the field type, or by using the `as title` syntax to designate a title field.

```seed
fieldName type "Display Name"
fieldName type as title
```

When a display name is explicitly provided, it will override the automatically generated name.

## Implicit CRUD Actions

For each model defined, SeedSpec automatically provides the following actions:

*   **`create Model { ... }`:** Creates a new instance of the model and adds it to the corresponding dataset.
*   **`update modelInstance { ... }`:** Updates the specified `modelInstance`.
*   **`delete modelInstance`:** Deletes the specified `modelInstance`.

These actions can be overridden with custom logic if needed.

Status: ✓ Available
