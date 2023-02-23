from Visitor import BaseVisitor
from AST import *
from StaticError import *
from functools import reduce


class TypeUtils:
    @staticmethod
    def isBoolType(x):
        return type(x) is BoolType

    @staticmethod
    def isIntType(x):
        return type(x) is IntType

    @staticmethod
    def isFloatType(x):
        return type(x) is FloatType

    @staticmethod
    def isNone(x):
        return type(x) is type(None)

    @staticmethod
    def isTheSameType(x, y):
        return type(x) is type(y)

    @staticmethod
    def inferType(id, typ, o):
        for env in o:
            if env[0] == id.name:
                if TypeUtils.isNone(env[1]):
                    env[1] = typ
                    return typ
                else:
                    return env[1]


class Quiz3TypeStaticChecker(BaseVisitor):
    def visitProgram(self, ctx: Program, o):
        o = []

        reduce(lambda _, decl: self.visit(decl, o), ctx.decl, [])
        reduce(lambda _, stmt: self.visit(stmt, o), ctx.stmts, [])

    def visitVarDecl(self, ctx: VarDecl, o):
        o += [[ctx.name, None]]

    def visitAssign(self, ctx: Assign, o):
        lhs = self.visit(ctx.lhs, o)
        rhs = self.visit(ctx.rhs, o)
        if TypeUtils.isNone(lhs) and TypeUtils.isNone(rhs):
            raise TypeCannotBeInferred(ctx)
        if TypeUtils.isNone(lhs):
            lhs = TypeUtils.inferType(ctx.lhs, rhs, o)
        if TypeUtils.isNone(rhs):
            rhs = TypeUtils.inferType(ctx.rhs, lhs, o)

        if not TypeUtils.isTheSameType(lhs, rhs):
            raise TypeMismatchInStatement(ctx)

    def visitBinOp(self, ctx: BinOp, o):
        e1 = self.visit(ctx.e1, o)
        e2 = self.visit(ctx.e2, o)

        if not TypeUtils.isNone(e1) and not TypeUtils.isNone(e2) and not TypeUtils.isTheSameType(e1, e2):
            raise TypeMismatchInExpression(ctx)

        if ctx.op in ["+", "-", "*", "/"]:
            if TypeUtils.isNone(e1):
                e1 = TypeUtils.inferType(ctx.e1, IntType(), o)

            if TypeUtils.isNone(e2):
                e2 = TypeUtils.inferType(ctx.e2, IntType(), o)
            return IntType()
        if ctx.op in ["+.", "-.", "*.", "/."]:
            if TypeUtils.isNone(e1):
                e1 = TypeUtils.inferType(ctx.e1, FloatType(), o)

            if TypeUtils.isNone(e2):
                e2 = TypeUtils.inferType(ctx.e2, FloatType(), o)
            return FloatType()
        if ctx.op in [">", "="]:
            if TypeUtils.isNone(e1):
                e1 = TypeUtils.inferType(ctx.e1, IntType(), o)

            if TypeUtils.isNone(e2):
                e2 = TypeUtils.inferType(ctx.e2, IntType(), o)
            return BoolType()
        if ctx.op in [">.", "=."]:
            if TypeUtils.isNone(e1):
                e1 = TypeUtils.inferType(ctx.e1, FloatType(), o)

            if TypeUtils.isNone(e2):
                e2 = TypeUtils.inferType(ctx.e2, FloatType(), o)
            return BoolType()
        if ctx.op in ["&&", "||", ">b", "=b"]:
            if TypeUtils.isNone(e1):
                e1 = TypeUtils.inferType(ctx.e1, BoolType(), o)

            if TypeUtils.isNone(e2):
                e2 = TypeUtils.inferType(ctx.e2, BoolType(), o)
            return BoolType()

    def visitUnOp(self, ctx: UnOp, o):
        e = self.visit(ctx.e, o)
        if ctx.op == "-":
            if TypeUtils.isNone(e):
                e = TypeUtils.inferType(ctx.e, IntType(), o)

            if not TypeUtils.isIntType(e):
                raise TypeMismatchInExpression(ctx)
            return IntType()
        if ctx.op == "-.":
            if TypeUtils.isNone(e):
                e = TypeUtils.inferType(ctx.e, FloatType(), o)
            if not TypeUtils.isFloatType(e):
                raise TypeMismatchInExpression(ctx)
            return FloatType()
        if ctx.op == "!":
            if TypeUtils.isNone(e):
                e = TypeUtils.inferType(ctx.e, BoolType(), o)
            if not TypeUtils.isBoolType(e):
                raise TypeMismatchInExpression(ctx)
            return BoolType()
        if ctx.op == "i2f":
            if TypeUtils.isNone(e):
                e = TypeUtils.inferType(ctx.e, IntType(), o)
            if not TypeUtils.isIntType(e):
                raise TypeMismatchInExpression(ctx)
            return FloatType()
        if ctx.op == "floor":
            if TypeUtils.isNone(e):
                e = TypeUtils.inferType(ctx.e, FloatType(), o)
            if not TypeUtils.isFloatType(e):
                raise TypeMismatchInExpression(ctx)
            return IntType()

    def visitIntLit(self, ctx: IntLit, o): return IntType()

    def visitFloatLit(self, ctx: FloatLit, o): return FloatType()

    def visitBoolLit(self, ctx: BoolLit, o): return BoolType()

    def visitId(self, ctx: Id, o):
        for id in o:
            if id[0] == ctx.name:
                return id[1]

        raise UndeclaredIdentifier(ctx.name)
