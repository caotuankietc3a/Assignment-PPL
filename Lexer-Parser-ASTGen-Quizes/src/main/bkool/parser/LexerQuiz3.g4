grammar LexerQuiz3;

@lexer::header {
from lexererr import *
}

options{
	language=Python3;
}

program: EOF;

LEXER_INIT: SINGLE_QUOTE STRING SINGLE_QUOTE;

WS : [ \t\r\n]+ -> skip ; // skip spaces, tabs, newlines

ERROR_TOKEN: .
  {
    raise ErrorToken(self.text)
  }
  ;

fragment STRING
  : (CHARACTER | SINGLE_QUOTE SINGLE_QUOTE)*
  ;

fragment CHARACTER
  : ~[']
  ;

fragment SINGLE_QUOTE
  : '\'' 
  ;
