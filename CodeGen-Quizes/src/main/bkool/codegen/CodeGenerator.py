from Utils import *
from StaticCheck import *
from StaticError import *
from Emitter import Emitter
from Frame import Frame
from abc import ABC, abstractmethod


class TypeUtils:
    @staticmethod
    def isIntType(x):
        return type(x) is IntType

    @staticmethod
    def isFloatType(x):
        return type(x) is FloatType

    @staticmethod
    def isTheSameType(x, y):
        return type(x) is y


class CodeGenerator(Utils):
    def __init__(self):
        self.libName = "io"

    def init(self):
        return [Symbol("getInt", MType(list(), IntType()), CName(self.libName)),
                Symbol("putInt", MType([IntType()],
                       VoidType()), CName(self.libName)),
                Symbol("putIntLn", MType([IntType()],
                       VoidType()), CName(self.libName)),
                Symbol("getFloat", MType(list(), FloatType()),
                       CName(self.libName)),
                Symbol("putFloat", MType([FloatType()],
                                         VoidType()), CName(self.libName)),
                Symbol("putFloatLn", MType([FloatType()],
                                           VoidType()), CName(self.libName))

                ]

    def gen(self, ast, dir_):
        # ast: AST
        # dir_: String

        gl = self.init()
        gc = CodeGenVisitor(ast, gl, dir_)
        gc.visit(ast, None)


class StringType(Type):

    def __str__(self):
        return "StringType"

    def accept(self, v, param):
        return None


class ArrayPointerType(Type):
    def __init__(self, ctype):
        # cname: String
        self.eleType = ctype

    def __str__(self):
        return "ArrayPointerType({0})".format(str(self.eleType))

    def accept(self, v, param):
        return None


class ClassType(Type):
    def __init__(self, cname):
        self.cname = cname

    def __str__(self):
        return "Class({0})".format(str(self.cname))

    def accept(self, v, param):
        return None


class SubBody():
    def __init__(self, frame, sym):
        # frame: Frame
        # sym: List[Symbol]

        self.frame = frame
        self.sym = sym


