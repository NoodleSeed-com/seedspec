# SeedSpec Core Concepts

This document outlines the minimal core concepts and structure of the SeedSpec language.

## Core Elements

- **Models**: Define data structures with typed fields
- **Screens**: Auto-generated CRUD interfaces for models

## Data Types

- **text**: Represents text values
- **num**: Represents numeric values  
- **bool**: Represents true/false values

## Grammar in BNF Form

```bnf
<spec> ::= <model>* <screen>*

<model> ::= "model" <identifier> "{" <field>* "}"
<field> ::= <identifier> <type> ["=" <literal>]

<screen> ::= "screen" <identifier> ["using" <identifier>]

<type> ::= "text" | "num" | "bool"
<identifier> ::= <letter> (<letter> | <digit> | "_")*
<literal> ::= <string> | <number> | "true" | "false"
```

## Example

```seed
model Task {
  title text
  done bool = false
}

screen Tasks using Task
```

This minimal specification provides:

- Basic data modeling with three core types
- Implicit CRUD operations for all models
- Auto-generated UI screens
- Basic data persistence

Additional features like validation, relationships, custom actions, workflows, and styling can be added incrementally as the language matures.
