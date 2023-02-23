from Visitor import BaseVisitor
from AST import *
from antlr4.atn.ATNDeserializer import RangeTransition
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
            if id.name in env:
                env[id.name] = typ
                return typ
        return None

    @staticmethod
    def inferTypeFunc(id, typ, o):
        for env in o:
            if id == env[0]:
                env[1] = typ
                return typ
        return None


class StaticChecker(BaseVisitor):
    global_envi = []

    def __init__(self, ast):
        self.ast = ast

    def check(self):
        return self.visit(self.ast, StaticChecker.global_envi)

    def visitProgram(self, ctx: Program, o):
        o = [{}]

        reduce(lambda _, decl: self.visit(decl, o), ctx.decl, [])
        reduce(lambda _, stmt: self.visit(stmt, o), ctx.stmts, [])

    def visitVarDecl(self, ctx: VarDecl, o):
        # print("var-start: ", o)
        if ctx.name in o[0]:
            raise Redeclared(ctx)
        o[0][ctx.name] = None
        # print("var-end: ", o)

    def visitFuncDecl(self, ctx: FuncDecl, o):
        # print("func-start: ", o)
        if ctx.name in o[0]:
            raise Redeclared(ctx)
        o[0][ctx.name] = {"type": None, "params": [
            [param.name, None] for param in ctx.param] if ctx.param else []}
        o1 = [{}] + o

        reduce(lambda _, param: self.visit(param, o1), ctx.param, [])
        reduce(lambda _, local: self.visit(local, o1), ctx.local, [])
        reduce(lambda _, stmt: self.visit(stmt, o1), ctx.stmts, [])

        for i, x in enumerate(o[0][ctx.name]["params"]):
            id_name = x[0]
            if id_name in o1[0] and not TypeUtils.isNone(o1[0][id_name]):
                o[0][ctx.name]["params"][i][1] = o1[0][id_name]

    def visitCallStmt(self, ctx: CallStmt, o):
        print("call: ", ctx)
        for x in o:
            if ctx.name in x:
                print(x[ctx.name])
                if not isinstance(x[ctx.name], dict):
                    raise UndeclaredIdentifier(ctx.name)
                params_func = x[ctx.name]["params"]
                if len(params_func) != len(ctx.args):
                    raise TypeMismatchInStatement(ctx)
                for idx, arg in enumerate(ctx.args):
                    arg_type = self.visit(arg, o)
                    if TypeUtils.isNone(arg_type) and TypeUtils.isNone(params_func[idx][1]):
                        raise TypeCannotBeInferred(ctx)

                    if TypeUtils.isNone(arg_type):
                        arg_type = TypeUtils.inferType(
                            arg, params_func[idx][1], o)

                    if TypeUtils.isNone(params_func[idx][1]):
                        print(params_func[idx][0], x[ctx.name]["params"])
                        params_func[idx][1] = TypeUtils.inferTypeFunc(
                            params_func[idx][0], arg_type, x[ctx.name]["params"])
                    if not TypeUtils.isTheSameType(arg_type, params_func[idx][1]):
                        raise TypeMismatchInStatement(ctx)
                return
        raise UndeclaredIdentifier(ctx.name)

    def visitAssign(self, ctx: Assign, o):
        print("assign: ", ctx)
        lhs = self.visit(ctx.lhs, o)
        rhs = self.visit(ctx.rhs, o)
        print(lhs, ctx.lhs)
        print(rhs, ctx.rhs)

        if TypeUtils.isNone(lhs) and TypeUtils.isNone(rhs):
            raise TypeCannotBeInferred(ctx)
        if TypeUtils.isNone(lhs):
            lhs = TypeUtils.inferType(ctx.lhs, rhs, o)
        if TypeUtils.isNone(rhs):
            rhs = TypeUtils.inferType(ctx.rhs, lhs, o)

        if not TypeUtils.isTheSameType(lhs, rhs):
            raise TypeMismatchInStatement(ctx)
        print(o)

        # print("assign: ", str(o))

    def visitIntLit(self, ctx: IntLit, o): return IntType()

    def visitFloatLit(self, ctx: FloatLit, o): return FloatType()

    def visitBoolLit(self, ctx: BoolLit, o): return BoolType()

    def visitId(self, ctx: Id, o):
        # print("id: ", str(o))
        for x in o:
            if ctx.name in x:
                return x[ctx.name]

        raise UndeclaredIdentifier(ctx.name)
