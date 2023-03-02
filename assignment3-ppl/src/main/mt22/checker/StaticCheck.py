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


class Array(Type):
    def __init__(self, val: int, lst: List[Type]) -> None:
        self.val = val
        self.lst = lst

    def __str__(self):
        return "Array({}, [{}])".format(str(self.val), ", ".join([str(exp) for exp in self.lst]))

    # Array(2, [Array(2, [IntType(), IntType()]), Array(2, [IntType(), IntType()])])
    @staticmethod
    def getDimensions(arr):
        if not TypeUtils.isArray(arr["type"]):
            return []

        arr_type = arr["type"]
        res = [arr_type.val]
        res1 = reduce(lambda acc, el: acc +
                      Array.getDimensions(el), arr_type.lst, [])
        return (res + [max(res1)]) if len(res1) != 0 else res

    @staticmethod
    def isDimensionsMatched(dimen1, dimen2, func):
        for d1, d2 in zip(dimen1, dimen2):
            if int(d1) < d2:
                func()
        return True


class TypeUtils:
    @ staticmethod
    def isInListType(x, lst):
        return type(x) in lst

    @ staticmethod
    def isBoolType(x):
        return type(x) is BooleanType

    @ staticmethod
    def isIntType(x):
        return type(x) is IntegerType

    @ staticmethod
    def isFloatType(x):
        return type(x) is FloatType

    @ staticmethod
    def isAutoType(x):
        return type(x) is AutoType

    @ staticmethod
    def isArrayType(x):
        return type(x) is ArrayType

    @ staticmethod
    def isArray(x):
        return type(x) is Array

    @ staticmethod
    def isArrayLit(x):
        return type(x) is ArrayLit

    @ staticmethod
    def isStringType(x):
        return type(x) is StringType

    @ staticmethod
    def isVoidType(x):
        return type(x) is VoidType

    @ staticmethod
    def isNone(x):
        return type(x) is type(None)

    @ staticmethod
    def isTheSameType(x, y):
        return type(x) is type(y)

    @ staticmethod
    def inferType(name, typ, c, kind=Variable):
        for env in c:
            if name in env and isinstance(env[name]["kind"], kind):
                env[name]["type"] = typ
                return {"type": typ}
        return {"type": None}


