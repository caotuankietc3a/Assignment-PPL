from MT22Visitor import MT22Visitor
from MT22Parser import MT22Parser
from AST import *


class ASTGeneration(MT22Visitor):
    # program: decls EOF ;
    def visitProgram(self, ctx: MT22Parser.ProgramContext):
        return Program(ctx.decls().accept(self))

    # decls: decl decls | decl;
    def visitDecls(self, ctx: MT22Parser.DeclsContext):
        return [*ctx.decl().accept(self), *ctx.decls().accept(self)] if ctx.getChildCount() == 2 else ctx.decl().accept(self)

    # decl: variable_decl | function_decl;
    def visitDecl(self, ctx: MT22Parser.DeclContext):
        return ctx.getChild(0).accept(self)

    # array_lit: LEFT_BRACE exprs_list? RIGHT_BRACE;
    def visitArray_lit(self, ctx: MT22Parser.Array_litContext):
        return ArrayLit(ctx.exprs_list().accept(self) if ctx.exprs_list() else [])

    # variable_decl: identifiers_list COLON (((atomic_type | array_type) (ASSIGN exprs_list_var_decl)?) | (auto_type ASSIGN exprs_list_var_decl)) SEMI_COLON;
    def visitVariable_decl(self, ctx: MT22Parser.Variable_declContext):
        if not ctx.exprs_list_var_decl():
            return [str(VarDecl(id, ctx.getChild(2).accept(self), None)) for id in ctx.identifiers_list().accept(self)]

        return [str(VarDecl(id, ctx.getChild(2).accept(self), expr)) for id, expr in zip(ctx.identifiers_list().accept(self), ctx.exprs_list_var_decl().accept(self))]

    # identifiers_list: ID (COMMA ID)*;
    def visitIdentifiers_list(self, ctx: MT22Parser.Identifiers_listContext):
        return [Id(x.getText()) for x in ctx.ID()]

    # function_decl: ID COLON FUNCTION (atomic_type | void_type | auto_type) LEFT_PAREN params_list? RIGHT_PAREN (INHERIT ID)? body;
    def visitFunction_decl(self, ctx: MT22Parser.Function_declContext):
        return [FuncDecl(Id(ctx.ID(0).getText()), ctx.getChild(3).accept(self), ctx.params_list().accept(self) if ctx.params_list() else [], ctx.INHERIT().getText() if ctx.INHERIT() else ctx.INHERIT(), ctx.body().accept(self))]

    # params_list : parameter_decl COMMA params_list | parameter_decl ;
    def visitParams_list(self, ctx: MT22Parser.Params_listContext):
        return [ctx.parameter_decl().accept(self), *ctx.params_list().accept(self)] if ctx.getChildCount() == 3 else [ctx.parameter_decl().accept(self)]

    # parameter_decl : INHERIT? OUT? ID COLON (atomic_type | array_type | auto_type) ;
    def visitParameter_decl(self, ctx: MT22Parser.Parameter_declContext):
        return ParamDecl(Id(ctx.ID().getText()), ctx.getChild(ctx.getChildCount() - 1).accept(self), True if ctx.OUT() else False, True if ctx.INHERIT() else False)

    # body: block_stmt;
    def visitBody(self, ctx: MT22Parser.BodyContext):
        return ctx.block_stmt().accept(self)

    # expr : string_expr ;
    def visitExpr(self, ctx: MT22Parser.ExprContext):
        return ctx.string_expr().accept(self)

    # string_expr : string_expr SR relational_expr | relational_expr ;
    def visitString_expr(self, ctx: MT22Parser.String_exprContext):
        return BinExpr(ctx.SR().getText(), ctx.relational_expr(0).accept(self), ctx.relational_expr(1).accept(self)) if ctx.getChildCount() == 3 else ctx.relational_expr(0).accept(self)

    # relational_expr : logical_expr_1 (EQ | NOT_EQ | GT | LT | LT_EQ | GT_EQ) logical_expr_1 | logical_expr_1 ;
    def visitRelational_expr(self, ctx: MT22Parser.Relational_exprContext):
        return BinExpr(ctx.getChild(1).getText(), ctx.logical_expr_1(0).accept(self), ctx.logical_expr_1(1).accept(self)) if ctx.getChildCount() == 3 else ctx.logical_expr_1(0).accept(self)

    # logical_expr_1 : logical_expr_1 (AND | OR) adding_expr | adding_expr ;
    def visitLogical_expr_1(self, ctx: MT22Parser.Logical_expr_1Context):
        return BinExpr(ctx.getChild(1).getText(), ctx.logical_expr_1().accept(self), ctx.adding_expr().accept(self)) if ctx.getChildCount() == 3 else ctx.adding_expr().accept(self)

    # adding_expr : adding_expr (ADD | MINUS) multiplying_expr | multiplying_expr ;
    def visitAdding_expr(self, ctx: MT22Parser.Adding_exprContext):
        return BinExpr(ctx.getChild(1).getText(), ctx.adding_expr().accept(self), ctx.multiplying_expr().accept(self)) if ctx.getChildCount() == 3 else ctx.multiplying_expr().accept(self)

    # multiplying_expr : multiplying_expr (MUL | DIV | MOD) logical_expr_2 | logical_expr_2 ;
    def visitMultiplying_expr(self, ctx: MT22Parser.Multiplying_exprContext):
        return BinExpr(ctx.getChild(1).getText(), ctx.multiplying_expr().accept(self), ctx.logical_expr_2().accept(self)) if ctx.getChildCount() == 3 else ctx.logical_expr_2().accept(self)

    # logical_expr_2 : NOT logical_expr_2 | sign_expr ;
    def visitLogical_expr_2(self, ctx: MT22Parser.Logical_expr_2Context):
        return UnExpr(ctx.NOT().getText(), ctx.logical_expr_2().accept(self)) if ctx.getChildCount() == 2 else ctx.sign_expr().accept(self)

    # sign_expr : MINUS sign_expr | index_expr ;
    def visitSign_expr(self, ctx: MT22Parser.Sign_exprContext):
        return UnExpr(ctx.MINUS().getText(), ctx.sign_expr().accept(self)) if ctx.getChildCount() == 2 else ctx.index_expr().accept(self)

    # index_expr : index_expr index_operator | operand_expr ;
    def visitIndex_expr(self, ctx: MT22Parser.Index_exprContext):
        return ArrayCell(ctx.index_expr().accept(self), ctx.index_operator().accept(self)) if ctx.getChildCount() == 2 else ctx.operand_expr().accept(self)

    # index_operator : LEFT_BRACK exprs_list RIGHT_BRACK ;
    def visitIndex_operator(self, ctx: MT22Parser.Index_operatorContext):
        return ctx.exprs_list().accept(self)

    # operand_expr : operand | LEFT_PAREN expr RIGHT_PAREN ;
    def visitOperand_expr(self, ctx: MT22Parser.Operand_exprContext):
        return ctx.expr().accept(self) if ctx.getChildCount() == 3 else ctx.operand().accept(self)

    # operand : literal | func_call | ID ;
    def visitOperand(self, ctx: MT22Parser.OperandContext):
        if ctx.ID():
            return Id(ctx.ID().getText())

        if ctx.func_call():
            return ctx.func_call().accept(self)[0]

        return ctx.literal().accept(self)

    # func_call: ID LEFT_PAREN exprs_list? RIGHT_PAREN;
    def visitFunc_call(self, ctx: MT22Parser.Func_callContext):
        id = Id(ctx.ID().getText())
        exprs_list = ctx.exprs_list().accept(self) if ctx.exprs_list() else []
        return [FuncCall(id, exprs_list), id, exprs_list]

    # literal : INTEGER_LIT | FLOAT_LIT | BOOLEAN_LIT | STRING_LIT | array_lit ;
    def visitLiteral(self, ctx: MT22Parser.LiteralContext):
        if ctx.INTEGER_LIT():
            return IntegerLit(ctx.getChild(0).getText())

        if ctx.FLOAT_LIT():
            return FloatLit(ctx.getChild(0).getText())

        if ctx.STRING_LIT():
            return StringLit(ctx.getChild(0).getText())

        if ctx.BOOLEAN_LIT():
            return BooleanLit(ctx.getChild(0).getText())

        if ctx.array_lit():
            return ctx.getChild(0).accept(self)

    # exprs_list_var_decl : expr COMMA exprs_list_var_decl | expr ;
    def visitExprs_list_var_decl(self, ctx: MT22Parser.Exprs_list_var_declContext):
        return [ctx.expr().accept(self), *ctx.exprs_list_var_decl().accept(self)] if ctx.getChildCount() == 3 else [ctx.expr().accept(self)]

    # exprs_list : expr COMMA exprs_list | expr ;
    def visitExprs_list(self, ctx: MT22Parser.Exprs_listContext):
        return [ctx.expr().accept(self), *ctx.exprs_list().accept(self)] if ctx.getChildCount() == 3 else [ctx.expr().accept(self)]

    # statements_list : (statement | variable_decl) statements_list | (statement | variable_decl) ;
    def visitStatements_list(self, ctx: MT22Parser.Statements_listContext):
        if ctx.variable_decl():
            return [*ctx.variable_decl().accept(self), *ctx.statements_list().accept(self)] if ctx.getChildCount() == 2 else ctx.variable_decl().accept(self)

        return [ctx.statement().accept(self), *ctx.statements_list().accept(self)] if ctx.getChildCount() == 2 else [ctx.statement().accept(self)]

    # statement : assign_stmt | if_stmt | for_stmt | while_stmt | do_while_stmt | break_stmt | continue_stmt | return_stmt | call_stmt | block_stmt ;
    def visitStatement(self, ctx: MT22Parser.StatementContext):
        return ctx.getChild(0).accept(self)

    # assign_stmt : assign_stmt_lhs ASSIGN assign_stmt_rhs SEMI_COLON ;
    def visitAssign_stmt(self, ctx: MT22Parser.Assign_stmtContext):
        return AssignStmt(ctx.assign_stmt_lhs().accept(self), ctx.assign_stmt_rhs().accept(self))

    # assign_stmt_lhs : scalar_var | ID index_operator ;
    def visitAssign_stmt_lhs(self, ctx: MT22Parser.Assign_stmt_lhsContext):
        return ArrayCell(Id(ctx.ID().getText()), ctx.index_operator().accept(self)) if ctx.getChildCount() == 2 else ctx.scalar_var().accept(self)

    # assign_stmt_rhs: expr;
    def visitAssign_stmt_rhs(self, ctx: MT22Parser.Assign_stmt_rhsContext):
        return ctx.expr().accept(self)

    # if_stmt : IF LEFT_PAREN expr RIGHT_PAREN statement (ELSE statement)? ;
    def visitIf_stmt(self, ctx: MT22Parser.If_stmtContext):
        return IfStmt(ctx.expr().accept(self), ctx.statement(0).accept(self), ctx.statement(1).accept(self) if ctx.statement(1) else ctx.statement(1))

    # for_stmt : FOR LEFT_PAREN init_expr COMMA condition_expr COMMA update_expr RIGHT_PAREN statement ;
    def visitFor_stmt(self, ctx: MT22Parser.For_stmtContext):
        return ForStmt(ctx.init_expr().accept(self), ctx.condition_expr().accept(self), ctx.update_expr().accept(self), ctx.statement().accept(self))

    # init_expr: scalar_var ASSIGN expr;
    def visitInit_expr(self, ctx: MT22Parser.Init_exprContext):
        return AssignStmt(ctx.scalar_var().accept(self), ctx.expr().accept(self))

    # condition_expr: expr;
    def visitCondition_expr(self, ctx: MT22Parser.Condition_exprContext):
        return ctx.expr().accept(self)

    # update_expr: expr;
    def visitUpdate_expr(self, ctx: MT22Parser.Update_exprContext):
        return ctx.expr().accept(self)

    # while_stmt : WHILE LEFT_PAREN expr RIGHT_PAREN statement ;
    def visitWhile_stmt(self, ctx: MT22Parser.While_stmtContext):
        return WhileStmt(ctx.expr().accept(self), ctx.statement().accept(self))

    # do_while_stmt: DO block_stmt WHILE LEFT_PAREN expr RIGHT_PAREN SEMI_COLON;
    def visitDo_while_stmt(self, ctx: MT22Parser.Do_while_stmtContext):
        return DoWhileStmt(ctx.expr().accept(self), ctx.block_stmt().accept(self))

    # break_stmt: BREAK SEMI_COLON;
    def visitBreak_stmt(self, ctx: MT22Parser.Break_stmtContext):
        return BreakStmt()

    # continue_stmt: CONTINUE SEMI_COLON;
    def visitContinue_stmt(self, ctx: MT22Parser.Continue_stmtContext):
        return ContinueStmt()

    # return_stmt: RETURN expr? SEMI_COLON;
    def visitReturn_stmt(self, ctx: MT22Parser.Return_stmtContext):
        return ReturnStmt(ctx.expr().accept(self) if ctx.expr() else ctx.expr())

    # call_stmt: func_call SEMI_COLON;
    def visitCall_stmt(self, ctx: MT22Parser.Call_stmtContext):
        func_call = ctx.func_call().accept(self)
        return CallStmt(func_call[1], func_call[2])

    # block_stmt: LEFT_BRACE statements_list? RIGHT_BRACE;
    def visitBlock_stmt(self, ctx: MT22Parser.Block_stmtContext):
        return BlockStmt(ctx.statements_list().accept(self) if ctx.statements_list() else [])

    # scalar_var: ID;
    def visitScalar_var(self, ctx: MT22Parser.Scalar_varContext):
        return Id(ctx.ID().getText())

    # boolean_type: BOOLEAN;
    def visitBoolean_type(self, ctx: MT22Parser.Boolean_typeContext):
        return BooleanType()

    # int_type: INTEGER;
    def visitInt_type(self, ctx: MT22Parser.Int_typeContext):
        return IntegerType()

    # float_type: FLOAT;
    def visitFloat_type(self, ctx: MT22Parser.Float_typeContext):
        return FloatType()

    # string_type: STRING;
    def visitString_type(self, ctx: MT22Parser.String_typeContext):
        return StringType()

    # void_type: VOID;
    def visitVoid_type(self, ctx: MT22Parser.Void_typeContext):
        return VoidType()

    # auto_type: AUTO;
    def visitAuto_type(self, ctx: MT22Parser.Auto_typeContext):
        return AutoType()

    # array_type: ARRAY LEFT_BRACK dimensions RIGHT_BRACK OF atomic_type;
    def visitArray_type(self, ctx: MT22Parser.Array_typeContext):
        return ArrayType(ctx.dimensions().accept(self), ctx.atomic_type().accept(self))

    # dimensions: INTEGER_LIT (COMMA INTEGER_LIT)* ;
    def visitDimensions(self, ctx: MT22Parser.DimensionsContext):
        return [str(x.getText()) for x in ctx.INTEGER_LIT()]

    # atomic_type : boolean_type | int_type | float_type | string_type ;
    def visitAtomic_type(self, ctx: MT22Parser.Atomic_typeContext):
        return ctx.getChild(0).accept(self)
