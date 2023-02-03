from BKOOLVisitor import BKOOLVisitor
from BKOOLParser import BKOOLParser
from AST import *


class ASTGeneration(BKOOLVisitor):
    # def visitProgram(self, ctx: BKOOLParser.ProgramContext):
    #     return Program([FuncDecl(Id("main"),
    #                     [],
    #                     self.visit(ctx.mptype()),
    #                     Block([], [self.visit(ctx.body())] if ctx.body() else []))])

    # # Count terminal nodes in parser tree
    # def visitProgram(self, ctx: BKOOLParser.ProgramContext):
    #     return ctx.vardecls().accept(self) + 1
    #
    # def visitVardecls(self, ctx: BKOOLParser.VardeclsContext):
    #     return ctx.vardecl().accept(self) + ctx.vardecltail().accept(self)
    #
    # def visitVardecltail(self, ctx: BKOOLParser.VardecltailContext):
    #     return (ctx.vardecl().accept(self) + ctx.vardecltail().accept(self)) if (ctx.vardecl() and ctx.vardecltail()) else 0
    #
    # def visitVardecl(self, ctx: BKOOLParser.VardeclContext):
    #     return ctx.mptype().accept(self) + ctx.ids().accept(self) + 1
    #
    # def visitMptype(self, ctx: BKOOLParser.MptypeContext):
    #     return 1
    #
    # def visitIds(self, ctx: BKOOLParser.IdsContext):
    #     return (2 + ctx.ids().accept(self)) if ctx.getChildCount() == 3 else 1

    # Count non-terminal nodes in parser tree
    # def visitProgram(self, ctx: BKOOLParser.ProgramContext):
    #     return ctx.vardecls().accept(self) + 1
    #
    # def visitVardecls(self, ctx: BKOOLParser.VardeclsContext):
    #     return ctx.vardecl().accept(self) + ctx.vardecltail().accept(self) + 1
    #
    # def visitVardecltail(self, ctx: BKOOLParser.VardecltailContext):
    #     return (ctx.vardecl().accept(self) + ctx.vardecltail().accept(self) + 1) if (ctx.vardecl() and ctx.vardecltail()) else 1
    #
    # def visitVardecl(self, ctx: BKOOLParser.VardeclContext):
    #     return ctx.mptype().accept(self) + ctx.ids().accept(self) + 1
    #
    # def visitMptype(self, ctx: BKOOLParser.MptypeContext):
    #     return 1
    #
    # def visitIds(self, ctx: BKOOLParser.IdsContext):
    #     return (1 + ctx.ids().accept(self)) if ctx.getChildCount() == 3 else 1

    # Generate the AST
    def visitProgram(self, ctx: BKOOLParser.ProgramContext):
        return Program(ctx.vardecls().accept(self))

    def visitVardecls(self, ctx: BKOOLParser.VardeclsContext):
        return [*ctx.vardecl().accept(self), *ctx.vardecltail().accept(self)]

    def visitVardecltail(self, ctx: BKOOLParser.VardecltailContext):
        return [*ctx.vardecl().accept(self), *ctx.vardecltail().accept(self)] if (ctx.vardecl() and ctx.vardecltail()) else []

    def visitVardecl(self, ctx: BKOOLParser.VardeclContext):
        return [str(VarDecl(x, ctx.mptype().accept(self))) for x in ctx.ids().accept(self)]

    def visitMptype(self, ctx: BKOOLParser.MptypeContext):
        return IntType() if ctx.INTTYPE() else FloatType()

    def visitIds(self, ctx: BKOOLParser.IdsContext):
        return [Id(ctx.ID().getText()), *ctx.ids().accept(self)] if ctx.getChildCount() == 3 else [Id(ctx.ID().getText())]

    def visitProgram(self, ctx: BKOOLParser.ProgramContext):
        return ctx.exp().accept(self)

    def visitExp(self, ctx: BKOOLParser.ExpContext):
        return Binary(ctx.ASSIGN().getText(), ctx.term().accept(self), ctx.exp().accept(self)) if ctx.getChildCount() == 3 else ctx.term().accept(self)

    def visitTerm(self, ctx: BKOOLParser.TermContext):
        return Binary(ctx.COMPARE().getText(), ctx.factor(0).accept(self), ctx.factor(1).accept(self)) if ctx.getChildCount() == 3 else ctx.factor(0).accept(self)

    def visitFactor(self, ctx: BKOOLParser.FactorContext):
        return Binary(ctx.ANDOR().getText(), ctx.factor().accept(self), ctx.operand().accept(self)) if ctx.getChildCount() == 3 else ctx.operand().accept(self)

    def visitOperand(self, ctx: BKOOLParser.OperandContext):
        if ctx.ID():
            return Id(ctx.ID().getText())
        if ctx.INTLIT():
            return IntLiteral(ctx.INTLIT().getText())
        if ctx.BOOLIT():
            return BooleanLiteral(ctx.BOOLIT().getText())

        return ctx.exp().accept(self)
    pass
