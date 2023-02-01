grammar BKOOL;

@lexer::header {
from lexererr import *
}

options{
	language=Python3;
}

/* program: exp EOF; */
/**/
/* exp: term ASSIGN exp | term; */
/**/
/* term: factor COMPARE factor | factor; */
/**/
/* factor: factor ANDOR operand | operand; */
/**/
/* operand: ID | INTLIT | BOOLIT | '(' exp ')'; */
/**/
/* INTLIT: [0-9]+ ; */
/**/
/* BOOLIT: 'True' | 'False' ; */
/**/
/* ANDOR: 'and' | 'or' ; */
/**/
/* ASSIGN: '+=' | '-=' | '&=' | '|=' | ':=' ; */
/**/
/* COMPARE: '=' | '<>' | '>=' | '<=' | '<' | '>' ; */
/**/
/* ID: [a-z]+ ; */

program: vardecl+ EOF;

vardecl: mptype ids ';' ;

mptype: INTTYPE | FLOATTYPE;

ids: ID (',' ID)*;

INTTYPE: 'int';

FLOATTYPE: 'float';

ID: [a-z]+ ;

WS: [ \t\r\n] -> skip;

ERROR_CHAR: . {raise ErrorToken(self.text)};
