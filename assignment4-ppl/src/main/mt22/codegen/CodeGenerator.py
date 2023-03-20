from Utils import *
from StaticCheck import *
from StaticError import *
from Emitter import Emitter
from Frame import Frame
# import AST as ast
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
    def retrieveType(originType, lst=[]):
        if TypeUtils.isArrayType(originType):
            return ArrayPointerType(originType.typ, lst)
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


class CodeGenerator(Utils):
    def __init__(self):
        self.libName = "io"

    def init(self):
        return [
            Symbol("readInteger", MType(
                [], IntegerType()), CName(self.libName)),
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


class MType:
    def __init__(self, partype, rettype, params=[]):
        self.partype = partype
        self.rettype = rettype

        # [{"<name>": {"isInherit": True || False, "type": Type}}]
        self.params = params


class Symbol:
    def __init__(self, name, mtype, value=None):
        self.name = name
        self.mtype = mtype
        self.value = value


class ArrayPointerType(Type):
    def __init__(self, ctype, lst=[]):
        # cname: String
        self.eleType = ctype
        self.lst = lst

    def __str__(self):
        return "ArrayPointerType({0},[{1}])".format(str(self.eleType), ", ".join(str(el) for el in self.lst))


class ClassType(Type):
    def __init__(self, cname):
        self.cname = cname

    def __str__(self):
        return "Class({0})".format(str(self.cname))


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

    def genMETHOD(self, decl: FuncDecl, sym, frame: Frame, global_vardecl_codes: list or None):
        # decl: FuncDecl
        # o: Any
        # frame: Frame
        # func_name = decl.name.name
        func_name = decl.name
        func_type = decl.return_type
        inherit = decl.inherit

        isInit = TypeUtils.isNone(func_type) and func_name == "<init>"
        isClassInit = TypeUtils.isNone(func_type) and func_name == "<clinit>"

        isMain = func_name == "main" and len(
            decl.params) == 0 and TypeUtils.isVoidType(func_type)
        returnType = VoidType() if isInit or isClassInit else TypeUtils.retrieveType(func_type)
        isProc = TypeUtils.isVoidType(returnType)
        intype = [ArrayPointerType(StringType())] if isMain else [
            TypeUtils.retrieveType(par.typ) for par in decl.params]
        mtype = MType(intype, returnType)

        self.emit.printout(self.emit.emitMETHOD(
            func_name, mtype, not isInit, frame))

        frame.enterScope(False if isClassInit else isProc)

        glenv = sym

        # Generate code for parameter declarations
        if isInit:
            self.emit.printout(self.emit.emitVAR(frame.getNewIndex(), "this", ClassType(
                self.className), frame.getStartLabel(), frame.getEndLabel(), frame))
        if isMain:
            self.emit.printout(self.emit.emitVAR(frame.getNewIndex(), "args", ArrayPointerType(
                StringType()), frame.getStartLabel(), frame.getEndLabel(), frame))

        subbody = SubBody(frame, glenv)
        for par in decl.params:
            subbody = self.visit(par, subbody)

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
                    if TypeUtils.isTheSameType(var_code[2], ArrayPointerType):
                        self.emit.printout(var_code[0])
                    else:
                        self.emit.printout(
                            var_code[0] + self.emit.emitPUTSTATIC(var_code[1], var_code[2], frame))

        glenv = [Symbol(func_name, mtype, CName(
            self.className))] + glenv

        subbody.sym = [Symbol(func_name, mtype, CName(
            self.className))] + subbody.sym

        self.visit(block, subbody)

        self.emit.printout(self.emit.emitLABEL(frame.getEndLabel(), frame))

        if isProc:
            self.emit.printout(self.emit.emitRETURN(VoidType(), frame))

        self.emit.printout(self.emit.emitENDMETHOD(frame))
        frame.exitScope()

        return SubBody(frame, glenv)

    def handleCall(self, ast: FuncCall or CallStmt, frame, symbols, isStmt=False):
        func_name = ast.name
        if func_name == "super" or func_name == "preventDefault":
            pass
        else:
            symbol = self.lookup(func_name, symbols, lambda sym: sym.name)
            cname = symbol.value.value
            ctype = symbol.mtype
            params_code = ""
            for p in ast.args:
                params_code += self.visit(p, Access(frame,
                                          symbols, False, False))[0]

            params_code += self.emit.emitINVOKESTATIC(
                cname + "/" + func_name, ctype, frame)
            if isStmt:
                self.emit.printout(params_code)
            return params_code, ctype.rettype

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
        self.genMETHOD(FuncDecl("<init>", None, list(), None,
                       BlockStmt(list())), e.sym, Frame("<init>", VoidType), None)

        # class init - static field
        self.genMETHOD(FuncDecl("<clinit>", None, list(), None,
                       BlockStmt(list())), e.sym, frame_clinit, var_decl_codes)

        self.emit.emitEPILOG()
        return c

    def visitVarDecl(self, ast: VarDecl, c: SubBody):
        print(ast)
        frame = c.frame
        sym = c.sym
        isGlobal = c.isGlobal
        var_name = ast.name
        var_type = ast.typ

        init_code, init_type = "", None

        dimens = []
        # val = 0
        idx = frame.getNewIndex() if not isGlobal else 0
        isArrayType = TypeUtils.isArrayType(var_type)
        hasInit = not TypeUtils.isNone(ast.init)
        if isArrayType:
            # init = (jcode, Type)
            dimens_size, dimens, arr_return_type = self.visit(
                var_type, None)
            arr_list_codes = []
            if hasInit:
                cur_dimen = 0
                arr = [dimens, cur_dimen]
                arr_list_codes = self.visit(
                    ast.init, Access(frame, sym, False, False, arr))

            self.arr_idx_global = 0

            init_code = reduce(lambda acc, el: acc + self.emit.emitDUP(frame) + self.emit.emitPUSHICONST(
                el[1], frame) + el[0] + (self.emit.emitI2F(frame) if TypeUtils.isFloatType(arr_return_type) and TypeUtils.isTheSameType(el[2], IntegerType) else "") + self.emit.emitASTORE(TypeUtils.retrieveType(arr_return_type),  frame), arr_list_codes, init_code)

            ob = {"idx": idx, "isStatic": False} if not isGlobal else {
                "name": self.className+"."+var_name, "isStatic": True}

            init_code = self.emit.emitInitNewArray(
                ob, dimens_size, TypeUtils.retrieveType(arr_return_type), frame,  init_code)
        else:
            if hasInit:
                init_code, init_type = self.visit(
                    ast.init, Access(frame, sym, False, False))

                init_code += (self.emit.emitI2F(frame)
                              if TypeUtils.isFloatType(var_type) and TypeUtils.isTheSameType(init_type, IntegerType) else "")

        if isGlobal:
            return SubBody(frame, [Symbol(var_name, var_type if isArrayType else TypeUtils.retrieveType(var_type, lst=dimens), CName(self.className))] + sym, True), self.emit.emitATTRIBUTE(
                var_name, TypeUtils.retrieveType(var_type, lst=dimens), False), (init_code, f"{self.className}.{var_name}", TypeUtils.retrieveType(var_type)) if hasInit else None

        self.emit.printout(self.emit.emitVAR(
            idx, var_name, TypeUtils.retrieveType(var_type), frame.getStartLabel(), frame.getEndLabel(), frame))

        new_sym = [Symbol(var_name, var_type if isArrayType else TypeUtils.retrieveType(
            var_type, lst=dimens), Index(idx))] + sym
        if hasInit:
            id = self.visit(Id(ast.name), Access(frame, new_sym, True, False))
            self.emit.printout(
                init_code + (id[0] if not isArrayType else ""))
        else:
            self.emit.printout(init_code)

        return SubBody(frame,  new_sym)

    def visitParamDecl(self, ast: ParamDecl, c: SubBody):
        print(ast)
        frame = c.frame
        sym = c.sym
        name = ast.name
        typ = ast.typ
        inherit = ast.inherit
        out = ast.out
        isArrayType = TypeUtils.isArrayType(typ)

        idx = frame.getNewIndex()
        self.emit.printout(self.emit.emitVAR(
            idx, name, TypeUtils.retrieveType(typ), frame.getStartLabel(), frame.getEndLabel(), frame))
        new_sym = [Symbol(name, typ if isArrayType else TypeUtils.retrieveType(
            typ), Index(idx))] + sym

        return SubBody(frame,  new_sym)
        # return self.visit(VarDecl(name, typ, None), c)

    def visitFuncDecl(self, ast: FuncDecl, c: SubBody):
        print(ast)
        sym = c.sym
        # name = ast.name.name
        name = ast.name
        frame = Frame(name, TypeUtils.retrieveType(ast.return_type))

        return self.genMETHOD(ast, sym, frame, None)

    def visitAssignStmt(self, ast: AssignStmt, c: SubBody):
        print(ast)
        frame = c.frame
        sym = c.sym
        rhs_code, rhs_type = self.visit(
            ast.rhs, Access(frame, sym, False, False))

        lhs_code, lhs_type = self.visit(
            ast.lhs, Access(frame, sym, True, True))
        if TypeUtils.isFloatType(lhs_type) and TypeUtils.isTheSameType(rhs_type, IntegerType):
            rhs_code += self.emit.emitI2F(frame)

        if TypeUtils.isTheSameType(lhs_code, list):  # ArrayCell
            self.emit.printout(lhs_code[0] + rhs_code + lhs_code[1])
        else:
            self.emit.printout(rhs_code+lhs_code)

        return False

    def visitBlockStmt(self, ast: BlockStmt, c: SubBody):
        frame = c.frame
        glenv = c.sym
        isBlockStmt = c.isBlockStmt
        if isBlockStmt:
            frame.enterScope(False)
            self.emit.printout(self.emit.emitLABEL(
                frame.getStartLabel(), frame))
        sub_body = SubBody(frame, glenv)
        hasReturnStmt = False
        for s in ast.body:
            if TypeUtils.isTheSameType(s, VarDecl):
                sub_body = self.visit(s, sub_body)
            else:  # Statements
                hasReturnStmt = self.visit(s, sub_body) or hasReturnStmt
        if isBlockStmt:
            self.emit.printout(self.emit.emitLABEL(frame.getEndLabel(), frame))
            frame.exitScope()
        return hasReturnStmt

    def visitIfStmt(self, ast: IfStmt, c: SubBody):
        ctxt = c
        frame = ctxt.frame
        nenv = ctxt.sym
        expCode, expType = self.visit(
            ast.cond, Access(frame, nenv, False, False))
        self.emit.printout(expCode)

        labelT = frame.getNewLabel()  # eval is true
        labelE = frame.getNewLabel()  # label end

        self.emit.printout(self.emit.emitIFTRUE(labelT, frame))  # false
        # False
        hasReturnStmt = self.visit(
            ast.fstmt, c) is True if not TypeUtils.isNone(ast.fstmt) else False

        if not hasReturnStmt:
            self.emit.printout(self.emit.emitGOTO(labelE, frame))  # go to end

        # True
        self.emit.printout(self.emit.emitLABEL(labelT, frame))
        hasReturnStmt = self.visit(ast.tstmt, c) and hasReturnStmt

        # End
        self.emit.printout(self.emit.emitLABEL(labelE, frame))
        return hasReturnStmt

    # def visitIfStmt(self, ast: IfStmt, c: SubBody):
    #     print(ast)
    #     ctxt = c
    #     frame = ctxt.frame
    #     nenv = ctxt.sym
    #     expCode, expType = self.visit(
    #         ast.cond, Access(frame, nenv, False, False))
    #     self.emit.printout(expCode)

    #     labelF = frame.getNewLabel()
    #     labelE = frame.getNewLabel()

    #     self.emit.printout(self.emit.emitIFFALSE(labelF, frame))

    #     hasReturnStmt = self.visit(ast.tstmt, c)

    #     if not hasReturnStmt:
    #         self.emit.printout(self.emit.emitGOTO(labelE, frame))

    #     self.emit.printout(self.emit.emitLABEL(labelF, frame))

    #     if ast.fstmt:  # Need to Check
    #         hasReturnStmt = self.visit(ast.fstmt, c)

    #     self.emit.printout(self.emit.emitLABEL(labelE, frame))

    #     return hasReturnStmt

    def visitForStmt(self, ast: ForStmt, c: SubBody):
        print(ast)
        frame = c.frame
        sym = c.sym
        labelS = frame.getNewLabel()
        id = ast.init.lhs
        init = ast.init
        cond = ast.cond
        upd = ast.upd
        symbol = self.lookup(id.name, c.sym, lambda sym: sym.name)
        if TypeUtils.isNone(symbol):
            c = self.visit(VarDecl(id.name, IntegerType(), None),
                           SubBody(frame, sym, False))

        self.visit(init, c)
        labelS = frame.getNewLabel()
        frame.enterLoop()

        cond_code, cond_type = self.visit(
            cond, Access(frame, c.sym, False, False))

        self.emit.printout(self.emit.emitLABEL(labelS, frame) + cond_code)

        self.emit.printout(self.emit.emitIFFALSE(
            frame.getBreakLabel(), frame))

        hasReturnStmt = self.visit(ast.stmt, c)

        self.emit.printout(self.emit.emitLABEL(
            frame.getContinueLabel(), frame))

        self.visit(AssignStmt(id, upd), c)

        if not hasReturnStmt:
            self.emit.printout(self.emit.emitGOTO(
                labelS, frame))

        self.emit.printout(self.emit.emitLABEL(
            frame.getBreakLabel(), frame))

        frame.exitLoop()

    def visitWhileStmt(self, ast: WhileStmt, c: SubBody):
        frame = c.frame
        nenv = c.sym
        cond_code, _ = self.visit(
            ast.cond, Access(frame, nenv, False, False))
        labelS = frame.getNewLabel()
        frame.enterLoop()
        self.emit.printout(self.emit.emitLABEL(labelS, frame) + cond_code)
        self.emit.printout(self.emit.emitIFFALSE(frame.getBreakLabel(), frame))

        hasReturnStmt = self.visit(ast.stmt, c)

        self.emit.printout(self.emit.emitLABEL(
            frame.getContinueLabel(), frame))

        if not hasReturnStmt:
            self.emit.printout(self.emit.emitGOTO(
                labelS, frame))
        self.emit.printout(self.emit.emitLABEL(frame.getBreakLabel(), frame))
        frame.exitLoop()

    def visitDoWhileStmt(self, ast: DoWhileStmt, c: SubBody):
        print(ast)
        frame = c.frame
        nenv = c.sym
        labelS = frame.getNewLabel()
        frame.enterLoop()
        self.emit.printout(self.emit.emitLABEL(labelS, frame))
        self.visit(ast.stmt, SubBody(frame, nenv, isBlockStmt=True))
        # self.visit(ast.stmt, SubBody(frame, nenv))

        cond_code, _ = self.visit(
            ast.cond, Access(frame, nenv, False, False))

        self.emit.printout(cond_code + self.emit.emitIFTRUE(labelS, frame))

        self.emit.printout(self.emit.emitLABEL(
            frame.getContinueLabel(), frame))

        self.emit.printout(self.emit.emitLABEL(frame.getBreakLabel(), frame))

        frame.exitLoop()

    def visitBreakStmt(self, ast: BreakStmt, c: SubBody):
        frame = c.frame
        self.emit.printout(self.emit.emitGOTO(frame.getBreakLabel(), frame))

    def visitContinueStmt(self, ast: ContinueStmt, c: SubBody):
        frame = c.frame
        self.emit.printout(self.emit.emitGOTO(frame.getContinueLabel(), frame))

    def visitReturnStmt(self, ast: ReturnStmt, c: SubBody):
        print(ast)
        frame = c.frame
        sym = c.sym
        returnType = frame.returnType
        if not TypeUtils.isVoidType(returnType):
            exp_code, exp_type = self.visit(
                ast.expr, Access(frame, sym, False, True))

            if TypeUtils.isFloatType(returnType) and TypeUtils.isTheSameType(exp_type, IntegerType):
                exp_code += self.emit.emitI2F(frame)
            self.emit.printout(exp_code)

        self.emit.printout(self.emit.emitRETURN(returnType, frame))
        return True

    def visitCallStmt(self, ast: CallStmt, c: SubBody):
        print(ast)
        frame = c.frame
        symbols = c.sym
        self.handleCall(ast, frame, symbols, True)

    def visitBinExpr(self, ast: BinExpr, c: Access):
        print(ast)
        frame = c.frame
        sym = c.sym
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
                symbol = Symbol("concat", MType(
                    [StringType()], StringType()), CName("java/lang/String"))
                return l_code + r_code + self.emit.emitINVOKEVIRTUAL(f"{symbol.value.value}/{symbol.name}", symbol.mtype, frame), symbol.mtype.rettype

    def visitUnExpr(self, ast: UnExpr, c: Access):
        frame = c.frame
        op = ast.op
        e_code, e_type = self.visit(ast.val, c)
        return e_code + (self.emit.emitNEGOP(e_type, frame) if op == "-" else self.emit.emitNOT(e_type, frame)), e_type

    def visitId(self, ast: Id, c: Access):
        print(ast)
        frame = c.frame
        isFirst = c.isFirst
        isLeft = c.isLeft
        symbol = self.lookup(ast.name, c.sym, lambda sym: sym.name)
        if not TypeUtils.isNone(symbol):
            isArrayType = TypeUtils.isArrayType(symbol.mtype)

            arr_dimens = [] if not isArrayType else symbol.mtype.dimensions
            # sym_type = TypeUtils.retrieveType(symbol.mtype, val=symbol.mtype.val if TypeUtils.isTheSameType(
            #     symbol.mtype, IntegerType) else 0, lst=arr_dimens)
            sym_type = TypeUtils.retrieveType(symbol.mtype,  lst=arr_dimens)
            if not isFirst and isLeft:
                frame.push()
            elif isFirst and not isLeft:
                frame.pop()
            if TypeUtils.isTheSameType(symbol.value, CName):
                return self.emit.emitPUTSTATIC(f"{symbol.value.value}.{symbol.name}", sym_type, frame) if isLeft and not isArrayType else self.emit.emitGETSTATIC(f"{symbol.value.value}.{symbol.name}", sym_type, frame), sym_type

            return self.emit.emitWRITEVAR(symbol.name, sym_type, symbol.value.value, frame) if isLeft and not isArrayType else self.emit.emitREADVAR(symbol.name, sym_type, symbol.value.value, frame), sym_type

    def visitArrayCell(self, ast: ArrayCell, c: Access):
        print(ast)
        frame = c.frame
        sym = c.sym
        isLeft = c.isLeft

        arr_code, arr_type = self.visit(
            Id(ast.name), Access(frame, sym, isLeft, False))

        dimens_codes = list(
            map(lambda x: self.visit(IntegerLit(x), c)[0], arr_type.lst))
        cells_codes = list(
            map(lambda cell: self.visit(
                cell, Access(frame, sym, False, False))[0], ast.cell))

        lst = []
        for i, d in enumerate(cells_codes[:-1]):
            lst.append(reduce(lambda acc, el: el + acc + self.emit.emitMULOP(
                "*", IntegerType(), frame), dimens_codes[i + 1:], d))
        lst.append(cells_codes[-1])
        arr_code += reduce(lambda acc, el: acc + el +
                           self.emit.emitADDOP("+", IntegerType(), frame), lst[1:], lst[0])

        if isLeft:
            return [arr_code,  self.emit.emitASTORE(
                arr_type.eleType, frame)], arr_type.eleType
        return arr_code + self.emit.emitALOAD(arr_type.eleType, frame), arr_type.eleType

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
                expr_code, expr_type = self.visit(exp, c)
                # [[expr_code, idx, type], ...]
                lst.append([expr_code, self.arr_idx_global, expr_type])
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
        print(ast)
        frame = c.frame
        symbols = c.sym
        return self.handleCall(ast, frame, symbols, False)

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
