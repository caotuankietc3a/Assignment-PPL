import unittest
from TestUtils import TestAST
from AST import *


class ASTGenSuite(unittest.TestCase):
    def test_vardecls_0(self):
        input = """x: integer;"""
        expect = str(Program([VarDecl(Id("x"), IntegerType())]))
        self.assertTrue(TestAST.test(input, expect, 300))

    def test_vardecls_1(self):
        input = """x, y, z: integer = 1, 2, 3;"""
        expect = r"""Program([
	VarDecl(Id(x), IntegerType, IntegerLit(1))
	VarDecl(Id(y), IntegerType, IntegerLit(2))
	VarDecl(Id(z), IntegerType, IntegerLit(3))
])"""
        self.assertTrue(TestAST.test(input, expect, 301))

    def test_vardecls_2(self):
        input = """x, y, z: integer = 1, 2, 3;
        a, b: float;"""
        expect = r"""Program([
	VarDecl(Id(x), IntegerType, IntegerLit(1))
	VarDecl(Id(y), IntegerType, IntegerLit(2))
	VarDecl(Id(z), IntegerType, IntegerLit(3))
	VarDecl(Id(a), FloatType)
	VarDecl(Id(b), FloatType)
])"""
        self.assertTrue(TestAST.test(input, expect, 302))

    def test_vardecls_3(self):
        input = r"""a,b,c,d: string = "12345", "test", "0000000", "Hello World\n";"""
        expect = r"""Program([
	VarDecl(Id(a), StringType, StringLit(12345))
	VarDecl(Id(b), StringType, StringLit(test))
	VarDecl(Id(c), StringType, StringLit(0000000))
	VarDecl(Id(d), StringType, StringLit(Hello World\n))
])"""
        self.assertTrue(TestAST.test(input, expect, 303))

    def test_vardecls_4(self):
        input = r"""a, b, c : boolean = false, true, false;"""
        expect = r"""Program([
	VarDecl(Id(a), BooleanType, BooleanLit(True))
	VarDecl(Id(b), BooleanType, BooleanLit(True))
	VarDecl(Id(c), BooleanType, BooleanLit(True))
])"""
        self.assertTrue(TestAST.test(input, expect, 304))

    def test_vardecls_5(self):
        input = r"""
a, b, c : auto = 1, true, "Hello World!";
"""
        expect = r"""Program([
	VarDecl(Id(a), AutoType, IntegerLit(1))
	VarDecl(Id(b), AutoType, BooleanLit(True))
	VarDecl(Id(c), AutoType, StringLit(Hello World!))
])"""
        self.assertTrue(TestAST.test(input, expect, 305))

    def test_vardecls_6(self):
        input = r"""
a,   b,   c   : array [2, 3] of integer;
"""
        expect = r"""Program([
	VarDecl(Id(a), ArrayType([2, 3], IntegerType))
	VarDecl(Id(b), ArrayType([2, 3], IntegerType))
	VarDecl(Id(c), ArrayType([2, 3], IntegerType))
])"""
        self.assertTrue(TestAST.test(input, expect, 306))

    def test_vardecls_7(self):
        input = r"""
a1,   b2,   c3   : array [2] of string;
a,   b,   c   : array [6, 3, 10] of float;
"""
        expect = r"""Program([
	VarDecl(Id(a1), ArrayType([2], StringType))
	VarDecl(Id(b2), ArrayType([2], StringType))
	VarDecl(Id(c3), ArrayType([2], StringType))
	VarDecl(Id(a), ArrayType([6, 3, 10], FloatType))
	VarDecl(Id(b), ArrayType([6, 3, 10], FloatType))
	VarDecl(Id(c), ArrayType([6, 3, 10], FloatType))
])"""
        self.assertTrue(TestAST.test(input, expect, 307))

    def test_vardecls_8(self):
        input = r"""
a,   b,   c   : array [2] of integer = {1, 3}, {9}, {};
"""
        expect = r"""Program([
	VarDecl(Id(a1), ArrayType([2], StringType))
	VarDecl(Id(b2), ArrayType([2], StringType))
	VarDecl(Id(c3), ArrayType([2], StringType))
	VarDecl(Id(a), ArrayType([6, 3, 10], FloatType))
	VarDecl(Id(b), ArrayType([6, 3, 10], FloatType))
	VarDecl(Id(c), ArrayType([6, 3, 10], FloatType))
])"""
        self.assertTrue(TestAST.test(input, expect, 308))

#     def test_funcdecls_1(self):
#         input = """main: function void () {
#         }"""
#         expect = """Program([
# 	FuncDecl(main, VoidType, [], None, BlockStmt([]))
# ])"""
#         self.assertTrue(TestAST.test(input, expect, 303))
# #
#
#     def test_funcdecls_2(self):
#         input = """main: function void () {
#             printInteger(4);
#         }"""
#         expect = """Program([
# 	FuncDecl(main, VoidType, [], None, BlockStmt([]))
# ])"""
#         self.assertTrue(TestAST.test(input, expect, 304))
#
#     def test_more_complex_program(self):
#         """More complex program"""
#         input = """main: function void () {
#             printInteger(4);
#         }"""
#         expect = """Program([
# 	FuncDecl(main, VoidType, [], None, BlockStmt([]))
# ])"""
#         self.assertTrue(TestAST.test(input, expect, 304))
