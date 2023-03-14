from Utils import *
from StaticCheck import *
from StaticError import *
from Emitter import Emitter
from Frame import Frame
from AST import *
from abc import ABC, abstractmethod
from functools import reduce


class TypeUtils:
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
    def isStringType(x):
        return type(x) is StringType

    @ staticmethod
    def isVoidType(x):
        return type(x) is VoidType

    @ staticmethod
    def isNone(x):
        return type(x) is type(None)

    @staticmethod
    def isTheSameType(x, y):
        return type(x) is y

    @staticmethod
    def mergeType(lType, rType):
        return FloatType() if FloatType in [type(x) for x in [lType, rType]] else IntegerType()

    @staticmethod
    def retrieveType(originType):
        if TypeUtils.isArrayType(originType):
            return ArrayPointerType(originType.typ)
        return originType


class OUtils:
    @staticmethod
    def isArithmeticOp(op):
        return str(op).lower() in ["+", "-", "*", "/", "%"]

    @staticmethod
    def isRelationalOp(op):
        return str(op).lower() in ["!=", "==", ">", "<", ">=", "<="]

    @staticmethod
    def isBooleanOp(op):
        return str(op).lower() in ["&&", "||"]

    @staticmethod
    def convertStringCode(s):
        return s.replace("\tldc ", "").replace("\"", "").replace("\n", "")


class CodeGenerator(Utils):
    def __init__(self):
        self.libName = "io"

    def init(self):
        return [
            Symbol("readInteger", MType([], IntegerType()), CName(self.libName)),
            Symbol("printInteger", MType(
                [IntegerType()], VoidType()), CName(self.libName)),
            Symbol("readFloat", MType([], FloatType()), CName(self.libName)),
            Symbol("writeFloat", MType(
                [FloatType()], VoidType()), CName(self.libName)),
            Symbol("readBoolean", MType([], BooleanType()), CName(self.libName)),
            Symbol("printBoolean", MType(
                [BooleanType()], VoidType()), CName(self.libName)),
            Symbol("readString", MType([], StringType()), CName(self.libName)),
            Symbol("printString", MType(
                [StringType()], VoidType()), CName(self.libName)),
            # Symbol("super", MType([[Expr()]], VoidType()),
            #        CName(self.libName)),
            # Symbol("preventDefault", MType(
            #     [], VoidType()), CName(self.libName)),
        ]

    def gen(self, ast, dir_):
        # ast: AST
        # dir_: String

        gl = self.init()
        gc = CodeGenVisitor(ast, gl, dir_)
        gc.visit(ast, None)


# class StringType(Type):

#     def __str__(self):
#         return "StringType"

#     # def accept(self, v, param):
#     #     return None


class ArrayPointerType(Type):
    def __init__(self, ctype, lst=[]):
        # cname: String
        self.eleType = ctype
        self.lst = lst

    def __str__(self):
        return "ArrayPointerType({0})".format(str(self.eleType))

    # def accept(self, v, param):
    #     return None


class ClassType(Type):
    def __init__(self, cname):
        self.cname = cname

    def __str__(self):
        return "Class({0})".format(str(self.cname))

    # def accept(self, v, param):
    #     return None


class SubBody():
    def __init__(self, frame, sym, isGlobal=False, isBlockStmt=False):
        # frame: Frame
        # sym: List[Symbol]

        self.frame = frame
        self.sym = sym
        self.isGlobal = isGlobal
        self.isBlockStmt = isBlockStmt


class Access():
    def __init__(self, frame, sym, isLeft, isFirst, arr=list()):
        # frame: Frame
        # sym: List[Symbol]
        # isLeft: Boolean
        # isFirst: Boolean

        self.frame = frame
        self.sym = sym
        self.isLeft = isLeft
        self.isFirst = isFirst
        self.arr = arr


class Val(ABC):
    pass


class Index(Val):
    def __init__(self, value):
        # value: Int

        self.value = value


class CName(Val):
    def __init__(self, value):
        # value: String

        self.value = value


