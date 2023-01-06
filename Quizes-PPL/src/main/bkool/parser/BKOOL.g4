grammar BKOOL;

@lexer::header {
from lexererr import *
}

options{
	language=Python3;
}

program
  : declare EOF
  ;

declare
  : (funcdecl | vardecl) declare 
  | (funcdecl | vardecl)
  ; 

funcdecl
  : type function_name LB function_params? RB LCB body RCB
  ;

body
  : (vardecl | statement) body
  |
  ;

statement
  : call_statement 
  | assign_statement 
  | return_statement
  ;

assign_statement
  : ID EQUAL expr SEMICOLON
  ;

call_statement
  : function_name LB expr RB SEMICOLON
  ;

return_statement
  : RETURN expr SEMICOLON
  ;

expr
  : 'expr' COMMA expr
  | 'expr'
  ;

vardecl
  : type variables SEMICOLON
  ;

variables
  : ID COMMA variables
  | ID
  ;

function_params
  : vardecl function_params
  | type variables
  ;

type
  : INT_TYPE 
  | FLOAT_TYPE
  ;

function_name
  : ID
  ;

INT_TYPE: 'int';

FLOAT_TYPE: 'float';

RETURN: 'return';

EQUAL: '=';

SEMICOLON: ';';

COMMA: ',';

LB: '(';

RB: ')';

LCB: '{';

RCB: '}';

MINUS: '-';

PLUS: '+';

MULTIPLY: '*';

DIVIDE: '/';

ID: [a-zA-Z_] [a-zA-Z0-9_]*;

INTEGER
  : NON_ZERO_DIGIT DIGIT*
  | '0'*
  ;

FLOAT
 : POINT_FLOAT
 | EXPONENT_FLOAT
 ;

fragment NON_ZERO_DIGIT
  : [1-9]
  ;

fragment DIGIT
  : [0-9]
  ;

fragment POINT_FLOAT
 : INT_PART? FRACTION
 | INT_PART '.'
 ;

fragment EXPONENT_FLOAT
 : ( INT_PART | POINT_FLOAT ) EXPONENT
 ;

fragment INT_PART
 : DIGIT+
 ;

fragment FRACTION
 : '.' DIGIT+
 ;

fragment EXPONENT
 : [eE] [+-]? DIGIT+
 ;

WS: [ \t\r\n] -> skip;

ERROR_CHAR: . {raise ErrorToken(self.text)};
