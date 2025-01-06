# SeedSpec Compiler Pipeline

This document explains the complete pipeline of how the SeedSpec compiler transforms a `.seed` file into a React application.

## Overview

The SeedSpec compiler follows a traditional compiler pipeline pattern, with specialized stages for generating React applications. Here's a detailed breakdown of each stage:

## 1. Entry Point (cli.py)

The process begins when a user runs the compiler with a `.seed` file:

```bash
python -m seed_compiler input.seed -o output_dir
```

The CLI:
- Handles command line arguments (input .seed file, output directory)
- Reads the .seed file content
- Orchestrates the parsing and generation process
- Provides error handling and user feedback

## 2. Lexical Analysis (SeedSpec.g4 → SeedSpecLexer.py)

ANTLR4 generates a lexer from the grammar definition that performs tokenization:

- Breaks input text into tokens:
  * Keywords: `app`, `model`, `screen`
  * Identifiers: Names for apps, models, fields
  * Types: `text`, `num`, `bool`, `email`
  * Literals: Strings, numbers
  * Punctuation: Braces, semicolons

Example:
```
app Todo "Todo App" {
  model Task { ... }
}
```
Gets broken into tokens: `[APP, ID("Todo"), STRING("Todo App"), LBRACE, MODEL, ...]`

## 3. Parsing (SeedSpec.g4 → SeedSpecParser.py)

ANTLR4 generates a parser that:
- Builds a parse tree following grammar rules:
  * program → app → declarations → models/screens
  * models → fields with types and properties
  * screens → references to models
- Validates syntax according to grammar rules
- Reports syntax errors with location information

## 4. Tree Walking (antlr_parser.py)

The SeedSpecCustomVisitor walks the parse tree and converts it into a structured JSON format:

```python
{
  'name': 'Todo',
  'title': 'Todo App',
  'models': [
    {
      'name': 'Task',
      'fields': [
        {
          'name': 'title',
          'type': 'text'
        },
        {
          'name': 'done',
          'type': 'bool',
          'default': 'false'
        }
      ]
    }
  ],
  'screens': [
    {
      'name': 'Tasks',
      'model': 'Task'
    }
  ]
}
```

## 5. Code Generation (generator.py)

The generator takes the JSON structure and creates a complete React application:

### a) Setup
- Creates directory structure:
  ```
  output_dir/
  ├── public/
  │   └── index.html
  ├── src/
  │   ├── components/
  │   ├── models/
  │   ├── screens/
  │   ├── App.js
  │   └── index.js
  ├── package.json
  └── tailwind.config.js
  ```
- Configures build tools (package.json, tailwind)
- Sets up React environment

### b) Component Generation
Uses Jinja2 templates to generate:

1. App.js (App.js.tmpl):
   - Main application shell
   - Routing configuration
   - Navigation menu
   - Error boundaries

2. Model.js (Model.js.tmpl):
   - Custom React hooks for data management
   - CRUD operations
   - Local storage persistence
   - Relationship handling

3. Screen.js (Screen.js.tmpl):
   - CRUD interfaces
   - Form handling
   - Error states
   - Loading indicators
   - Responsive layout

### c) Template Processing
- Injects model/screen data into templates
- Generates proper React components
- Creates type-specific form inputs
- Sets up data relationships

## 6. Final Output

The result is a complete React application with:
- Data models with CRUD operations
- UI screens with forms
- Navigation and routing
- Error handling
- Styling (Tailwind CSS)
- Build configuration

## Running the Generated Application

```bash
cd output_dir
npm install
npm start
```

This will start a development server at http://localhost:3000 with your generated React application.
