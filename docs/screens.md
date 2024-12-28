# Screens

Define application screens/pages in SeedSpec. SeedSpec automatically generates CRUD (Create, Read, Update, Delete) screens for each model defined in the application. These screens provide a basic interface for managing instances of the model.

## Implicit Screen Generation

For each model, a screen named `Manage<ModelName>` is implicitly generated. For example, for a `Todo` model, a `ManageTodos` screen is automatically created. This screen provides a default UI for performing CRUD operations on the model's data.

## Explicitly Requesting Implicit Screens

You can explicitly request the use of an implicit screen using the following syntax:

```seed
screen Name using Model
```

For example:

```seed
screen Todos using Todo
```

This is useful when you want to customize the screen or when the screen name doesn't match the dataset name.

## Model Inference from Dataset

If a screen is named after a dataset (e.g., `screen Todos`), and that dataset is explicitly typed in the `data` block (e.g., `Todos: Todo[]`), the screen will automatically infer the associated model (`Todo` in this case) and use the implicit CRUD screen for that model.

**Example:**

```seed
model Todo {
  title text as title
  completed bool = false
}

data {
  Todos: Todo[] [
    { title: "Task 1", completed: false },
    { title: "Task 2", completed: true }
  ]
}

screen Todos // Implicitly uses the 'Todo' model and provides the CRUD interface
```

## Customizing Implicit Screens

You can customize an implicitly generated screen by defining a `screen` with the same name. You can add custom components, actions, or override the default layout.

**Example:**

```seed
screen Todos {
  button "Add Todo" -> MyCustomAddAction
}
```

This adds a custom button to the `Todos` screen while retaining the rest of the default CRUD interface.

Status: ✓ Available
