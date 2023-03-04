import unittest
from TestUtils import TestChecker
from AST import *


class CheckerSuite(unittest.TestCase):
    #     def test_0(self):
    #         input = """
    #     x: integer = 3;
    #     x: string;
    #     main: function void(){}
    # """

    #         expect = "Redeclared Variable: x"
    #         self.assertTrue(TestChecker.test(input, expect, 400))

    #     def test_1(self):
    #         input = """
    #     x: integer = 3;
    #     y: auto;
    #     main: function void(){}
    # """

    #         expect = "Invalid Variable: y"
    #         self.assertTrue(TestChecker.test(input, expect, 401))

    #     def test_2(self):
    #         input = """
    #     x: integer = 3;
    #     y: auto = x;
    #     main: function void(){}
    # """

    #         expect = "[]"
    #         self.assertTrue(TestChecker.test(input, expect, 402))

    #     def test_3(self):
    #         input = """
    #     x: integer = 3;
    #     y: float = 3.100;
    #     z: auto = y + x;
    #     main: function void(){}
    # """

    #         expect = "[]"
    #         self.assertTrue(TestChecker.test(input, expect, 403))

    #     def test_4(self):
    #         input = """
    #     x: boolean;
    #     y: auto = 3.100;
    #     z: auto = y + x;
    #     main: function void(){}
    # """

    #         expect = "Type Mismatch In Expression: BinExpr(+, Id(y), Id(x))"
    #         self.assertTrue(TestChecker.test(input, expect, 404))

    #     def test_5(self):
    #         input = """
    #     x: string = "hello";
    #     y: auto = x == "Hiiii";
    #     main: function void(){}
    # """

    #         expect = "Type Mismatch In Expression: BinExpr(==, Id(x), StringLit(Hiiii))"
    #         self.assertTrue(TestChecker.test(input, expect, 405))

    #     def test_6(self):
    #         input = """
    #     x: boolean = false;
    #     y: auto = x == true;
    #     main: function void(){}
    # """

    #         expect = "[]"
    #         self.assertTrue(TestChecker.test(input, expect, 406))

    #     def test_7(self):
    #         input = """
    #     x: integer = 100;
    #     y: auto = x == true;
    #     main: function void(){}
    # """

    #         expect = "Type Mismatch In Expression: BinExpr(==, Id(x), BooleanLit(True))"
    #         self.assertTrue(TestChecker.test(input, expect, 407))

    #     def test_8(self):
    #         input = """
    #     x: integer = 100;
    #     y: auto = x != 5;
    #     main: function void(){}
    # """

    #         expect = "[]"
    #         self.assertTrue(TestChecker.test(input, expect, 408))

    #     def test_9(self):
    #         input = """
    #     x: integer = 100;
    #     y: integer = x != 5;
    #     main: function void(){}
    # """

    #         expect = "Type Mismatch In Expression: VarDecl(Id(y), IntegerType, BinExpr(!=, Id(x), IntegerLit(5)))"
    #         self.assertTrue(TestChecker.test(input, expect, 409))

    #     def test_10(self):
    #         input = """
    #     x: integer = -100;
    #     y: integer = -x;
    #     main: function void(){}
    # """

    #         expect = "[]"
    #         self.assertTrue(TestChecker.test(input, expect, 410))

    #     def test_11(self):
    #         input = """
    #     y: integer =  true || (true && false);
    #     main: function void(){}
    # """

    #         expect = "Type Mismatch In Expression: VarDecl(Id(y), IntegerType, BinExpr(||, BooleanLit(True), BinExpr(&&, BooleanLit(True), BooleanLit(True))))"
    #         self.assertTrue(TestChecker.test(input, expect, 411))

    #     def test_12(self):
    #         input = """
    #     x: integer = -100_999;
    #     y: float = x;
    #     main: function void(){}
    # """

    #         expect = "[]"
    #         self.assertTrue(TestChecker.test(input, expect, 412))

    #     def test_13(self):
    #         input = """
    #     x: float = -100_999.123;
    #     y: integer = x;
    #     main: function void(){}
    # """

    #         expect = "Type Mismatch In Expression: VarDecl(Id(y), IntegerType, Id(x))"
    #         self.assertTrue(TestChecker.test(input, expect, 413))

    #     def test_14(self):
    #         input = """
    #     a : array [2] of integer;
    #     main: function void(){}
    # """

    #         expect = "[]"
    #         self.assertTrue(TestChecker.test(input, expect, 414))

    #     def test_15(self):
    #         input = """
    #     a : array [2] of integer = {-1.0, 3.0};
    #     main: function void(){}
    # """

    #         expect = "Type Mismatch In Statement: VarDecl(Id(a), ArrayType([2], IntegerType), ArrayLit([UnExpr(-, FloatLit(1.0)), FloatLit(3.0)]))"
    #         self.assertTrue(TestChecker.test(input, expect, 415))

    #         def test_16(self):
    #             input = """
    #     a : array [2] of integer = {-1, 3};
    #     main: function void(){}
    # """

    #             expect = "[]"
    #             self.assertTrue(TestChecker.test(input, expect, 416))

    #     def test_17(self):
    #         input = """
    #     a: array [2] of integer = {1, 2};
    #     main: function void(){}
    # """

    #         expect = "[]"
    #         self.assertTrue(TestChecker.test(input, expect, 417))

    #     def test_18(self):
    #         input = """
    #     b: array [2, 3] of integer = {{}, {}};
    #     main: function void(){}
    # """

    #         expect = "[]"
    #         self.assertTrue(TestChecker.test(input, expect, 418))

    #     def test_19(self):
    #         input = """
    #     c: array [2, 3] of integer = {{1}, {1, 2, 3}};
    #     main: function void(){}
    # """

    #         expect = "[]"
    #         self.assertTrue(TestChecker.test(input, expect, 419))

    #     def test_20(self):
    #         input = """
    #     d: array [2, 3, 5] of integer = {{{1, 3, 4}, {5, 6}, {}}, {{1}, {2}, {1}}};
    #     main: function void(){}
    # """

    #         expect = "[]"
    #         self.assertTrue(TestChecker.test(input, expect, 420))

    #     def test_21(self):
    #         input = """
    #     e: array [2, 3] of integer = {{1.0}, {1, 2, 3}};
    #     main: function void(){}
    # """

    #         expect = "Type Mismatch In Statement: VarDecl(Id(e), ArrayType([2, 3], IntegerType), ArrayLit([ArrayLit([FloatLit(1.0)]), ArrayLit([IntegerLit(1), IntegerLit(2), IntegerLit(3)])]))"
    #         self.assertTrue(TestChecker.test(input, expect, 421))

    #     def test_22(self):
    #         input = """
    #     f: array [2, 3] of integer = {{1, 1}, {1.0, 2, 3}};
    #     main: function void(){}
    # """

    #         expect = "Illegal Array Literal: ArrayLit([FloatLit(1.0), IntegerLit(2), IntegerLit(3)])"
    #         self.assertTrue(TestChecker.test(input, expect, 422))

    #     def test_23(self):
    #         input = """
    #         x, y, z: integer = 1, 2, 3;
    #         a: array [3, 2] of integer = {{x + z}, {y, z}};
    #         main: function void(){}
    # """

    #         expect = "[]"
    #         self.assertTrue(TestChecker.test(input, expect, 423))

    #     def test_24(self):
    #         input = """
    #     // c : integer = 1;
    #     c : array [1] of integer = {1};
    #     b : integer = 10;
    #     // a : array [2, 2] of integer = {{3, c[0.1 + 3]}, {b, 199}};
    #     a : array [2, 2] of integer = {{3, c[1 + 3, 3 + 4]}, {b, 199}};
    #     main: function void(){}
    # """

    #         expect = "[]"
    #         self.assertTrue(TestChecker.test(input, expect, 424))

    #     def test_25(self):
    #         input = """
    #     a3 : array [2, 2] of boolean = {{3.3, 3.5}, {123.1, 199.10}};
    #     main: function void(){}
    # """

    #         expect = "Type Mismatch In Statement: VarDecl(Id(a3), ArrayType([2, 2], BooleanType), ArrayLit([ArrayLit([FloatLit(3.3), FloatLit(3.5)]), ArrayLit([FloatLit(123.1), FloatLit(199.10)])]))"
    #         self.assertTrue(TestChecker.test(input, expect, 425))

    #     def test_26(self):
    #         input = """
    #     a2 : array [2, 2] of integer = {{3.3, 3.5}, {123.1, 199.10}};
    #     main: function void(){}
    # """

    #         expect = "Type Mismatch In Statement: VarDecl(Id(a2), ArrayType([2, 2], IntegerType), ArrayLit([ArrayLit([FloatLit(3.3), FloatLit(3.5)]), ArrayLit([FloatLit(123.1), FloatLit(199.10)])]))"
    #         self.assertTrue(TestChecker.test(input, expect, 426))

    #     def test_27(self):
    #         input = """
    #     a : array [2, 2] of float = {{3, 3}, {123, 199}};
    #     main: function void(){}
    # """

    #         expect = "[]"
    #         self.assertTrue(TestChecker.test(input, expect, 427))

    #     def test_28(self):
    #         input = """
    #     a : array [2, 2] of float = {{3, 3}, {123, 199, 123}, {123}};
    #     main: function void(){}
    # """

    #         expect = "Type Mismatch In Statement: VarDecl(Id(a), ArrayType([2, 2], FloatType), ArrayLit([ArrayLit([IntegerLit(3), IntegerLit(3)]), ArrayLit([IntegerLit(123), IntegerLit(199), IntegerLit(123)]), ArrayLit([IntegerLit(123)])]))"
    #         self.assertTrue(TestChecker.test(input, expect, 428))

    #     def test_29(self):
    #         input = """
    #     a : array [2, 2] of float = {false};
    #     main: function void(){}
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
    #         y: float = 3.100;
    #         z: auto = y + x;

    #         c : array [1] of integer = {1};
    #         b : integer = 10;
    #         a : array [2, 2] of integer = {{3, c[1 + 3]}, {b, 199}};
    #     }
    #     main: function void(){}
    # """

    #         expect = "[]"
    #         self.assertTrue(TestChecker.test(input, expect, 436))

    #     def test_37(self):
    #         input = """
    #     x: float = 3.0;
    #     fact : function integer (n : integer) {
    #         if (n == 10) {}
    #         else {
    #         }
    #     }
    #     main: function void(){}
    # """

    #         expect = "[]"
    #         self.assertTrue(TestChecker.test(input, expect, 437))

    #     def test_38(self):
    #         input = """
    #     x: float = 3.0;
    #     fact : function integer (n : integer) {
    #         if (n + 10) {}
    #         else {
    #         }
    #     }
    #     main: function void(){}
    # """

    #         expect = "Type Mismatch In Statement: IfStmt(BinExpr(+, Id(n), IntegerLit(10)), BlockStmt([]), BlockStmt([]))"
    #         self.assertTrue(TestChecker.test(input, expect, 438))

    #     def test_39(self):
    #         input = """
    #     x: float = 3.0;
    #     a : array [2] of integer;
    #     fact : function integer (n : integer) {
    #         n = n + 10;
    #         a[0] = 1239;
    #     }
    #     main: function void(){}
    # """

    #         expect = "Type Mismatch In Statement: AssignStmt(ArrayCell(Id(a), [IntegerLit(0)]), IntegerLit(1239))"
    #         self.assertTrue(TestChecker.test(input, expect, 439))

    #     def test_40(self):
    #         input = """
    #     x: float = 3.0;
    #     a : array [2] of integer;
    #     foo: function auto(){}
    #     fact : function integer (n : integer) {
    #         b: float;
    #         n = b + 1;
    #         // foo(): callstmt
    #     }
    #     main: function void(){}
    # """

    #         expect = "Type Mismatch In Statement: AssignStmt(Id(n), BinExpr(+, Id(b), IntegerLit(1)))"
    #         self.assertTrue(TestChecker.test(input, expect, 440))

    #     def test_40(self):
    #         input = """
    #     a : array [2] of integer;
    #     // foo: function auto(){}
    #     foo: function auto(x: integer){}
    #     // foo1: function auto(y: float){}
    #     fact : function integer (n : integer) {
    #         foo: float = 3.0;
    #         b: integer;
    #         // n1: float = foo(foo(1)); // foo(int)
    #         // n1: float = foo(1) + foo1(foo(100)); // foo: float foo1: float
    #         // n1: float = foo(1) + 1; // foo: int
    #         //n1: float = !foo(1) + 1; // TypeMisMatch
    #         n1: boolean = -foo(1) == true;
    #         // n1: float = -foo(1) + 1; // foo: float
    #     }
    #     main: function void(){}
    # """

    #         expect = "Type Mismatch In Statement: AssignStmt(Id(n), BinExpr(+, Id(b), IntegerLit(1)))"
    #         self.assertTrue(TestChecker.test(input, expect, 440))

    #     def test_41(self):
    #         input = """
    #     foo: function auto(x: integer){}
    #     foo1: function auto(x: float){}
    #     fact : function integer (n : integer) {
    #         // b: integer = 99;
    #         // b = foo(100); // foo: int
    #         // foo(19) = b // don't have this

    #         a : array [2] of integer;
    #         a[1] = (foo1(foo(1900)) + 1);
    #         // a[0] = 19;
    #         // a[2] = 10.1231;
    #         // a[2] = false;

    #         // foo: float = 3.0;
    #         // foo = foo(100);

    #         // n1: float = foo(foo(1)); // foo(int)
    #         // n1: float = foo(1) + foo1(foo(100)); // foo: float foo1: float
    #         // n1: float = foo(1) + 1; // foo: int
    #         //n1: float = !foo(1) + 1; // TypeMisMatch
    #         // n1: boolean = -foo(1) == true;
    #         // n1: float = -foo(1) + 1; // foo: float
    #     }
    #     main: function void(){}
    # """

    #         expect = "Type Mismatch In Statement: AssignStmt(Id(n), BinExpr(+, Id(b), IntegerLit(1)))"
    #         self.assertTrue(TestChecker.test(input, expect, 441))

    #     def test_43(self):
    #         input = """
    #     // foo: function auto(){}
    #     foo1: function auto(y: boolean){}
    #     foo2: function boolean(){}
    #     fact : function integer (n : integer) {
    #         // if (foo1(foo()) == true){}
    #         a : array [2] of integer;
    #         // if (8 < 5){}
    #         // if (8.0 < 5){}
    #         // if (a[1, 2, 3] > 100){}
    #         // if (a[1, 2, 3] > foo()){}
    #         // if (!foo()){}
    #         // if (!foo2()){}
    #         i: float = 3;
    #         for (i = 123, 9 > 8, i + 1){}
    #     }
    #     main: function void(){}
    # """

    #         expect = "Type Mismatch In Statement: AssignStmt(Id(n), BinExpr(+, Id(b), IntegerLit(1)))"
    #         self.assertTrue(TestChecker.test(input, expect, 443))

    #     def test_44(self):
    #         input = """
    #     // foo: function auto(){}
    #     // foo1: function auto(y: boolean){}
    #     foo2: function boolean(i: integer){}
    #     /*fact : function integer () {
    #         // a : array [2] of integer;
    #         // i: float = 3;
    #     }*/
    #     main: function void(){

    #         // i: integer = 3;
    #         // for (i = 123, i > 8, i + 1){}

    #         for (i = 123, i > 8, foo2(1)){}
    #         // for (i = 123, i > 8, i + 1.4){}
    #     }
    # """

    #         expect = "[]"
    #         self.assertTrue(TestChecker.test(input, expect, 444))

    #     def test_45(self):
    #         input = """
    #     foo2: function auto(i: integer){
    #         return 1;
    #     }

    #     main: function void(){}
    # """

    #         expect = "[]"
    #         self.assertTrue(TestChecker.test(input, expect, 445))

    def test_46(self):
        input = """

    foo1: function integer(){}

    // foo2: function float(inherit x: float) inherit foo1{
    foo2: function float(inherit x: boolean){
        // super(10);
        // i: integer = 4; error
        return 1;
    }
    // super: function integer(){} -> Redeclared
    // foo3: function float() inherit foo1{
    foo3: function float() inherit foo1{
    // foo3: function float(){
        printInteger(1);
        preventDefault();
        // super();
        // preventDefault();
        // i: integer = 4; error
        // super(1, 322, 324); -> Invalid Statement In Function: foo3
        return 1.123;
    }

    main: function void(){
        x: integer = readInteger();
    }
"""

        expect = "[]"
        self.assertTrue(TestChecker.test(input, expect, 446))
