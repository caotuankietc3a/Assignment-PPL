/* 2053166 */
grammar MT22;

options{
	language=Python3;
}

@lexer::header {
from lexererr import *
}

@parser::members {
@property
def ids_size(self):
    try:
        return self._ids_size
    except AttributeError: 
        self._ids_size = -1
        return self._ids_size

@property
def exprs_size(self):
    try:
        return self._exprs_size
    except AttributeError:
        self._exprs_size = -1
        return self._exprs_size

@ids_size.setter
def ids_size(self, value):
    self._ids_size = value

@exprs_size.setter
def exprs_size(self, value):
    self._exprs_size = value
}

program: decls EOF ;

decls
  : decl decls
  | decl
  ;

decl
  : variable_decl 
  | function_decl
  ;


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
  : (POINT_FLOAT | EXPONENT_FLOAT)
  {
    self.text = self.text.replace('_', '')
  }
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

array_lit
  : LEFT_BRACE exprs_list? RIGHT_BRACE
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


// ====================== Declarations ========================

// Don't make spaces with python codes
variable_decl
  : identifiers_list COLON (((atomic_type | array_type) (ASSIGN exprs_list_var_decl)?) | (auto_type ASSIGN exprs_list_var_decl))
  {
if self.exprs_size != -1 and self.exprs_size != self.ids_size: 
    raise RecognitionException()
self.ids_size = -1
self.exprs_size = -1
}
  SEMI_COLON
  ;

identifiers_list: ID {self.ids_size += 2} (COMMA ID{self.ids_size += 1})*;

function_decl
  : ID COLON FUNCTION (atomic_type | void_type | auto_type) LEFT_PAREN params_list? RIGHT_PAREN (INHERIT ID)? body
  ;

params_list
  : parameter_decl COMMA params_list
  | parameter_decl
  ;

parameter_decl
  : INHERIT? OUT? ID COLON (atomic_type | array_type | auto_type)
  ;

body: block_stmt;

// ====================== Expressions ========================
expr
  : string_expr
  ;

string_expr
  : string_expr SR relational_expr 
  | relational_expr
  ;

relational_expr
  : logical_expr_1 (EQ | NOT_EQ | GT | LT | LT_EQ | GT_EQ) logical_expr_1
  | logical_expr_1
  ;

logical_expr_1
  : logical_expr_1 (AND | OR) adding_expr
  | adding_expr
  ;

adding_expr
  : adding_expr (ADD | MINUS) multiplying_expr
  | multiplying_expr
  ;

multiplying_expr
  : multiplying_expr (MUL | DIV | MOD) logical_expr_2
  | logical_expr_2
  ;

logical_expr_2
  : NOT logical_expr_2
  | sign_expr
  ;

sign_expr
  : MINUS sign_expr
  | index_expr
  ;

index_expr
  : index_expr index_operator
  | operand_expr
  ;

index_operator
  : LEFT_BRACK exprs_list RIGHT_BRACK
  ;

operand_expr
  : operand
  | LEFT_PAREN expr RIGHT_PAREN
  ;

operand
  : literal
  | func_call
  | ID
  ;

func_call: ID LEFT_PAREN exprs_list? RIGHT_PAREN;

literal
  : INTEGER_LIT
  | FLOAT_LIT
  | BOOLEAN_LIT
  | STRING_LIT
  | array_lit
  ;

exprs_list_var_decl
  : expr {self.exprs_size += 1} COMMA exprs_list_var_decl
  | expr {self.exprs_size += 2}
  ;

exprs_list
  : expr COMMA exprs_list 
  | expr
  ;

// ====================== Statements ========================

statements_list
  : (statement | variable_decl) statements_list
  | (statement | variable_decl)
  ;

statement
  : assign_stmt
  | if_stmt
  | for_stmt
  | while_stmt
  | do_while_stmt
  | break_stmt
  | continue_stmt
  | return_stmt
  | call_stmt
  | block_stmt
  ;

assign_stmt
  : assign_stmt_lhs ASSIGN assign_stmt_rhs SEMI_COLON
  ;

assign_stmt_lhs
  : scalar_var 
  | ID index_operator
  ;

assign_stmt_rhs: expr;

if_stmt
  : IF LEFT_PAREN expr RIGHT_PAREN statement (ELSE statement)?
  ;

for_stmt
  : FOR LEFT_PAREN init_expr COMMA condition_expr COMMA update_expr RIGHT_PAREN statement
  ;

init_expr: scalar_var ASSIGN expr;

condition_expr: expr;

update_expr: expr;

while_stmt
  : WHILE LEFT_PAREN expr RIGHT_PAREN statement
  ;

do_while_stmt: DO block_stmt WHILE LEFT_PAREN expr RIGHT_PAREN SEMI_COLON;

break_stmt: BREAK SEMI_COLON;

continue_stmt: CONTINUE SEMI_COLON;

return_stmt: RETURN expr? SEMI_COLON;

call_stmt: func_call SEMI_COLON;

block_stmt: LEFT_BRACE statements_list? RIGHT_BRACE;

scalar_var: ID;


// ====================== Type system and values ========================
boolean_type: BOOLEAN; 

int_type: INTEGER;

float_type: FLOAT;

string_type: STRING;

void_type: VOID;

auto_type: AUTO;

array_type: ARRAY LEFT_BRACK dimensions RIGHT_BRACK OF atomic_type;

dimensions: INTEGER_LIT (COMMA INTEGER_LIT)* ;

atomic_type
  : boolean_type
  | int_type
  | float_type
  | string_type
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

ERROR_CHAR
  : .
  {
    raise ErrorToken(self.text)
  }
  ;
