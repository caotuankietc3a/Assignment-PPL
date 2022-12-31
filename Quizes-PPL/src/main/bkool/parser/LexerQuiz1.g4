grammar LexerQuiz1;

@lexer::header {
from lexererr import *
}

options{
	language=Python3;
}

program: EOF;

LexerInit: [a-z] [a-z0-9]*;

WS : [ \t\r\n]+ -> skip ; // skip spaces, tabs, newlines

ERROR_FIRST_CHARACTER: ~[a-z]
  {
    raise ErrorToken(self.text)
  }
  ;

ERROR_OTHER_CHARACTER: ~[a-z0-9]
  {
    raise ErrorToken(self.text)
  }
  ;
