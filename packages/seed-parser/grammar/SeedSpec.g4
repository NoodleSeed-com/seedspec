grammar SeedSpec;

// Top-level rule
program
  : modelDeclaration+
  ;

// Model declaration
modelDeclaration
  : 'model' IDENTIFIER '{' fieldDeclaration* '}'
  ;

// Field declaration
fieldDeclaration
  : IDENTIFIER typeName ('as' 'title')? ('=' defaultValue)? ('?')?
  ;

// Type names
typeName
  : 'text' | 'num' | 'bool'
  ;

// Default value (simplified for now)
defaultValue
  : STRING_LITERAL | NUMBER_LITERAL | BOOLEAN_LITERAL
  ;

// Identifiers, literals, etc. (tokens)
IDENTIFIER : [a-zA-Z_][a-zA-Z0-9_]*;
STRING_LITERAL : '"' .*? '"'; // Very basic string literal
NUMBER_LITERAL : [0-9]+ ('.' [0-9]+)?;
BOOLEAN_LITERAL : 'true' | 'false';
WS : [ \t\r\n]+ -> skip; // Whitespace
