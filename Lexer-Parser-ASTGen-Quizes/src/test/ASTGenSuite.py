import unittest
from TestUtils import TestAST
from AST import *


class ASTGenSuite(unittest.TestCase):
    # def test_simple_program(self):
    #     input = """int a; int b;"""
    #     expect = str(10)
    #     self.assertTrue(TestAST.test(input, expect, 1))
    #
    # def test_simple_program_1(self):
    #     input = """int a, b, c;"""
    #     expect = str(8)
    #     self.assertTrue(TestAST.test(input, expect, 2))
    #
    # def test_simple_program_2(self):
    #     input = """int a;"""
    #     expect = str(6)
    #     self.assertTrue(TestAST.test(input, expect, 3))

    # def test_quiz3_1(self):
    #     input = """int a;"""
    #     expect = "Program([VarDecl(Id(a),IntType)])"
    #     self.assertTrue(TestAST.test(input, expect, 4))
    #
    # def test_quiz3_2(self):
    #     input = """int a,b;"""
    #     expect = "Program([VarDecl(Id(a),IntType),VarDecl(Id(b),IntType)])"
    #     self.assertTrue(TestAST.test(input, expect, 5))
    #
    # def test_quiz3_3(self):
    #     input = "int a;float b;"
    #     expect = "Program([VarDecl(Id(a),IntType),VarDecl(Id(b),FloatType)])"
    #     self.assertTrue(TestAST.test(input, expect, 6))
    #
    # def test_quiz3_4(self):
    #     input = "int a,b;float c;"
    #     expect = "Program([VarDecl(Id(a),IntType),VarDecl(Id(b),IntType),VarDecl(Id(c),FloatType)])"
    #     self.assertTrue(TestAST.test(input, expect, 7))
    #
    # def test_quiz3_5(self):
    #     input = "int a,b;float c,d,e;"
    #     expect = "Program([VarDecl(Id(a),IntType),VarDecl(Id(b),IntType),VarDecl(Id(c),FloatType),VarDecl(Id(d),FloatType),VarDecl(Id(e),FloatType)])"
    #     self.assertTrue(TestAST.test(input, expect, 8))

    def test_quiz5_1(self):
        input = "a := b := 4"
        expect = "Binary(:=,Id(a),Binary(:=,Id(b),IntLiteral(4)))"
        self.assertTrue(TestAST.test(input, expect, 9))

    def test_quiz5_2(self):
        input = "a >= b"
        expect = "Binary(>=,Id(a),Id(b))"
        self.assertTrue(TestAST.test(input, expect, 10))

    def test_quiz5_3(self):
        input = "(a := c := 4) >= b"
        expect = "Binary(>=,Binary(:=,Id(a),Binary(:=,Id(c),IntLiteral(4))),Id(b))"
        self.assertTrue(TestAST.test(input, expect, 11))

    # def test_quiz5_4(self):
    #     input = "(a  c) >= b"
    #     expect = "Binary(>=,Id(a),Id(b))"
    #     self.assertTrue(TestAST.test(input, expect, 12))
