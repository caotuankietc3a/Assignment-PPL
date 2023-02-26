from AST import *
from Utils import Utils
from Visitor import *
from StaticError import *
from functools import reduce


class MType:
    def __init__(self, partype, rettype):
        self.partype = partype
        self.rettype = rettype


class Symbol:
    def __init__(self, name, mtype, value=None):
        self.name = name
        self.mtype = mtype
        self.value = value


class TypeUtils:
    @staticmethod
    def isInListType(x, lst):
        return type(x) in lst

    @staticmethod
    def isBoolType(x):
        return type(x) is BooleanType

    @staticmethod
    def isIntType(x):
        return type(x) is IntegerType

    @staticmethod
    def isFloatType(x):
        return type(x) is FloatType

    @staticmethod
    def isAutoType(x):
        return type(x) is AutoType

    @staticmethod
    def isArrayType(x):
        return type(x) is ArrayType

    @staticmethod
    def isStringType(x):
        return type(x) is StringType

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


class StaticChecker(BaseVisitor, Utils):

    global_envi = [
        Symbol("readInteger", MType([], IntegerType())),
        Symbol("printInteger", MType([IntegerType()], VoidType())),
        Symbol("readFloat", MType([], FloatType())),
        Symbol("printFloat", MType([FloatType()], VoidType())),
        Symbol("readBoolean", MType([], BooleanType())),
        Symbol("printBoolean", MType([BooleanType()], VoidType())),
        Symbol("readString", MType([], StringType())),
        Symbol("printString", MType([StringType()], VoidType())),
        Symbol("super", MType([[Expr()]], VoidType())),
        Symbol("preventDefault", MType([], VoidType())),
    ]

    def __init__(self, ast):
        self.ast = ast
        self.envs = [{}]

    def check(self):
        return self.visit(self.ast, StaticChecker.global_envi)

    def visitProgram(self, ast: Program, c):
        reduce(lambda _, decl: self.visit(decl, c), ast.decls, [])
        print(self.envs)
        return ""

    def visitVarDecl(self, ast: VarDecl, c):
        name = ast.name.name
        typ = ast.typ
        print(typ)
        if name in self.envs[0]:
            raise Redeclared(Variable(), name)

        if not TypeUtils.isNone(ast.init):
            if TypeUtils.isArrayType(typ):
                arr_dimensions = typ.dimensions
                arr_type = typ.typ
                init = self.visit(
                    ast.init, {"type": arr_type, "dimensions": arr_dimensions, "flag": True})
                self.envs[0][name] = {
                    "type": typ, "kind": Variable()}
            else:
                init = self.visit(ast.init, c)
                init_type = init["type"]
                if TypeUtils.isIntType(init_type) and TypeUtils.isFloatType(typ):
                    self.envs[0][name] = {
                        "type": FloatType(), "kind": Variable()}
                    return
                if not TypeUtils.isTheSameType(typ, init_type):
                    raise TypeMismatchInExpression(ast)
                self.envs[0][name] = {"type": init_type if TypeUtils.isAutoType(
                    typ) else typ, "kind": Variable()}
        else:
            if TypeUtils.isAutoType(typ):
                raise Invalid(Variable(), name)

            self.envs[0][name] = {"type": typ, "kind": Variable()}

    def visitParamDecl(self, ast: ParamDecl, c):
        pass

    def visitFuncDecl(self, ast: FuncDecl, c):
        pass

    def visitAssignStmt(self, ast: AssignStmt, c):
        pass

    def visitBlockStmt(self, ast: BlockStmt, c):
        pass

    def visitIfStmt(self, ast: IfStmt, c):
        pass

    def visitForStmt(self, ast: ForStmt, c):
        pass

    def visitWhileStmt(self, ast: WhileStmt, c):
        pass

    def visitDoWhileStmt(self, ast: DoWhileStmt, c):
        pass

    def visitBreakStmt(self, ast: BreakStmt, c):
        pass

    def visitContinueStmt(self, ast: ContinueStmt, c):
        pass

    def visitReturnStmt(self, ast: ReturnStmt, c):
        pass

    def visitCallStmt(self, ast: CallStmt, c):
        pass

    # return Type
    def visitBinExpr(self, ast: BinExpr, c):
        left_expr = self.visit(ast.left, c)
        right_expr = self.visit(ast.right, c)
        left_type = left_expr["type"]
        right_type = right_expr["type"]
        op = ast.op

        if op in ["+", "-", "*", "/"]:
            if not TypeUtils.isInListType(left_type, [IntegerType, FloatType]) or not TypeUtils.isInListType(right_type, [IntegerType, FloatType]):
                raise TypeMismatchInExpression(ast)

            if TypeUtils.isFloatType(left_type) or TypeUtils.isFloatType(right_type):
                return {"type": FloatType()}
            return {"type": IntegerType()}

        if op == "%":
            if not TypeUtils.isIntType(left_type) or not TypeUtils.isIntType(right_type):
                raise TypeMismatchInExpression(ast)
            return {"type": IntegerType()}

        if op == "::":
            if not TypeUtils.isStringType(left_type) or not TypeUtils.isStringType(right_type):
                raise TypeMismatchInExpression(ast)
            return {"type": StringType()}

        if op in ["==", "!="]:
            if not TypeUtils.isInListType(left_type, [IntegerType, BooleanType]) or not TypeUtils.isInListType(right_type, [IntegerType, BooleanType]):
                raise TypeMismatchInExpression(ast)

            if (TypeUtils.isIntType(left_type) and TypeUtils.isIntType(right_type)) or (TypeUtils.isBoolType(left_type) and TypeUtils.isBoolType(right_type)):
                return {"type": BooleanType()}

            raise TypeMismatchInExpression(ast)

        if op in ["<", ">", "<=", ">="]:
            if not TypeUtils.isInListType(left_type, [IntegerType, FloatType]) or not TypeUtils.isInListType(right_type, [IntegerType, FloatType]):
                raise TypeMismatchInExpression(ast)

            if (TypeUtils.isIntType(left_type) and TypeUtils.isIntType(right_type)) or (TypeUtils.isFloatType(left_type) and TypeUtils.isFloatType(right_type)):
                return {"type": BooleanType()}

            raise TypeMismatchInExpression(ast)

        if op in ["&&", "||"]:
            if not TypeUtils.isBoolType(left_type) or not TypeUtils.isBoolType(right_type):
                raise TypeMismatchInExpression(ast)
            return {"type": BooleanType()}

    # return Type

    def visitUnExpr(self, ast: UnExpr, c):
        expr = self.visit(ast.val, c)
        op = ast.op
        typ = expr["type"]
        if op == "!":
            if not TypeUtils.isBoolType(typ) or not TypeUtils.isBoolType(typ):
                raise TypeMismatchInExpression(ast)
            return {"type": BooleanType()}
        if op == "-":
            if not TypeUtils.isInListType(typ, [IntegerType, FloatType]):
                raise TypeMismatchInExpression(ast)
            return {"type": typ}

    def visitId(self, ast: Id, c):
        for x in self.envs:
            if ast.name in x:
                return x[ast.name]

        raise Undeclared(Identifier(), ast.name)

    def visitArrayCell(self, ast: ArrayCell, c):
        pass

    def visitIntegerLit(self, ast: IntegerLit, c):
        return {"type": IntegerType()}

    def visitFloatLit(self, ast: FloatLit, c):
        return {"type": FloatType()}

    def visitStringLit(self, ast: StringLit, c):
        return {"type": StringType()}

    def visitBooleanLit(self, ast: BooleanLit, c):
        return {"type": BooleanType()}

    def visitArrayLit(self, ast: ArrayLit, c):

        # typ = c["type"]
        # dimensions = c["dimensions"]
        # expr_list = ast.exprlist
        # if len(dimensions) > len(expr_list):
        #     return

        # for expr in expr_list:
        #     if TypeUtils.isTheSameType(expr, ArrayLit()):
        #         exp = self.visit(
        #             expr, {"type": arr_type, "dimensions": arr_dimensions, "flag": False})
        #     if not TypeUtils.isTheSameType(exp["type"], typ):
        #         raise IllegalArrayLiteral(ast)
        pass

    def visitFuncCall(self, ast: FuncCall, c):
        pass

    def visitIntegerType(self, ast: IntegerType, c):
        return IntegerType()

    def visitFloatType(self, ast: FloatType, c):
        return FloatType()

    def visitStringType(self, ast: StringType, c):
        return StringType()

    def visitBooleanType(self, ast: BooleanType, c):
        return BooleanType()

    def visitArrayType(self, ast: ArrayType, c):
        return ast

    def visitAutoType(self, ast: AutoType, c):
        return {"type": AutoType()}

    def visitVoidType(self, ast: VoidType, c):
        return {"type": VoidType()}
