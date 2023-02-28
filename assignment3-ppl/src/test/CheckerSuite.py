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
    #     a : array [2] of integer = {-1.0, 3.0};
    # """

    #         expect = "Type Mismatch In Statement: VarDecl(Id(a), ArrayType([2], IntegerType), ArrayLit([UnExpr(-, FloatLit(1.0)), FloatLit(3.0)]))"
    #         self.assertTrue(TestChecker.test(input, expect, 415))

    #         def test_16(self):
    #             input = """
    #     a : array [2] of integer = {-1, 3};
    # """

    #             expect = "[]"
    #             self.assertTrue(TestChecker.test(input, expect, 416))

    #     def test_17(self):
    #         input = """
    #         a: array [2] of integer = {1, 2};
    # """

    #         expect = "[]"
    #         self.assertTrue(TestChecker.test(input, expect, 417))

    #     def test_18(self):
    #         input = """
    #         b: array [2, 3] of integer = {{}, {}};
    # """

    #         expect = "[]"
    #         self.assertTrue(TestChecker.test(input, expect, 418))

    #     def test_19(self):
    #         input = """
    #         c: array [2, 3] of integer = {{1}, {1, 2, 3}};
    # """

    #         expect = "[]"
    #         self.assertTrue(TestChecker.test(input, expect, 419))

    #     def test_20(self):
    #         input = """
    #         d: array [2, 3, 5] of integer = {{{1, 3, 4}, {5, 6}, {}}, {{1}, {2}, {1}}};
    # """

    #         expect = "[]"
    #         self.assertTrue(TestChecker.test(input, expect, 420))

    #     def test_21(self):
    #         input = """
    #         e: array [2, 3] of integer = {{1.0}, {1, 2, 3}};
    # """

    #         expect = "Type Mismatch In Statement: VarDecl(Id(e), ArrayType([2, 3], IntegerType), ArrayLit([ArrayLit([FloatLit(1.0)]), ArrayLit([IntegerLit(1), IntegerLit(2), IntegerLit(3)])]))"
    #         self.assertTrue(TestChecker.test(input, expect, 421))

    #     def test_22(self):
    #         input = """
    #         f: array [2, 3] of integer = {{1, 1}, {1.0, 2, 3}};
    # """

    #         expect = "Illegal Array Literal: ArrayLit([FloatLit(1.0), IntegerLit(2), IntegerLit(3)])"
    #         self.assertTrue(TestChecker.test(input, expect, 422))

    #     def test_23(self):
    #         input = """
    #         x, y, z: integer = 1, 2, 3;
    #         a: array [3, 2] of integer = {{x + z}, {y, z}};
    # """

    #         expect = "[]"
    #         self.assertTrue(TestChecker.test(input, expect, 423))

    def test_24(self):
        input = """
    // c : integer = 1;
    c : array [1] of integer = {1};
    b : integer = 10;
    // a : array [2, 2] of integer = {{3, c[0.1 + 3]}, {b, 199}};
    a : array [2, 2] of integer = {{3, c[1 + 3, 3 + 4]}, {b, 199}};
    main: function void(){}
"""

        expect = "[]"
        self.assertTrue(TestChecker.test(input, expect, 424))

    #     def test_25(self):
    #         input = """
    #     a3 : array [2, 2] of boolean = {{3.3, 3.5}, {123.1, 199.10}};
    # """

    #         expect = "Type Mismatch In Statement: VarDecl(Id(a3), ArrayType([2, 2], BooleanType), ArrayLit([ArrayLit([FloatLit(3.3), FloatLit(3.5)]), ArrayLit([FloatLit(123.1), FloatLit(199.10)])]))"
    #         self.assertTrue(TestChecker.test(input, expect, 425))

    #     def test_26(self):
    #         input = """
    #     a2 : array [2, 2] of integer = {{3.3, 3.5}, {123.1, 199.10}};
    # """

    #         expect = "Type Mismatch In Statement: VarDecl(Id(a2), ArrayType([2, 2], IntegerType), ArrayLit([ArrayLit([FloatLit(3.3), FloatLit(3.5)]), ArrayLit([FloatLit(123.1), FloatLit(199.10)])]))"
    #         self.assertTrue(TestChecker.test(input, expect, 426))

    #     def test_27(self):
    #         input = """
    #     a : array [2, 2] of float = {{3, 3}, {123, 199}};
    # """

    #         expect = "[]"
    #         self.assertTrue(TestChecker.test(input, expect, 427))

    #     def test_28(self):
    #         input = """
    #     a : array [2, 2] of float = {{3, 3}, {123, 199, 123}, {123}};
    # """

    #         expect = "Type Mismatch In Statement: VarDecl(Id(a), ArrayType([2, 2], FloatType), ArrayLit([ArrayLit([IntegerLit(3), IntegerLit(3)]), ArrayLit([IntegerLit(123), IntegerLit(199), IntegerLit(123)]), ArrayLit([IntegerLit(123)])]))"
    #         self.assertTrue(TestChecker.test(input, expect, 428))

    #     def test_29(self):
    #         input = """
    #     a : array [2, 2] of float = {false};
    # """

    #         expect = "Type Mismatch In Statement: VarDecl(Id(a), ArrayType([2, 2], FloatType), ArrayLit([BooleanLit(True)]))"
    #         self.assertTrue(TestChecker.test(input, expect, 429))

    #     def test_30(self):
    #         input = """
    #     main: function void(){}
    # """

    #         expect = "[]"
    #         self.assertTrue(TestChecker.test(input, expect, 430))

    #     def test_31(self):
    #         input = """
    #     fact : function integer (n : integer) {}
    # """

    #         expect = "No entry point"
    #         self.assertTrue(TestChecker.test(input, expect, 431))

    #     def test_32(self):
    #         input = """
    #     fact : function integer (n : integer) {}
    #     main: function void(){}
    # """

    #         expect = "[]"
    #         self.assertTrue(TestChecker.test(input, expect, 432))

    #     def test_33(self):
    #         input = """
    #     fact : function integer (n : integer, n : float) {}
    #     main: function void(){}
    # """

    #         expect = "Redeclared Parameter: n"
    #         self.assertTrue(TestChecker.test(input, expect, 433))

    #     def test_34(self):
    #         input = """
    #     fact : function integer (n : integer) {}
    #     fact : function float () {}
    #     main: function void(){}
    # """

    #         expect = "Redeclared Function: fact"
    #         self.assertTrue(TestChecker.test(input, expect, 434))

    #     def test_35(self):
    #         input = """
    #     x: float = 3.0;
    #     fact : function integer (n : integer) {
    #         x: integer = 3;
    #         x: boolean = false;
    #     }
    #     main: function void(){}
    # """

    #         expect = "Redeclared Variable: x"
    #         self.assertTrue(TestChecker.test(input, expect, 435))

    #     def test_36(self):
    #         input = """
    #     x: float = 3.0;
    #     fact : function integer (n : integer) {
    #         x: integer = 3;
    #     }
    #     main: function void(){}
    # """

    #         expect = "[]"
    #         self.assertTrue(TestChecker.test(input, expect, 436))
