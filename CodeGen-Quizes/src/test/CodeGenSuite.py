import unittest
from TestUtils import TestCodeGen
from AST import *


class CheckCodeGenSuite(unittest.TestCase):
    # def test_int(self):
    #     """Simple program: int main() {} """
    #     input = """void main() {putInt(100);}"""
    #     expect = "100"
    #     self.assertTrue(TestCodeGen.test(input,expect,500))
    # def test_int_ast(self):
    #     input = Program([
    #         FuncDecl(Id("main"), [], VoidType(), Block([], [
    #             CallExpr(Id("putInt"), [IntLiteral(5)])]))])
    #     expect = "5"
    #     self.assertTrue(TestCodeGen.test(input, expect, 501))

    # def test_1(self):
    #     """Simple program: int main() {} """
    #     input = Program(
    #         [FuncDecl(Id("main"), [], VoidType(), Block([], [IntLiteral(5)]))])
    #     expect = ""
    #     self.assertTrue(TestCodeGen.test(input, expect, 100))

    # def test(self):
    #     input = Program([VarDecl(Id("x"), IntType()), FuncDecl(Id("main"), [], VoidType(), Block([VarDecl(Id("x"), FloatType(
    #     )), VarDecl(Id("y"), IntType()), VarDecl(Id("z"), FloatType())], []))])
    #     expect = ""
    #     self.assertTrue(TestCodeGen.test(input, expect, 501))

    # def test_1(self):
    #     input = Program([VarDecl(Id("x"), IntType()), FuncDecl(Id("main"), [], VoidType(), Block(
    #         [VarDecl(Id("x"), FloatType()), VarDecl(Id("y"), IntType())], [Block([VarDecl(Id("z"), FloatType())], []), Block([VarDecl(Id("t"), FloatType())], [])]))])
    #     expect = ""
    #     self.assertTrue(TestCodeGen.test(input, expect, 502))

    def test_2(self):
        input = Program([VarDecl(Id("x"), FloatType()), VarDecl(Id("y"), IntType()), FuncDecl(Id("main"), [], VoidType(
        ), Block([], [Assign(Id("x"), IntLiteral(10)), CallExpr(Id("putInt"), [Id("x")])]))])
        expect = "10"
        self.assertTrue(TestCodeGen.test(input, expect, 503))
