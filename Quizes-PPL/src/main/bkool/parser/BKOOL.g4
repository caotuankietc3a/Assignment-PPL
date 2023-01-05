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

vardecl
  : type variables SEMICOLON
  ;

funcdecl
  : type function_name LB function_params? RB body
  ;

body: 'body';

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

SEMICOLON
  : ';' 
  ;

COMMA
  : ',' 
  ;

ID: [a-zA-Z_] [a-zA-Z0-9_]*;

LB: '(';

RB: ')';

WS: [ \t\r\n] -> skip;

ERROR_CHAR: . {raise ErrorToken(self.text)};
