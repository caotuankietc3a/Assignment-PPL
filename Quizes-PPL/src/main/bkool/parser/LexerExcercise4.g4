grammar LexerExcercise4;

@lexer::header {
from lexererr import *
}

options{
language=Python3;
}

program: EOF;

SHEXA: NON_ZERO_DIGIT (ODD_CHAR | EVEN_CHAR)* EVEN_CHAR;

ERROR_TOKEN: .
  {
    raise ErrorToken(self.text)
  }
  ;


fragment EVEN_DIGIT
  : [02468]
  ;

fragment ODD_DIGIT
  : [13579]
  ;

fragment NON_ZERO_DIGIT
  : [1-9]
  ;

fragment ODD_CHAR
  : [13579bBdDfF]
  ;

fragment EVEN_CHAR
  : [02468aAcCeE]
  ;
