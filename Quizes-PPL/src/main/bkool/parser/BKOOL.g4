grammar BKOOL;

@lexer::header {
from lexererr import *
}

options{
	language=Python3;
}

program
  : declare 
  ;

declare
  : (funcdecl | vardecl) declare 
  | (funcdecl | vardecl)
  ; 

funcdecl
  : type function_name LB function_params? RB body
  ;

body
  : LCB (vardecl | call_statement | assign_statement | return_statement)* RCB
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

INT_TYPE
  : 'int' 
  ;

FLOAT_TYPE
  : 'float' 
  ;

RETURN
  : 'return'
  ;

ID: [a-zA-Z_] [a-zA-Z0-9_]*;

SEMICOLON
  : ';' 
  ;

COMMA
  : ',' 
  ;

EQUAL
  : '='
  ;

LB: '(';

RB: ')';

LCB: '{';

RCB: '}';


WS: [ \t\r\n] -> skip;

ERROR_CHAR: . {raise ErrorToken(self.text)};
