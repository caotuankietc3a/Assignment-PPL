grammar LexerExcercise1;

@lexer::header {
from lexererr import *
}

options{
language=Python3;
}

program: EOF;

IPV4: STRING DOT STRING DOT STRING DOT STRING;

ERROR_TOKEN: .
  {
    raise ErrorToken(self.text)
  }
  ;

fragment STRING
  : '0' 
  | NON_ZERO_DIGIT DIGIT?
  | '1' DIGIT? DIGIT?
  | '2' [0-4]? DIGIT?
  | '25' [0-5]? 
  ;

fragment DOT
  : '.'
  ;

fragment DIGIT
  : [0-9]
  ;

fragment NON_ZERO_DIGIT
  : [1-9]
  ;

