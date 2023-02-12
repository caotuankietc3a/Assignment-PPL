grammar LexerExcercise1;

@lexer::header {
from lexererr import *
}

options{
language=Python3;
}

program: EOF;

BKNetID: NAME DOT SURNAME OPTIONAL_STRING;

fragment NAME
  : LOWERCASE_CHARACTER+
  ;

fragment SURNAME
  : LOWERCASE_CHARACTER+
  ;

fragment OPTIONAL_STRING 
  : (LOWERCASE_CHARACTER | UNDERSCORE | DIGIT | DOT)* (LOWERCASE_CHARACTER | UNDERSCORE | DIGIT)
  ;

WS : [ \t\r\n]+ -> skip ; // skip spaces, tabs, newlines

ERROR_TOKEN: .
  {
    raise ErrorToken(self.text)
  }
  ;


fragment DOT
  : '.'
  ;

fragment UNDERSCORE
: '_'
;

fragment DIGIT
: [0-9]
;

fragment LOWERCASE_CHARACTER
  : [a-z]
  ;
