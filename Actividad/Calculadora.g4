grammar Calculadora;

prog: expresion EOF ;
// Regla principal
expresion  : addExpr ;

addExpr    : multExpr ( ('+'|'-') multExpr )* ;        // suma/resta
multExpr   : powExpr  ( ('*'|'/') powExpr  )* ;        // multiplicación/división
powExpr    : unaryExpr ( '^' powExpr )? ;              // potencia
unaryExpr  : '-' unaryExpr        # Negacion          // negativo unario
           | primary             # Positivo
           ;

primary
    : FUNC_NAME '(' expresion ')'   # Funcion
    | '(' expresion ')'             # Parentesis
    | NUMBER                        # Numero
    ;

// Tokens
NUMBER    : [0-9]+ ('.' [0-9]+)? ;
FUNC_NAME : 'sqrt' | 'abs' | 'sin' | 'cos' | 'log' ;
WS        : [ \t\r\n]+ -> skip ;
