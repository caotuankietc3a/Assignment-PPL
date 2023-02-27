import unittest
from TestUtils import TestChecker
from AST import *


class CheckerSuite(unittest.TestCase):
    #     def test_0(self):
    #         input = """
    #     x: integer = 3;
    #     x: string;
    # """

    #         expect = "Redeclared Variable: x"
    #         self.assertTrue(TestChecker.test(input, expect, 400))

    #     def test_1(self):
    #         input = """
    #     x: integer = 3;
    #     y: auto;
    # """

    #         expect = "Invalid Variable: y"
    #         self.assertTrue(TestChecker.test(input, expect, 401))

    #     def test_2(self):
    #         input = """
    #     x: integer = 3;
    #     y: auto = x;
    # """

    #         expect = "[]"
    #         self.assertTrue(TestChecker.test(input, expect, 402))

    #     def test_3(self):
    #         input = """
    #     x: integer = 3;
    #     y: float = 3.100;
    #     z: auto = y + x;
    # """

    #         expect = "[]"
    #         self.assertTrue(TestChecker.test(input, expect, 403))

    #     def test_4(self):
    #         input = """
    #     x: boolean;
    #     y: auto = 3.100;
    #     z: auto = y + x;
    # """

    #         expect = "Type Mismatch In Expression: BinExpr(+, Id(y), Id(x))"
    #         self.assertTrue(TestChecker.test(input, expect, 404))

    #     def test_5(self):
    #         input = """
    #     x: string = "hello";
    #     y: auto = x == "Hiiii";
    # """

    #         expect = "Type Mismatch In Expression: BinExpr(==, Id(x), StringLit(Hiiii))"
    #         self.assertTrue(TestChecker.test(input, expect, 405))

    #     def test_6(self):
    #         input = """
    #     x: boolean = false;
    #     y: auto = x == true;
    # """

    #         expect = "[]"
    #         self.assertTrue(TestChecker.test(input, expect, 406))

    #     def test_7(self):
    #         input = """
    #     x: integer = 100;
    #     y: auto = x == true;
    # """

    #         expect = "Type Mismatch In Expression: BinExpr(==, Id(x), BooleanLit(True))"
    #         self.assertTrue(TestChecker.test(input, expect, 407))

    #     def test_8(self):
    #         input = """
    #     x: integer = 100;
    #     y: auto = x != 5;
    # """

    #         expect = "[]"
    #         self.assertTrue(TestChecker.test(input, expect, 408))

    #     def test_9(self):
    #         input = """
    #     x: integer = 100;
    #     y: integer = x != 5;
    # """

    #         expect = "Type Mismatch In Expression: VarDecl(Id(y), IntegerType, BinExpr(!=, Id(x), IntegerLit(5)))"
    #         self.assertTrue(TestChecker.test(input, expect, 409))

    #     def test_10(self):
    #         input = """
    #     x: integer = -100;
    #     y: integer = -x;
    # """

    #         expect = "[]"
    #         self.assertTrue(TestChecker.test(input, expect, 410))

    #     def test_11(self):
    #         input = """
    #     y: integer =  true || (true && false);
    # """

    #         expect = "Type Mismatch In Expression: VarDecl(Id(y), IntegerType, BinExpr(||, BooleanLit(True), BinExpr(&&, BooleanLit(True), BooleanLit(True))))"
    #         self.assertTrue(TestChecker.test(input, expect, 411))

    #     def test_12(self):
    #         input = """
    #     x: integer = -100_999;
    #     y: float = x;
    # """

    #         expect = "[]"
    #         self.assertTrue(TestChecker.test(input, expect, 412))

    #     def test_13(self):
    #         input = """
    #     x: float = -100_999.123;
    #     y: integer = x;
    # """

    #         expect = "Type Mismatch In Expression: VarDecl(Id(y), IntegerType, Id(x))"
    #         self.assertTrue(TestChecker.test(input, expect, 413))

    #     def test_14(self):
    #         input = """
    # a : array [2] of integer;
    # """

    #         expect = "[]"
    #         self.assertTrue(TestChecker.test(input, expect, 414))

    #     def test_15(self):
    #         input = """
    # a : array [2] of integer = {-1.0, 3.0};
    # """

    #         expect = "Illegal Array Literal: ArrayLit([UnExpr(-, FloatLit(1.0)), FloatLit(3.0)])"
    #         self.assertTrue(TestChecker.test(input, expect, 415))

    #         def test_16(self):
    #             input = """
    #     a : array [2] of integer = {-1, 3};
    # """

    #             expect = "[]"
    #             self.assertTrue(TestChecker.test(input, expect, 416))

    def test_17(self):
        input = """
    b : integer = 10;
    a3 : array [2, 2] of integer = {{1, 3, 4, 5}};
    //a3 : array [2, 2] of integer = {{} , {}};
    // a4 : array [2, 2] of integer = {{3, 199}, 1};
    // a5 : array [2, 2] of integer = {3.0, 199, 1};
"""

        expect = "[]"
        self.assertTrue(TestChecker.test(input, expect, 417))

#     def test_18(self):
#         input = """
#     c : array [1] of integer = {1}
#     b : integer = 10;
#     a : array [2, 2] of integer = {{b, c[1]}, {3, 199}};
# """

#         expect = "[]"
#         self.assertTrue(TestChecker.test(input, expect, 418))