class Search:
    @staticmethod
    def search(name, lst, func, kind=Variable):
        for x in lst:
            if name in x and isinstance(x[name]["kind"], kind):
                return x[name]
        return func()

    @staticmethod
    def check(name, dic, func) -> None:
        if name in dic:
            func()


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
        self.illegal_array_literal = None
        self.is_func_decl = False

    def check(self):
        return self.visit(self.ast, StaticChecker.global_envi)

    def raise_(self, ex):
        raise ex

    def visitProgram(self, ast: Program, c):
        has_entry_point = False
        for decl in ast.decls:
            if type(decl) is FuncDecl:
                name = decl.name.name
                return_type = decl.return_type
                params = decl.params
                if type(decl) is FuncDecl and name == "main" and TypeUtils.isVoidType(return_type) and len(params) == 0:
                    has_entry_point = True
            self.visit(decl, (self.envs, None))

        if not has_entry_point:
            self.raise_(NoEntryPoint())

        print(self.envs)
        return ""

    def visitVarDecl(self, ast: VarDecl, c):
        (o, _) = c
        name = ast.name.name
        typ = ast.typ
        Search.check(name, o[0], lambda: self.raise_(
            Redeclared(Variable(), name)))

        if not TypeUtils.isNone(ast.init):
            if TypeUtils.isArrayType(typ):
                arr_dimensions = typ.dimensions
                arr_type = typ.typ
                self.illegal_array_literal = {
                    "type": arr_type, "dimensions": arr_dimensions, "ast": ast}
                init = self.visit(ast.init, (o, typ))
                dimension_lst = Array.getDimensions(init)
                if Array.isDimensionsMatched(arr_dimensions, dimension_lst, lambda: self.raise_(TypeMismatchInStatement(ast))):
                    o[0][name] = {
                        "type": typ, "kind": Variable(), "dimensions": dimension_lst}
                    self.illegal_array_literal = None
            else:
                init = self.visit(ast.init, (o, typ))
                init_type = init["type"]
                if TypeUtils.isIntType(init_type) and TypeUtils.isFloatType(typ):
                    o[0][name] = {
                        "type": FloatType(), "kind": Variable()}
                    return
                if not TypeUtils.isTheSameType(typ, init_type) and not TypeUtils.isAutoType(typ):
                    self.raise_(TypeMismatchInExpression(ast))

                o[0][name] = {"type": init_type if TypeUtils.isAutoType(
                    typ) else typ, "kind": Variable()}
        else:
            if TypeUtils.isAutoType(typ):
                self.raise_(Invalid(Variable(), name))

            o[0][name] = {"type": typ, "kind": Variable()}

    def visitParamDecl(self, ast: ParamDecl, c):
        (o, _) = c
        name = ast.name.name
        typ = ast.typ
        inherit = ast.inherit
        out = ast.out
        Search.check(name, o[0], lambda: self.raise_(
            Redeclared(Parameter(), name)))
        res = {"type": typ, "kind": Variable(),
               "inherit": inherit, "out": out}
        o[0][name] = res
        return res

    def visitFuncDecl(self, ast: FuncDecl, c):
        (o, _) = c
        self.is_func_decl = True
        name = ast.name.name
        params = ast.params
        return_type = ast.return_type
        inherit = ast.inherit
        body = ast.body
        Search.check(name, o, lambda: self.raise_(
            Redeclared(Function(), name)))
        o1 = [{}] + o

        o[0][name] = {"type": return_type, "kind": Function(
        ), "params": list(map(lambda el: self.visit(el, (o1, None)), params))}

        self.visit(body, (o1, None))
        self.is_func_decl = False

    def visitAssignStmt(self, ast: AssignStmt, c):
        (o, t) = c
        lhs = self.visit(ast.lhs, c)

        if TypeUtils.isArrayType(lhs["type"]) or TypeUtils.isVoidType(lhs["type"]):
            self.raise_(TypeMismatchInStatement(ast))

        rhs = self.visit(ast.rhs, c)
        if TypeUtils.isAutoType(rhs["type"]):
            # func = TypeUtils.inferType(name, c, lambda: self.raise_(
            #     Undeclared(Function(), name)), Function)
            pass

        else:
            if not (TypeUtils.isFloatType(lhs["type"]) and TypeUtils.isIntType(rhs["type"])):
                if not TypeUtils.isTheSameType(lhs["type"], rhs["type"]):
                    self.raise_(TypeMismatchInStatement(ast))

    def visitBlockStmt(self, ast: BlockStmt, c):
        (o, t) = c
        reduce(lambda _, el: self.visit(
            el, (o if self.is_func_decl else [{}] + o, t)), ast.body, [])

    def visitIfStmt(self, ast: IfStmt, c):
        condition = self.visit(ast.cond, c)
        if not TypeUtils.isBoolType(condition["type"]):
            self.raise_(TypeMismatchInStatement(ast))

        self.visit(ast.tstmt, c)
        if not TypeUtils.isNone(ast.fstmt):
            self.visit(ast.fstmt, c)

    def visitForStmt(self, ast: ForStmt, c):
        # condition = self.visit(ast.cond, c)
        # if not TypeUtils.isBoolType(condition["type"]):
        #     self.raise_(TypeMismatchInStatement(ast))

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

    def visitBinExpr(self, ast: BinExpr, c):
        (o, t) = c
        left_expr = self.visit(ast.left, c)
        right_expr = self.visit(ast.right, c)
        left_type = left_expr["type"]
        right_type = right_expr["type"]
        op = ast.op

        if isinstance(ast.right, FuncCall) or isinstance(ast.left, FuncCall):
            if TypeUtils.isAutoType(right_type) and TypeUtils.isAutoType(left_type):
                right_type = TypeUtils.inferType(
                    right_expr["name"], t, o, Function)["type"]
                left_type = TypeUtils.inferType(
                    left_expr["name"], t, o, Function)["type"]
            elif TypeUtils.isAutoType(left_type):
                left_type = TypeUtils.inferType(
                    left_expr["name"], right_type, o, Function)["type"]
            elif TypeUtils.isAutoType(right_type):
                right_type = TypeUtils.inferType(
                    right_expr["name"], left_type, o, Function)["type"]

        if op in ["+", "-", "*", "/"]:
            if not TypeUtils.isInListType(left_type, [IntegerType, FloatType]) or not TypeUtils.isInListType(right_type, [IntegerType, FloatType]):
                self.raise_(TypeMismatchInExpression(ast))

            if TypeUtils.isFloatType(left_type) or TypeUtils.isFloatType(right_type):
                return {"type": FloatType()}
            return {"type": IntegerType()}

        if op == "%":
            if not TypeUtils.isIntType(left_type) or not TypeUtils.isIntType(right_type):
                self.raise_(TypeMismatchInExpression(ast))
            return {"type": IntegerType()}

        if op == "::":
            if not TypeUtils.isStringType(left_type) or not TypeUtils.isStringType(right_type):
                self.raise_(TypeMismatchInExpression(ast))
            return {"type": StringType()}

        if op in ["==", "!="]:
            if not TypeUtils.isInListType(left_type, [IntegerType, BooleanType]) or not TypeUtils.isInListType(right_type, [IntegerType, BooleanType]):
                self.raise_(TypeMismatchInExpression(ast))

            if (TypeUtils.isIntType(left_type) and TypeUtils.isIntType(right_type)) or (TypeUtils.isBoolType(left_type) and TypeUtils.isBoolType(right_type)):
                return {"type": BooleanType()}

            self.raise_(TypeMismatchInExpression(ast))

        if op in ["<", ">", "<=", ">="]:
            if not TypeUtils.isInListType(left_type, [IntegerType, FloatType]) or not TypeUtils.isInListType(right_type, [IntegerType, FloatType]):
                self.raise_(TypeMismatchInExpression(ast))

            if (TypeUtils.isIntType(left_type) and TypeUtils.isIntType(right_type)) or (TypeUtils.isFloatType(left_type) and TypeUtils.isFloatType(right_type)):
                return {"type": BooleanType()}

            self.raise_(TypeMismatchInExpression(ast))

        if op in ["&&", "||"]:
            if not TypeUtils.isBoolType(left_type) or not TypeUtils.isBoolType(right_type):
                self.raise_(TypeMismatchInExpression(ast))
            return {"type": BooleanType()}

    def visitUnExpr(self, ast: UnExpr, c):
        (o, t) = c
        expr = self.visit(ast.val, c)
        op = ast.op
        typ = expr["type"]
        if op == "!":
            if not TypeUtils.isBoolType(typ) or not TypeUtils.isBoolType(typ):
                self.raise_(TypeMismatchInExpression(ast))
            return {"type": BooleanType()}
        if op == "-":
            if not TypeUtils.isInListType(typ, [IntegerType, FloatType]):
                self.raise_(TypeMismatchInExpression(ast))
            return {"type": typ}

    def visitId(self, ast: Id, c):
        (o, _) = c
        return Search.search(ast.name, o[0], lambda: self.raise_(
            Undeclared(Identifier(), ast.name)), Variable)

    def visitArrayCell(self, ast: ArrayCell, c):
        id = self.visit(ast.name, c)
        if not TypeUtils.isArrayType(id["type"]):
            self.raise_(TypeMismatchInExpression(ast))

        reduce(lambda _, el: self.raise_(TypeMismatchInExpression(ast))
               if not TypeUtils.isIntType(self.visit(el, c)["type"]) else None, ast.cell, [])

        return {"type": id["type"]}

    def visitIntegerLit(self, ast: IntegerLit, c):
        return {"type": IntegerType()}

    def visitFloatLit(self, ast: FloatLit, c):
        return {"type": FloatType()}

    def visitStringLit(self, ast: StringLit, c):
        return {"type": StringType()}

    def visitBooleanLit(self, ast: BooleanLit, c):
        return {"type": BooleanType()}

    def visitArrayLit(self, ast: ArrayLit, c):
        expr_list = ast.explist

        result = list(map(lambda exp: self.visit(exp, c), expr_list))
        if len(result) != 0:
            first_el_type = result[0]["type"]
            list(map(lambda res: self.raise_(IllegalArrayLiteral(
                ast)) if not TypeUtils.isTheSameType(res["type"] if not TypeUtils.isArrayType(res["type"]) else res["type"].typ, first_el_type) else None, result))

            for res in result:
                res_type = res["type"] if not TypeUtils.isArrayType(
                    res["type"]) else res["type"].typ
                if (not TypeUtils.isTheSameType(self.illegal_array_literal["type"], res_type)) and (not (TypeUtils.isFloatType(
                        self.illegal_array_literal["type"]) and TypeUtils.isIntType(res_type))) and not TypeUtils.isArray(res_type):
                    self.raise_(TypeMismatchInStatement(
                        self.illegal_array_literal["ast"]))
            # list(map(lambda res: self.raise_(TypeMismatchInStatement(
            #     self.illegal_array_literal["ast"])) if (not TypeUtils.isTheSameType(self.illegal_array_literal["type"], res["type"])) and (not (TypeUtils.isFloatType(
            #         self.illegal_array_literal["type"]) and TypeUtils.isIntType(res["type"]))) and not TypeUtils.isArray(res["type"]) else None, result))
            return {"type": Array(len(expr_list), result)}
        return {"type": Array(0, [])}

    def visitFuncCall(self, ast: FuncCall, c):
        print("============================= FuncCall")
        (o, t) = c
        name = ast.name.name
        func = Search.search(name, o, lambda: self.raise_(
            Undeclared(Function(), name)), Function)
        params = func["params"]
        # args = list(map(lambda x: self.visit(x, c), ast.args))
        if len(ast.args) != len(params) or TypeUtils.isVoidType(func["type"]):
            self.raise_(TypeMismatchInExpression(ast))
        # for el in zip(params, args):
        for el in zip(params, ast.args):
            el_type = self.visit(el[1], (o, el[0]["type"]))["type"]

            # if TypeUtils.isAutoType(func_type):
            #     func_type = TypeUtils.inferType(
            #         name, el[1]["type"], o, Function)
            if not TypeUtils.isTheSameType(el[0]["type"], el_type):
                self.raise_(TypeMismatchInExpression(ast))
        # reduce(lambda _, el: self.raise_(TypeMismatchInExpression(ast)) if TypeUtils.isTheSameType(
        #     el[0]["type"], el[1]["type"]) else None, zip(params, args), [])
        if TypeUtils.isAutoType(func["type"]):
            func["type"] = TypeUtils.inferType(name, t, o, Function)["type"]
        print("======================= End FuncCall")
        return {"type": func["type"], "name": name}

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
