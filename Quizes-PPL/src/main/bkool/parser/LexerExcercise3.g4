grammar LexerExcercise3;

@lexer::header {
from lexererr import *
}

options{
language=Python3;
}

program: EOF;

PHPINTs: ((NON_ZERO_DIGIT (UNDERSCORE | DIGIT)*) | '0')
  {
    self.text = self.text.replace('_', '')
  }
  ;

ERROR_TOKEN: .
  {
    raise ErrorToken(self.text)
  }
  ;


fragment DIGIT
  : [0-9]
  ;

fragment NON_ZERO_DIGIT
  : [1-9]
  ;

fragment UNDERSCORE
  : '_'
  ;
