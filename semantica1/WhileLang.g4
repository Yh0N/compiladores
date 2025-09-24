grammar WhileLang;

program: statement+ EOF;

statement
    : declaration
    | assignment
    | whileStatement
    | ifStatement
    | breakStatement
    | continueStatement
    ;

declaration
    : type ID ASSIGN expr SEMI
    | type ID SEMI
    ;

assignment
    : ID ASSIGN expr SEMI
    ;

whileStatement
    : WHILE LPAREN condition RPAREN LBRACE statement* RBRACE
    ;

ifStatement
    : IF LPAREN condition RPAREN LBRACE statement* RBRACE (ELSE LBRACE statement* RBRACE)?
    ;

breakStatement
    : BREAK SEMI
    ;

continueStatement
    : CONTINUE SEMI
    ;

// ===== CAMBIO: ahora permite 'expr' sola o 'expr op expr'
condition
    : expr (operator expr)?
    ;

expr
    : ID
    | NUMBER
    | STRING
    | expr (PLUS | MINUS | MULT | DIV) expr
    ;

operator
    : GT | LT | EQ | NE
    ;

type
    : INT
    | STRING_T
    ;

INT: 'int';
STRING_T: 'string';

WHILE: 'while';
IF: 'if';
ELSE: 'else';
BREAK: 'break';
CONTINUE: 'continue';

PLUS: '+';
MINUS: '-';
MULT: '*';
DIV: '/';

GT: '>';
LT: '<';
EQ: '==';
NE: '!=';

ASSIGN: '=';
SEMI: ';';
LPAREN: '(';
RPAREN: ')';
LBRACE: '{';
RBRACE: '}';

ID: [a-zA-Z_][a-zA-Z_0-9]*;
NUMBER: [0-9]+;
STRING: '"' (~["\\] | '\\' .)* '"';

WS: [ \t\r\n]+ -> skip;