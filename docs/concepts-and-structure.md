# Basic Concepts

This document outlines the basic concepts and structure of the SeedSpec language.

## Core Elements

-   **Models**: Define the data structures and their relationships.
-   **Screens**: Represent the user interface components and layouts.
-   **Workflows**: Describe the interactions and data flow between screens and models.
-   **Actions**: Define operations that can be performed on models or screens.

## Data Types

-   **String**: Represents text.
-   **Number**: Represents numeric values.
-   **Boolean**: Represents true/false values.
-   **Object**: Represents a collection of key-value pairs.
-   **Array**: Represents an ordered list of values.

## Grammar in BNF Form

```bnf
<spec> ::= <model_definitions> <screen_definitions> <workflow_definitions>

<model_definitions> ::= <model> | <model> <model_definitions>
<model> ::= "model" <identifier> "{" <model_body> "}"
<model_body> ::= <field> | <field> <model_body>
<field> ::= <identifier> ":" <type>

<screen_definitions> ::= <screen> | <screen> <screen_definitions>
<screen> ::= "screen" <identifier> "{" <screen_body> "}"
<screen_body> ::= <component> | <component> <screen_body>
<component> ::= <identifier> ":" <component_type>

<workflow_definitions> ::= <workflow> | <workflow> <workflow_definitions>
<workflow> ::= "workflow" <identifier> "{" <workflow_body> "}"
<workflow_body> ::= <action> | <action> <workflow_body>
<action> ::= "action" <identifier> "{" <action_body> "}"
<action_body> ::= <statement> | <statement> <action_body>

<type> ::= "String" | "Number" | "Boolean" | "Object" | "Array"
<component_type> ::= "Text" | "Button" | "Input" | "List" | "Image"

<identifier> ::= <letter> { <letter> | <digit> | "_" }
<letter> ::= "a" | "b" | ... | "z" | "A" | "B" | ... | "Z"
<digit> ::= "0" | "1" | ... | "9"
<statement> ::= <assignment> | <conditional> | <loop>
<assignment> ::= <identifier> "=" <expression>
<conditional> ::= "if" "(" <expression> ")" "{" <statement> "}" [ "else" "{" <statement> "}" ]
<loop> ::= "for" "(" <identifier> "in" <expression> ")" "{" <statement> "}"
<expression> ::= <identifier> | <literal> | <expression> <operator> <expression>
<literal> ::= <string_literal> | <number_literal> | <boolean_literal>
<string_literal> ::= '"' { <character> } '"'
<number_literal> ::= <digit> { <digit> }
<boolean_literal> ::= "true" | "false"
<operator> ::= "+" | "-" | "*" | "/" | "==" | "!=" | "<" | ">" | "<=" | ">="
