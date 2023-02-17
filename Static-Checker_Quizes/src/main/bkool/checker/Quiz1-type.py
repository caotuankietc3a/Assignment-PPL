from Visitor import BaseVisitor
from AST import *
from StaticError import *


class Quiz1TypeStaticChecker(BaseVisitor):

    def visitBinOp(self, ctx: BinOp, o):
        e1 = self.visit(ctx.e1, o)
        e2 = self.visit(ctx.e2, o)

        if ctx.op in ["+", "-", "*", "/"] and (type(e1) not in [FloatType, IntType] or type(e2) not in [FloatType, IntType]):
            raise TypeMismatchInExpression(ctx)
        elif ctx.op in ["&&", "||"] and ((type(e1) is not BoolType) or (type(e2) is not BoolType)):
            raise TypeMismatchInExpression(ctx)
        elif ctx.op in [">", "<", "==", "!="] and type(e1) is not type(e2):
            raise TypeMismatchInExpression(ctx)

        if ctx.op in ["+", "-", "*"]:
            return IntType() if type(e1) is IntType and type(e2) is IntType else FloatType()

        if ctx.op == "/":
            return FloatType()

        if ctx.op in ["&&", "||", "<", ">", "==", "!="]:
            return BoolType()

    def visitUnOp(self, ctx: UnOp, o):
        e = self.visit(ctx.e, o)
        if (ctx.op == "!" and type(e) is not BoolType) or (ctx.op == "-" and type(e) not in [FloatType, IntType]):
            raise TypeMismatchInExpression(ctx)
        return e

    def visitIntLit(self, ctx: IntLit, o): return IntType()

    def visitFloatLit(self, ctx: FloatLit, o): return FloatType()

    def visitBoolLit(self, ctx: BoolLit, o): return BoolType()
