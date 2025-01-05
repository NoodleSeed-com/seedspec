# SeedSpec Grammar Structure

```
Program Structure
================
program
   └── app
       ├── name (ID)
       ├── title (STRING)
       └── declarations
           ├── model*
           │   ├── name (ID)
           │   └── fields*
           │       ├── name (ID)
           │       ├── type (TYPE)
           │       ├── role? (AS ID)
           │       └── default? (VALUE)
           │
           └── screen*
               ├── name (ID)
               └── modelRef (USING ID)

Lexical Elements
===============
Keywords                 Types                   Values
--------                 -----                   ------
APP ('app')             'text'                  STRING (quoted text)
MODEL ('model')         'num'                   NUMBER (digits + optional decimal)
SCREEN ('screen')       'bool'                  'true'/'false'
USING ('using')         'email'
AS ('as')

Identifiers            Special Characters       Hidden Elements
-----------           ------------------       ---------------
ID                    SEMICOLON (';')         NEWLINE
└── [a-zA-Z]          STRING_QUOTE ('"')      WHITESPACE
    [a-zA-Z0-9]*                             COMMENTS (//)

Flow of Parsing
==============
1. Lexical Analysis
   └── Input text → Tokens (using Lexer rules)
       
2. Syntactic Analysis
   └── Tokens → Parse Tree (using Parser rules)
       
3. Semantic Processing
   └── Parse Tree → AST → Code Generation

Example Structure
===============
app TodoApp "Todo Application" {
    model Task {              // Model declaration
        title text;           // Basic field
        done bool = false;    // Field with default
        dueDate text as date; // Field with role
    }
    
    screen TaskList using Task;  // Screen declaration
}
```

## Key Concepts

1. **Hierarchical Structure**
   - Every program must have exactly one app
   - Apps can have multiple models and screens
   - Models contain fields with types and optional attributes

2. **Type System**
   - Built-in primitive types (text, num, bool, email)
   - Type roles for semantic meaning (using AS keyword)
   - Default values for initialization

3. **UI Integration**
   - Screens are tied to models via USING relationship
   - This enables automatic UI generation based on model structure

4. **Lexical Design**
   - Keywords are reserved and case-sensitive
   - Identifiers follow standard naming conventions
   - Whitespace and comments are ignored in parsing

## Compilation Pipeline

1. **Grammar Definition (ANTLR4)**
   - Uses ANTLR4 grammar specification (SeedSpec.g4)
   - Defines lexical and syntactic rules
   - ANTLR4 generates Python lexer and parser classes

2. **Lexical Analysis (ANTLR4 Generated Lexer)**
   - Input: Raw text of SeedSpec DSL
   - Process: Breaks input into tokens using SeedSpecLexer
   - Output: Stream of tokens (identifiers, keywords, etc.)
   - Libraries: antlr4-python3-runtime
   - Key Components:
     * CommonTokenStream for token management
     * Custom error listeners for detailed error reporting

3. **Syntactic Analysis (ANTLR4 Generated Parser)**
   - Input: Token stream from lexer
   - Process: Builds parse tree using SeedSpecParser
   - Output: Abstract Syntax Tree (AST)
   - Libraries: antlr4-python3-runtime
   - Key Components:
     * SeedSpecCustomVisitor for tree traversal
     * ParseTreeWalker for walking the parse tree
     * Custom error handling for syntax errors

4. **Code Generation (Custom Generator)**
   - Input: Parsed AST representation
   - Process: Transforms AST into React application code
   - Output: Complete React application structure
   - Libraries:
     * Jinja2 for template rendering
     * Built-in Python libraries (os, json)
   - Generated Components:
     * React components (using templates)
     * Model definitions
     * Screen components
     * Configuration files (package.json, tailwind config)
     * Project structure setup

## Generated Application Stack

1. **Frontend Framework**
   - React (^17.0.2)
   - React Router (^5.2.0)
   - React Scripts (^5.0.1)

2. **Styling**
   - Tailwind CSS (^3.3.0)
   - @tailwindcss/forms (^0.5.3)
   - PostCSS (^8.4.21)
   - Autoprefixer (^10.4.14)

3. **Project Structure**
   ```
   generated-app/
   ├── public/
   │   └── index.html
   ├── src/
   │   ├── components/
   │   │   └── ErrorBoundary.js
   │   ├── models/
   │   │   └── [Generated Model Files]
   │   ├── screens/
   │   │   └── [Generated Screen Components]
   │   ├── App.js
   │   ├── index.js
   │   └── index.css
   ├── package.json
   ├── postcss.config.js
   └── tailwind.config.js
   ```
