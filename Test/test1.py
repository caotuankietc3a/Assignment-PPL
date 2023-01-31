class Exp:
    def __init__(self, op: str) -> None:
        self.op = op


class BinExp(Exp):
    def __init__(self, first_operand, op: str, second_operand) -> None:
        self.first_operand = first_operand
        self.second_operand = second_operand
        super().__init__(op)

    def eval(self):
        match self.op:
            case "+":
                return self.first_operand.eval() + self.second_operand.eval()
            case "-":
                return self.first_operand.eval() - self.second_operand.eval()
            case "*":
                return self.first_operand.eval() * self.second_operand.eval()
            case ":":
                return self.first_operand.eval() / self.second_operand.eval()

    def printPrefix(self):
        return f"{self.op} {self.first_operand.printPrefix()} {self.second_operand.printPrefix()}"


class UnExp(Exp):
    def __init__(self, op: str, operand) -> None:
        self.operand = operand
        super().__init__(op)

    def eval(self):
        match self.op:
            case "+":
                return self.operand.eval()
            case "-":
                return - self.operand.eval()

    def printPrefix(self):
        return f"{self.op}. {self.operand.printPrefix()}"


class IntLit:
    def __init__(self, number: int) -> None:
        self.number = number

    def eval(self) -> int:
        return self.number

    def printPrefix(self):
        return self.number


class FloatLit:
    def __init__(self, float_number: float) -> None:
        self.float_number = float_number

    def eval(self) -> float:
        return self.float_number

    def printPrefix(self):
        return self.float_number


x1 = IntLit(1)

x2 = FloatLit(2.0)

x3 = BinExp(x1, "+", x1)

x4 = UnExp("-", x1)

# -1 + 4 * 2.0
x5 = BinExp(x4, "+", BinExp(IntLit(4), "*", x2))

# print(x1.eval())
#
# print(x2.eval())
#
# print(x3.eval())
#
# print(x4.eval())
#
# print(x5.eval())

print(x1.printPrefix())

print(x2.printPrefix())

print(x3.printPrefix())

print(x4.printPrefix())

print(x5.printPrefix())
