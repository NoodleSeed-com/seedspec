grammar SeedSpec;

// Parser Rules
program
    : declaration* EOF
    ;

declaration
    : appDeclaration
    | modelDeclaration
    | dataDeclaration
    | screenDeclaration
    | actionDeclaration
    ;

appDeclaration
    : 'app' IDENTIFIER STRING_LITERAL '{' declaration* '}'
    ;

modelDeclaration
    : 'model' IDENTIFIER '{' fieldDeclaration* '}'
    ;

fieldDeclaration
    : IDENTIFIER typeName ('as' 'title')? ('=' defaultValue)? ('?')?
    | IDENTIFIER 'in' '[' IDENTIFIER (',' IDENTIFIER)* ']' ('=' IDENTIFIER)?
    ;

dataDeclaration
    : 'data' '{' datasetDeclaration* '}'
    ;

datasetDeclaration
    : IDENTIFIER ':' IDENTIFIER '[]' '[' dataInstance (',' dataInstance)* ']'
    ;

dataInstance
    : '{' (dataValue (',' dataValue)*)? '}'
    ;

dataValue
    : IDENTIFIER ':' value
    | value
    ;

screenDeclaration
    : 'screen' IDENTIFIER
    ;

actionDeclaration
    : 'action' IDENTIFIER '(' parameterList? ')' '{' actionStatement* '}'
    ;

parameterList
    : parameter (',' parameter)*
    ;

parameter
    : IDENTIFIER ':' typeName ('?')?
    ;

actionStatement
    : 'create' IDENTIFIER '{' fieldAssignment (',' fieldAssignment)* '}'
    ;

fieldAssignment
    : IDENTIFIER ':' IDENTIFIER
    ;

// Type names
typeName
    : 'text'
    | 'num'
    | 'bool'
    | 'date'
    | IDENTIFIER
    ;

// Values
value
    : STRING_LITERAL
    | NUMBER_LITERAL
    | BOOLEAN_LITERAL
    | DATE_LITERAL
    | IDENTIFIER '[' NUMBER_LITERAL ']'
    ;

defaultValue
    : STRING_LITERAL
    | NUMBER_LITERAL
    | BOOLEAN_LITERAL
    | DATE_LITERAL
    | IDENTIFIER
    ;

// Lexer Rules
IDENTIFIER : [a-zA-Z_][a-zA-Z0-9_]*;
STRING_LITERAL : '"' (~["\r\n])* '"';
NUMBER_LITERAL : '-'? [0-9]+ ('.' [0-9]+)?;
BOOLEAN_LITERAL : 'true' | 'false';
DATE_LITERAL : [0-9][0-9][0-9][0-9] '-' [0-9][0-9] '-' [0-9][0-9];
WS : [ \t\r\n]+ -> skip;
COMMENT : '//' ~[\r\n]* -> skip;
