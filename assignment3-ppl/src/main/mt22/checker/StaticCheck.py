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
    def __init__(self, val: int, el: Type) -> None:
        self.val = val
        self.el = el

    def __str__(self):
        return "Array({}, {})".format(str(self.val), str(self.el))

    # Array(2, Array(3, IntegerType)) -> [2, 3]
    @ staticmethod
    def getDimensions(arr):
        if not TypeUtils.isArray(arr):
            return [arr]

        return [arr.val, *Array.getDimensions(arr.el)]

    @ staticmethod
    def isDimensionsMatched(dimen1, dimen2, func):
        if (len(dimen1) != len(dimen2)):
            func()
        # for d1, d2 in zip(dimen1, dimen2):
        #     if int(d1) < d2:
        #         func()
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
    def isArrayCell(x):
        return type(x) is ArrayCell

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
    @ staticmethod
    def search(name, lst, func, kind=Variable):
        for x in lst:
            if name in x and isinstance(x[name]["kind"], kind):
                return x[name]
        return func()

    @ staticmethod
    def check(name, dic, func) -> None:
        if name in dic:
            func()


class StaticChecker(BaseVisitor, Utils):

    global_envi = [
        Symbol("readInteger", MType([], IntegerType())),
        Symbol("printInteger", MType([IntegerType()], VoidType())),
        Symbol("readFloat", MType([], FloatType())),
        Symbol("writeFloat", MType([FloatType()], VoidType())),
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
        self.func_decl = {"flag": False, "return_type": None,
                          "name": None, "inherit": {"func": None, "super_or_preventDefault": None}, "has_first_stmt_return": False}
        self.loop = {"flag": False, "ast": None}
        self.if_stmt = []
        self.for_loop = []
        self.while_loop = []
        self.do_while_loop = []

    def addElToIf(self, el):
        self.if_stmt.append(el)

    def addElToForLoop(self, el):
        self.for_loop.append(el)

    def addElToWhileLoop(self, el):
        self.while_loop.append(el)

    def addElToDoWhileLoop(self, el):
        self.do_while_loop.append(el)

    def removeElFromIf(self):
        self.if_stmt.pop()

    def removeElFromForLoop(self):
        self.for_loop.pop()

    def removeElFromWhileLoop(self):
        self.while_loop.pop()

    def removeElFromDoWhileLoop(self):
        self.do_while_loop.pop()

    def getSizeForLoop(self):
        return len(self.for_loop)

    def getSizeWhileLoop(self):
        return len(self.while_loop)

    def getSizeDoWhileLoop(self):
        return len(self.do_while_loop)

    def getSizeIf(self):
        return len(self.if_stmt)

    def setLoop(self, flag, ast):
        self.loop["flag"] = flag
        self.loop["ast"] = ast

    def resetLoop(self):
        self.loop["flag"] = False
        self.loop["ast"] = None

    def setFunc_decl(self, flag, return_type, name):
        self.func_decl["flag"] = flag
        self.func_decl["return_type"] = return_type
        self.func_decl["name"] = name

    def resetFunc_decl(self):
        self.func_decl = {"flag": False, "return_type": None,
                          "name": None, "inherit": {"func": None, "super_or_preventDefault": None}, "has_first_stmt_return": False}

    def check(self):
        return self.visit(self.ast, StaticChecker.global_envi)

    def checkValidInherit(self, name, o, typ):
        if not TypeUtils.isNone(self.func_decl["inherit"]["func"]) and self.func_decl["inherit"]["super_or_preventDefault"] == "super":
            func = Search.search(
                self.func_decl["inherit"]["func"]["name"], o, None, Function)
            param = self.lookup(
                name, func["params_inherit"], lambda par: par["name"])
            if not TypeUtils.isNone(param) and param["inherit"]:
                self.raise_(Invalid(Parameter(), name))

    def raise_(self, ex):
        raise ex

    def visitProgram(self, ast: Program, c):
        for decl in ast.decls:
            if type(decl) is FuncDecl:
                return_type = decl.return_type
                params = []
                Search.check(decl.name, self.envs[0], lambda: self.raise_(
                    Redeclared(Function(), decl.name)))
                for el in decl.params:
                    for p in params:
                        if p["name"] == el.name:
                            self.raise_(Redeclared(Parameter(), el.name))

                    par = {"type": el.typ, "kind": Variable(),
                           "inherit": el.inherit, "out": el.out, "name": el.name}
                    params.append(par)

                self.envs[0][decl.name] = {"type": return_type, "kind": Function(
                ), "params": params}

        has_entry_point = False
        for decl in ast.decls:
            if type(decl) is FuncDecl:
                return_type = decl.return_type
                params = decl.params
                if type(decl) is FuncDecl and decl.name == "main" and TypeUtils.isVoidType(return_type) and len(params) == 0:
                    has_entry_point = True
            self.visit(decl, (self.envs, None))

        if not has_entry_point:
            self.raise_(NoEntryPoint())

        return ""

    def visitVarDecl(self, ast: VarDecl, c):
        (o, _) = c
        name = ast.name
        Search.check(name, o[0], lambda: self.raise_(
            Redeclared(Variable(), name)))
        typ = ast.typ
        # self.checkValidInherit(name, o, Variable())

        if not TypeUtils.isNone(ast.init):

            if TypeUtils.isArrayLit(ast.init):
                self.illegal_array_literal = {
                    "type": typ, "ast": ast, "astInit": ast.init}

            if TypeUtils.isArrayType(typ):
                arr_dimensions = typ.dimensions
                arr_type = typ.typ
                self.illegal_array_literal = {
                    "type": arr_type, "ast": ast, "astInit": ast.init}

                if not TypeUtils.isArrayLit(ast.init) and not TypeUtils.isArrayCell(ast.init):
                    self.raise_(TypeMismatchInVarDecl(ast))

                init = self.visit(ast.init, (o, arr_type))
                dimension_lst = Array.getDimensions(init["type"])
                dimension_lst = dimension_lst[:-1]

                if Array.isDimensionsMatched(arr_dimensions, dimension_lst, lambda: self.raise_(TypeMismatchInVarDecl(ast))):
                    o[0][name] = {
                        "type": typ, "kind": Variable(), "dimensions": dimension_lst}
                self.illegal_array_literal = None
            else:

                init = self.visit(ast.init, (o, typ))
                init_type = init["type"]
                if TypeUtils.isAutoType(init_type):
                    init["type"] = typ
                    o[0][name] = {"type":  typ, "kind": Variable()}
                    return

                if TypeUtils.isAutoType(typ):
                    if TypeUtils.isArray(init_type):
                        init_type = Array.getDimensions(init_type)[-1]
                    o[0][name] = {"type":  init_type, "kind": Variable()}
                    return

                if TypeUtils.isArrayLit(ast.init):
                    self.raise_(TypeMismatchInVarDecl(ast))

                if TypeUtils.isIntType(init_type) and TypeUtils.isFloatType(typ):
                    o[0][name] = {
                        "type": FloatType(), "kind": Variable()}
                    return

                if not TypeUtils.isTheSameType(typ, init_type):
                    self.raise_(TypeMismatchInVarDecl(ast))

                o[0][name] = {"type": init_type, "kind": Variable()}
                self.illegal_array_literal = None
        else:
            if TypeUtils.isAutoType(typ):
                self.raise_(Invalid(Variable(), name))

            o[0][name] = {"type": typ, "kind": Variable()}
            self.illegal_array_literal = None

    def visitParamDecl(self, ast: ParamDecl, c):
        (o, _) = c
        name = ast.name
        if name in o[0]:
            if o[0][name]["inherit"]:
                self.raise_(Invalid(Parameter(), name))

        typ = ast.typ
        inherit = ast.inherit
        out = ast.out

        res = {"type": typ, "kind": Variable(),
               "inherit": inherit, "out": out}
        o[0][name] = res
        res["name"] = name
        return res

    def visitFuncDecl(self, ast: FuncDecl, c):
        (o, _) = c

        name = ast.name
        symbol = self.lookup(
            name, StaticChecker.global_envi, lambda sym: sym.name)
        if not TypeUtils.isNone(symbol):
            self.raise_(Redeclared(Function(), name))

        return_type = ast.return_type
        inherit = ast.inherit
        body = ast.body
        o1 = [{}] + o
        self.setFunc_decl(True, {"type": return_type}, name)

        if not TypeUtils.isNone(inherit):
            inherit_func = Search.search(inherit, o1, lambda: self.raise_(
                Undeclared(Function(), inherit)), Function)

            if len(inherit_func["params"]) != 0:
                for p in inherit_func["params"]:
                    if p["inherit"]:
                        o1[0][p["name"]] = p

                for el in ast.params:
                    par = self.visit(el, (o1, None))

                if len(body.body) == 0:
                    self.raise_(InvalidStatementInFunction(name))

                first_stmt = body.body[0]

                if not isinstance(first_stmt, CallStmt):
                    self.raise_(InvalidStatementInFunction(name))

                first_stmt_name = first_stmt.name
                if first_stmt_name != "super" and first_stmt_name != "preventDefault":
                    self.raise_(InvalidStatementInFunction(name))
                self.func_decl["inherit"]["super_or_preventDefault"] = "preventDefault" if first_stmt_name == "preventDefault" else "super" if first_stmt_name == "super" else None
            else:
                for el in ast.params:
                    par = self.visit(el, (o1, None))

                if len(body.body) != 0:
                    first_stmt = body.body[0]
                    if isinstance(first_stmt, CallStmt):
                        first_stmt_name = first_stmt.name
                        self.func_decl["inherit"]["super_or_preventDefault"] = "preventDefault" if first_stmt_name == "preventDefault" else "super" if first_stmt_name == "super" else None
                    else:
                        self.func_decl["inherit"]["super_or_preventDefault"] = "super"

            self.func_decl["inherit"]["func"] = {
                **inherit_func, **{"name": inherit}}
        else:
            for el in ast.params:
                par = self.visit(el, (o1, None))

        self.visit(body, (o1, None))
        self.resetFunc_decl()

    def visitAssignStmt(self, ast: AssignStmt, c):
        (o, _) = c
        lhs_type = None
        lhs_expr = None
        if self.loop["flag"]:
            name = ast.lhs.name
            id = Search.search(name, o, lambda: None, Variable)
            if TypeUtils.isNone(id):
                o[0][name] = {
                    "type": IntegerType(), "kind": Variable()}
                lhs_type = IntegerType()
            else:
                if TypeUtils.isAutoType(id["type"]):
                    id["type"] = IntegerType()
                else:
                    if not TypeUtils.isIntType(id["type"]):
                        self.raise_(TypeMismatchInStatement(self.loop["ast"]))
                lhs_type = id["type"]
        else:
            lhs_expr = self.visit(ast.lhs, c)
            lhs_type = lhs_expr["type"]
            if TypeUtils.isArrayType(lhs_type) or TypeUtils.isVoidType(lhs_type):
                self.raise_(TypeMismatchInStatement(ast))

        rhs_expr = self.visit(ast.rhs, (o, lhs_type))
        rhs_type = rhs_expr["type"]

        if TypeUtils.isAutoType(lhs_type):
            lhs_expr["type"] = lhs_type = rhs_type
        elif TypeUtils.isAutoType(rhs_type):
            rhs_expr["type"] = rhs_type = lhs_type

        if not (TypeUtils.isFloatType(lhs_type) and TypeUtils.isIntType(rhs_type)):
            if not TypeUtils.isTheSameType(lhs_type, rhs_type):
                self.raise_(TypeMismatchInStatement(
                    ast if not self.loop["flag"] else self.loop["ast"]))

    def visitBlockStmt(self, ast: BlockStmt, c):
        (o, t) = c
        reduce(lambda _, el: self.visit(
            el, (o if self.func_decl["flag"] or self.loop["flag"] else [{}] + o, t)), ast.body, [])

    def visitIfStmt(self, ast: IfStmt, c):
        self.addElToIf(True)
        condition = self.visit(ast.cond, c)
        if not TypeUtils.isBoolType(condition["type"]):
            self.raise_(TypeMismatchInStatement(ast))

        self.visit(ast.tstmt, c)
        if not TypeUtils.isNone(ast.fstmt):
            self.visit(ast.fstmt, c)

        self.removeElFromIf()

    def visitForStmt(self, ast: ForStmt, c):
        (o, t) = c
        self.setLoop(True, ast)
        self.addElToForLoop(True)
        o1 = [{}] + o

        self.visit(ast.init, (o1, t))
        self.resetLoop()

        condition_expr = self.visit(ast.cond, (o1, t))
        condition_type = condition_expr["type"]
        if TypeUtils.isAutoType(condition_type):
            condition_type = condition_expr["type"] = BooleanType()

        if not TypeUtils.isBoolType(condition_type):
            self.raise_(TypeMismatchInStatement(ast))

        upd_type = self.visit(ast.upd, (o1, t))["type"]
        if not TypeUtils.isIntType(upd_type):
            self.raise_(TypeMismatchInStatement(ast))

        self.visit(ast.stmt, (o1, t))
        self.removeElFromForLoop()

    def visitWhileStmt(self, ast: WhileStmt, c):
        self.addElToWhileLoop(True)

        condition_expr = self.visit(ast.cond, c)
        condition_type = condition_expr["type"]
        if TypeUtils.isAutoType(condition_type):
            condition_type = condition_expr["type"] = BooleanType()

        if not TypeUtils.isBoolType(condition_type):
            self.raise_(TypeMismatchInStatement(ast))
        self.visit(ast.stmt, c)
        self.removeElFromWhileLoop()

    def visitDoWhileStmt(self, ast: DoWhileStmt, c):
        self.addElToDoWhileLoop(True)
        self.visit(ast.stmt, c)

        condition_expr = self.visit(ast.cond, c)
        condition_type = condition_expr["type"]
        if TypeUtils.isAutoType(condition_type):
            condition_type = condition_expr["type"] = BooleanType()

        if not TypeUtils.isBoolType(condition_type):
            self.raise_(TypeMismatchInStatement(ast))
        self.removeElFromDoWhileLoop()

    def visitBreakStmt(self, ast: BreakStmt, c):
        if self.getSizeForLoop() == 0 and self.getSizeWhileLoop() == 0 and self.getSizeDoWhileLoop() == 0:
            self.raise_(MustInLoop(ast))

    def visitContinueStmt(self, ast: ContinueStmt, c):
        if self.getSizeForLoop() == 0 and self.getSizeWhileLoop() == 0 and self.getSizeDoWhileLoop() == 0:
            self.raise_(MustInLoop(ast))

    def visitReturnStmt(self, ast: ReturnStmt, c):
        (o, _) = c

        if self.func_decl["flag"]:
            func_type = self.func_decl["return_type"]["type"]

            expr = None
            expr_type = VoidType()
            if not TypeUtils.isNone(ast.expr):
                expr = self.visit(ast.expr, c)
                expr_type = expr["type"]

            if TypeUtils.isAutoType(func_type):
                self.func_decl["return_type"] = TypeUtils.inferType(
                    self.func_decl["name"], expr_type, o, Function)
                func_type = self.func_decl["return_type"]["type"]

            elif TypeUtils.isAutoType(expr_type):
                expr_type = expr["type"] = func_type

            if self.getSizeForLoop() != 0 or self.getSizeWhileLoop() != 0 or self.getSizeDoWhileLoop() != 0 or self.getSizeIf() != 0:
                if not (TypeUtils.isFloatType(func_type) and TypeUtils.isIntType(expr_type)):
                    if not TypeUtils.isTheSameType(expr_type, func_type):
                        self.raise_(TypeMismatchInStatement(ast))
            else:
                if not self.func_decl["has_first_stmt_return"]:
                    if not (TypeUtils.isFloatType(func_type) and TypeUtils.isIntType(expr_type)):
                        if not TypeUtils.isTheSameType(expr_type, func_type):
                            self.raise_(TypeMismatchInStatement(ast))
                    self.func_decl["has_first_stmt_return"] = True

    def visitCallStmt(self, ast: CallStmt, c):
        (o, _) = c
        name = ast.name
        symbol = self.lookup(
            name, StaticChecker.global_envi, lambda sym: sym.name)
        params = None
        func_type = None
        func = dict()
        if TypeUtils.isNone(symbol):
            func = Search.search(name, o, lambda: self.raise_(
                Undeclared(Function(), name)), Function)
            func_type = func["type"]
            params = func["params"]

            # if TypeUtils.isAutoType(func_type):
            #     func["type"] = func_type = VoidType()
        else:
            if name == "super" or name == "preventDefault":
                if (self.func_decl["flag"] and TypeUtils.isNone(self.func_decl["inherit"]["func"])) or TypeUtils.isNone(self.func_decl["inherit"]["super_or_preventDefault"]):
                    self.raise_(InvalidStatementInFunction(
                        self.func_decl["name"]))
                params = self.func_decl["inherit"]["func"]["params"] if name == "super" else symbol.mtype.partype
            else:
                params = list(map(lambda par: self.visit(
                    par, c), symbol.mtype.partype))
            func_type = symbol.mtype.rettype

        if name != "super":
            if len(ast.args) != len(params):
                self.raise_(TypeMismatchInStatement(ast))
        else:
            if len(params) < len(ast.args):
                self.raise_(TypeMismatchInExpression(ast.args[len(params)]))

            if len(params) > len(ast.args):
                self.raise_(TypeMismatchInExpression(None))

        for el in zip(params, ast.args):
            el0_type = el[0]["type"]
            el_type = self.visit(el[1], (o, el0_type))["type"]

            if TypeUtils.isArray(el_type):
                el_type = Array.getDimensions(el_type)[-1]

            if TypeUtils.isAutoType(el0_type):
                el0_type = el[0]["type"] = el_type

            if not (TypeUtils.isFloatType(el0_type) and TypeUtils.isIntType(el_type)):
                if not TypeUtils.isAutoType(el0_type):
                    if not TypeUtils.isTheSameType(el0_type, el_type):
                        self.raise_(TypeMismatchInExpression(
                            el[1]) if name == "super" else TypeMismatchInStatement(ast))

        return {"type": func_type}

    def visitBinExpr(self, ast: BinExpr, c):
        (o, t) = c
        left_type = None
        right_type = None
        op = ast.op

        if isinstance(ast.right, FuncCall) and isinstance(ast.left, FuncCall):
            name_right = ast.right.name
            symbol_right = self.lookup(
                name_right, StaticChecker.global_envi, lambda sym: sym.name)
            func_right_type = Search.search(name_right, o, lambda: self.raise_(
                Undeclared(Function(), name_right)), Function)["type"] if TypeUtils.isNone(symbol_right) else symbol_right.mtype.rettype

            name_left = ast.left.name
            func_left_type = None
            symbol_left = self.lookup(
                name_left, StaticChecker.global_envi, lambda sym: sym.name)

            func_left_type = Search.search(name_left, o, lambda: self.raise_(
                Undeclared(Function(), name_left)), Function)["type"] if TypeUtils.isNone(symbol_left) else symbol_left.mtype.rettype

            if TypeUtils.isAutoType(func_right_type) and TypeUtils.isAutoType(func_left_type):
                left_type = self.visit(ast.left, c)["type"]
                right_type = self.visit(ast.right, c)["type"]
            elif TypeUtils.isAutoType(func_left_type):
                left_type = self.visit(ast.left, (o, func_right_type))["type"]
                right_type = func_right_type
            elif TypeUtils.isAutoType(func_right_type):
                right_type = self.visit(ast.right, (o, func_left_type))["type"]
                left_type = func_left_type
        elif isinstance(ast.right, FuncCall):
            name_right = ast.right.name
            symbol_right = self.lookup(
                name_right, StaticChecker.global_envi, lambda sym: sym.name)
            func_right_type = Search.search(name_right, o, lambda: self.raise_(
                Undeclared(Function(), name_right)), Function)["type"] if TypeUtils.isNone(symbol_right) else symbol_right.mtype.rettype
            left_type = self.visit(ast.left, c)["type"]
            right_type = self.visit(
                ast.right, (o, left_type if TypeUtils.isAutoType(func_right_type) else t))["type"]
        elif isinstance(ast.left, FuncCall):
            name_left = ast.left.name
            func_left_type = None
            symbol_left = self.lookup(
                name_left, StaticChecker.global_envi, lambda sym: sym.name)

            func_left_type = Search.search(name_left, o, lambda: self.raise_(
                Undeclared(Function(), name_left)), Function)["type"] if TypeUtils.isNone(symbol_left) else symbol_left.mtype.rettype
            right_type = self.visit(ast.right, c)["type"]
            left_type = self.visit(
                ast.left, (o, right_type if TypeUtils.isAutoType(func_left_type) else t))["type"]
        else:

            left_expr = self.visit(ast.left, c)
            left_type = left_expr["type"]

            right_expr = self.visit(ast.right, c)
            right_type = right_expr["type"]

            if TypeUtils.isAutoType(left_type):
                left_type = left_expr["type"] = right_type
            elif TypeUtils.isAutoType(right_type):
                right_type = right_expr["type"] = left_type

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

            # if (TypeUtils.isIntType(left_type) and TypeUtils.isIntType(right_type)) or (TypeUtils.isBoolType(left_type) and TypeUtils.isBoolType(right_type)):
            #     return {"type": BooleanType()}

            # self.raise_(TypeMismatchInExpression(ast))
            return {"type": BooleanType()}

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
        return Search.search(ast.name, o, lambda: self.raise_(
            Undeclared(Identifier(), ast.name)), Variable)

    def visitArrayCell(self, ast: ArrayCell, c):
        id = self.visit(Id(ast.name), c)
        if not TypeUtils.isArrayType(id["type"]) and not TypeUtils.isArray(id["type"]):
            self.raise_(TypeMismatchInExpression(ast))

        if TypeUtils.isArray(id["type"]):
            return {"type": id["type"]}

        reduce(lambda _, el: self.raise_(TypeMismatchInExpression(ast))
               if not TypeUtils.isIntType(self.visit(el, c)["type"]) else None, ast.cell, [])

        # [2, 2, 3] -> [2, 3] -> [3, 2] -> Array(2, Array(3, IntegerType))
        dimensions = id["type"].dimensions[len(ast.cell):][::-1]
        if (len(dimensions) != 0):
            res = reduce(lambda acc, el: Array(el, acc),
                         dimensions[1:], Array(dimensions[0], id["type"].typ if TypeUtils.isArrayType(id["type"]) else id["type"]))
            return {"type": res}

        return {"type": id["type"].typ}

    def visitIntegerLit(self, ast: IntegerLit, c):
        return {"type": IntegerType()}

    def visitFloatLit(self, ast: FloatLit, c):
        return {"type": FloatType()}

    def visitStringLit(self, ast: StringLit, c):
        return {"type": StringType()}

    def visitBooleanLit(self, ast: BooleanLit, c):
        return {"type": BooleanType()}

    def visitArrayLit(self, ast: ArrayLit, c):
        (o, typ) = c
        expr_list = ast.explist

        result = list(map(lambda exp: self.visit(exp, c), expr_list))
        # result [{'type': <StaticCheck.Array object at 0x7f5b774b2a40>}, {'type': <StaticCheck.Array object at 0x7f5b774b0640>}, {'type': <StaticCheck.Array object at 0x7f5b774b0100>}]
        if len(result) != 0:
            first_el_type = result[0]["type"]
            if TypeUtils.isArray(first_el_type):
                max_val = first_el_type
                for i in result:
                    if i["type"].val >= max_val.val:
                        max_val = i["type"]
                return {"type": Array(len(expr_list), max_val)}

            list(map(lambda res: self.raise_(IllegalArrayLiteral(
                self.illegal_array_literal["astInit"])) if not TypeUtils.isTheSameType(res["type"] if not TypeUtils.isArrayType(res["type"]) else res["type"].typ, first_el_type) else None, result))

            self.illegal_array_literal["first_el_type"] = first_el_type

            for res in result:
                res_type = res["type"] if not TypeUtils.isArrayType(
                    res["type"]) else res["type"].typ
                if not TypeUtils.isAutoType(typ):
                    if (not TypeUtils.isTheSameType(self.illegal_array_literal["type"], res_type)) and (not (TypeUtils.isFloatType(
                            self.illegal_array_literal["type"]) and TypeUtils.isIntType(res_type))) and not TypeUtils.isArray(res_type):
                        self.raise_(TypeMismatchInStatement(
                            self.illegal_array_literal["ast"]))

            return {"type": Array(len(expr_list), first_el_type)}
        return {"type": Array(0, typ)}

    def visitFuncCall(self, ast: FuncCall, c):
        (o, t) = c
        name = ast.name
        symbol = self.lookup(
            name, StaticChecker.global_envi, lambda sym: sym.name)
        params = None
        func_type = None
        func = dict()
        if TypeUtils.isNone(symbol):
            func = Search.search(name, o, lambda: self.raise_(
                Undeclared(Function(), name)), Function)
            func_type = func["type"]
            params = func["params"]

        else:
            if name == "super" or name == "preventDefault":
                if self.func_decl["flag"] and TypeUtils.isNone(self.func_decl["inherit"]["func"]):
                    self.raise_(InvalidStatementInFunction(
                        self.func_decl["name"]))
                params = self.func_decl["inherit"]["func"]["params"] if name == "super" else symbol.mtype.partype
            else:
                params = list(map(lambda par: self.visit(
                    par, c), symbol.mtype.partype))
            func_type = symbol.mtype.rettype

        if name != "super":
            if len(ast.args) != len(params) or TypeUtils.isVoidType(func_type):
                self.raise_(TypeMismatchInExpression(ast))
        else:
            if len(params) < len(ast.args):
                self.raise_(TypeMismatchInExpression(ast.args[len(params)]))

            if len(params) > len(ast.args):
                self.raise_(TypeMismatchInExpression(None))

        for el in zip(params, ast.args):

            el0_type = el[0]["type"]
            el_type = self.visit(el[1], (o, el0_type))["type"]
            if TypeUtils.isArray(el_type):
                el_type = Array.getDimensions(el_type)[-1]
            if TypeUtils.isAutoType(el0_type):
                el0_type = el[0]["type"] = el_type

            if not (TypeUtils.isFloatType(el0_type) and TypeUtils.isIntType(el_type)):
                if not TypeUtils.isAutoType(el0_type):
                    if not TypeUtils.isTheSameType(el0_type, el_type):
                        self.raise_(TypeMismatchInExpression(
                            el[1] if name == "super" else ast))

        if TypeUtils.isAutoType(func_type) and TypeUtils.isNone(symbol):
            func_type = TypeUtils.inferType(
                name, t, o, Function)["type"]
            func["type"] = func_type

        return {"type": func_type}

    def visitIntegerType(self, ast: IntegerType, c):
        return {"type": IntegerType()}

    def visitFloatType(self, ast: FloatType, c):
        return {"type": FloatType()}

    def visitStringType(self, ast: StringType, c):
        return {"type": StringType()}

    def visitBooleanType(self, ast: BooleanType, c):
        return {"type": BooleanType()}

    def visitArrayType(self, ast: ArrayType, c):
        return ast

    def visitAutoType(self, ast: AutoType, c):
        return {"type": AutoType()}

    def visitVoidType(self, ast: VoidType, c):
        return {"type": VoidType()}
