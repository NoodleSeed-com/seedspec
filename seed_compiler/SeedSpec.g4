grammar SeedSpec;

// Top-level Parser Rules
// The entry point of the grammar - a program consists of a single app definition followed by end of file
program: app EOF;

// An app has a name identifier, a title string, and contains multiple declarations inside curly braces
app: APP name=ID title=STRING '{' declaration* '}';

// A declaration can be either a model or screen definition - this allows mixing them in any order
declaration
    : model
    | screen
    ;

// A model defines a data structure with a name and contains multiple field definitions
model: MODEL name=ID '{' field* '}';

// A field has a name, type, optional role (using AS), and optional default value
// The # BasicField label allows targeting this rule specifically in visitors/listeners
field
    : name=ID type=TYPE (AS role=ID)? ('=' default=VALUE)? ';' # BasicField
    ;

// A screen represents a UI view, associated with a specific model through the USING keyword
screen: SCREEN name=ID USING modelRef=ID ';';

// Lexer Rules - Define the vocabulary of our language

// Keywords - Must be defined before ID to take precedence
APP: 'app';                    // Keyword for declaring an application
MODEL: 'model';                // Keyword for declaring a data model
SCREEN: 'screen';              // Keyword for declaring a screen/view
USING: 'using';                // Keyword for associating screens with models
AS: 'as';                      // Keyword for aliasing/roles

// Built-in types supported by the language
TYPE: 'text' | 'num' | 'bool' | 'email';

// String literals - anything between double quotes except newlines
STRING: '"' (~["\r\n])* '"';

// Number literals - integers and decimals
NUMBER: DIGIT+ ('.' DIGIT+)?;

// Values that can be used as defaults - booleans, numbers, or strings
VALUE
    : 'true'                   // Boolean true
    | 'false'                  // Boolean false
    | NUMBER                   // Numeric values
    | STRING                   // String values
    ;

// Identifiers - start with letter, can contain letters and digits
ID: LETTER (LETTER | DIGIT)*;

// Fragment rules - building blocks for other lexer rules
fragment LETTER: [a-zA-Z];     // Basic letter definition
fragment DIGIT: [0-9];         // Basic digit definition

// Punctuation
SEMICOLON: ';';                // Statement terminator

// Whitespace and comment handling
NEWLINE: [\r\n]+ -> channel(HIDDEN);    // Hide newlines from parser
WS: [ \t]+ -> channel(HIDDEN);          // Hide whitespace from parser
COMMENT: '//' ~[\r\n]* -> skip;         // Skip single-line comments
