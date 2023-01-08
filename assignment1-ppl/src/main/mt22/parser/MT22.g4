/* 2053166 */
grammar MT22;

options{
	language=Python3;
}

@lexer::header {
from lexererr import *
}

@lexer::members {
@property
def ids_size(self):
  try:
    return self._ids_size
  except AttributeError: 
    self._ids_size = 0
    return self._ids_size

@property
def exprs_size(self):
  try:
    return self._exprs_size
  except AttributeError:
    self._exprs_size = 0
    return self._exprs_size
}

program: EOF ;



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
  : ~[\\\n"]
  ;

fragment ESC_SEQ
  : '\\b'
  | '\\f'
  | '\\r'
  | '\\n'
  | '\\\\'
  | '\\\''
  | '\\t'
  | '\\"'
  | '\'"'
  ;

fragment ESC_ERR
  : '\\' ~[bfrnt\\']
  | '\'' ~'"'
  ;

// Should Check
array_lit
  : LEFT_BRACE exprs RIGHT_BRACE
  ;


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

// ====================== Expressions ========================
exprs
  : 'exprs' COMMA exprs {self.exprs_size += 1}
  | 'exprs' {self.exprs_size += 1}
  ;

// ====================== Declarations ========================
///////////////////////////////////// Start test //////////////////////////

/* Variable declarations */
variable_decl
  : identifiers_list COLON (((atomic_type | array_type) ASSIGN exprs?) | (auto_type ASSIGN exprs)) SEMI_COLON
  {
    if self.exprs_size != self.ids_size:
      self.skip()
  }
  ;

identifiers_list
  : ID COMMA {self.ids_size += 1}
  | ID {self.ids_size += 1}
  ;

/* Function declaratinons */
parameter_decl
  : OUT? ID COLON (atomic_type | array_type | auto_type)
  ;

///////////////////////////////////// End test //////////////////////////


// ====================== Type system and values ========================
///////////////////////////////////// Start test //////////////////////////

/* Atomic types */
boolean_type: BOOLEAN; 
int_type: INT;
float_type: FLOAT;
string_type: STRING;
void_type: VOID;
auto_type: AUTO;
array_type: ARRAY dimensions OF atomic_type;
dimensions: LEFT_BRACK INTEGER_LIT (COMMA INTEGER_LIT)* RIGHT_BRACK;
atomic_type
  : boolean_type
  | int_type
  | float_type
  | string_type
  ;

///////////////////////////////////// End test //////////////////////////

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
INT: 'int';
RETURN: 'return';
STRING: 'string';
TRUE: 'true';
ARRAY: 'array';
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

ILLEGAL_ESCAPE
  : '"' (STR_CHAR | ESC_SEQ)* ESC_ERR
  {
    raise IllegalEscape(str(self.text[1:]))
  }
  ;
