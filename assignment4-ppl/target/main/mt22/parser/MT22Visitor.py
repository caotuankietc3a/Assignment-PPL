# Generated from main/mt22/parser/MT22.g4 by ANTLR 4.11.1
from antlr4 import *
if __name__ is not None and "." in __name__:
    from .MT22Parser import MT22Parser
else:
    from MT22Parser import MT22Parser

# This class defines a complete generic visitor for a parse tree produced by MT22Parser.

class MT22Visitor(ParseTreeVisitor):

    # Visit a parse tree produced by MT22Parser#program.
    def visitProgram(self, ctx:MT22Parser.ProgramContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MT22Parser#decls.
    def visitDecls(self, ctx:MT22Parser.DeclsContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MT22Parser#decl.
    def visitDecl(self, ctx:MT22Parser.DeclContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MT22Parser#array_lit.
    def visitArray_lit(self, ctx:MT22Parser.Array_litContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MT22Parser#variable_decl.
    def visitVariable_decl(self, ctx:MT22Parser.Variable_declContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MT22Parser#identifiers_list.
    def visitIdentifiers_list(self, ctx:MT22Parser.Identifiers_listContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MT22Parser#function_decl.
    def visitFunction_decl(self, ctx:MT22Parser.Function_declContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MT22Parser#params_list.
    def visitParams_list(self, ctx:MT22Parser.Params_listContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MT22Parser#parameter_decl.
    def visitParameter_decl(self, ctx:MT22Parser.Parameter_declContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MT22Parser#body.
    def visitBody(self, ctx:MT22Parser.BodyContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MT22Parser#expr.
    def visitExpr(self, ctx:MT22Parser.ExprContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MT22Parser#string_expr.
    def visitString_expr(self, ctx:MT22Parser.String_exprContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MT22Parser#relational_expr.
    def visitRelational_expr(self, ctx:MT22Parser.Relational_exprContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MT22Parser#logical_expr_1.
    def visitLogical_expr_1(self, ctx:MT22Parser.Logical_expr_1Context):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MT22Parser#adding_expr.
    def visitAdding_expr(self, ctx:MT22Parser.Adding_exprContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MT22Parser#multiplying_expr.
    def visitMultiplying_expr(self, ctx:MT22Parser.Multiplying_exprContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MT22Parser#logical_expr_2.
    def visitLogical_expr_2(self, ctx:MT22Parser.Logical_expr_2Context):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MT22Parser#sign_expr.
    def visitSign_expr(self, ctx:MT22Parser.Sign_exprContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MT22Parser#index_expr.
    def visitIndex_expr(self, ctx:MT22Parser.Index_exprContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MT22Parser#index_operator.
    def visitIndex_operator(self, ctx:MT22Parser.Index_operatorContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MT22Parser#operand_expr.
    def visitOperand_expr(self, ctx:MT22Parser.Operand_exprContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MT22Parser#operand.
    def visitOperand(self, ctx:MT22Parser.OperandContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MT22Parser#func_call.
    def visitFunc_call(self, ctx:MT22Parser.Func_callContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MT22Parser#literal.
    def visitLiteral(self, ctx:MT22Parser.LiteralContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MT22Parser#exprs_list_var_decl.
    def visitExprs_list_var_decl(self, ctx:MT22Parser.Exprs_list_var_declContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MT22Parser#exprs_list.
    def visitExprs_list(self, ctx:MT22Parser.Exprs_listContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MT22Parser#statements_list.
    def visitStatements_list(self, ctx:MT22Parser.Statements_listContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MT22Parser#statement.
    def visitStatement(self, ctx:MT22Parser.StatementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MT22Parser#assign_stmt.
    def visitAssign_stmt(self, ctx:MT22Parser.Assign_stmtContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MT22Parser#assign_stmt_lhs.
    def visitAssign_stmt_lhs(self, ctx:MT22Parser.Assign_stmt_lhsContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MT22Parser#assign_stmt_rhs.
    def visitAssign_stmt_rhs(self, ctx:MT22Parser.Assign_stmt_rhsContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MT22Parser#if_stmt.
    def visitIf_stmt(self, ctx:MT22Parser.If_stmtContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MT22Parser#for_stmt.
    def visitFor_stmt(self, ctx:MT22Parser.For_stmtContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MT22Parser#init_expr.
    def visitInit_expr(self, ctx:MT22Parser.Init_exprContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MT22Parser#condition_expr.
    def visitCondition_expr(self, ctx:MT22Parser.Condition_exprContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MT22Parser#update_expr.
    def visitUpdate_expr(self, ctx:MT22Parser.Update_exprContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MT22Parser#while_stmt.
    def visitWhile_stmt(self, ctx:MT22Parser.While_stmtContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MT22Parser#do_while_stmt.
    def visitDo_while_stmt(self, ctx:MT22Parser.Do_while_stmtContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MT22Parser#break_stmt.
    def visitBreak_stmt(self, ctx:MT22Parser.Break_stmtContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MT22Parser#continue_stmt.
    def visitContinue_stmt(self, ctx:MT22Parser.Continue_stmtContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MT22Parser#return_stmt.
    def visitReturn_stmt(self, ctx:MT22Parser.Return_stmtContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MT22Parser#call_stmt.
    def visitCall_stmt(self, ctx:MT22Parser.Call_stmtContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MT22Parser#block_stmt.
    def visitBlock_stmt(self, ctx:MT22Parser.Block_stmtContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MT22Parser#scalar_var.
    def visitScalar_var(self, ctx:MT22Parser.Scalar_varContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MT22Parser#boolean_type.
    def visitBoolean_type(self, ctx:MT22Parser.Boolean_typeContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MT22Parser#int_type.
    def visitInt_type(self, ctx:MT22Parser.Int_typeContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MT22Parser#float_type.
    def visitFloat_type(self, ctx:MT22Parser.Float_typeContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MT22Parser#string_type.
    def visitString_type(self, ctx:MT22Parser.String_typeContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MT22Parser#void_type.
    def visitVoid_type(self, ctx:MT22Parser.Void_typeContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MT22Parser#auto_type.
    def visitAuto_type(self, ctx:MT22Parser.Auto_typeContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MT22Parser#array_type.
    def visitArray_type(self, ctx:MT22Parser.Array_typeContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MT22Parser#dimensions.
    def visitDimensions(self, ctx:MT22Parser.DimensionsContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MT22Parser#atomic_type.
    def visitAtomic_type(self, ctx:MT22Parser.Atomic_typeContext):
        return self.visitChildren(ctx)



del MT22Parser