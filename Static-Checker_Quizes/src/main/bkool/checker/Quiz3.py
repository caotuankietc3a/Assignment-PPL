from AST import *
from Visitor import *
from StaticError import *


class Quiz3Checker(BaseVisitor):
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
        for decl in ctx.param:
            self.visit(decl, o1)

        for decl in ctx.body:
            self.visit(decl, o1)

    def visitIntType(self, ctx: IntType, o: object):
        pass

    def visitFloatType(self, ctx: FloatType, o: object):
        pass

    def visitIntLit(self, ctx: IntLit, o: object):
        pass
