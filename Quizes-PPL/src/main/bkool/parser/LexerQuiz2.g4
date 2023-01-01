grammar LexerQuiz2;

@lexer::header {
from lexererr import *
}

options{
	language=Python3;
}

program: EOF;

LexerInit: DIGIT+ FRACTION? EXPONENT?;

WS : [ \t\r\n]+ -> skip ; // skip spaces, tabs, newlines

ERROR_TOKEN: .
  {
    raise ErrorToken(self.text)
  }
  ;

fragment EXPONENT
  : [eE] (MINUS | PLUS)? DIGIT+
  ;

fragment DIGIT
  :[0-9]
  ;

fragment FRACTION
  :DOT? DIGIT+
  ;

fragment DOT
  : '.'
  ;

fragment MINUS
  : '-'
  ;

fragment PLUS
  : '+'
  ;

/* FLOAT_NUMBER */
/*  : POINT_FLOAT */
/*  | EXPONENT_FLOAT */
/*  ; */
/**/
/* fragment POINT_FLOAT */
/*  : INT_PART? FRACTION */
/*  | INT_PART '.' */
/*  ; */
/**/
/* fragment EXPONENT_FLOAT */
/*  : ( INT_PART | POINT_FLOAT ) EXPONENT */
/*  ; */
/**/
/* fragment INT_PART */
/*  : DIGIT+ */
/*  ; */
/**/
/* fragment FRACTION */
/*  : '.' DIGIT+ */
/*  ; */
/**/
/* fragment EXPONENT */
/*  : [eE] [+-]? DIGIT+ */
/*  ; */