class CodeGenVisitor(BaseVisitor, Utils):
    def __init__(self, astTree, env, dir_):
        # astTree: AST
        # env: List[Symbol]
        # dir_: File

        self.astTree = astTree
        self.env = env
        # self.className = "BKOOLClass"
        self.className = "MT22Class"
        self.path = dir_
        self.emit = Emitter(self.path + "/" + self.className + ".j")
        self.arr_idx_global = 0

        # self.var_decl_codes = []

    def genMETHOD(self, decl: FuncDecl, o, frame: Frame, global_vardecl_codes: list or None):
        # decl: FuncDecl
        # o: Any
        # frame: Frame
        func_name = decl.name.name
        func_type = decl.return_type

        isInit = TypeUtils.isNone(func_type) and func_name == "<init>"
        isClassInit = TypeUtils.isNone(func_type) and func_name == "<clinit>"

        isMain = func_name == "main" and len(
            decl.params) == 0 and TypeUtils.isVoidType(func_type)
        returnType = VoidType() if isInit or isClassInit else func_type
        isProc = TypeUtils.isVoidType(returnType)
        intype = [ArrayPointerType(StringType())] if isMain else list()
        mtype = MType(intype, returnType)

        self.emit.printout(self.emit.emitMETHOD(
            func_name, mtype, not isInit, frame))

        frame.enterScope(False if isClassInit else isProc)

        glenv = o

        # Generate code for parameter declarations
        if isInit:
            self.emit.printout(self.emit.emitVAR(frame.getNewIndex(), "this", ClassType(
                self.className), frame.getStartLabel(), frame.getEndLabel(), frame))
        if isMain:
            self.emit.printout(self.emit.emitVAR(frame.getNewIndex(), "args", ArrayPointerType(
                StringType()), frame.getStartLabel(), frame.getEndLabel(), frame))

        block = decl.body
        self.emit.printout(self.emit.emitLABEL(frame.getStartLabel(), frame))

        # Generate code for statements
        if isInit:
            self.emit.printout(self.emit.emitREADVAR(
                "this", ClassType(self.className), 0, frame))
            self.emit.printout(self.emit.emitINVOKESPECIAL(frame))

        if isClassInit:
            if not TypeUtils.isNone(global_vardecl_codes):
                for var_code in global_vardecl_codes:
                    # var_code = (jcode, MT22Class.<atr_name>, Type)
                    print(TypeUtils.isTheSameType(
                        var_code[2], ArrayPointerType))
                    if TypeUtils.isTheSameType(var_code[2], ArrayPointerType):
                        self.emit.printout(var_code[0])
                    else:
                        self.emit.printout(
                            var_code[0] + self.emit.emitPUTSTATIC(var_code[1], var_code[2], frame))

                # list(map(lambda var_code: self.emit.printout(
                #     var_code[0] + self.emit.emitPUTSTATIC(var_code[1], var_code[2], frame)), global_vardecl_codes))

        self.visit(block, SubBody(frame, glenv, isInit))

        self.emit.printout(self.emit.emitLABEL(frame.getEndLabel(), frame))

        if isProc:
            self.emit.printout(self.emit.emitRETURN(VoidType(), frame))

        self.emit.printout(self.emit.emitENDMETHOD(frame))
        frame.exitScope()

    def handelCall(self, ast: FuncCall or CallStmt, frame, symbols, isStmt=False):
        func_name = ast.name.name
        symbol = self.lookup(func_name, symbols, lambda sym: sym.name)
        cname = symbol.value.value
        ctype = symbol.mtype
        params_code = ""
        for p in ast.args:
            params_code += self.visit(p, Access(frame,
                                      symbols, False, True))[0]

        if isStmt:
            self.emit.printout(params_code + self.emit.emitINVOKESTATIC(
                cname + "/" + func_name, ctype, frame))

    def visitProgram(self, ast: Program, c):
        print(ast)
        self.emit.printout(self.emit.emitPROLOG(
            self.className, "java.lang.Object"))
        frame_clinit = Frame("<clinit>", VoidType)
        e = SubBody(frame_clinit, self.env, True)

        var_decl_codes = []
        for x in ast.decls:
            if not TypeUtils.isTheSameType(x, FuncDecl):
                e, jcode_0, var = self.visit(x, e)
                self.emit.printout(jcode_0)
                if not TypeUtils.isNone(var):
                    # self.var_decl_codes.append(var)
                    var_decl_codes.append(var)

        for x in ast.decls:
            if TypeUtils.isTheSameType(x, FuncDecl):
                e = self.visit(x, e)

        # generate default constructor
        self.genMETHOD(FuncDecl(Id("<init>"), None, list(), None,
                       BlockStmt(list())), e.sym, Frame("<init>", VoidType), None)

        # class init - static field
        self.genMETHOD(FuncDecl(Id("<clinit>"), None, list(), None,
                       BlockStmt(list())), e.sym, frame_clinit, var_decl_codes)

        self.emit.emitEPILOG()
        return c

    def visitVarDecl(self, ast: VarDecl, c: SubBody):
        print(ast)
        frame = c.frame
        sym = c.sym
        isGlobal = c.isGlobal
        var_name = ast.name.name
        var_type = ast.typ

        init_code, init_type = "", None

        if isGlobal:
            if not TypeUtils.isNone(ast.init):
                if TypeUtils.isArrayType(var_type):
                    # init = (jcode, Type)
                    dimens_size, dimens, arr_type = self.visit(
                        var_type, None)
                    cur_dimen, cur_idx = 0, 0
                    # arr = [0, dimens, cur_dimen, cur_idx]
                    arr = [dimens, cur_dimen]
                    arr_code = ""
                    arr_list_codes = self.visit(
                        ast.init, Access(frame, sym, False, False, arr))
                    self.arr_idx_global = 0
                    list(map(lambda el: arr_code, arr_list_codes))
                    arr_code = reduce(lambda acc, el: acc + self.emit.emitDUP(frame) + self.emit.emitPUSHICONST(
                        el[1], frame) + el[0] + self.emit.emitASTORE(arr_type,  frame), arr_list_codes, "")

                    init_code = self.emit.emitInitNewArray(
                        {"name": self.className+"."+var_name, "isStatic": True}, dimens_size, arr_type, frame,  arr_code)
                else:
                    init_code, init_type = self.visit(
                        ast.init, Access(frame, sym, False, False))

            return SubBody(frame, [Symbol(var_name, var_type, CName(self.className))] + sym, True), self.emit.emitATTRIBUTE(
                var_name, TypeUtils.retrieveType(var_type), False), (init_code, f"{self.className}.{var_name}", TypeUtils.retrieveType(var_type)) if not TypeUtils.isNone(init_code) else None

        idx = frame.getNewIndex()

        self.emit.printout(self.emit.emitVAR(
            idx, var_name, TypeUtils.retrieveType(var_type), frame.getStartLabel(), frame.getEndLabel(), frame))

        new_sym = [Symbol(var_name, var_type, Index(idx))] + sym
        id = self.visit(ast.name, Access(frame, new_sym, True, False))
        if not TypeUtils.isNone(ast.init):
            self.emit.printout(init[0] + id[0])

        return SubBody(frame,  new_sym)

    def visitParamDecl(self, ast: ParamDecl, c: SubBody):
        pass

    def visitFuncDecl(self, ast: FuncDecl, c: SubBody):
        sym = c.sym
        name = ast.name.name
        frame = Frame(name, ast.return_type)
        self.genMETHOD(ast, sym, frame, None)
        return SubBody(frame, [Symbol(name, MType(list(), ast.return_type), CName(self.className))] + sym)

    def visitAssignStmt(self, ast: AssignStmt, c):
        pass

    def visitBlockStmt(self, ast: BlockStmt, c: SubBody):
        frame = c.frame
        glenv = c.sym
        isBlockStmt = c.isBlockStmt
        if isBlockStmt:
            frame.enterScope(False)
            self.emit.printout(self.emit.emitLABEL(
                frame.getStartLabel(), frame))
        sub_body = SubBody(frame, glenv)
        for s in ast.body:
            if TypeUtils.isTheSameType(s, VarDecl):
                sub_body = self.visit(s, sub_body)
            else:  # Statements
                self.visit(s, sub_body)
        if isBlockStmt:
            self.emit.printout(self.emit.emitLABEL(frame.getEndLabel(), frame))
            frame.exitScope()

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

    def visitCallStmt(self, ast: CallStmt, c: SubBody):
        frame = c.frame
        symbols = c.sym
        self.handelCall(ast, frame, symbols, True)

    def visitBinExpr(self, ast: BinExpr, c):
        frame = c.frame
        op = ast.op
        l_code, l_type = self.visit(ast.left, c)
        r_code, r_type = self.visit(ast.right, c)
        if OUtils.isArithmeticOp(op) or OUtils.isRelationalOp(op):
            mtype = FloatType() if op == "/" else TypeUtils.mergeType(l_type, r_type)
            if not TypeUtils.isTheSameType(mtype, type(l_type)):
                l_code += self.emit.emitI2F(frame)
            if not TypeUtils.isTheSameType(mtype, type(r_type)):
                r_code += self.emit.emitI2F(frame)
            if op in ["+", "-"]:
                return l_code + r_code + self.emit.emitADDOP(op, mtype, frame), mtype
            elif op in ["*", "/"]:
                return l_code + r_code + self.emit.emitMULOP(op, mtype, frame), mtype
            elif op == "%":
                return l_code + r_code + self.emit.emitMOD(frame), mtype
            else:  # ==, <, <=, >, >=, !=
                return l_code + r_code + self.emit.emitREOP(op, mtype, frame), BooleanType()
        elif OUtils.isBooleanOp(op):
            mtype = BooleanType()
            if op == "&&":
                return l_code + r_code + self.emit.emitANDOP(frame), mtype
            else:
                return l_code + r_code + self.emit.emitOROP(frame), mtype
        else:
            if op == "::":
                l_val = OUtils.convertStringCode(l_code)
                r_val = OUtils.convertStringCode(r_code)
                return self.visit(StringLit(l_val + r_val), c)

    def visitUnExpr(self, ast: UnExpr, c):
        frame = c.frame
        op = ast.op
        e_code, e_type = self.visit(ast.val, c)
        return e_code + (self.emit.emitNEGOP(e_type, frame) if op == "-" else self.emit.emitNOT(e_type, frame)), e_type

    def visitId(self, ast: Id, c: Access):
        frame = c.frame
        symbol = self.lookup(ast.name, c.sym, lambda sym: sym.name)
        sym_type = TypeUtils.retrieveType(symbol.mtype)
        if symbol is not None:
            if TypeUtils.isTheSameType(symbol.value, CName):
                # if type(symbol.value) is CName:
                return self.emit.emitGETSTATIC(f"{symbol.value.value}.{symbol.name}", sym_type, frame) if not c.isLeft else self.emit.emitPUTSTATIC(f"{symbol.value.value}.{symbol.name}", sym_type, frame), sym_type

            return self.emit.emitREADVAR(symbol.name, sym_type, symbol.value.value, frame) if not c.isLeft else self.emit.emitWRITEVAR(symbol.name, sym_type, symbol.value.value, frame), sym_type

    def visitArrayCell(self, ast: ArrayCell, c: Access):
        frame = c.frame
        sym = c.sym

        arr_code, arr_type = self.visit(
            ast.name, Access(frame, sym, False, False))
        print(arr_code, arr_type)
        # cell_code, cell_type = self.visit(ast.name, c)

    def visitIntegerLit(self, ast: IntegerLit, c: Access):
        frame = c.frame
        return self.emit.emitPUSHICONST(ast.val, frame), IntegerType()

    def visitFloatLit(self, ast: FloatLit, c: Access):
        frame = c.frame
        return self.emit.emitPUSHFCONST(str(ast.val), frame), FloatType()

    def visitStringLit(self, ast: StringLit, c: Access):
        frame = c.frame
        return self.emit.emitPUSHCONST(ast.val, StringType(), frame), StringType()

    def visitBooleanLit(self, ast: BooleanLit, c: Access):
        frame = c.frame
        return self.emit.emitPUSHICONST(str(ast.val).lower(), frame), BooleanType()

    def visitArrayLit(self, ast: ArrayLit, c: Access):
        frame = c.frame
        sym = c.sym
        cur_dimen = c.arr[1]
        if not TypeUtils.isTheSameType(ast.explist[0], ArrayLit):
            lst = []
            idx = 0
            for exp in ast.explist:
                lst.append([self.visit(exp, c)[0], self.arr_idx_global])
                idx += 1
                self.arr_idx_global += 1

            for _ in range(idx, c.arr[0][cur_dimen]):
                self.arr_idx_global += 1

            return lst

        cur_dimen += 1
        return reduce(lambda acc, el: acc + self.visit(el, Access(
            frame, sym, False, False, [c.arr[0], cur_dimen])), ast.explist[1:], self.visit(ast.explist[0], Access(
                frame, sym, False, False, [c.arr[0], cur_dimen])))

    def visitFuncCall(self, ast: FuncCall, c):
        pass

    def visitIntegerType(self, ast: IntegerType, c):
        pass

    def visitFloatType(self, ast: FloatType, c):
        pass

    def visitStringType(self, ast: StringType, c):
        pass

    def visitBooleanType(self, ast: BooleanType, c):
        pass

    def visitArrayType(self, ast: ArrayType, c):
        return reduce(lambda acc, el: int(el) * int(acc), ast.dimensions[1:], ast.dimensions[0]), ast.dimensions, ast.typ

    def visitAutoType(self, ast: AutoType, c):
        pass

    def visitVoidType(self, ast: VoidType, c):
        pass
