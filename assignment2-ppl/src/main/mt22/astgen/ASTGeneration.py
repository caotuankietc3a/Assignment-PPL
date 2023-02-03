from MT22Visitor import MT22Visitor
from MT22Parser import MT22Parser
from AST import *


class ASTGeneration(MT22Visitor):
    def visitProgram(self, ctx: MT22Parser.ProgramContext):
        return Program(ctx.decls().accept(self))

    def visitDecls(self, ctx: MT22Parser.DeclsContext):
        return [ctx.decl().accept(self), *ctx.decls().accept(self)] if ctx.getChildCount() == 2 else [ctx.decl().accept(self)]

    def visitDecl(self, ctx: MT22Parser.DeclContext):
        return ctx.variable_decl().accept(self) if ctx.variable_decl() else ctx.function_decl().accept(self)

    def visitArray_lit(self, ctx: MT22Parser.Array_litContext):
        return ArrayLit(ctx.exprs_list() if ctx.exprs_list() else [])

    def visitVariable_decl(self, ctx: MT22Parser.Variable_declContext):
        return [VarDecl(id, ctx.getChild(2).getText(), expr) for id, expr in zip(ctx.identifiers_list().accept(self), ctx.exprs_list().accept(self))]

    def visitIdentifiers_list(self, ctx: MT22Parser.Identifiers_listContext):
        return [Id(x.getText()) for x in ctx.ID()]

    def visitFunction_decl(self, ctx: MT22Parser.Function_declContext):
        return [FuncDecl(ctx.ID(0).getText(), ctx.getChild(3).accept(self), ctx.params_list().accept(self) if ctx.params_list() else [], ctx.INHERIT().getText() if ctx.INHERIT() else ctx.INHERIT(), ctx.body().accept(self))]

    def visitParams_list(self, ctx: MT22Parser.Params_listContext):
        return [ctx.parameter_decl().accept(self), *ctx.params_list().accept(self)] if ctx.getChildCount() == 3 else [ctx.parameter_decl().accept(self)]

    def visitParameter_decl(self, ctx: MT22Parser.Parameter_declContext):
        return ParamDecl(ctx.ID().getText(), ctx.getChild(ctx.getChildCount() - 1).accept(self), True if ctx.OUT() else False, True if ctx.INHERIT() else False)

    def visitBody(self, ctx: MT22Parser.BodyContext):
        return ctx.block_stmt().accept(self)

    def visitExpr(self, ctx: MT22Parser.ExprContext):
        return ctx.string_expr().accept(self)

    def visitString_expr(self, ctx: MT22Parser.String_exprContext):
        return BinExpr(ctx.SR().getText(), ctx.string_expr().accept(self), ctx.relational_expr().accept(self)) if ctx.getChildCount() == 3 else ctx.relational_expr().accept(self)

    def visitRelational_expr(self, ctx: MT22Parser.Relational_exprContext):
        return BinExpr(ctx.getChild(1).getText(), ctx.logical_expr_1(0).accept(self), ctx.logical_expr_1(1).accept(self)) if ctx.getChildCount() == 3 else ctx.logical_expr_1().accept(self)

    def visitLogical_expr_1(self, ctx: MT22Parser.Logical_expr_1Context):
        return UnExpr(ctx.getChild(1).getText(), ctx.adding_expr().accept(self)) if ctx.getChildCount() == 3 else ctx.adding_expr().accept(self)

    def visitAdding_expr(self, ctx: MT22Parser.Adding_exprContext):
        return BinExpr(ctx.getChild(1).getText(), ctx.adding_expr().accept(self), ctx.multiplying_expr().accept(self)) if ctx.getChildCount() == 3 else ctx.multiplying_expr().accept(self)

    def visitMultiplying_expr(self, ctx: MT22Parser.Multiplying_exprContext):
        return BinExpr(ctx.getChild(1).getText(), ctx.multiplying_expr().accept(self), ctx.logical_expr_2().accept(self)) if ctx.getChildCount() == 3 else ctx.logical_expr_2().accept(self)

    def visitLogical_expr_2(self, ctx: MT22Parser.Logical_expr_2Context):
        return UnExpr(ctx.NOT().getText(), ctx.logical_expr_2().accept(self)) if ctx.getChildCount() == 2 else ctx.sign_expr().accept(self)

    def visitSign_expr(self, ctx: MT22Parser.Sign_exprContext):
        return UnExpr(ctx.MINUS().getText(), ctx.sign_expr().accept(self)) if ctx.getChildCount() == 2 else ctx.index_expr().accept(self)

    def visitIndex_expr(self, ctx: MT22Parser.Index_exprContext):
        return ArrayCell(ctx.index_expr().accept(self), ctx.index_operator().accept(self)) if ctx.getChildCount() == 2 else ctx.operand_expr().accept(self)

    def visitIndex_operator(self, ctx: MT22Parser.Index_operatorContext):
        return ctx.exprs_list().accept(self)

    def visitOperand_expr(self, ctx: MT22Parser.Operand_exprContext):
        return ctx.expr().accept(self) if ctx.getChildCount() == 3 else ctx.operand().accept(self)

    def visitOperand(self, ctx: MT22Parser.OperandContext):
        return ctx.ID().getText() if ctx.ID() else ctx.getChild(0).accept(self)

    def visitFunc_call(self, ctx: MT22Parser.Func_callContext):
        return FuncCall(ctx.ID().getText(), ctx.exprs_list().accept(self))

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

    def visitExprs_list(self, ctx: MT22Parser.Exprs_listContext):
        return [ctx.expr().accept(self), *ctx.exprs_list().accept(self)] if ctx.getChildCount() == 3 else [ctx.expr().accept(self)]

    def visitStatements_list(self, ctx: MT22Parser.Statements_listContext):
        return [ctx.statement().accept(self), *ctx.statements_list().accept(self)] if ctx.getChildCount() == 2 else [ctx.statement().accept(self)]

    def visitStatement(self, ctx: MT22Parser.StatementContext):
        return ctx.getChild(0).accept(self)

    def visitAssign_stmt(self, ctx: MT22Parser.Assign_stmtContext):
        return AssignStmt(ctx.assign_stmt_lhs().accept(self), ctx.assign_stmt_rhs().accept(self))

    def visitAssign_stmt_lhs(self, ctx: MT22Parser.Assign_stmt_lhsContext):
        return ArrayCell(ctx.ID().getText(), ctx.index_operator().accept(self)) if ctx.getChildCount() == 2 else ctx.scalar_var().accept(self)

    def visitAssign_stmt_rhs(self, ctx: MT22Parser.Assign_stmt_rhsContext):
        return ctx.expr().accept(self)

    def visitIf_stmt(self, ctx: MT22Parser.If_stmtContext):
        return IfStmt(ctx.expr().accept(self), ctx.statement(0).accept(self), ctx.statement(1).accept(self) if ctx.statement(1) else ctx.statement(1))

    def visitFor_stmt(self, ctx: MT22Parser.For_stmtContext):
        return ForStmt(ctx.init_expr().accept(self), ctx.condition_expr().accept(self), ctx.update_expr().accept(self), ctx.statement().accept(self))

    def visitInit_expr(self, ctx: MT22Parser.Init_exprContext):
        return AssignStmt(ctx.scalar_var().accept(self), ctx.expr().accept(self))

    def visitCondition_expr(self, ctx: MT22Parser.Condition_exprContext):
        return ctx.expr().accept(self)

    def visitUpdate_expr(self, ctx: MT22Parser.Update_exprContext):
        return ctx.expr().accept(self)

    def visitWhile_stmt(self, ctx: MT22Parser.While_stmtContext):
        return WhileStmt(ctx.expr().accept(self), ctx.statement().accept(self))

    def visitDo_while_stmt(self, ctx: MT22Parser.Do_while_stmtContext):
        return DoWhileStmt(ctx.expr().accept(self), ctx.block_stmt().accept(self))

    def visitBreak_stmt(self, ctx: MT22Parser.Break_stmtContext):
        return BreakStmt()

    def visitContinue_stmt(self, ctx: MT22Parser.Continue_stmtContext):
        return ContinueStmt()

    def visitReturn_stmt(self, ctx: MT22Parser.Return_stmtContext):
        return ctx.expr().accept(self) if ctx.expr() else None

    def visitCall_stmt(self, ctx: MT22Parser.Call_stmtContext):
        return CallStmt(ctx.func_call().ID().gettext(), ctx.func_call().exprs_list().accept(self))

    def visitBlock_stmt(self, ctx: MT22Parser.Block_stmtContext):
        return BlockStmt(ctx.statements_list().accept(self) if ctx.statements_list() else [])

    def visitScalar_var(self, ctx: MT22Parser.Scalar_varContext):
        return ctx.ID().getText()

    def visitBoolean_type(self, ctx: MT22Parser.Boolean_typeContext):
        return BooleanType()

    def visitInt_type(self, ctx: MT22Parser.Int_typeContext):
        return IntegerType()

    def visitFloat_type(self, ctx: MT22Parser.Float_typeContext):
        return FloatType()

    def visitString_type(self, ctx: MT22Parser.String_typeContext):
        return StringType()

    def visitVoid_type(self, ctx: MT22Parser.Void_typeContext):
        return VoidType()

    def visitAuto_type(self, ctx: MT22Parser.Auto_typeContext):
        return AutoType()

    def visitArray_type(self, ctx: MT22Parser.Array_typeContext):
        return ArrayType(ctx.demensions().accept(self), ctx.atomic_type().accept(self))

    def visitDimensions(self, ctx: MT22Parser.DimensionsContext):
        return [IntegerLit(x.getText()) for x in ctx.INTEGER_LIT()]

    def visitAtomic_type(self, ctx: MT22Parser.Atomic_typeContext):
        return ctx.getChild(0).accept(self)
