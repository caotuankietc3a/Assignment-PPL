from MT22Visitor import MT22Visitor
from MT22Parser import MT22Parser
from ..utils.AST import *


class ASTGeneration(MT22Visitor):
    def visitProgram(self, ctx: MT22Parser.ProgramContext):
        return Program(ctx.decls().accept(self))

    def visitDecls(self, ctx: MT22Parser.DeclsContext):
        return [ctx.decl().accept(self), ctx.decls().accept(self)] if ctx.getChildCount() == 2 else [ctx.decl().accept(self)]

    def visitDecl(self, ctx: MT22Parser.DeclContext):
        return ctx.variable_decl().accept(self) if ctx.variable_decl() else ctx.function_decl().accept(self)

    def visitArray_lit(self, ctx: MT22Parser.Array_litContext):
        return None

    def visitVariable_decl(self, ctx: MT22Parser.Variable_declContext):
        ids = ctx.identifiers_list().accept(self)
        exprs = ctx.exprs_list().accept(self)
        return [VarDecl(id, ctx.getChild(2).getText(), expr) for id, expr in zip(ids, exprs)]

    def visitIdentifiers_list(self, ctx: MT22Parser.Identifiers_listContext):
        return [Id(x.getText()) for x in ctx.ID()]

    def visitFunction_decl(self, ctx: MT22Parser.Function_declContext):
        return None

    def visitParams_list(self, ctx: MT22Parser.Params_listContext):
        return None

    def visitParameter_decl(self, ctx: MT22Parser.Parameter_declContext):
        return None

    def visitBody(self, ctx: MT22Parser.BodyContext):
        return None

    def visitExpr(self, ctx: MT22Parser.ExprContext):
        return None

    def visitString_expr(self, ctx: MT22Parser.String_exprContext):
        return None

    def visitRelational_expr(self, ctx: MT22Parser.Relational_exprContext):
        return None

    def visitLogical_expr_1(self, ctx: MT22Parser.Logical_expr_1Context):
        return None

    def visitAdding_expr(self, ctx: MT22Parser.Adding_exprContext):
        return None

    def visitMultiplying_expr(self, ctx: MT22Parser.Multiplying_exprContext):
        return None

    def visitLogical_epxr_2(self, ctx: MT22Parser.Logical_epxr_2Context):
        return None

    def visitSign_expr(self, ctx: MT22Parser.Sign_exprContext):
        return None

    def visitIndex_expr(self, ctx: MT22Parser.Index_exprContext):
        return None

    def visitOperand_expr(self, ctx: MT22Parser.Operand_exprContext):
        return None

    def visitOperand(self, ctx: MT22Parser.OperandContext):
        return None

    def visitFunc_call(self, ctx: MT22Parser.Func_callContext):
        return None

    def visitLiteral(self, ctx: MT22Parser.LiteralContext):
        return None

    def visitExprs_list(self, ctx: MT22Parser.Exprs_listContext):
        return [ctx.expr().accept(self), ctx.exprs_list().accept(self)] if ctx.getChildCount() == 3 else [ctx.expr().accept(self)]

    def visitStatements_list(self, ctx: MT22Parser.Statements_listContext):
        return None

    def visitStatement(self, ctx: MT22Parser.StatementContext):
        return None

    def visitAssign_stmt(self, ctx: MT22Parser.Assigment_stmtContext):
        return None

    def visitAssign_stmt_lhs(self, ctx: MT22Parser.Assigment_stmt_lhsContext):
        return None

    def visitAssign_stmt_rhs(self, ctx: MT22Parser.Assign_stmt_rhsContext):
        return None

    def visitFor_stmt(self, ctx: MT22Parser.For_stmtContext):
        return None

    def visitInit_expr(self, ctx: MT22Parser.Init_exprContext):
        return None

    def visitCondition_expr(self, ctx: MT22Parser.Condition_exprContext):
        return None

    def visitUpdate_expr(self, ctx: MT22Parser.Update_exprContext):
        return None

    def visitWhile_stmt(self, ctx: MT22Parser.While_stmtContext):
        return None

    def visitDo_while_stmt(self, ctx: MT22Parser.Do_while_stmtContext):
        return None

    def visitBreak_stmt(self, ctx: MT22Parser.Break_stmtContext):
        return None

    def visitContinue_stmt(self, ctx: MT22Parser.Continue_stmtContext):
        return None

    def visitReturn_stmt(self, ctx: MT22Parser.Return_stmtContext):
        return None

    def visitCall_stmt(self, ctx: MT22Parser.Call_stmtContext):
        return None

    def visitBlock_stmt(self, ctx: MT22Parser.Block_stmtContext):
        return None

    def visitScalar_var(self, ctx: MT22Parser.Scalar_varContext):
        return None

    def visitBoolean_type(self, ctx: MT22Parser.Boolean_typeContext):
        return None

    def visitInt_type(self, ctx: MT22Parser.Int_typeContext):
        return None

    def visitFloat_type(self, ctx: MT22Parser.Float_typeContext):
        return None

    def visitString_type(self, ctx: MT22Parser.String_typeContext):
        return None

    def visitVoid_type(self, ctx: MT22Parser.Void_typeContext):
        return None

    def visitAuto_type(self, ctx: MT22Parser.Auto_typeContext):
        return AutoType()

    def visitArray_type(self, ctx: MT22Parser.Array_typeContext):
        return ArrayType(ctx.demensions().accept(self), ctx.atomic_type().accept(self))

    def visitDimensions(self, ctx: MT22Parser.DimensionsContext):
        return None

    def visitAtomic_type(self, ctx: MT22Parser.Atomic_typeContext):
        if ctx.boolean_type():
            return ctx.boolean_type().accept(self)

        if ctx.int_type():
            return ctx.int_type().accept(self)

        if ctx.float_type():
            return ctx.float_type().accept(self)

        return ctx.string_type().accept(self)
