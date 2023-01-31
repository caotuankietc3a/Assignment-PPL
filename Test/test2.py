from abc import ABC


class Exp(ABC):
    pass


class BinExp(Exp):
    def __init__(self, o1, op, o2):
        self.left = o1
        self.op = op
        self.right = o2


class UnExp(Exp):
    def __init__(self, op, o1):
        self.op = op
        self.operand = o1


class IntLit(Exp):
    def __init__(self, v):
        self.value = v


class FloatLit(Exp):
    def __init__(self, v):
        self.value = v


class Eval:
    def visit(self, ctx):
        if isinstance(ctx, BinExp) == True:
            match ctx.op:
                case "+":
                    return self.visit(ctx.left) + self.visit(ctx.right)
                case "-":
                    return self.visit(ctx.left) - self.visit(ctx.right)
                case "*":
                    return self.visit(ctx.left) * self.visit(ctx.right)
                case ":":
                    return self.visit(ctx.left) / self.visit(ctx.right)
        elif isinstance(ctx, UnExp):
            match ctx.op:
                case "+":
                    return self.visit(ctx.operand)
                case "-":
                    return - self.visit(ctx.operand)
        elif isinstance(ctx, IntLit) or isinstance(ctx, FloatLit):
            return ctx.value


class PrintPrefix:
    def visit(self, ctx):
        if isinstance(ctx, BinExp):
            return f"{ctx.op} {self.visit(ctx.left)} {self.visit(ctx.right)}"
        elif isinstance(ctx, UnExp):
            return f"{ctx.op}. {self.visit(ctx.operand)}"
        elif isinstance(ctx, IntLit) or isinstance(ctx, FloatLit):
            return str(ctx.value)


v1 = Eval()
v2 = PrintPrefix()

x1 = IntLit(1)
x2 = FloatLit(2.0)
x3 = BinExp(x1, "+", x1)
x4 = UnExp("-", x1)
x5 = BinExp(x4, "+", BinExp(IntLit(4), "*", x2))

print(v1.visit(x1))
print(v1.visit(x2))
print(v1.visit(x3))
print(v1.visit(x4))
print(v1.visit(x5))

print(v2.visit(x1))
print(v2.visit(x2))
print(v2.visit(x3))
print(v2.visit(x4))
print(v2.visit(x5))