class Access():
    def __init__(self, frame, sym, isLeft, isFirst):
        # frame: Frame
        # sym: List[Symbol]
        # isLeft: Boolean
        # isFirst: Boolean

        self.frame = frame
        self.sym = sym
        self.isLeft = isLeft
        self.isFirst = isFirst


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
        self.className = "BKOOLClass"
        self.path = dir_
        self.emit = Emitter(self.path + "/" + self.className + ".j")

    def visitProgram(self, ast: Program, c):
        # ast: Program
        # c: Any

        self.emit.printout(self.emit.emitPROLOG(
            self.className, "java.lang.Object"))
        func_env = SubBody(None, self.env)
        for x in ast.decl:
            if TypeUtils.isTheSameType(x, VarDecl):
                func_env.sym += [self.visit(x, func_env)]
            else:
                func_env = self.visit(x, func_env)
        # generate default constructor
        self.genMETHOD(FuncDecl(Id("<init>"), list(), None, Block(
            list(), list())), c, Frame("<init>", VoidType))
        self.emit.emitEPILOG()
        return c

    def genMETHOD(self, consdecl, o, frame):
        # consdecl: FuncDecl
        # o: Any
        # frame: Frame

        isInit = consdecl.returnType is None
        isMain = consdecl.name.name == "main" and len(
            consdecl.param) == 0 and type(consdecl.returnType) is VoidType
        returnType = VoidType() if isInit else consdecl.returnType
        methodName = "<init>" if isInit else consdecl.name.name
        intype = [ArrayPointerType(StringType())] if isMain else list()
        mtype = MType(intype, returnType)

        self.emit.printout(self.emit.emitMETHOD(
            methodName, mtype, not isInit, frame))

        frame.enterScope(True)

        glenv = o

        # Generate code for parameter declarations
        if isInit:
            self.emit.printout(self.emit.emitVAR(frame.getNewIndex(), "this", ClassType(
                self.className), frame.getStartLabel(), frame.getEndLabel(), frame))
        if isMain:
            self.emit.printout(self.emit.emitVAR(frame.getNewIndex(), "args", ArrayPointerType(
                StringType()), frame.getStartLabel(), frame.getEndLabel(), frame))

        body = consdecl.body
        self.emit.printout(self.emit.emitLABEL(frame.getStartLabel(), frame))

        # Generate code for statements
        if isInit:
            self.emit.printout(self.emit.emitREADVAR(
                "this", ClassType(self.className), 0, frame))
            self.emit.printout(self.emit.emitINVOKESPECIAL(frame))
        list(map(lambda x: self.visit(x, SubBody(frame, glenv)), body.decl))
        list(map(lambda x: self.visit(x, SubBody(frame, glenv)), body.stmt))

        self.emit.printout(self.emit.emitLABEL(frame.getEndLabel(), frame))
        if type(returnType) is VoidType:
            self.emit.printout(self.emit.emitRETURN(VoidType(), frame))
        self.emit.printout(self.emit.emitENDMETHOD(frame))
        frame.exitScope()

    def visitFuncDecl(self, ast, o):
        # ast: FuncDecl
        # o: Any

        subctxt = o
        frame = Frame(ast.name, ast.returnType)
        self.genMETHOD(ast, subctxt.sym, frame)
        return SubBody(None, [Symbol(ast.name, MType(list(), ast.returnType), CName(self.className))] + subctxt.sym)

    def visitCallExpr(self, ast, o):
        # ast: CallExpr
        # o: Any

        ctxt = o
        frame = ctxt.frame
        nenv = ctxt.sym
        sym = self.lookup(ast.method.name, nenv, lambda x: x.name)
        cname = sym.value.value

        ctype = sym.mtype

        in_ = ("", list())
        for x in ast.param:
            str1, typ1 = self.visit(x, Access(frame, nenv, False, True))
            in_ = (in_[0] + str1, in_[1].append(typ1))
        self.emit.printout(in_[0])
        self.emit.printout(self.emit.emitINVOKESTATIC(
            cname + "/" + ast.method.name, ctype, frame))

    # Quiz 1
    def visitIntLiteral(self, ast, o):
        # ast: IntLiteral
        # o: Any

        return self.emit.emitPUSHICONST(ast.value, o.frame), IntType()

    # Quiz 2
    def visitFloatLiteral(self, ast, o):
        return self.emit.emitPUSHFCONST(ast.value, o.frame), FloatType()

    # Quiz 3
    def visitBinExpr(self, ast, o):
        e1 = self.visit(ast.e1, o)
        self.emit.printout(e1[0])
        e2 = self.visit(ast.e2, o)
        self.emit.printout(e2[0])
        op = ast.op
        frame = o.frame

        if op in ["+", "+."]:
            return self.emit.emitADDOP("+", IntType() if op == "+" else FloatType(), frame), IntType() if op == "+" else FloatType()
        if op in ["-", "-."]:
            return self.emit.emitADDOP("-", IntType() if op == "-" else FloatType(), frame), IntType() if op == "-" else FloatType()
        if op in ["*", "*."]:
            return self.emit.emitMULOP("*", IntType() if op == "*" else FloatType(), frame), IntType() if op == "*" else FloatType()
        if op in ["/", "/."]:
            return self.emit.emitMULOP("/", IntType() if op == "/" else FloatType(), frame), IntType() if op == "/" else FloatType()

    # Quiz 4
    # def visitId(self, ast, o):
    #     frame = o.frame
    #     symbol = self.lookup(ast.name, o.sym, lambda sym: sym.name)
    #     if symbol is not None:
    #         if type(symbol.value) is CName:
    #             return self.emit.emitGETSTATIC(f"{symbol.value.value}.{symbol.name}", symbol.mtype, frame), symbol.mtype
    #         return self.emit.emitREADVAR(symbol.name, symbol.mtype, symbol.value.value, frame), symbol.mtype

    # Quiz 2 - Codegen 2
    def visitId(self, ast, o):
        frame = o.frame
        symbol = self.lookup(ast.name, o.sym, lambda sym: sym.name)
        if symbol is not None:
            if type(symbol.value) is CName:
                return self.emit.emitGETSTATIC(f"{symbol.value.value}.{symbol.name}", symbol.mtype, frame) if not o.isLeft else self.emit.emitPUTSTATIC(f"{symbol.value.value}.{symbol.name}", symbol.mtype, frame), symbol.mtype
            return self.emit.emitREADVAR(symbol.name, symbol.mtype, symbol.value.value, frame) if not o.isLeft else self.emit.emitWRITEVAR(symbol.name, symbol.mtype, symbol.value.value, frame), symbol.mtype

    # Quiz 5
    # def visitBinExpr(self, ctx, o):
    #     e1str, e1type = ctx.e1.accept(self, o)
    #     e2str, e2type = ctx.e2.accept(self, o)

    #     if ctx.op in ('+', '-'):
    #         if type(e1type) is FloatType and type(e2type) is IntType:
    #             return e1str + e2str + self.emit.emitI2F(o.frame) + self.emit.emitADDOP(ctx.op, FloatType(), o.frame), FloatType()

    #         if type(e1type) is IntType and type(e2type) is FloatType:
    #             return e1str + self.emit.emitI2F(o.frame) + e2str + self.emit.emitADDOP(ctx.op, FloatType(), o.frame), FloatType()

    #         if type(e1type) is FloatType and type(e2type) is FloatType:
    #             return e1str + e2str + self.emit.emitADDOP(ctx.op, FloatType(), o.frame), FloatType()
    #         else:
    #             return e1str + e2str + self.emit.emitADDOP(ctx.op, IntType(), o.frame), IntType()

    #     if ctx.op == '*':
    #         if type(e1type) is FloatType and type(e2type) is IntType:
    #             return e1str + e2str + self.emit.emitI2F(o.frame) + self.emit.emitMULOP(ctx.op, FloatType(), o.frame), FloatType()

    #         if type(e1type) is IntType and type(e2type) is FloatType:
    #             return e1str + self.emit.emitI2F(o.frame) + e2str + self.emit.emitMULOP(ctx.op, FloatType(), o.frame), FloatType()

    #         if type(e1type) is FloatType and type(e2type) is FloatType:
    #             return e1str + e2str + self.emit.emitMULOP(ctx.op, FloatType(), o.frame), FloatType()
    #         else:
    #             return e1str + e2str + self.emit.emitMULOP(ctx.op, IntType(), o.frame), IntType()

    #     if ctx.op == '/':
    #         if type(e1type) is FloatType and type(e2type) is IntType:
    #             return e1str + e2str + self.emit.emitI2F(o.frame) + self.emit.emitMULOP(ctx.op, FloatType(), o.frame), FloatType()

    #         if type(e1type) is IntType and type(e2type) is FloatType:
    #             return e1str + self.emit.emitI2F(o.frame) + e2str + self.emit.emitMULOP(ctx.op, FloatType(), o.frame), FloatType()

    #         if type(e1type) is FloatType and type(e2type) is FloatType:
    #             return e1str + e2str + self.emit.emitMULOP(ctx.op, FloatType(), o.frame), FloatType()
    #         else:
    #             return e1str + self.emit.emitI2F(o.frame) + e2str + self.emit.emitI2F(o.frame) + self.emit.emitMULOP(ctx.op, FloatType(), o.frame), FloatType()
    #     else:
    #         if type(e1type) is FloatType and type(e2type) is IntType:
    #             return e1str + e2str + self.emit.emitI2F(o.frame) + self.emit.emitREOP(ctx.op, FloatType(), o.frame), BoolType()

    #         if type(e1type) is IntType and type(e2type) is FloatType:
    #             return e1str + self.emit.emitI2F(o.frame) + e2str + self.emit.emitREOP(ctx.op, FloatType(), o.frame), BoolType()

    #         if type(e1type) is FloatType and type(e2type) is FloatType:
    #             return e1str + e2str + self.emit.emitREOP(ctx.op, FloatType(), o.frame), BoolType()
    #         else:
    #             return e1str + e2str + self.emit.emitREOP(ctx.op, IntType(), o.frame), BoolType()

    # Quiz 6
    def visitVarDecl(self, ast, o):
        id = ast.name.name
        typ = ast.typ
        if o.frame is None:  # Global Var
            self.emit.printout(self.emit.emitATTRIBUTE(
                id, typ, False))
            return Symbol(id, typ, CName(self.className))
        else:  # Local Var
            idx = o.frame.getNewIndex()
            self.emit.printout(self.emit.emitVAR(
                idx, id, typ, o.frame.getStartLabel(), o.frame.getEndLabel(), o.frame))
            return Symbol(id, typ, Index(idx))

    def visitAssign(self, ast, o):
        rhs, _ = self.visit(
            ast.rhs, Access(o.frame, o.sym, False, False))
        lhs, _ = self.visit(
            ast.lhs, Access(o.frame, o.sym, True, False))

        self.emit.printout(rhs + lhs)

    def visitBlock(self, ast, o):
        frame = o.frame
        glenv = o.sym
        frame.enterScope(False)
        self.emit.printout(self.emit.emitLABEL(frame.getStartLabel(), frame))
        list(map(lambda x: self.visit(x, SubBody(frame, glenv)), ast.decl))
        list(map(lambda x: self.visit(x, SubBody(frame, glenv)), ast.stmt))
        self.emit.printout(self.emit.emitLABEL(frame.getEndLabel(), frame))
        frame.exitScope()

    def visitIf(self, ast, o):
        ctxt = o
        frame = ctxt.frame
        nenv = ctxt.sym
        expCode, expType = self.visit(
            ast.expr, Access(frame, nenv, False, False))
        self.emit.printout(expCode)

        labelF = frame.getNewLabel()  # eval is true
        labelE = frame.getNewLabel()  # label end

        self.emit.printout(self.emit.emitIFFALSE(labelF, frame))

        self.visit(ast.tstmt, o)
        self.emit.printout(self.emit.emitGOTO(labelE, frame))

        self.emit.printout(self.emit.emitLABEL(labelF, frame))
        if ast.estmt:
            self.visit(ast.estmt, o)

        self.emit.printout(self.emit.emitLABEL(labelE, frame))

    def visitWhile(self, ast, o):
        frame = o.frame
        nenv = o.sym
        expr, _ = self.visit(
            ast.expr, Access(frame, nenv, False, False))
        labelS = frame.getNewLabel()
        frame.enterLoop()
        self.emit.printout(self.emit.emitLABEL(labelS, frame) + expr)
        self.emit.printout(self.emit.emitIFFALSE(frame.getBreakLabel(), frame))
        self.visit(ast.stmt, o)
        self.emit.printout(self.emit.emitGOTO(
            labelS, frame))
        self.emit.printout(self.emit.emitLABEL(
            frame.getContinueLabel(), frame))

        self.emit.printout(self.emit.emitLABEL(frame.getBreakLabel(), frame))

        frame.exitLoop()
