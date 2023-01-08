/* 2053166 */
grammar MT22;

@lexer::header {
from lexererr import *
}

options{
	language=Python3;
}

program: EOF ;

/* LEXICAL STRUCTURE */

// ====================== Expressions ========================


// ====================== Operators ========================

 /* ====== Arithmetic Ops ======= */
ADD: '+';
MINUS : '-';
MUL: '*';
DIV : '/';
MOD: '%';

/* ====== Logical Ops ======= */
NOT: '!';
AND: '&&';
OR: '||';

/* ====== Comparison Ops ======= */
EQ: '==';
NOT_EQ: '!=';
LT: '<';
LT_EQ: '<=';
GT: '>';
GT_EQ: '>=';

/* ====== Scope Resolution Ops ======= */
SR: '::';

// ====================== Seperators ========================
LEFT_PAREN: '(';
RIGHT_PAREN: ')';
LEFT_BRACK: '[';
RIGHT_BRACK: ']';
LEFT_BRACE: '{';
RIGHT_BRACE: '}';
COMMA: ',';
DOT: '.';
SEMI_COLON: ';';
COLON: ':';
ASSIGN: '=';
UNDERSCORE: '_';

// ====================== Literals ========================

INTEGER_LIT
  : ((NON_ZERO_DIGIT DIGIT* (UNDERSCORE DIGIT+)*) | '0')
  {
    self.text = self.text.replace('_', '')
  }
  ;

FLOAT_LIT
 : POINT_FLOAT
 | EXPONENT_FLOAT
 ;

BOOLEAN_LIT
  : TRUE 
  | FALSE
  ;

STRING_LIT
  : '"' (STR_CHAR | ESC_SEQ)* '"'
  {
    self.text = str(self.text[1:-1])
  }
  ;

fragment STR_CHAR
  : ~[\\\n]
  ;

fragment ESC_SEQ
  : '\\b'
  | '\\f'
  | '\\r'
  | '\\n'
  | '\\\\'
  | '\\\''
  | '\\t'
  ;

// Should Check
/* ARRAY_LIT */
/*   : LEFT_BRACE expr RIGHT_BRACE */
/*   ; */
/**/
/* expr */
/*   : (STRING_LIT | BOOLEAN_LIT | INTEGER_LIT) COMMA expr */
/*   | (STRING_LIT | BOOLEAN_LIT | INTEGER_LIT) */
/*   ; */

fragment POINT_FLOAT
 : INTEGER_LIT? DECIMAL
 | INTEGER_LIT '.'
 ;

fragment EXPONENT_FLOAT
 : ( INTEGER_LIT | POINT_FLOAT ) EXPONENT
 ;

fragment DECIMAL
 : '.' DIGIT+
 ;

fragment EXPONENT
 : [eE] [+-]? DIGIT+
 ;

fragment NON_ZERO_DIGIT
  : [1-9]
  ;

fragment DIGIT
  : [0-9]
  ;

// ====================== Keywords ========================
AUTO: 'auto';
BREAK: 'break';
BOOLEAN: 'boolean';
DO: 'do';
ELSE: 'else';
FALSE: 'false';
FLOAT: 'float';
FOR: 'for';
FUNCTION: 'function';
IF: 'if';
INTEGER: 'integer';
RETURN: 'return';
STRING: 'string';
TRUE: 'true';
VOID: 'void';
WHILE: 'while';
OUT: 'out';
CONTINUE: 'continue';
OF: 'of';
INHERIT: 'inherit';

// ====================== Program comment ========================

BLOCK_COMMENT
  : '/*' (.)+? '*/' -> skip
  ;

LINE_COMMENT
  : '//' ~[\n\r]* -> skip
  ;

// ====================== Identifiers ========================

ID
  : [a-zA-Z_] [a-zA-Z0-9_]*
  ;


WS : [ \b\f\t\r\n]+ -> skip ; // skip spaces, tabs, newlines

ERROR_CHAR
  : .
  {
    raise ErrorToken(self.text)
  }
  ;

UNCLOSE_STRING
  : '"' (STR_CHAR | ESC_SEQ)* (EOF | '\n')
  {
    content = str(self.text)
    esc = '\n'
    if content[-1] in esc:
      raise UncloseString(content[1:-1])
    else:
      raise UncloseString(content[1:])
  }
  ;
ILLEGAL_ESCAPE: .;
