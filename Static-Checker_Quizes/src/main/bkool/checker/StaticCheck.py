from Visitor import BaseVisitor
from AST import *
from StaticError import *


class StaticChecker(BaseVisitor):
    global_envi = []

    def __init__(self, ast):
        self.ast = ast

    def check(self):
        return self.visit(self.ast, StaticChecker.global_envi)

    def visitProgram(self, ast, o):
        o = []
        for decl in ast.decl:
            self.visit(decl, o)
        return ""

    def visitVarDecl(self, ctx: VarDecl, o: object):
        if ctx.name in o:
            raise RedeclaredVariable(ctx.name)
        o += [ctx.name]

    def visitConstDecl(self, ctx: ConstDecl, o: object):
        if ctx.name in o:
            raise RedeclaredConst(ctx.name)
        o += [ctx.name]

    def visitFuncDecl(self, ctx: FuncDecl, o: object):
        if ctx.name in o:
            raise RedeclaredFunction(ctx.name)
        o += [ctx.name]

        o1 = []

        for p in ctx.param:
            self.visit(p, o1)

        for decl in ctx.body[0]:
            if type(decl) is FuncDecl:
                o1 = list(set(o + o1))
                self.visit(decl, o1)
            else:
                self.visit(decl, o1)

        for exp in ctx.body[1]:
            self.visit(exp, list(set(o+o1)))

    def visitIntType(self, ctx: IntType, o: object):
        pass

    def visitFloatType(self, ctx: FloatType, o: object):
        pass

    def visitIntLit(self, ctx: IntLit, o: object):
        pass

    def visitId(self, ctx: Id, o: object):
        if ctx.name not in o:
            raise UndeclaredIdentifier(ctx.name)
