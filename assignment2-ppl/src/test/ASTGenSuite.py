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
a,   b,   c   : array [2] of integer = {-1, 3}, {9}, {};
"""
        expect = r"""Program([
	VarDecl(Id(a), ArrayType([2], IntegerType), ArrayLit([UnExpr(-, IntegerLit(1)), IntegerLit(3)]))
	VarDecl(Id(b), ArrayType([2], IntegerType), ArrayLit([IntegerLit(9)]))
	VarDecl(Id(c), ArrayType([2], IntegerType), ArrayLit([]))
])"""
        self.assertTrue(TestAST.test(input, expect, 308))

    def test_vardecls_9(self):
        input = r"""
a,   b,   c   : array [2, 3] of integer = {{1, 2, 3}, {0, 5, 6}}, {{}, {}}, {{2, 3}, {}};
"""
        expect = r"""Program([
	VarDecl(Id(a), ArrayType([2, 3], IntegerType), ArrayLit([ArrayLit([IntegerLit(1), IntegerLit(2), IntegerLit(3)]), ArrayLit([IntegerLit(0), IntegerLit(5), IntegerLit(6)])]))
	VarDecl(Id(b), ArrayType([2, 3], IntegerType), ArrayLit([ArrayLit([]), ArrayLit([])]))
	VarDecl(Id(c), ArrayType([2, 3], IntegerType), ArrayLit([ArrayLit([IntegerLit(2), IntegerLit(3)]), ArrayLit([])]))
])"""
        self.assertTrue(TestAST.test(input, expect, 309))

    def test_vardecls_10(self):
        input = r"""
a,   b,   c   : array [2, 3] of boolean = {{false, true, false}, {true, false, true}}, {{}, {}}, {{true, false}, {}};
"""
        expect = r"""Program([
	VarDecl(Id(a), ArrayType([2, 3], BooleanType), ArrayLit([ArrayLit([BooleanLit(True), BooleanLit(True), BooleanLit(True)]), ArrayLit([BooleanLit(True), BooleanLit(True), BooleanLit(True)])]))
	VarDecl(Id(b), ArrayType([2, 3], BooleanType), ArrayLit([ArrayLit([]), ArrayLit([])]))
	VarDecl(Id(c), ArrayType([2, 3], BooleanType), ArrayLit([ArrayLit([BooleanLit(True), BooleanLit(True)]), ArrayLit([])]))
])"""
        self.assertTrue(TestAST.test(input, expect, 310))

    def test_vardecls_11(self):
        input = r"""
a1,   b1,   c1   : array [2, 3] of string = {{"hello", "world", "!!!"}, {"test\n", "string\t"}}, {{}, {}}, {{"hahaha"}, {}};
"""
        expect = r"""Program([
	VarDecl(Id(a1), ArrayType([2, 3], StringType), ArrayLit([ArrayLit([StringLit(hello), StringLit(world), StringLit(!!!)]), ArrayLit([StringLit(test\n), StringLit(string\t)])]))
	VarDecl(Id(b1), ArrayType([2, 3], StringType), ArrayLit([ArrayLit([]), ArrayLit([])]))
	VarDecl(Id(c1), ArrayType([2, 3], StringType), ArrayLit([ArrayLit([StringLit(hahaha)]), ArrayLit([])]))
])"""
        self.assertTrue(TestAST.test(input, expect, 311))

    def test_vardecls_12(self):
        input = r"""
a2,   b2,   c2   : array [2, 3] of float = {{1.33333, .5555e1, 189.00000}, {157., 1_2_3_4., 1_2_3_56.1234}}, {{}, {}}, {{0.33E-3, 12e8}, {}};
"""
        expect = r"""Program([
	VarDecl(Id(a2), ArrayType([2, 3], FloatType), ArrayLit([ArrayLit([FloatLit(1.33333), FloatLit(.5555e1), FloatLit(189.00000)]), ArrayLit([FloatLit(157.), FloatLit(1234.), FloatLit(12356.1234)])]))
	VarDecl(Id(b2), ArrayType([2, 3], FloatType), ArrayLit([ArrayLit([]), ArrayLit([])]))
	VarDecl(Id(c2), ArrayType([2, 3], FloatType), ArrayLit([ArrayLit([FloatLit(0.33E-3), FloatLit(12e8)]), ArrayLit([])]))
])"""
        self.assertTrue(TestAST.test(input, expect, 312))

    def test_vardecls_13(self):
        input = r"""
a1,   b1,   c1   : array [2, 3] of integer = {{1, 2, 3}, {0, 5, 6}}, {{}, {}}, {{2, 3}, {}};
a2,   b2,   c2   : array [2, 3] of boolean = {{false, true, false}, {true, false, true}}, {{}, {}}, {{true, false}, {}};
a3,   b3,   c3   : array [2, 3] of string = {{"hello", "world", "!!!"}, {"test\n", "string\t"}}, {{}, {}}, {{"hahaha"}, {}};
a4,   b4,   c4   : array [2, 3] of float = {{1.33333, .5555e1, 189.00000}, {157., 1_2_3_4., 1_2_3_56.1234}}, {{}, {}}, {{0.33E-3, 12e8}, {}};
"""
        expect = r"""Program([
	VarDecl(Id(a1), ArrayType([2, 3], IntegerType), ArrayLit([ArrayLit([IntegerLit(1), IntegerLit(2), IntegerLit(3)]), ArrayLit([IntegerLit(0), IntegerLit(5), IntegerLit(6)])]))
	VarDecl(Id(b1), ArrayType([2, 3], IntegerType), ArrayLit([ArrayLit([]), ArrayLit([])]))
	VarDecl(Id(c1), ArrayType([2, 3], IntegerType), ArrayLit([ArrayLit([IntegerLit(2), IntegerLit(3)]), ArrayLit([])]))
	VarDecl(Id(a2), ArrayType([2, 3], BooleanType), ArrayLit([ArrayLit([BooleanLit(True), BooleanLit(True), BooleanLit(True)]), ArrayLit([BooleanLit(True), BooleanLit(True), BooleanLit(True)])]))
	VarDecl(Id(b2), ArrayType([2, 3], BooleanType), ArrayLit([ArrayLit([]), ArrayLit([])]))
	VarDecl(Id(c2), ArrayType([2, 3], BooleanType), ArrayLit([ArrayLit([BooleanLit(True), BooleanLit(True)]), ArrayLit([])]))
	VarDecl(Id(a3), ArrayType([2, 3], StringType), ArrayLit([ArrayLit([StringLit(hello), StringLit(world), StringLit(!!!)]), ArrayLit([StringLit(test\n), StringLit(string\t)])]))
	VarDecl(Id(b3), ArrayType([2, 3], StringType), ArrayLit([ArrayLit([]), ArrayLit([])]))
	VarDecl(Id(c3), ArrayType([2, 3], StringType), ArrayLit([ArrayLit([StringLit(hahaha)]), ArrayLit([])]))
	VarDecl(Id(a4), ArrayType([2, 3], FloatType), ArrayLit([ArrayLit([FloatLit(1.33333), FloatLit(.5555e1), FloatLit(189.00000)]), ArrayLit([FloatLit(157.), FloatLit(1234.), FloatLit(12356.1234)])]))
	VarDecl(Id(b4), ArrayType([2, 3], FloatType), ArrayLit([ArrayLit([]), ArrayLit([])]))
	VarDecl(Id(c4), ArrayType([2, 3], FloatType), ArrayLit([ArrayLit([FloatLit(0.33E-3), FloatLit(12e8)]), ArrayLit([])]))
])"""
        self.assertTrue(TestAST.test(input, expect, 313))

    def test_funcdecls_0(self):
        input = """main: function void () {
        }"""
        expect = """Program([
	FuncDecl(Id(main), VoidType, [], None, BlockStmt([]))
])"""
        self.assertTrue(TestAST.test(input, expect, 314))

    def test_funcdecls_1(self):
        input = """main: function void () {
            printInteger(4);
        }"""
        expect = """Program([
	FuncDecl(Id(main), VoidType, [], None, BlockStmt([CallStmt(Id(printInteger), IntegerLit(4))]))
])"""
        self.assertTrue(TestAST.test(input, expect, 315))

    def test_funcdecls_2(self):
        input = r"""
main : function void () {
    found : boolean = true;
    is_Num, is_String: string = "", "";
    is_String = "TEST";
}
"""
        expect = r"""Program([
	FuncDecl(Id(main), VoidType, [], None, BlockStmt([VarDecl(Id(found), BooleanType, BooleanLit(True)), VarDecl(Id(is_Num), StringType, StringLit()), VarDecl(Id(is_String), StringType, StringLit()), AssignStmt(Id(is_String), StringLit(TEST))]))
])"""
        self.assertTrue(TestAST.test(input, expect, 316))

    def test_funcdecls_3(self):
        input = r"""
main : function void () {
    nE : integer = 0;
    for (i = 0, i < nE, i + 1) {
        if (nE == 10 + 5) {
            return nE;
        }
    }
}
"""
        expect = r"""Program([
	FuncDecl(Id(main), VoidType, [], None, BlockStmt([VarDecl(Id(nE), IntegerType, IntegerLit(0)), ForStmt(AssignStmt(Id(i), IntegerLit(0)), BinExpr(<, Id(i), Id(nE)), BinExpr(+, Id(i), IntegerLit(1)), BlockStmt([IfStmt(BinExpr(==, Id(nE), BinExpr(+, IntegerLit(10), IntegerLit(5))), BlockStmt([ReturnStmt(Id(nE))]))]))]))
])"""
        self.assertTrue(TestAST.test(input, expect, 317))

    def test_funcdecls_4(self):
        input = r"""
main : function void () {
    nE : integer = 0;
    for (i = 0, i < nE, i + 1) 
        if (nE == 10 + 5) 
            return nE;
}
"""
        expect = r"""Program([
	FuncDecl(Id(main), VoidType, [], None, BlockStmt([VarDecl(Id(nE), IntegerType, IntegerLit(0)), ForStmt(AssignStmt(Id(i), IntegerLit(0)), BinExpr(<, Id(i), Id(nE)), BinExpr(+, Id(i), IntegerLit(1)), IfStmt(BinExpr(==, Id(nE), BinExpr(+, IntegerLit(10), IntegerLit(5))), ReturnStmt(Id(nE))))]))
])"""
        self.assertTrue(TestAST.test(input, expect, 318))

    def test_funcdecls_5(self):
        input = r"""
main : function void () {
    nE : integer = 0;
    for (i = 0, i < nE, i + 1) 
        if (nE == 10 + 5) 
            return nE;
        else i = i + 1;
}
"""
        expect = r"""Program([
	FuncDecl(Id(main), VoidType, [], None, BlockStmt([VarDecl(Id(nE), IntegerType, IntegerLit(0)), ForStmt(AssignStmt(Id(i), IntegerLit(0)), BinExpr(<, Id(i), Id(nE)), BinExpr(+, Id(i), IntegerLit(1)), IfStmt(BinExpr(==, Id(nE), BinExpr(+, IntegerLit(10), IntegerLit(5))), ReturnStmt(Id(nE)), AssignStmt(Id(i), BinExpr(+, Id(i), IntegerLit(1)))))]))
])"""
        self.assertTrue(TestAST.test(input, expect, 319))

    def test_funcdecls_6(self):
        input = r"""
main : function void () {
    nE : float = 0;
    for (i = 0, i < nE, i + 1) 
        if (nE == (10 + 5)) 
            return nE;
        else {i = i + 1;}
}
"""
        expect = r"""Program([
	FuncDecl(Id(main), VoidType, [], None, BlockStmt([VarDecl(Id(nE), FloatType, IntegerLit(0)), ForStmt(AssignStmt(Id(i), IntegerLit(0)), BinExpr(<, Id(i), Id(nE)), BinExpr(+, Id(i), IntegerLit(1)), IfStmt(BinExpr(==, Id(nE), BinExpr(+, IntegerLit(10), IntegerLit(5))), ReturnStmt(Id(nE)), BlockStmt([AssignStmt(Id(i), BinExpr(+, Id(i), IntegerLit(1)))])))]))
])"""
        self.assertTrue(TestAST.test(input, expect, 320))

    def test_funcdecls_7(self):
        input = r"""
main : function void () {
    nE : integer = 0;
    do {
        if (nE == 10) 
            break;
        else {
            nE = nE + 1;
            continue;
        }
    } while(true);
}
"""
        expect = r"""Program([
	FuncDecl(Id(main), VoidType, [], None, BlockStmt([VarDecl(Id(nE), IntegerType, IntegerLit(0)), DoWhileStmt(BooleanLit(True), BlockStmt([IfStmt(BinExpr(==, Id(nE), IntegerLit(10)), BreakStmt(), BlockStmt([AssignStmt(Id(nE), BinExpr(+, Id(nE), IntegerLit(1))), ContinueStmt()]))]))]))
])"""
        self.assertTrue(TestAST.test(input, expect, 321))

    def test_funcdecls_8(self):
        input = r"""
x : integer = 65;
fact : function integer (n : integer) {
    if (n == 0) return 1;
    else return n*fact(n-1);
}
"""
        expect = r"""Program([
	VarDecl(Id(x), IntegerType, IntegerLit(65))
	FuncDecl(Id(fact), IntegerType, [Param(Id(n), IntegerType)], None, BlockStmt([IfStmt(BinExpr(==, Id(n), IntegerLit(0)), ReturnStmt(IntegerLit(1)), ReturnStmt(BinExpr(*, Id(n), FuncCall(Id(fact), [BinExpr(-, Id(n), IntegerLit(1))]))))]))
])"""
        self.assertTrue(TestAST.test(input, expect, 322))

    def test_funcdecls_9(self):
        input = r"""
x : integer = 65;
fact : function integer (n : integer) {
    if (n == 0) return 1;
    else return n*fact(n-1);
}
main : function void () {
    delta : integer = fact(3);
    printegerinteger(x);
}
"""
        expect = r"""Program([
	VarDecl(Id(x), IntegerType, IntegerLit(65))
	FuncDecl(Id(fact), IntegerType, [Param(Id(n), IntegerType)], None, BlockStmt([IfStmt(BinExpr(==, Id(n), IntegerLit(0)), ReturnStmt(IntegerLit(1)), ReturnStmt(BinExpr(*, Id(n), FuncCall(Id(fact), [BinExpr(-, Id(n), IntegerLit(1))]))))]))
	FuncDecl(Id(main), VoidType, [], None, BlockStmt([VarDecl(Id(delta), IntegerType, FuncCall(Id(fact), [IntegerLit(3)])), CallStmt(Id(printegerinteger), Id(x))]))
])"""
        self.assertTrue(TestAST.test(input, expect, 323))

    def test_funcdecls_10(self):
        input = r"""
x : integer = 65;
fact : function integer (n : integer) {
    if (n == 0) return 1;
    else return n*fact(n-1);
}
main : function void () {
    delta : integer = fact(3);
    inc (x, delta);
    printegerinteger(x);
}
inc : function void (out n: integer, delta : integer) {
    n = n + delta;
}
"""
        expect = r"""Program([
	VarDecl(Id(x), IntegerType, IntegerLit(65))
	FuncDecl(Id(fact), IntegerType, [Param(Id(n), IntegerType)], None, BlockStmt([IfStmt(BinExpr(==, Id(n), IntegerLit(0)), ReturnStmt(IntegerLit(1)), ReturnStmt(BinExpr(*, Id(n), FuncCall(Id(fact), [BinExpr(-, Id(n), IntegerLit(1))]))))]))
	FuncDecl(Id(main), VoidType, [], None, BlockStmt([VarDecl(Id(delta), IntegerType, FuncCall(Id(fact), [IntegerLit(3)])), CallStmt(Id(inc), Id(x), Id(delta)), CallStmt(Id(printegerinteger), Id(x))]))
	FuncDecl(Id(inc), VoidType, [OutParam(Id(n), IntegerType), Param(Id(delta), IntegerType)], None, BlockStmt([AssignStmt(Id(n), BinExpr(+, Id(n), Id(delta)))]))
])"""
        self.assertTrue(TestAST.test(input, expect, 324))

    def test_funcdecls_11(self):
        input = r"""
lengthOfFirstWord: function auto() {return "";}
lengthOfLastWord: function auto() inherit lengthOfFirstWord {
    return "lengthOfLastWord";
}
"""
        expect = r"""Program([
	FuncDecl(Id(lengthOfFirstWord), AutoType, [], None, BlockStmt([ReturnStmt(StringLit())]))
	FuncDecl(Id(lengthOfLastWord), AutoType, [], inherit, BlockStmt([ReturnStmt(StringLit(lengthOfLastWord))]))
])"""
        self.assertTrue(TestAST.test(input, expect, 325))

    def test_funcdecls_12(self):
        input = r"""
inc : function void (out n: integer, delta : integer) {
    nE : integer = 0;
    do {
        for (i = 0, i < nE, i + 1) 
            if (nE == 10 + 5) 
                return nE;
            else 
                nE = nE + 1;
            continue;
    } while(true);
}
"""
        expect = r"""Program([
	FuncDecl(Id(inc), VoidType, [OutParam(Id(n), IntegerType), Param(Id(delta), IntegerType)], None, BlockStmt([VarDecl(Id(nE), IntegerType, IntegerLit(0)), DoWhileStmt(BooleanLit(True), BlockStmt([ForStmt(AssignStmt(Id(i), IntegerLit(0)), BinExpr(<, Id(i), Id(nE)), BinExpr(+, Id(i), IntegerLit(1)), IfStmt(BinExpr(==, Id(nE), BinExpr(+, IntegerLit(10), IntegerLit(5))), ReturnStmt(Id(nE)), AssignStmt(Id(nE), BinExpr(+, Id(nE), IntegerLit(1))))), ContinueStmt()]))]))
])"""
        self.assertTrue(TestAST.test(input, expect, 326))

    def test_funcdecls_13(self):
        input = r"""
check_prime: function boolean (n : integer) {
  if (n < 2)
    return false;

  for (i = 2, i <= sqrt(n), i+1) {
    if (n % i == 0)
      return false;
  }
  return true;
}
"""
        expect = r"""Program([
	FuncDecl(Id(check_prime), BooleanType, [Param(Id(n), IntegerType)], None, BlockStmt([IfStmt(BinExpr(<, Id(n), IntegerLit(2)), ReturnStmt(BooleanLit(True))), ForStmt(AssignStmt(Id(i), IntegerLit(2)), BinExpr(<=, Id(i), FuncCall(Id(sqrt), [Id(n)])), BinExpr(+, Id(i), IntegerLit(1)), BlockStmt([IfStmt(BinExpr(==, BinExpr(%, Id(n), Id(i)), IntegerLit(0)), ReturnStmt(BooleanLit(True)))])), ReturnStmt(BooleanLit(True))]))
])"""
        self.assertTrue(TestAST.test(input, expect, 327))

    def test_funcdecls_14(self):
        input = r"""
x : integer = 65;
main : function void () {
    arr : array [2, 3] of integer;
    if(check_prime(7)){
        arr[1, 2] = 10;
        arr[arr[0, 1], 2] = 10;
    }
}
check_prime: function boolean (n : integer) {
  if (n < 2)
    return false;

  for (i = 2, i <= sqrt(n), i+1) {
    if (n % i == 0)
      return false;
  }
  return true;
}
"""
        expect = r"""Program([
	VarDecl(Id(x), IntegerType, IntegerLit(65))
	FuncDecl(Id(main), VoidType, [], None, BlockStmt([VarDecl(Id(arr), ArrayType([2, 3], IntegerType)), IfStmt(FuncCall(Id(check_prime), [IntegerLit(7)]), BlockStmt([AssignStmt(ArrayCell(Id(arr), [IntegerLit(1), IntegerLit(2)]), IntegerLit(10)), AssignStmt(ArrayCell(Id(arr), [ArrayCell(Id(arr), [IntegerLit(0), IntegerLit(1)]), IntegerLit(2)]), IntegerLit(10))]))]))
	FuncDecl(Id(check_prime), BooleanType, [Param(Id(n), IntegerType)], None, BlockStmt([IfStmt(BinExpr(<, Id(n), IntegerLit(2)), ReturnStmt(BooleanLit(True))), ForStmt(AssignStmt(Id(i), IntegerLit(2)), BinExpr(<=, Id(i), FuncCall(Id(sqrt), [Id(n)])), BinExpr(+, Id(i), IntegerLit(1)), BlockStmt([IfStmt(BinExpr(==, BinExpr(%, Id(n), Id(i)), IntegerLit(0)), ReturnStmt(BooleanLit(True)))])), ReturnStmt(BooleanLit(True))]))
])"""
        self.assertTrue(TestAST.test(input, expect, 328))

    def test_funcdecls_15(self):
        input = r"""
Fibonacci: function integer(n: integer) {
    f0,   f1,   fn: auto = 0, 1, 1;
    if (n < 0) {
        return -1;
    }
    if ((n == 0) || (n == 1)) {
        return n;
    } else {
        for (i = 2, i < n, i + 1) {
          f0 = f1;
          f1 = fn;
          fn = f0 + f1;
        }
    }
    return fn;
}
"""
        expect = r"""Program([
	FuncDecl(Id(Fibonacci), IntegerType, [Param(Id(n), IntegerType)], None, BlockStmt([VarDecl(Id(f0), AutoType, IntegerLit(0)), VarDecl(Id(f1), AutoType, IntegerLit(1)), VarDecl(Id(fn), AutoType, IntegerLit(1)), IfStmt(BinExpr(<, Id(n), IntegerLit(0)), BlockStmt([ReturnStmt(UnExpr(-, IntegerLit(1)))])), IfStmt(BinExpr(||, BinExpr(==, Id(n), IntegerLit(0)), BinExpr(==, Id(n), IntegerLit(1))), BlockStmt([ReturnStmt(Id(n))]), BlockStmt([ForStmt(AssignStmt(Id(i), IntegerLit(2)), BinExpr(<, Id(i), Id(n)), BinExpr(+, Id(i), IntegerLit(1)), BlockStmt([AssignStmt(Id(f0), Id(f1)), AssignStmt(Id(f1), Id(fn)), AssignStmt(Id(fn), BinExpr(+, Id(f0), Id(f1)))]))])), ReturnStmt(Id(fn))]))
])"""
        self.assertTrue(TestAST.test(input, expect, 329))

    def test_funcdecls_16(self):
        input = r"""
x : integer = 65;
main : function void () {
    arr : array [2, 3] of integer;
    if(check_prime(7)){
        arr[1, 2] = Fibonacci(10);
    }

}
Fibonacci: function integer(n: integer) {
    f0,   f1,   fn: auto = 0, 1, 1;
    if (n < 0) {
        return -1;
    }
    if ((n == 0) || (n == 1)) {
        return n;
    } else {
        for (i = 2, i < n, i + 1) {
          f0 = f1;
          f1 = fn;
          fn = f0 + f1;
        }
    }
    return fn;
}
check_prime: function boolean (n : integer) {
  if (n < 2)
    return false;

  for (i = 2, i <= sqrt(n), i+1) {
    if (n % i == 0)
      return false;
  }
  return true;
}
"""
        expect = r"""Program([
	VarDecl(Id(x), IntegerType, IntegerLit(65))
	FuncDecl(Id(main), VoidType, [], None, BlockStmt([VarDecl(Id(arr), ArrayType([2, 3], IntegerType)), IfStmt(FuncCall(Id(check_prime), [IntegerLit(7)]), BlockStmt([AssignStmt(ArrayCell(Id(arr), [IntegerLit(1), IntegerLit(2)]), FuncCall(Id(Fibonacci), [IntegerLit(10)]))]))]))
	FuncDecl(Id(Fibonacci), IntegerType, [Param(Id(n), IntegerType)], None, BlockStmt([VarDecl(Id(f0), AutoType, IntegerLit(0)), VarDecl(Id(f1), AutoType, IntegerLit(1)), VarDecl(Id(fn), AutoType, IntegerLit(1)), IfStmt(BinExpr(<, Id(n), IntegerLit(0)), BlockStmt([ReturnStmt(UnExpr(-, IntegerLit(1)))])), IfStmt(BinExpr(||, BinExpr(==, Id(n), IntegerLit(0)), BinExpr(==, Id(n), IntegerLit(1))), BlockStmt([ReturnStmt(Id(n))]), BlockStmt([ForStmt(AssignStmt(Id(i), IntegerLit(2)), BinExpr(<, Id(i), Id(n)), BinExpr(+, Id(i), IntegerLit(1)), BlockStmt([AssignStmt(Id(f0), Id(f1)), AssignStmt(Id(f1), Id(fn)), AssignStmt(Id(fn), BinExpr(+, Id(f0), Id(f1)))]))])), ReturnStmt(Id(fn))]))
	FuncDecl(Id(check_prime), BooleanType, [Param(Id(n), IntegerType)], None, BlockStmt([IfStmt(BinExpr(<, Id(n), IntegerLit(2)), ReturnStmt(BooleanLit(True))), ForStmt(AssignStmt(Id(i), IntegerLit(2)), BinExpr(<=, Id(i), FuncCall(Id(sqrt), [Id(n)])), BinExpr(+, Id(i), IntegerLit(1)), BlockStmt([IfStmt(BinExpr(==, BinExpr(%, Id(n), Id(i)), IntegerLit(0)), ReturnStmt(BooleanLit(True)))])), ReturnStmt(BooleanLit(True))]))
])"""
        self.assertTrue(TestAST.test(input, expect, 330))

    def test_funcdecls_17(self):
        input = r"""
check_str_code: function boolean (code : string, size: integer) {
    if (code == "")
        return false;
    for (i = 0, i < size, i+ 1) {
        if (!(((code[i] >= "a") && (code[i] <= "z")) ||
              ((code[i] >= "A") && (code[i] <= "Z")))) {
            return false;
        }
    }
    return true;
}
"""
        expect = r"""Program([
	FuncDecl(Id(check_str_code), BooleanType, [Param(Id(code), StringType), Param(Id(size), IntegerType)], None, BlockStmt([IfStmt(BinExpr(==, Id(code), StringLit()), ReturnStmt(BooleanLit(True))), ForStmt(AssignStmt(Id(i), IntegerLit(0)), BinExpr(<, Id(i), Id(size)), BinExpr(+, Id(i), IntegerLit(1)), BlockStmt([IfStmt(UnExpr(!, BinExpr(||, BinExpr(&&, BinExpr(>=, ArrayCell(Id(code), [Id(i)]), StringLit(a)), BinExpr(<=, ArrayCell(Id(code), [Id(i)]), StringLit(z))), BinExpr(&&, BinExpr(>=, ArrayCell(Id(code), [Id(i)]), StringLit(A)), BinExpr(<=, ArrayCell(Id(code), [Id(i)]), StringLit(Z))))), BlockStmt([ReturnStmt(BooleanLit(True))]))])), ReturnStmt(BooleanLit(True))]))
])"""
        self.assertTrue(TestAST.test(input, expect, 331))

    def test_funcdecls_18(self):
        input = r"""
check_str_code: function boolean (code : string, size: integer) {
    if (code == "")
        return false;
    for (i = 0, i < size, i + 6 - 3) {
        if (!i) {
            break;
        }
    }
    return true;
}
"""
        expect = r"""Program([
	FuncDecl(Id(check_str_code), BooleanType, [Param(Id(code), StringType), Param(Id(size), IntegerType)], None, BlockStmt([IfStmt(BinExpr(==, Id(code), StringLit()), ReturnStmt(BooleanLit(True))), ForStmt(AssignStmt(Id(i), IntegerLit(0)), BinExpr(<, Id(i), Id(size)), BinExpr(-, BinExpr(+, Id(i), IntegerLit(6)), IntegerLit(3)), BlockStmt([IfStmt(UnExpr(!, Id(i)), BlockStmt([BreakStmt()]))])), ReturnStmt(BooleanLit(True))]))
])"""
        self.assertTrue(TestAST.test(input, expect, 332))

    def test_funcdecls_19(self):
        input = r"""
reverse_string: function string(str: string, size: integer) {
    for (i = 0, i < size / 2, i+1) {
        x : string = str[i];
        str[i] = str[size - i - 1];
        str[size - i - 1] = x;
    }
    return str;
}
"""
        expect = r"""Program([
	FuncDecl(Id(reverse_string), StringType, [Param(Id(str), StringType), Param(Id(size), IntegerType)], None, BlockStmt([ForStmt(AssignStmt(Id(i), IntegerLit(0)), BinExpr(<, Id(i), BinExpr(/, Id(size), IntegerLit(2))), BinExpr(+, Id(i), IntegerLit(1)), BlockStmt([VarDecl(Id(x), StringType, ArrayCell(Id(str), [Id(i)])), AssignStmt(ArrayCell(Id(str), [Id(i)]), ArrayCell(Id(str), [BinExpr(-, BinExpr(-, Id(size), Id(i)), IntegerLit(1))])), AssignStmt(ArrayCell(Id(str), [BinExpr(-, BinExpr(-, Id(size), Id(i)), IntegerLit(1))]), Id(x))])), ReturnStmt(Id(str))]))
])"""
        self.assertTrue(TestAST.test(input, expect, 333))

    def test_funcdecls_20(self):
        input = r"""
reverse_string: function string(str: string, size: integer) {
    for (i = 0, i < size / 2, i+1) {
        x : string = str[i];
        str[i] = str[size - i - 1];
        str[size - i - 1] = x;
    }
    return str;
}
main : function void () {
    reverse_string("Hello World!", 12);
}
"""
        expect = r"""Program([
	FuncDecl(Id(reverse_string), StringType, [Param(Id(str), StringType), Param(Id(size), IntegerType)], None, BlockStmt([ForStmt(AssignStmt(Id(i), IntegerLit(0)), BinExpr(<, Id(i), BinExpr(/, Id(size), IntegerLit(2))), BinExpr(+, Id(i), IntegerLit(1)), BlockStmt([VarDecl(Id(x), StringType, ArrayCell(Id(str), [Id(i)])), AssignStmt(ArrayCell(Id(str), [Id(i)]), ArrayCell(Id(str), [BinExpr(-, BinExpr(-, Id(size), Id(i)), IntegerLit(1))])), AssignStmt(ArrayCell(Id(str), [BinExpr(-, BinExpr(-, Id(size), Id(i)), IntegerLit(1))]), Id(x))])), ReturnStmt(Id(str))]))
	FuncDecl(Id(main), VoidType, [], None, BlockStmt([CallStmt(Id(reverse_string), StringLit(Hello World!), IntegerLit(12))]))
])"""
        self.assertTrue(TestAST.test(input, expect, 334))

    def test_funcdecls_21(self):
        input = r"""
Recursive: function void (nums: array[100] of integer, size: integer, index: integer , count: integer, sum: integer , minjump: integer) {
    if (sum >= size) {
        if (minjump > count)
            minjump = count;
    } else {
        for (i = 1, i <= nums[index], i + 1) {
          Recursive(nums, index + i, count + 1, sum + i, minjump);
        }
    }
}
"""
        expect = r"""Program([
	FuncDecl(Id(Recursive), VoidType, [Param(Id(nums), ArrayType([100], IntegerType)), Param(Id(size), IntegerType), Param(Id(index), IntegerType), Param(Id(count), IntegerType), Param(Id(sum), IntegerType), Param(Id(minjump), IntegerType)], None, BlockStmt([IfStmt(BinExpr(>=, Id(sum), Id(size)), BlockStmt([IfStmt(BinExpr(>, Id(minjump), Id(count)), AssignStmt(Id(minjump), Id(count)))]), BlockStmt([ForStmt(AssignStmt(Id(i), IntegerLit(1)), BinExpr(<=, Id(i), ArrayCell(Id(nums), [Id(index)])), BinExpr(+, Id(i), IntegerLit(1)), BlockStmt([CallStmt(Id(Recursive), Id(nums), BinExpr(+, Id(index), Id(i)), BinExpr(+, Id(count), IntegerLit(1)), BinExpr(+, Id(sum), Id(i)), Id(minjump))]))]))]))
])"""
        self.assertTrue(TestAST.test(input, expect, 335))

    def test_funcdecls_22(self):
        input = r"""
Recursive: function void (nums: array[100] of integer, size: integer, index: integer , count: integer, sum: integer , minjump: integer) {
    if (sum >= size) {
        if (minjump > count)
            minjump = count;
    } else {
        for (i = 1, i <= nums[index], i + 1) {
          Recursive(nums, index + i, count + 1, sum + i, minjump);
        }
    }
}
main : function void () {
    nums: array[100] of integer;
    Recursive(nums, 1 + 2, 1 / 2, 1 % 31, 1, -1);
}
"""
        expect = r"""Program([
	FuncDecl(Id(Recursive), VoidType, [Param(Id(nums), ArrayType([100], IntegerType)), Param(Id(size), IntegerType), Param(Id(index), IntegerType), Param(Id(count), IntegerType), Param(Id(sum), IntegerType), Param(Id(minjump), IntegerType)], None, BlockStmt([IfStmt(BinExpr(>=, Id(sum), Id(size)), BlockStmt([IfStmt(BinExpr(>, Id(minjump), Id(count)), AssignStmt(Id(minjump), Id(count)))]), BlockStmt([ForStmt(AssignStmt(Id(i), IntegerLit(1)), BinExpr(<=, Id(i), ArrayCell(Id(nums), [Id(index)])), BinExpr(+, Id(i), IntegerLit(1)), BlockStmt([CallStmt(Id(Recursive), Id(nums), BinExpr(+, Id(index), Id(i)), BinExpr(+, Id(count), IntegerLit(1)), BinExpr(+, Id(sum), Id(i)), Id(minjump))]))]))]))
	FuncDecl(Id(main), VoidType, [], None, BlockStmt([VarDecl(Id(nums), ArrayType([100], IntegerType)), CallStmt(Id(Recursive), Id(nums), BinExpr(+, IntegerLit(1), IntegerLit(2)), BinExpr(/, IntegerLit(1), IntegerLit(2)), BinExpr(%, IntegerLit(1), IntegerLit(31)), IntegerLit(1), UnExpr(-, IntegerLit(1)))]))
])"""
        self.assertTrue(TestAST.test(input, expect, 336))

    def test_funcdecls_23(self):
        input = r"""
Test: function void (i: integer){return i / 2;}
Recursive: function void (inherit nums: array[100] of integer, size: integer, index: integer , count: integer, sum: integer , minjump: integer) inherit Test {
    if (sum >= size) {
        if (minjump > count)
            minjump = count;
    } else {
        for (i = 1, i <= nums[index], i + 1) {
          Recursive(nums, index + i, count + 1, sum + i, minjump);
        }
    }
}
main : function void () {
    nums: array[100] of integer;
    Recursive(nums, 1 + 2, 1 / 2, 1 % 31, 1, -1);
}
"""
        expect = r"""Program([
	FuncDecl(Id(Test), VoidType, [Param(Id(i), IntegerType)], None, BlockStmt([ReturnStmt(BinExpr(/, Id(i), IntegerLit(2)))]))
	FuncDecl(Id(Recursive), VoidType, [InheritParam(Id(nums), ArrayType([100], IntegerType)), Param(Id(size), IntegerType), Param(Id(index), IntegerType), Param(Id(count), IntegerType), Param(Id(sum), IntegerType), Param(Id(minjump), IntegerType)], inherit, BlockStmt([IfStmt(BinExpr(>=, Id(sum), Id(size)), BlockStmt([IfStmt(BinExpr(>, Id(minjump), Id(count)), AssignStmt(Id(minjump), Id(count)))]), BlockStmt([ForStmt(AssignStmt(Id(i), IntegerLit(1)), BinExpr(<=, Id(i), ArrayCell(Id(nums), [Id(index)])), BinExpr(+, Id(i), IntegerLit(1)), BlockStmt([CallStmt(Id(Recursive), Id(nums), BinExpr(+, Id(index), Id(i)), BinExpr(+, Id(count), IntegerLit(1)), BinExpr(+, Id(sum), Id(i)), Id(minjump))]))]))]))
	FuncDecl(Id(main), VoidType, [], None, BlockStmt([VarDecl(Id(nums), ArrayType([100], IntegerType)), CallStmt(Id(Recursive), Id(nums), BinExpr(+, IntegerLit(1), IntegerLit(2)), BinExpr(/, IntegerLit(1), IntegerLit(2)), BinExpr(%, IntegerLit(1), IntegerLit(31)), IntegerLit(1), UnExpr(-, IntegerLit(1)))]))
])"""
        self.assertTrue(TestAST.test(input, expect, 337))

    def test_funcdecls_24(self):
        input = r"""
lookUp: function boolean (name: string) { 
    // Undeclared
    for (scopeFounded = 10, scopeFounded >= 0, scopeFounded-1) {
        if (isExist(name, scopeFounded)) {
            return true; 
        }
    }
    return false;
} 
"""
        expect = r"""Program([
	FuncDecl(Id(lookUp), BooleanType, [Param(Id(name), StringType)], None, BlockStmt([ForStmt(AssignStmt(Id(scopeFounded), IntegerLit(10)), BinExpr(>=, Id(scopeFounded), IntegerLit(0)), BinExpr(-, Id(scopeFounded), IntegerLit(1)), BlockStmt([IfStmt(FuncCall(Id(isExist), [Id(name), Id(scopeFounded)]), BlockStmt([ReturnStmt(BooleanLit(True))]))])), ReturnStmt(BooleanLit(True))]))
])"""
        self.assertTrue(TestAST.test(input, expect, 338))

    def test_funcdecls_25(self):
        input = r"""
lookUp: function boolean (name: string) { 
    for (scopeFounded = 10, scopeFounded >= 0, scopeFounded-1) {
        if (isExist(name, scopeFounded)) {
            return true; 
        }
    }
    return false;
} 
main : function void () {
    lookUp("test", 1);
}
"""
        expect = r"""Program([
	FuncDecl(Id(lookUp), BooleanType, [Param(Id(name), StringType)], None, BlockStmt([ForStmt(AssignStmt(Id(scopeFounded), IntegerLit(10)), BinExpr(>=, Id(scopeFounded), IntegerLit(0)), BinExpr(-, Id(scopeFounded), IntegerLit(1)), BlockStmt([IfStmt(FuncCall(Id(isExist), [Id(name), Id(scopeFounded)]), BlockStmt([ReturnStmt(BooleanLit(True))]))])), ReturnStmt(BooleanLit(True))]))
	FuncDecl(Id(main), VoidType, [], None, BlockStmt([CallStmt(Id(lookUp), StringLit(test), IntegerLit(1))]))
])"""
        self.assertTrue(TestAST.test(input, expect, 339))

    def test_funcdecls_26(self):
        input = r"""
longestSublist: function integer (words: array[100] of string, size: integer) {
    if(!size) return 0;
    result : integer = 1;
    for (i = 0, i < size - 1, i + 1) {
        if (!(words[i][0] == words[i + 1][0])) {
          pre_result, j: integer  = 2 , i + 1;
          while (true) {
            if (words[j][0] != words[j + 1][0]) {
              pre_result = pre_result + 1;
              j = j + 1;
            } else {
              continue;
            }
          }
          if(pre_result > result) result = result / pre_result;
        }
    }
    return result;
}
"""
        expect = r"""Program([
	FuncDecl(Id(longestSublist), IntegerType, [Param(Id(words), ArrayType([100], StringType)), Param(Id(size), IntegerType)], None, BlockStmt([IfStmt(UnExpr(!, Id(size)), ReturnStmt(IntegerLit(0))), VarDecl(Id(result), IntegerType, IntegerLit(1)), ForStmt(AssignStmt(Id(i), IntegerLit(0)), BinExpr(<, Id(i), BinExpr(-, Id(size), IntegerLit(1))), BinExpr(+, Id(i), IntegerLit(1)), BlockStmt([IfStmt(UnExpr(!, BinExpr(==, ArrayCell(ArrayCell(Id(words), [Id(i)]), [IntegerLit(0)]), ArrayCell(ArrayCell(Id(words), [BinExpr(+, Id(i), IntegerLit(1))]), [IntegerLit(0)]))), BlockStmt([VarDecl(Id(pre_result), IntegerType, IntegerLit(2)), VarDecl(Id(j), IntegerType, BinExpr(+, Id(i), IntegerLit(1))), WhileStmt(BooleanLit(True), BlockStmt([IfStmt(BinExpr(!=, ArrayCell(ArrayCell(Id(words), [Id(j)]), [IntegerLit(0)]), ArrayCell(ArrayCell(Id(words), [BinExpr(+, Id(j), IntegerLit(1))]), [IntegerLit(0)])), BlockStmt([AssignStmt(Id(pre_result), BinExpr(+, Id(pre_result), IntegerLit(1))), AssignStmt(Id(j), BinExpr(+, Id(j), IntegerLit(1)))]), BlockStmt([ContinueStmt()]))])), IfStmt(BinExpr(>, Id(pre_result), Id(result)), AssignStmt(Id(result), BinExpr(/, Id(result), Id(pre_result))))]))])), ReturnStmt(Id(result))]))
])"""
        self.assertTrue(TestAST.test(input, expect, 340))

    def test_funcdecls_27(self):
        input = r"""
equalSumIndex: function integer (words: array[100] of string, size: integer) {
    if(!size) return 0;
    result : integer = 1;
    if(size == 1) return 0;
    sumRight, sumLeft, j: integer = 0, 0, 1;

    for (i = 1, i < size, i * 2) {
        sumRight = sumRight + nums[i];
    }

    for (i = 0, j < size, i + 1) {
        sumRight = sumRight - nums[j];
        sumLeft = sumLeft + nums[i];
        if (sumLeft == sumRight) return i+1;
        j = j + 1;
    }
    return -1;
}
"""
        expect = r"""Program([
	FuncDecl(Id(equalSumIndex), IntegerType, [Param(Id(words), ArrayType([100], StringType)), Param(Id(size), IntegerType)], None, BlockStmt([IfStmt(UnExpr(!, Id(size)), ReturnStmt(IntegerLit(0))), VarDecl(Id(result), IntegerType, IntegerLit(1)), IfStmt(BinExpr(==, Id(size), IntegerLit(1)), ReturnStmt(IntegerLit(0))), VarDecl(Id(sumRight), IntegerType, IntegerLit(0)), VarDecl(Id(sumLeft), IntegerType, IntegerLit(0)), VarDecl(Id(j), IntegerType, IntegerLit(1)), ForStmt(AssignStmt(Id(i), IntegerLit(1)), BinExpr(<, Id(i), Id(size)), BinExpr(*, Id(i), IntegerLit(2)), BlockStmt([AssignStmt(Id(sumRight), BinExpr(+, Id(sumRight), ArrayCell(Id(nums), [Id(i)])))])), ForStmt(AssignStmt(Id(i), IntegerLit(0)), BinExpr(<, Id(j), Id(size)), BinExpr(+, Id(i), IntegerLit(1)), BlockStmt([AssignStmt(Id(sumRight), BinExpr(-, Id(sumRight), ArrayCell(Id(nums), [Id(j)]))), AssignStmt(Id(sumLeft), BinExpr(+, Id(sumLeft), ArrayCell(Id(nums), [Id(i)]))), IfStmt(BinExpr(==, Id(sumLeft), Id(sumRight)), ReturnStmt(BinExpr(+, Id(i), IntegerLit(1)))), AssignStmt(Id(j), BinExpr(+, Id(j), IntegerLit(1)))])), ReturnStmt(UnExpr(-, IntegerLit(1)))]))
])"""
        self.assertTrue(TestAST.test(input, expect, 341))

    def test_funcdecls_28(self):
        input = r"""
findGCD: function integer (a: integer, b: integer)
{
    if(b){
        return findGCD(b, a % b);
    }
    return a;
}
"""
        expect = r"""Program([
	FuncDecl(Id(findGCD), IntegerType, [Param(Id(a), IntegerType), Param(Id(b), IntegerType)], None, BlockStmt([IfStmt(Id(b), BlockStmt([ReturnStmt(FuncCall(Id(findGCD), [Id(b), BinExpr(%, Id(a), Id(b))]))])), ReturnStmt(Id(a))]))
])"""
        self.assertTrue(TestAST.test(input, expect, 342))

    def test_funcdecls_29(self):
        input = r"""
n: integer = 10;
reverseFactorial: function integer (out n: integer, i: integer) {
    if(n == 1){
        return i - 1;
    }
    if(n % i){
        return -1;
    }
    return reverseFactorial(n / i, i + 1);
}
"""
        expect = r"""Program([
	VarDecl(Id(n), IntegerType, IntegerLit(10))
	FuncDecl(Id(reverseFactorial), IntegerType, [OutParam(Id(n), IntegerType), Param(Id(i), IntegerType)], None, BlockStmt([IfStmt(BinExpr(==, Id(n), IntegerLit(1)), BlockStmt([ReturnStmt(BinExpr(-, Id(i), IntegerLit(1)))])), IfStmt(BinExpr(%, Id(n), Id(i)), BlockStmt([ReturnStmt(UnExpr(-, IntegerLit(1)))])), ReturnStmt(FuncCall(Id(reverseFactorial), [BinExpr(/, Id(n), Id(i)), BinExpr(+, Id(i), IntegerLit(1))]))]))
])"""
        self.assertTrue(TestAST.test(input, expect, 343))

    def test_funcdecls_30(self):
        input = r"""
n: integer = 10;
reverseFactorial: function integer (out n: integer, i: integer) {
    if(n == 1){
        return i - 1;
    }
    if(n % i){
        return -1;
    }
    return reverseFactorial(n / i, i + 1);
}
main : function void () {
    reverseFactorial(n, 2);
}
"""
        expect = r"""Program([
	VarDecl(Id(n), IntegerType, IntegerLit(10))
	FuncDecl(Id(reverseFactorial), IntegerType, [OutParam(Id(n), IntegerType), Param(Id(i), IntegerType)], None, BlockStmt([IfStmt(BinExpr(==, Id(n), IntegerLit(1)), BlockStmt([ReturnStmt(BinExpr(-, Id(i), IntegerLit(1)))])), IfStmt(BinExpr(%, Id(n), Id(i)), BlockStmt([ReturnStmt(UnExpr(-, IntegerLit(1)))])), ReturnStmt(FuncCall(Id(reverseFactorial), [BinExpr(/, Id(n), Id(i)), BinExpr(+, Id(i), IntegerLit(1))]))]))
	FuncDecl(Id(main), VoidType, [], None, BlockStmt([CallStmt(Id(reverseFactorial), Id(n), IntegerLit(2))]))
])"""
        self.assertTrue(TestAST.test(input, expect, 344))

    def test_funcdecls_31(self):
        input = r"""
findGCD: function integer (a: integer, b: integer) {
    if(b){
        return findGCD(b, a % b);
    }
    return a;
}

findLCM: function integer (a: integer, b: integer){
    return (a*b)/findGCD(a, b);
}

main : function void () {
    findLCM(144, 12);
}
"""
        expect = r"""Program([
	FuncDecl(Id(findGCD), IntegerType, [Param(Id(a), IntegerType), Param(Id(b), IntegerType)], None, BlockStmt([IfStmt(Id(b), BlockStmt([ReturnStmt(FuncCall(Id(findGCD), [Id(b), BinExpr(%, Id(a), Id(b))]))])), ReturnStmt(Id(a))]))
	FuncDecl(Id(findLCM), IntegerType, [Param(Id(a), IntegerType), Param(Id(b), IntegerType)], None, BlockStmt([ReturnStmt(BinExpr(/, BinExpr(*, Id(a), Id(b)), FuncCall(Id(findGCD), [Id(a), Id(b)])))]))
	FuncDecl(Id(main), VoidType, [], None, BlockStmt([CallStmt(Id(findLCM), IntegerLit(144), IntegerLit(12))]))
])"""
        self.assertTrue(TestAST.test(input, expect, 345))

    def test_funcdecls_32(self):
        input = r"""
printegerPattern: function void (n: integer) {
  if (n <= 0)
    isZero = 1;
  if (isZero) {
    no_count = no_count - 1;
    if (no_count == -1)
      return;
    else {
      printeger(" ");
    }
    printegerPattern(n + 5);
  } else {
    printeger(" ");
    no_count = no_count + 1;
    printegerPattern(n - 5);
  }
}
"""
        expect = r"""Program([
	FuncDecl(Id(printegerPattern), VoidType, [Param(Id(n), IntegerType)], None, BlockStmt([IfStmt(BinExpr(<=, Id(n), IntegerLit(0)), AssignStmt(Id(isZero), IntegerLit(1))), IfStmt(Id(isZero), BlockStmt([AssignStmt(Id(no_count), BinExpr(-, Id(no_count), IntegerLit(1))), IfStmt(BinExpr(==, Id(no_count), UnExpr(-, IntegerLit(1))), ReturnStmt(), BlockStmt([CallStmt(Id(printeger), StringLit( ))])), CallStmt(Id(printegerPattern), BinExpr(+, Id(n), IntegerLit(5)))]), BlockStmt([CallStmt(Id(printeger), StringLit( )), AssignStmt(Id(no_count), BinExpr(+, Id(no_count), IntegerLit(1))), CallStmt(Id(printegerPattern), BinExpr(-, Id(n), IntegerLit(5)))]))]))
])"""
        self.assertTrue(TestAST.test(input, expect, 346))

    def test_funcdecls_33(self):
        input = r"""
isZero, no_count : boolean = 0, 0;
printegerPattern: function void (n: integer, out isZero: boolean, out no_count: boolean) {
  if (n <= 0)
    isZero = 1;
  if (isZero) {
    no_count = no_count - 1;
    if (no_count == -1)
      return;
    else {
      printeger(" ");
    }
    printegerPattern(n + 5);
  } else {
    printeger(" ");
    no_count = no_count + 1;
    printegerPattern(n - 5);
  }
}

main : function void () {
    printegerPattern(10, isZero, no_count);
}
"""
        expect = r"""Program([
	VarDecl(Id(isZero), BooleanType, IntegerLit(0))
	VarDecl(Id(no_count), BooleanType, IntegerLit(0))
	FuncDecl(Id(printegerPattern), VoidType, [Param(Id(n), IntegerType), OutParam(Id(isZero), BooleanType), OutParam(Id(no_count), BooleanType)], None, BlockStmt([IfStmt(BinExpr(<=, Id(n), IntegerLit(0)), AssignStmt(Id(isZero), IntegerLit(1))), IfStmt(Id(isZero), BlockStmt([AssignStmt(Id(no_count), BinExpr(-, Id(no_count), IntegerLit(1))), IfStmt(BinExpr(==, Id(no_count), UnExpr(-, IntegerLit(1))), ReturnStmt(), BlockStmt([CallStmt(Id(printeger), StringLit( ))])), CallStmt(Id(printegerPattern), BinExpr(+, Id(n), IntegerLit(5)))]), BlockStmt([CallStmt(Id(printeger), StringLit( )), AssignStmt(Id(no_count), BinExpr(+, Id(no_count), IntegerLit(1))), CallStmt(Id(printegerPattern), BinExpr(-, Id(n), IntegerLit(5)))]))]))
	FuncDecl(Id(main), VoidType, [], None, BlockStmt([CallStmt(Id(printegerPattern), IntegerLit(10), Id(isZero), Id(no_count))]))
])"""
        self.assertTrue(TestAST.test(input, expect, 347))

    def test_funcdecls_34(self):
        input = r"""
countWaysUtil: function integer (x: integer, n: integer, num: integer)
{
    // Base cases
    val: integer = (x - pow(num, n));
    if (val == 0)
        return 1;
    if (val < 0)
        return 0;

    return countWaysUtil(val, n, num + 1) +
           countWaysUtil(x, n, num + 1);
}

countWaySumOfSquare: function integer (x: integer)
{
    return countWaysUtil(x, 2, 1);
}
"""
        expect = r"""Program([
	FuncDecl(Id(countWaysUtil), IntegerType, [Param(Id(x), IntegerType), Param(Id(n), IntegerType), Param(Id(num), IntegerType)], None, BlockStmt([VarDecl(Id(val), IntegerType, BinExpr(-, Id(x), FuncCall(Id(pow), [Id(num), Id(n)]))), IfStmt(BinExpr(==, Id(val), IntegerLit(0)), ReturnStmt(IntegerLit(1))), IfStmt(BinExpr(<, Id(val), IntegerLit(0)), ReturnStmt(IntegerLit(0))), ReturnStmt(BinExpr(+, FuncCall(Id(countWaysUtil), [Id(val), Id(n), BinExpr(+, Id(num), IntegerLit(1))]), FuncCall(Id(countWaysUtil), [Id(x), Id(n), BinExpr(+, Id(num), IntegerLit(1))])))]))
	FuncDecl(Id(countWaySumOfSquare), IntegerType, [Param(Id(x), IntegerType)], None, BlockStmt([ReturnStmt(FuncCall(Id(countWaysUtil), [Id(x), IntegerLit(2), IntegerLit(1)]))]))
])"""
        self.assertTrue(TestAST.test(input, expect, 348))

    def test_funcdecls_35(self):
        input = r"""
countWaysUtil: function integer (x: integer, n: integer, num: integer)
{
    // Base cases
    val: integer = (x - pow(num, n));
    if (val == 0)
        return 1;
    if (val < 0)
        return 0;

    return countWaysUtil(val, n, num + 1) +
           countWaysUtil(x, n, num + 1);
}

countWaySumOfSquare: function integer (x: integer)
{
    return countWaysUtil(x, 2, 1);
}

main: function void(){
    printeger(countWaySumOfSquare(100));
}
"""
        expect = r"""Program([
	FuncDecl(Id(countWaysUtil), IntegerType, [Param(Id(x), IntegerType), Param(Id(n), IntegerType), Param(Id(num), IntegerType)], None, BlockStmt([VarDecl(Id(val), IntegerType, BinExpr(-, Id(x), FuncCall(Id(pow), [Id(num), Id(n)]))), IfStmt(BinExpr(==, Id(val), IntegerLit(0)), ReturnStmt(IntegerLit(1))), IfStmt(BinExpr(<, Id(val), IntegerLit(0)), ReturnStmt(IntegerLit(0))), ReturnStmt(BinExpr(+, FuncCall(Id(countWaysUtil), [Id(val), Id(n), BinExpr(+, Id(num), IntegerLit(1))]), FuncCall(Id(countWaysUtil), [Id(x), Id(n), BinExpr(+, Id(num), IntegerLit(1))])))]))
	FuncDecl(Id(countWaySumOfSquare), IntegerType, [Param(Id(x), IntegerType)], None, BlockStmt([ReturnStmt(FuncCall(Id(countWaysUtil), [Id(x), IntegerLit(2), IntegerLit(1)]))]))
	FuncDecl(Id(main), VoidType, [], None, BlockStmt([CallStmt(Id(printeger), FuncCall(Id(countWaySumOfSquare), [IntegerLit(100)]))]))
])"""
        self.assertTrue(TestAST.test(input, expect, 349))

    def test_funcdecls_36(self):
        input = r"""
buyCar: function integer (nums : array [200] of integer, length: integer, k: integer) {
  sort(nums, nums + length);
  result, i: integer = 0, 0;
  while ((k > 0) && (k - nums[i] >= 0)) {
    result = result + 1;
    k = k - nums[i];
    i = i + 1;
  }
  return result;
}
"""
        expect = r"""Program([
	FuncDecl(Id(buyCar), IntegerType, [Param(Id(nums), ArrayType([200], IntegerType)), Param(Id(length), IntegerType), Param(Id(k), IntegerType)], None, BlockStmt([CallStmt(Id(sort), Id(nums), BinExpr(+, Id(nums), Id(length))), VarDecl(Id(result), IntegerType, IntegerLit(0)), VarDecl(Id(i), IntegerType, IntegerLit(0)), WhileStmt(BinExpr(&&, BinExpr(>, Id(k), IntegerLit(0)), BinExpr(>=, BinExpr(-, Id(k), ArrayCell(Id(nums), [Id(i)])), IntegerLit(0))), BlockStmt([AssignStmt(Id(result), BinExpr(+, Id(result), IntegerLit(1))), AssignStmt(Id(k), BinExpr(-, Id(k), ArrayCell(Id(nums), [Id(i)]))), AssignStmt(Id(i), BinExpr(+, Id(i), IntegerLit(1)))])), ReturnStmt(Id(result))]))
])"""
        self.assertTrue(TestAST.test(input, expect, 350))

    def test_funcdecls_37(self):
        input = r"""
buyCar: function integer (nums : array [200] of integer, length: integer, k: integer) {
  sort(nums, nums + length);
  result, i: integer = 0, 0;
  while ((k > 0) && (k - nums[i] >= 0)) {
    result = result + 1;
    k = k - nums[i];
    i = i + 1;
  }
  return result;
}
main: function void(){
    nums: array [5] of integer = {90,30,40,90,20};
    length : integer = sizeof(nums)/sizeof(nums[0]);
    printeger(buyCar(nums, length, 90));
}
"""
        expect = r"""Program([
	FuncDecl(Id(buyCar), IntegerType, [Param(Id(nums), ArrayType([200], IntegerType)), Param(Id(length), IntegerType), Param(Id(k), IntegerType)], None, BlockStmt([CallStmt(Id(sort), Id(nums), BinExpr(+, Id(nums), Id(length))), VarDecl(Id(result), IntegerType, IntegerLit(0)), VarDecl(Id(i), IntegerType, IntegerLit(0)), WhileStmt(BinExpr(&&, BinExpr(>, Id(k), IntegerLit(0)), BinExpr(>=, BinExpr(-, Id(k), ArrayCell(Id(nums), [Id(i)])), IntegerLit(0))), BlockStmt([AssignStmt(Id(result), BinExpr(+, Id(result), IntegerLit(1))), AssignStmt(Id(k), BinExpr(-, Id(k), ArrayCell(Id(nums), [Id(i)]))), AssignStmt(Id(i), BinExpr(+, Id(i), IntegerLit(1)))])), ReturnStmt(Id(result))]))
	FuncDecl(Id(main), VoidType, [], None, BlockStmt([VarDecl(Id(nums), ArrayType([5], IntegerType), ArrayLit([IntegerLit(90), IntegerLit(30), IntegerLit(40), IntegerLit(90), IntegerLit(20)])), VarDecl(Id(length), IntegerType, BinExpr(/, FuncCall(Id(sizeof), [Id(nums)]), FuncCall(Id(sizeof), [ArrayCell(Id(nums), [IntegerLit(0)])]))), CallStmt(Id(printeger), FuncCall(Id(buyCar), [Id(nums), Id(length), IntegerLit(90)]))]))
])"""
        self.assertTrue(TestAST.test(input, expect, 351))

    def test_funcdecls_38(self):
        input = r"""
consecutiveOnes: function boolean(nums : array [200] of integer, size: integer) {
    found: boolean = false;
    for (i = 0, i < size, i + 1) {
        if (nums[i] == 1) {
            if(found) return false;
            while (i < size) {
                if(nums[i] != 1){
                    found = true;
                    break;
                }
                i = i+1;
            }
        }

        i = i+1;
    }
    return true;
}
"""
        expect = r"""Program([
	FuncDecl(Id(consecutiveOnes), BooleanType, [Param(Id(nums), ArrayType([200], IntegerType)), Param(Id(size), IntegerType)], None, BlockStmt([VarDecl(Id(found), BooleanType, BooleanLit(True)), ForStmt(AssignStmt(Id(i), IntegerLit(0)), BinExpr(<, Id(i), Id(size)), BinExpr(+, Id(i), IntegerLit(1)), BlockStmt([IfStmt(BinExpr(==, ArrayCell(Id(nums), [Id(i)]), IntegerLit(1)), BlockStmt([IfStmt(Id(found), ReturnStmt(BooleanLit(True))), WhileStmt(BinExpr(<, Id(i), Id(size)), BlockStmt([IfStmt(BinExpr(!=, ArrayCell(Id(nums), [Id(i)]), IntegerLit(1)), BlockStmt([AssignStmt(Id(found), BooleanLit(True)), BreakStmt()])), AssignStmt(Id(i), BinExpr(+, Id(i), IntegerLit(1)))]))])), AssignStmt(Id(i), BinExpr(+, Id(i), IntegerLit(1)))])), ReturnStmt(BooleanLit(True))]))
])"""
        self.assertTrue(TestAST.test(input, expect, 352))

    def test_funcdecls_39(self):
        input = r"""
reverse: function void(s: string, from: integer, to: integer) {
  temp: string = s;
  for (i = 0, i < to - from, i+1) {
    s[from + i] = temp[to - 1 - i];
  }
}
"""
        expect = r"""Program([
	FuncDecl(Id(reverse), VoidType, [Param(Id(s), StringType), Param(Id(from), IntegerType), Param(Id(to), IntegerType)], None, BlockStmt([VarDecl(Id(temp), StringType, Id(s)), ForStmt(AssignStmt(Id(i), IntegerLit(0)), BinExpr(<, Id(i), BinExpr(-, Id(to), Id(from))), BinExpr(+, Id(i), IntegerLit(1)), BlockStmt([AssignStmt(ArrayCell(Id(s), [BinExpr(+, Id(from), Id(i))]), ArrayCell(Id(temp), [BinExpr(-, BinExpr(-, Id(to), IntegerLit(1)), Id(i))]))]))]))
])"""
        self.assertTrue(TestAST.test(input, expect, 353))

    def test_funcdecls_40(self):
        input = r"""
removeDuplicates: function string (S: string, length: integer){
  ans: string;
  push_back(ans, S[0]);
  for (i = 1, i < length, i+1) {

    if (S[i] == back(ans)) {
      pop_back(ans);
    } else {
      push_back(ans, S[i]);
    }
  }

  return ans;
}
"""
        expect = r"""Program([
	FuncDecl(Id(removeDuplicates), StringType, [Param(Id(S), StringType), Param(Id(length), IntegerType)], None, BlockStmt([VarDecl(Id(ans), StringType), CallStmt(Id(push_back), Id(ans), ArrayCell(Id(S), [IntegerLit(0)])), ForStmt(AssignStmt(Id(i), IntegerLit(1)), BinExpr(<, Id(i), Id(length)), BinExpr(+, Id(i), IntegerLit(1)), BlockStmt([IfStmt(BinExpr(==, ArrayCell(Id(S), [Id(i)]), FuncCall(Id(back), [Id(ans)])), BlockStmt([CallStmt(Id(pop_back), Id(ans))]), BlockStmt([CallStmt(Id(push_back), Id(ans), ArrayCell(Id(S), [Id(i)]))]))])), ReturnStmt(Id(ans))]))
])"""
        self.assertTrue(TestAST.test(input, expect, 354))

    def test_funcdecls_41(self):
        input = r"""
removeDuplicates: function string (S: string, length: integer){
  // ans: string;
  push_back(ans, S[0]);
  for (i = 1, i < length, i+1)
    if (S[i] == back(ans)) {
      pop_back(ans);
    } else push_back(ans, S[i]);

  return ans;
}
"""
        expect = r"""Program([
	FuncDecl(Id(removeDuplicates), StringType, [Param(Id(S), StringType), Param(Id(length), IntegerType)], None, BlockStmt([CallStmt(Id(push_back), Id(ans), ArrayCell(Id(S), [IntegerLit(0)])), ForStmt(AssignStmt(Id(i), IntegerLit(1)), BinExpr(<, Id(i), Id(length)), BinExpr(+, Id(i), IntegerLit(1)), IfStmt(BinExpr(==, ArrayCell(Id(S), [Id(i)]), FuncCall(Id(back), [Id(ans)])), BlockStmt([CallStmt(Id(pop_back), Id(ans))]), CallStmt(Id(push_back), Id(ans), ArrayCell(Id(S), [Id(i)])))), ReturnStmt(Id(ans))]))
])"""
        self.assertTrue(TestAST.test(input, expect, 355))

    def test_funcdecls_42(self):
        input = r"""
midSquare: function integer (seed: integer) {
    newSeed: integer = pow(seed, 2);
    s: string = to_string(newSeed);
    erase(s, begin() + size(s) - 2, end(s));
    return stoi(substr(s, size(s) - 4));
}
"""
        expect = r"""Program([
	FuncDecl(Id(midSquare), IntegerType, [Param(Id(seed), IntegerType)], None, BlockStmt([VarDecl(Id(newSeed), IntegerType, FuncCall(Id(pow), [Id(seed), IntegerLit(2)])), VarDecl(Id(s), StringType, FuncCall(Id(to_string), [Id(newSeed)])), CallStmt(Id(erase), Id(s), BinExpr(-, BinExpr(+, FuncCall(Id(begin), []), FuncCall(Id(size), [Id(s)])), IntegerLit(2)), FuncCall(Id(end), [Id(s)])), ReturnStmt(FuncCall(Id(stoi), [FuncCall(Id(substr), [Id(s), BinExpr(-, FuncCall(Id(size), [Id(s)]), IntegerLit(4))])]))]))
])"""
        self.assertTrue(TestAST.test(input, expect, 356))

    def test_funcdecls_43(self):
        input = r"""
moduloDivision: function integer (seed: integer, mod: integer) { return seed % mod; }
"""
        expect = r"""Program([
	FuncDecl(Id(moduloDivision), IntegerType, [Param(Id(seed), IntegerType), Param(Id(mod), IntegerType)], None, BlockStmt([ReturnStmt(BinExpr(%, Id(seed), Id(mod)))]))
])"""
        self.assertTrue(TestAST.test(input, expect, 357))

    def test_funcdecls_44(self):
        input = r"""
moduloDivision: function integer (seed: integer, mod: integer) { return seed % mod; }

digitExtraction: function integer (seed: integer, extractDigits: array[100] of integer, size: integer) {
  s, strSeed: string = "", to_string(seed);
  for (i = 0, i < size, i+1) {
    s = s + strSeed[extractDigits[i]];
  }
  return stoi(s);
}
"""
        expect = r"""Program([
	FuncDecl(Id(moduloDivision), IntegerType, [Param(Id(seed), IntegerType), Param(Id(mod), IntegerType)], None, BlockStmt([ReturnStmt(BinExpr(%, Id(seed), Id(mod)))]))
	FuncDecl(Id(digitExtraction), IntegerType, [Param(Id(seed), IntegerType), Param(Id(extractDigits), ArrayType([100], IntegerType)), Param(Id(size), IntegerType)], None, BlockStmt([VarDecl(Id(s), StringType, StringLit()), VarDecl(Id(strSeed), StringType, FuncCall(Id(to_string), [Id(seed)])), ForStmt(AssignStmt(Id(i), IntegerLit(0)), BinExpr(<, Id(i), Id(size)), BinExpr(+, Id(i), IntegerLit(1)), BlockStmt([AssignStmt(Id(s), BinExpr(+, Id(s), ArrayCell(Id(strSeed), [ArrayCell(Id(extractDigits), [Id(i)])])))])), ReturnStmt(FuncCall(Id(stoi), [Id(s)]))]))
])"""
        self.assertTrue(TestAST.test(input, expect, 358))

    def test_funcdecls_45(self):
        input = r"""
foldShift: function integer (key: integer, addressSize: integer)
{
    x: string = to_string(key);
    sum: integer = 0;
  for (i = 0, i < length(x), i + 1) {
    s: string = substr(x, i, addressSize);
    i = i + addressSize;
    sum = sum + stoi(s);
  }
  test : integer = pow(10, addressSize);
  return sum % (test);
}
"""
        expect = r"""Program([
	FuncDecl(Id(foldShift), IntegerType, [Param(Id(key), IntegerType), Param(Id(addressSize), IntegerType)], None, BlockStmt([VarDecl(Id(x), StringType, FuncCall(Id(to_string), [Id(key)])), VarDecl(Id(sum), IntegerType, IntegerLit(0)), ForStmt(AssignStmt(Id(i), IntegerLit(0)), BinExpr(<, Id(i), FuncCall(Id(length), [Id(x)])), BinExpr(+, Id(i), IntegerLit(1)), BlockStmt([VarDecl(Id(s), StringType, FuncCall(Id(substr), [Id(x), Id(i), Id(addressSize)])), AssignStmt(Id(i), BinExpr(+, Id(i), Id(addressSize))), AssignStmt(Id(sum), BinExpr(+, Id(sum), FuncCall(Id(stoi), [Id(s)])))])), VarDecl(Id(test), IntegerType, FuncCall(Id(pow), [IntegerLit(10), Id(addressSize)])), ReturnStmt(BinExpr(%, Id(sum), Id(test)))]))
])"""
        self.assertTrue(TestAST.test(input, expect, 359))

    def test_funcdecls_46(self):
        input = r"""
rotation: function integer (key: integer, addressSize: integer)
{
  x: string = to_string(key);
  temp: string = x[length(x) - 1];
  for (i = length(x) - 1, i > 0, i-1) {
    x[i] = x[i - 1];
  }
  x[0] = temp;
  return foldShift(stoll(x), addressSize);
}
"""
        expect = r"""Program([
	FuncDecl(Id(rotation), IntegerType, [Param(Id(key), IntegerType), Param(Id(addressSize), IntegerType)], None, BlockStmt([VarDecl(Id(x), StringType, FuncCall(Id(to_string), [Id(key)])), VarDecl(Id(temp), StringType, ArrayCell(Id(x), [BinExpr(-, FuncCall(Id(length), [Id(x)]), IntegerLit(1))])), ForStmt(AssignStmt(Id(i), BinExpr(-, FuncCall(Id(length), [Id(x)]), IntegerLit(1))), BinExpr(>, Id(i), IntegerLit(0)), BinExpr(-, Id(i), IntegerLit(1)), BlockStmt([AssignStmt(ArrayCell(Id(x), [Id(i)]), ArrayCell(Id(x), [BinExpr(-, Id(i), IntegerLit(1))]))])), AssignStmt(ArrayCell(Id(x), [IntegerLit(0)]), Id(temp)), ReturnStmt(FuncCall(Id(foldShift), [FuncCall(Id(stoll), [Id(x)]), Id(addressSize)]))]))
])"""
        self.assertTrue(TestAST.test(input, expect, 360))

    def test_funcdecls_47(self):
        input = r"""
left: function integer (i: integer) { return (2 * i + 1); }
right: function integer (i: integer) { return (2 * i + 2); }
parent: function integer (i: integer) { return (i - 1) / 2; }
swap: function void(x: integer,y: integer) {
  k: integer = x;
  x = y;
  y = k;
}
"""
        expect = r"""Program([
	FuncDecl(Id(left), IntegerType, [Param(Id(i), IntegerType)], None, BlockStmt([ReturnStmt(BinExpr(+, BinExpr(*, IntegerLit(2), Id(i)), IntegerLit(1)))]))
	FuncDecl(Id(right), IntegerType, [Param(Id(i), IntegerType)], None, BlockStmt([ReturnStmt(BinExpr(+, BinExpr(*, IntegerLit(2), Id(i)), IntegerLit(2)))]))
	FuncDecl(Id(parent), IntegerType, [Param(Id(i), IntegerType)], None, BlockStmt([ReturnStmt(BinExpr(/, BinExpr(-, Id(i), IntegerLit(1)), IntegerLit(2)))]))
	FuncDecl(Id(swap), VoidType, [Param(Id(x), IntegerType), Param(Id(y), IntegerType)], None, BlockStmt([VarDecl(Id(k), IntegerType, Id(x)), AssignStmt(Id(x), Id(y)), AssignStmt(Id(y), Id(k))]))
])"""
        self.assertTrue(TestAST.test(input, expect, 361))

    def test_funcdecls_48(self):
        input = r"""
left: function integer (i: integer) { return (2 * i + 1); }
right: function integer (i: integer) { return (2 * i + 2); }
parent: function integer (i: integer) { return (i - 1) / 2; }
swap: function void(x: integer,y: integer) {
  k: integer = x;
  x = y;
  y = k;
}
reheapUp: function void(maxHeap: array[100] of integer, numberOfElements: integer , index: integer ) {
  if (index < numberOfElements) {
    if (index && maxHeap[parent(index)] < maxHeap[index]) {
      swap(maxHeap[index], maxHeap[parent(index)]);
      reheapUp(maxHeap, numberOfElements, parent(index));
    }
  }

}
"""
        expect = r"""Program([
	FuncDecl(Id(left), IntegerType, [Param(Id(i), IntegerType)], None, BlockStmt([ReturnStmt(BinExpr(+, BinExpr(*, IntegerLit(2), Id(i)), IntegerLit(1)))]))
	FuncDecl(Id(right), IntegerType, [Param(Id(i), IntegerType)], None, BlockStmt([ReturnStmt(BinExpr(+, BinExpr(*, IntegerLit(2), Id(i)), IntegerLit(2)))]))
	FuncDecl(Id(parent), IntegerType, [Param(Id(i), IntegerType)], None, BlockStmt([ReturnStmt(BinExpr(/, BinExpr(-, Id(i), IntegerLit(1)), IntegerLit(2)))]))
	FuncDecl(Id(swap), VoidType, [Param(Id(x), IntegerType), Param(Id(y), IntegerType)], None, BlockStmt([VarDecl(Id(k), IntegerType, Id(x)), AssignStmt(Id(x), Id(y)), AssignStmt(Id(y), Id(k))]))
	FuncDecl(Id(reheapUp), VoidType, [Param(Id(maxHeap), ArrayType([100], IntegerType)), Param(Id(numberOfElements), IntegerType), Param(Id(index), IntegerType)], None, BlockStmt([IfStmt(BinExpr(<, Id(index), Id(numberOfElements)), BlockStmt([IfStmt(BinExpr(<, BinExpr(&&, Id(index), ArrayCell(Id(maxHeap), [FuncCall(Id(parent), [Id(index)])])), ArrayCell(Id(maxHeap), [Id(index)])), BlockStmt([CallStmt(Id(swap), ArrayCell(Id(maxHeap), [Id(index)]), ArrayCell(Id(maxHeap), [FuncCall(Id(parent), [Id(index)])])), CallStmt(Id(reheapUp), Id(maxHeap), Id(numberOfElements), FuncCall(Id(parent), [Id(index)]))]))]))]))
])"""
        self.assertTrue(TestAST.test(input, expect, 362))

    def test_funcdecls_49(self):
        input = r"""
left: function integer (i: integer) { return (2 * i + 1); }
right: function integer (i: integer) { return (2 * i + 2); }
parent: function integer (i: integer) { return (i - 1) / 2; }
swap: function void(x: integer,y: integer) {
  k: integer = x;
  x = y;
  y = k;
}
reheapDown: function void (maxHeap: array[100] of integer, numberOfElements: integer , index: integer ) {
    if (index < numberOfElements) {
          l, r, largest: integer = left(index), right(index), index;
          if ((l < numberOfElements) && (maxHeap[l] > maxHeap[index])) {
            largest = l;
          }
        
          if ((r < numberOfElements) && (maxHeap[r] > maxHeap[largest])) {
            largest = r;
          }
        
          if (largest != index) {
            swap(maxHeap[index], maxHeap[largest]);
            reheapDown(maxHeap, numberOfElements, largest);
          }
    }
  
}
"""
        expect = r"""Program([
	FuncDecl(Id(left), IntegerType, [Param(Id(i), IntegerType)], None, BlockStmt([ReturnStmt(BinExpr(+, BinExpr(*, IntegerLit(2), Id(i)), IntegerLit(1)))]))
	FuncDecl(Id(right), IntegerType, [Param(Id(i), IntegerType)], None, BlockStmt([ReturnStmt(BinExpr(+, BinExpr(*, IntegerLit(2), Id(i)), IntegerLit(2)))]))
	FuncDecl(Id(parent), IntegerType, [Param(Id(i), IntegerType)], None, BlockStmt([ReturnStmt(BinExpr(/, BinExpr(-, Id(i), IntegerLit(1)), IntegerLit(2)))]))
	FuncDecl(Id(swap), VoidType, [Param(Id(x), IntegerType), Param(Id(y), IntegerType)], None, BlockStmt([VarDecl(Id(k), IntegerType, Id(x)), AssignStmt(Id(x), Id(y)), AssignStmt(Id(y), Id(k))]))
	FuncDecl(Id(reheapDown), VoidType, [Param(Id(maxHeap), ArrayType([100], IntegerType)), Param(Id(numberOfElements), IntegerType), Param(Id(index), IntegerType)], None, BlockStmt([IfStmt(BinExpr(<, Id(index), Id(numberOfElements)), BlockStmt([VarDecl(Id(l), IntegerType, FuncCall(Id(left), [Id(index)])), VarDecl(Id(r), IntegerType, FuncCall(Id(right), [Id(index)])), VarDecl(Id(largest), IntegerType, Id(index)), IfStmt(BinExpr(&&, BinExpr(<, Id(l), Id(numberOfElements)), BinExpr(>, ArrayCell(Id(maxHeap), [Id(l)]), ArrayCell(Id(maxHeap), [Id(index)]))), BlockStmt([AssignStmt(Id(largest), Id(l))])), IfStmt(BinExpr(&&, BinExpr(<, Id(r), Id(numberOfElements)), BinExpr(>, ArrayCell(Id(maxHeap), [Id(r)]), ArrayCell(Id(maxHeap), [Id(largest)]))), BlockStmt([AssignStmt(Id(largest), Id(r))])), IfStmt(BinExpr(!=, Id(largest), Id(index)), BlockStmt([CallStmt(Id(swap), ArrayCell(Id(maxHeap), [Id(index)]), ArrayCell(Id(maxHeap), [Id(largest)])), CallStmt(Id(reheapDown), Id(maxHeap), Id(numberOfElements), Id(largest))]))]))]))
])"""
        self.assertTrue(TestAST.test(input, expect, 363))

    def test_funcdecls_50(self):
        input = r"""
buildMaxHeap: function void (arr: array[100] of integer, numOfEl: integer) {
    for (i = numOfEl / 2 - 1, i >= 0, i-1) {
      heapify(arr, numOfEl, i);
    }
}
"""
        expect = r"""Program([
	FuncDecl(Id(buildMaxHeap), VoidType, [Param(Id(arr), ArrayType([100], IntegerType)), Param(Id(numOfEl), IntegerType)], None, BlockStmt([ForStmt(AssignStmt(Id(i), BinExpr(-, BinExpr(/, Id(numOfEl), IntegerLit(2)), IntegerLit(1))), BinExpr(>=, Id(i), IntegerLit(0)), BinExpr(-, Id(i), IntegerLit(1)), BlockStmt([CallStmt(Id(heapify), Id(arr), Id(numOfEl), Id(i))]))]))
])"""
        self.assertTrue(TestAST.test(input, expect, 364))

    def test_funcdecls_51(self):
        input = r"""
heapSort: function void (start: array[100] of integer, end: array[100] of integer) {
    numOfEl: integer = end - start;
    buildMaxHeap(start, numOfEl);
    for (i = numOfEl - 1, i >= 0, i-1) {
      temp: integer = start[0];
      start[0] = start[i];
      start[i] = temp;
      heapify(start, i, 0);
    }
    printegerArray(start, end);
  }
"""
        expect = r"""Program([
	FuncDecl(Id(heapSort), VoidType, [Param(Id(start), ArrayType([100], IntegerType)), Param(Id(end), ArrayType([100], IntegerType))], None, BlockStmt([VarDecl(Id(numOfEl), IntegerType, BinExpr(-, Id(end), Id(start))), CallStmt(Id(buildMaxHeap), Id(start), Id(numOfEl)), ForStmt(AssignStmt(Id(i), BinExpr(-, Id(numOfEl), IntegerLit(1))), BinExpr(>=, Id(i), IntegerLit(0)), BinExpr(-, Id(i), IntegerLit(1)), BlockStmt([VarDecl(Id(temp), IntegerType, ArrayCell(Id(start), [IntegerLit(0)])), AssignStmt(ArrayCell(Id(start), [IntegerLit(0)]), ArrayCell(Id(start), [Id(i)])), AssignStmt(ArrayCell(Id(start), [Id(i)]), Id(temp)), CallStmt(Id(heapify), Id(start), Id(i), IntegerLit(0))])), CallStmt(Id(printegerArray), Id(start), Id(end))]))
])"""
        self.assertTrue(TestAST.test(input, expect, 365))

    def test_funcdecls_52(self):
        input = r"""
heapify: function void(arr: array[100] of integer, numOfEl: integer, i: integer) {
    left, right, largest: integer = 2 * i + 1, 2 * i + 2, i;
    if ((left < numOfEl) && (arr[left] > arr[largest]))
      largest = left;

    if ((right < numOfEl) && (arr[right] > arr[largest]))
      largest = right;

    // Swap and continue heapifying if root is not largest
    if (largest != i) {
      temp: integer = arr[i];
      arr[i] = arr[largest];
      arr[largest] = temp;
      heapify(arr, numOfEl, largest);
    }
  }
"""
        expect = r"""Program([
	FuncDecl(Id(heapify), VoidType, [Param(Id(arr), ArrayType([100], IntegerType)), Param(Id(numOfEl), IntegerType), Param(Id(i), IntegerType)], None, BlockStmt([VarDecl(Id(left), IntegerType, BinExpr(+, BinExpr(*, IntegerLit(2), Id(i)), IntegerLit(1))), VarDecl(Id(right), IntegerType, BinExpr(+, BinExpr(*, IntegerLit(2), Id(i)), IntegerLit(2))), VarDecl(Id(largest), IntegerType, Id(i)), IfStmt(BinExpr(&&, BinExpr(<, Id(left), Id(numOfEl)), BinExpr(>, ArrayCell(Id(arr), [Id(left)]), ArrayCell(Id(arr), [Id(largest)]))), AssignStmt(Id(largest), Id(left))), IfStmt(BinExpr(&&, BinExpr(<, Id(right), Id(numOfEl)), BinExpr(>, ArrayCell(Id(arr), [Id(right)]), ArrayCell(Id(arr), [Id(largest)]))), AssignStmt(Id(largest), Id(right))), IfStmt(BinExpr(!=, Id(largest), Id(i)), BlockStmt([VarDecl(Id(temp), IntegerType, ArrayCell(Id(arr), [Id(i)])), AssignStmt(ArrayCell(Id(arr), [Id(i)]), ArrayCell(Id(arr), [Id(largest)])), AssignStmt(ArrayCell(Id(arr), [Id(largest)]), Id(temp)), CallStmt(Id(heapify), Id(arr), Id(numOfEl), Id(largest))]))]))
])"""
        self.assertTrue(TestAST.test(input, expect, 366))

    def test_funcdecls_53(self):
        input = r"""
minWaitingTime: function integer (n: integer, arrvalTime: array[100] of integer, completeTime: array[100] of integer) {
    sort(a, a + n, greater());
    minTegerime : integer = 0;

    // Iterate through the groups
    for (i = 0, i < n, i + k)
        // Update the time taken for each group
        minTegerime = minTegerime + (2 * a[i]);

    // Return the total time taken
    return minTegerime;
}
"""
        expect = r"""Program([
	FuncDecl(Id(minWaitingTime), IntegerType, [Param(Id(n), IntegerType), Param(Id(arrvalTime), ArrayType([100], IntegerType)), Param(Id(completeTime), ArrayType([100], IntegerType))], None, BlockStmt([CallStmt(Id(sort), Id(a), BinExpr(+, Id(a), Id(n)), FuncCall(Id(greater), [])), VarDecl(Id(minTegerime), IntegerType, IntegerLit(0)), ForStmt(AssignStmt(Id(i), IntegerLit(0)), BinExpr(<, Id(i), Id(n)), BinExpr(+, Id(i), Id(k)), AssignStmt(Id(minTegerime), BinExpr(+, Id(minTegerime), BinExpr(*, IntegerLit(2), ArrayCell(Id(a), [Id(i)]))))), ReturnStmt(Id(minTegerime))]))
])"""
        self.assertTrue(TestAST.test(input, expect, 367))

    def test_funcdecls_54(self):
        input = r"""
containStr: function boolean (S1: string , S2: string, sizeS1: integer, sizeS2: integer) {
  b : array[1000] of boolean;
  for (i = 0, i < sizeS2, i + 1) {
    found: boolean = false;
    for (j = 0, j < sizeS1, j + 1) {
      if (!b[j]) {
        if (S2[i] == S1[j]) {
          found = true;
          b[j] = true;
        }
      }
    }
    if (!found) {
      return false;
    }
  }
  return true;
}
"""
        expect = r"""Program([
	FuncDecl(Id(containStr), BooleanType, [Param(Id(S1), StringType), Param(Id(S2), StringType), Param(Id(sizeS1), IntegerType), Param(Id(sizeS2), IntegerType)], None, BlockStmt([VarDecl(Id(b), ArrayType([1000], BooleanType)), ForStmt(AssignStmt(Id(i), IntegerLit(0)), BinExpr(<, Id(i), Id(sizeS2)), BinExpr(+, Id(i), IntegerLit(1)), BlockStmt([VarDecl(Id(found), BooleanType, BooleanLit(True)), ForStmt(AssignStmt(Id(j), IntegerLit(0)), BinExpr(<, Id(j), Id(sizeS1)), BinExpr(+, Id(j), IntegerLit(1)), BlockStmt([IfStmt(UnExpr(!, ArrayCell(Id(b), [Id(j)])), BlockStmt([IfStmt(BinExpr(==, ArrayCell(Id(S2), [Id(i)]), ArrayCell(Id(S1), [Id(j)])), BlockStmt([AssignStmt(Id(found), BooleanLit(True)), AssignStmt(ArrayCell(Id(b), [Id(j)]), BooleanLit(True))]))]))])), IfStmt(UnExpr(!, Id(found)), BlockStmt([ReturnStmt(BooleanLit(True))]))])), ReturnStmt(BooleanLit(True))]))
])"""
        self.assertTrue(TestAST.test(input, expect, 368))

    def test_funcdecls_55(self):
        input = r"""
minStr: function string (S1: string , S2: string, sizeS1: integer, sizeS2: integer) {
  result : string = "";
  for (i = 0, i <= sizeS2 - sizeS1, i + 1) {
    result = S1::S2;
    if (containStr(S1, result)) {
      return result;
    }
  }
  return "Not found";
}
"""
        expect = r"""Program([
	FuncDecl(Id(minStr), StringType, [Param(Id(S1), StringType), Param(Id(S2), StringType), Param(Id(sizeS1), IntegerType), Param(Id(sizeS2), IntegerType)], None, BlockStmt([VarDecl(Id(result), StringType, StringLit()), ForStmt(AssignStmt(Id(i), IntegerLit(0)), BinExpr(<=, Id(i), BinExpr(-, Id(sizeS2), Id(sizeS1))), BinExpr(+, Id(i), IntegerLit(1)), BlockStmt([AssignStmt(Id(result), BinExpr(::, Id(S1), Id(S2))), IfStmt(FuncCall(Id(containStr), [Id(S1), Id(result)]), BlockStmt([ReturnStmt(Id(result))]))])), ReturnStmt(StringLit(Not found))]))
])"""
        self.assertTrue(TestAST.test(input, expect, 369))

    def test_funcdecls_56(self):
        input = r"""
Check: function boolean (nums: array[100] of integer, size: integer) {
  count: integer  = 0;
  for (i = 0, i < size, i + 1) {
    if (nums[i] < 0)
      count = count + 1;
  }
  if (count % 2 == 0)
    return true;
  else
    return false;
}
"""
        expect = r"""Program([
	FuncDecl(Id(Check), BooleanType, [Param(Id(nums), ArrayType([100], IntegerType)), Param(Id(size), IntegerType)], None, BlockStmt([VarDecl(Id(count), IntegerType, IntegerLit(0)), ForStmt(AssignStmt(Id(i), IntegerLit(0)), BinExpr(<, Id(i), Id(size)), BinExpr(+, Id(i), IntegerLit(1)), BlockStmt([IfStmt(BinExpr(<, ArrayCell(Id(nums), [Id(i)]), IntegerLit(0)), AssignStmt(Id(count), BinExpr(+, Id(count), IntegerLit(1))))])), IfStmt(BinExpr(==, BinExpr(%, Id(count), IntegerLit(2)), IntegerLit(0)), ReturnStmt(BooleanLit(True)), ReturnStmt(BooleanLit(True)))]))
])"""
        self.assertTrue(TestAST.test(input, expect, 370))

    def test_funcdecls_57(self):
        input = r"""
Checkzero: function boolean(nums: array[100] of integer, size: integer) {
  found: boolean = false;
  for (i = 0, i < size && !found, i + 1) {
    if (nums[i] == 0)
      found = true;
  }
  if (found)
    return true;
  else
    return false;
}
"""
        expect = r"""Program([
	FuncDecl(Id(Checkzero), BooleanType, [Param(Id(nums), ArrayType([100], IntegerType)), Param(Id(size), IntegerType)], None, BlockStmt([VarDecl(Id(found), BooleanType, BooleanLit(True)), ForStmt(AssignStmt(Id(i), IntegerLit(0)), BinExpr(<, Id(i), BinExpr(&&, Id(size), UnExpr(!, Id(found)))), BinExpr(+, Id(i), IntegerLit(1)), BlockStmt([IfStmt(BinExpr(==, ArrayCell(Id(nums), [Id(i)]), IntegerLit(0)), AssignStmt(Id(found), BooleanLit(True)))])), IfStmt(Id(found), ReturnStmt(BooleanLit(True)), ReturnStmt(BooleanLit(True)))]))
])"""
        self.assertTrue(TestAST.test(input, expect, 371))

    def test_funcdecls_58(self):
        input = r"""
search: function integer(nums: array[100] of integer, size: integer, target: integer) {
    left, right: integer = 0, size - 1;
    index: integer = -1;
    found: boolean = false;
    while (left <= right && !found) {
      mid: integer = (left + right) / 2;
      if (nums[mid] == target) {
        found = true;
        index = mid;
      }
      if (nums[mid] >= nums[left]) {
        if (nums[mid] > target) {
          if (target < nums[left])
            left = mid + 1;
          else
            right = mid - 1;
        } else
          left = mid + 1;
      } else {
        if (target > nums[mid]) {
          if (target > nums[right])
            right = mid - 1;
          else
            left = mid + 1;
        } else
          right = mid - 1;
      }
    }
    return index;
}
"""
        expect = r"""Program([
	FuncDecl(Id(search), IntegerType, [Param(Id(nums), ArrayType([100], IntegerType)), Param(Id(size), IntegerType), Param(Id(target), IntegerType)], None, BlockStmt([VarDecl(Id(left), IntegerType, IntegerLit(0)), VarDecl(Id(right), IntegerType, BinExpr(-, Id(size), IntegerLit(1))), VarDecl(Id(index), IntegerType, UnExpr(-, IntegerLit(1))), VarDecl(Id(found), BooleanType, BooleanLit(True)), WhileStmt(BinExpr(<=, Id(left), BinExpr(&&, Id(right), UnExpr(!, Id(found)))), BlockStmt([VarDecl(Id(mid), IntegerType, BinExpr(/, BinExpr(+, Id(left), Id(right)), IntegerLit(2))), IfStmt(BinExpr(==, ArrayCell(Id(nums), [Id(mid)]), Id(target)), BlockStmt([AssignStmt(Id(found), BooleanLit(True)), AssignStmt(Id(index), Id(mid))])), IfStmt(BinExpr(>=, ArrayCell(Id(nums), [Id(mid)]), ArrayCell(Id(nums), [Id(left)])), BlockStmt([IfStmt(BinExpr(>, ArrayCell(Id(nums), [Id(mid)]), Id(target)), BlockStmt([IfStmt(BinExpr(<, Id(target), ArrayCell(Id(nums), [Id(left)])), AssignStmt(Id(left), BinExpr(+, Id(mid), IntegerLit(1))), AssignStmt(Id(right), BinExpr(-, Id(mid), IntegerLit(1))))]), AssignStmt(Id(left), BinExpr(+, Id(mid), IntegerLit(1))))]), BlockStmt([IfStmt(BinExpr(>, Id(target), ArrayCell(Id(nums), [Id(mid)])), BlockStmt([IfStmt(BinExpr(>, Id(target), ArrayCell(Id(nums), [Id(right)])), AssignStmt(Id(right), BinExpr(-, Id(mid), IntegerLit(1))), AssignStmt(Id(left), BinExpr(+, Id(mid), IntegerLit(1))))]), AssignStmt(Id(right), BinExpr(-, Id(mid), IntegerLit(1))))]))])), ReturnStmt(Id(index))]))
])"""
        self.assertTrue(TestAST.test(input, expect, 372))

    def test_funcdecls_59(self):
        input = r"""
lengthOfLastWord: function integer(s: array[100] of string, size: integer) {
    count: integer = 0;
    if (size == 0)
      return 0;
    i: integer = size - 1;
    while ((s[i] == " ") && i >= 0) {
      i = i - 1;
    }
    while ((i >= 0) && s[i] != " ") {
      count = count + 1;
      i = i - 1;
    }
    return count;
}
"""
        expect = r"""Program([
	FuncDecl(Id(lengthOfLastWord), IntegerType, [Param(Id(s), ArrayType([100], StringType)), Param(Id(size), IntegerType)], None, BlockStmt([VarDecl(Id(count), IntegerType, IntegerLit(0)), IfStmt(BinExpr(==, Id(size), IntegerLit(0)), ReturnStmt(IntegerLit(0))), VarDecl(Id(i), IntegerType, BinExpr(-, Id(size), IntegerLit(1))), WhileStmt(BinExpr(>=, BinExpr(&&, BinExpr(==, ArrayCell(Id(s), [Id(i)]), StringLit( )), Id(i)), IntegerLit(0)), BlockStmt([AssignStmt(Id(i), BinExpr(-, Id(i), IntegerLit(1)))])), WhileStmt(BinExpr(!=, BinExpr(&&, BinExpr(>=, Id(i), IntegerLit(0)), ArrayCell(Id(s), [Id(i)])), StringLit( )), BlockStmt([AssignStmt(Id(count), BinExpr(+, Id(count), IntegerLit(1))), AssignStmt(Id(i), BinExpr(-, Id(i), IntegerLit(1)))])), ReturnStmt(Id(count))]))
])"""
        self.assertTrue(TestAST.test(input, expect, 373))

    def test_funcdecls_60(self):
        input = r"""
completeNum: function boolean(N: integer) {
  sum: integer = 0;
  for (i = 1, i < N, i + 1) {
    if (N % i == 0) {
      sum = sum + i;
    }
  }
  if (sum == N) {
    return true;
  }
  return false;
}
"""
        expect = r"""Program([
	FuncDecl(Id(completeNum), BooleanType, [Param(Id(N), IntegerType)], None, BlockStmt([VarDecl(Id(sum), IntegerType, IntegerLit(0)), ForStmt(AssignStmt(Id(i), IntegerLit(1)), BinExpr(<, Id(i), Id(N)), BinExpr(+, Id(i), IntegerLit(1)), BlockStmt([IfStmt(BinExpr(==, BinExpr(%, Id(N), Id(i)), IntegerLit(0)), BlockStmt([AssignStmt(Id(sum), BinExpr(+, Id(sum), Id(i)))]))])), IfStmt(BinExpr(==, Id(sum), Id(N)), BlockStmt([ReturnStmt(BooleanLit(True))])), ReturnStmt(BooleanLit(True))]))
])"""
        self.assertTrue(TestAST.test(input, expect, 374))

    def test_funcdecls_61(self):
        input = r"""
max_two_nums: function auto (a: integer, b: integer) { 
    if (a > b) {
        return a;
    }
    return b;
}
"""
        expect = r"""Program([
	FuncDecl(Id(max_two_nums), AutoType, [Param(Id(a), IntegerType), Param(Id(b), IntegerType)], None, BlockStmt([IfStmt(BinExpr(>, Id(a), Id(b)), BlockStmt([ReturnStmt(Id(a))])), ReturnStmt(Id(b))]))
])"""
        self.assertTrue(TestAST.test(input, expect, 375))

    def test_funcdecls_62(self):
        input = r"""
min_two_nums: function auto (a: integer, b: integer) { 
    if (a < b) {
        return a;
    }
    return b;
}
"""
        expect = r"""Program([
	FuncDecl(Id(min_two_nums), AutoType, [Param(Id(a), IntegerType), Param(Id(b), IntegerType)], None, BlockStmt([IfStmt(BinExpr(<, Id(a), Id(b)), BlockStmt([ReturnStmt(Id(a))])), ReturnStmt(Id(b))]))
])"""
        self.assertTrue(TestAST.test(input, expect, 376))

    def test_funcdecls_63(self):
        input = r"""
findMax: function auto(vals: array[100] of integer, numEls: integer) {
  max: integer = vals[0];
  for (i = 1, i < numEls, i+1) {
    if (vals[i] > max) {
      max = vals[i];
    }
  }
  return max;
}
"""
        expect = r"""Program([
	FuncDecl(Id(findMax), AutoType, [Param(Id(vals), ArrayType([100], IntegerType)), Param(Id(numEls), IntegerType)], None, BlockStmt([VarDecl(Id(max), IntegerType, ArrayCell(Id(vals), [IntegerLit(0)])), ForStmt(AssignStmt(Id(i), IntegerLit(1)), BinExpr(<, Id(i), Id(numEls)), BinExpr(+, Id(i), IntegerLit(1)), BlockStmt([IfStmt(BinExpr(>, ArrayCell(Id(vals), [Id(i)]), Id(max)), BlockStmt([AssignStmt(Id(max), ArrayCell(Id(vals), [Id(i)]))]))])), ReturnStmt(Id(max))]))
])"""
        self.assertTrue(TestAST.test(input, expect, 377))

    def test_funcdecls_64(self):
        input = r"""
findMin: function auto(vals: array[100] of integer, numEls: integer) {
  min: integer = vals[0];
  for (i = 1, i < numEls, i+1) {
    if (vals[i] < min) {
      min = vals[i];
    }
  }
  return min;
}
"""
        expect = r"""Program([
	FuncDecl(Id(findMin), AutoType, [Param(Id(vals), ArrayType([100], IntegerType)), Param(Id(numEls), IntegerType)], None, BlockStmt([VarDecl(Id(min), IntegerType, ArrayCell(Id(vals), [IntegerLit(0)])), ForStmt(AssignStmt(Id(i), IntegerLit(1)), BinExpr(<, Id(i), Id(numEls)), BinExpr(+, Id(i), IntegerLit(1)), BlockStmt([IfStmt(BinExpr(<, ArrayCell(Id(vals), [Id(i)]), Id(min)), BlockStmt([AssignStmt(Id(min), ArrayCell(Id(vals), [Id(i)]))]))])), ReturnStmt(Id(min))]))
])"""
        self.assertTrue(TestAST.test(input, expect, 378))

    def test_funcdecls_65(self):
        input = r"""
isPalindrome: function boolean(str: array[100] of string, strSize: integer) {
  for (i = 0, i < strSize / 2, i+1) {
    if (str[i] != str[strSize-i-1]) {
      return false;
    }
  }
  return true;
}
"""
        expect = r"""Program([
	FuncDecl(Id(isPalindrome), BooleanType, [Param(Id(str), ArrayType([100], StringType)), Param(Id(strSize), IntegerType)], None, BlockStmt([ForStmt(AssignStmt(Id(i), IntegerLit(0)), BinExpr(<, Id(i), BinExpr(/, Id(strSize), IntegerLit(2))), BinExpr(+, Id(i), IntegerLit(1)), BlockStmt([IfStmt(BinExpr(!=, ArrayCell(Id(str), [Id(i)]), ArrayCell(Id(str), [BinExpr(-, BinExpr(-, Id(strSize), Id(i)), IntegerLit(1))])), BlockStmt([ReturnStmt(BooleanLit(True))]))])), ReturnStmt(BooleanLit(True))]))
])"""
        self.assertTrue(TestAST.test(input, expect, 379))

    def test_funcdecls_66(self):
        input = r"""
checkElementsUniqueness: function boolean (arr: array[100] of integer, n: integer) {
  if ((n > 1000) || (n < 0))
    return false;
  for (i = 0, i < n - 1, i+1) {
    for (j = i + 1, j < n, j+1) {
      if (arr[i] == arr[j])
        return false;
    }
  }
  return true;
}
"""
        expect = r"""Program([
	FuncDecl(Id(checkElementsUniqueness), BooleanType, [Param(Id(arr), ArrayType([100], IntegerType)), Param(Id(n), IntegerType)], None, BlockStmt([IfStmt(BinExpr(||, BinExpr(>, Id(n), IntegerLit(1000)), BinExpr(<, Id(n), IntegerLit(0))), ReturnStmt(BooleanLit(True))), ForStmt(AssignStmt(Id(i), IntegerLit(0)), BinExpr(<, Id(i), BinExpr(-, Id(n), IntegerLit(1))), BinExpr(+, Id(i), IntegerLit(1)), BlockStmt([ForStmt(AssignStmt(Id(j), BinExpr(+, Id(i), IntegerLit(1))), BinExpr(<, Id(j), Id(n)), BinExpr(+, Id(j), IntegerLit(1)), BlockStmt([IfStmt(BinExpr(==, ArrayCell(Id(arr), [Id(i)]), ArrayCell(Id(arr), [Id(j)])), ReturnStmt(BooleanLit(True)))]))])), ReturnStmt(BooleanLit(True))]))
])"""
        self.assertTrue(TestAST.test(input, expect, 380))

    def test_funcdecls_67(self):
        input = r"""
checkElementsUniqueness: function boolean (arr: array[100] of integer, n: integer) {
  if ((n > 1000) || (n < 0))
    return false;
  for (i = 0, i < n - 1, i+1) {
    for (j = i + 1, j < n, j+1) {
      if (arr[i] == arr[j])
        return false;
    }
  }
  return true;
}

main: function void() {
    arr   : array [6] of integer = {1, 91, 0, -100, 100, 200};
    if (checkElementsUniqueness(arr, 6)) printString("Correct!");
    else printString("Wrong!");
}
"""
        expect = r"""Program([
	FuncDecl(Id(checkElementsUniqueness), BooleanType, [Param(Id(arr), ArrayType([100], IntegerType)), Param(Id(n), IntegerType)], None, BlockStmt([IfStmt(BinExpr(||, BinExpr(>, Id(n), IntegerLit(1000)), BinExpr(<, Id(n), IntegerLit(0))), ReturnStmt(BooleanLit(True))), ForStmt(AssignStmt(Id(i), IntegerLit(0)), BinExpr(<, Id(i), BinExpr(-, Id(n), IntegerLit(1))), BinExpr(+, Id(i), IntegerLit(1)), BlockStmt([ForStmt(AssignStmt(Id(j), BinExpr(+, Id(i), IntegerLit(1))), BinExpr(<, Id(j), Id(n)), BinExpr(+, Id(j), IntegerLit(1)), BlockStmt([IfStmt(BinExpr(==, ArrayCell(Id(arr), [Id(i)]), ArrayCell(Id(arr), [Id(j)])), ReturnStmt(BooleanLit(True)))]))])), ReturnStmt(BooleanLit(True))]))
	FuncDecl(Id(main), VoidType, [], None, BlockStmt([VarDecl(Id(arr), ArrayType([6], IntegerType), ArrayLit([IntegerLit(1), IntegerLit(91), IntegerLit(0), UnExpr(-, IntegerLit(100)), IntegerLit(100), IntegerLit(200)])), IfStmt(FuncCall(Id(checkElementsUniqueness), [Id(arr), IntegerLit(6)]), CallStmt(Id(printString), StringLit(Correct!)), CallStmt(Id(printString), StringLit(Wrong!)))]))
])"""
        self.assertTrue(TestAST.test(input, expect, 381))

    def test_funcdecls_68(self):
        input = r"""
gcdIteration: function integer(p: integer, q: integer) {
  while (p * q != 0) {
    if (p > q) {
      p = p % q;
    } else {
      q = q % p;
    }
  }
  return p + q;
}
"""
        expect = r"""Program([
	FuncDecl(Id(gcdIteration), IntegerType, [Param(Id(p), IntegerType), Param(Id(q), IntegerType)], None, BlockStmt([WhileStmt(BinExpr(!=, BinExpr(*, Id(p), Id(q)), IntegerLit(0)), BlockStmt([IfStmt(BinExpr(>, Id(p), Id(q)), BlockStmt([AssignStmt(Id(p), BinExpr(%, Id(p), Id(q)))]), BlockStmt([AssignStmt(Id(q), BinExpr(%, Id(q), Id(p)))]))])), ReturnStmt(BinExpr(+, Id(p), Id(q)))]))
])"""
        self.assertTrue(TestAST.test(input, expect, 382))

    def test_funcdecls_69(self):
        input = r"""
gcdRecursion: function integer(p: integer, q: integer) {
  if (q == 0)
    return p;
  return gcdRecursion(q, p % q);
}
"""
        expect = r"""Program([
	FuncDecl(Id(gcdRecursion), IntegerType, [Param(Id(p), IntegerType), Param(Id(q), IntegerType)], None, BlockStmt([IfStmt(BinExpr(==, Id(q), IntegerLit(0)), ReturnStmt(Id(p))), ReturnStmt(FuncCall(Id(gcdRecursion), [Id(q), BinExpr(%, Id(p), Id(q))]))]))
])"""
        self.assertTrue(TestAST.test(input, expect, 383))

    def test_funcdecls_70(self):
        input = r"""
recursiveSearch: function integer(out n: integer, m: integer, arr: array[100] of integer, index: integer) {
  index = index + 1;
  if (index > n) {
    return -1;
  }
  if (arr[index - 1] == m) {
    for (i = index - 1, i < n - 1, i+1) {
      arr[i] = arr[i + 1];
    }
    n = n - 1;
    return index - 1;
  }
  return recursiveSearch(n, m, arr, index);
}
"""
        expect = r"""Program([
	FuncDecl(Id(recursiveSearch), IntegerType, [OutParam(Id(n), IntegerType), Param(Id(m), IntegerType), Param(Id(arr), ArrayType([100], IntegerType)), Param(Id(index), IntegerType)], None, BlockStmt([AssignStmt(Id(index), BinExpr(+, Id(index), IntegerLit(1))), IfStmt(BinExpr(>, Id(index), Id(n)), BlockStmt([ReturnStmt(UnExpr(-, IntegerLit(1)))])), IfStmt(BinExpr(==, ArrayCell(Id(arr), [BinExpr(-, Id(index), IntegerLit(1))]), Id(m)), BlockStmt([ForStmt(AssignStmt(Id(i), BinExpr(-, Id(index), IntegerLit(1))), BinExpr(<, Id(i), BinExpr(-, Id(n), IntegerLit(1))), BinExpr(+, Id(i), IntegerLit(1)), BlockStmt([AssignStmt(ArrayCell(Id(arr), [Id(i)]), ArrayCell(Id(arr), [BinExpr(+, Id(i), IntegerLit(1))]))])), AssignStmt(Id(n), BinExpr(-, Id(n), IntegerLit(1))), ReturnStmt(BinExpr(-, Id(index), IntegerLit(1)))])), ReturnStmt(FuncCall(Id(recursiveSearch), [Id(n), Id(m), Id(arr), Id(index)]))]))
])"""
        self.assertTrue(TestAST.test(input, expect, 384))

    def test_funcdecls_71(self):
        input = r"""
isSymmetry: function boolean(head: array[100] of integer, tail: array[100] of integer, size: integer) {
  for (i = 0, i < size / 2, i+1) {
    if (head[i] != tail[i])
      return false;
  }
  return true;
}
"""
        expect = r"""Program([
	FuncDecl(Id(isSymmetry), BooleanType, [Param(Id(head), ArrayType([100], IntegerType)), Param(Id(tail), ArrayType([100], IntegerType)), Param(Id(size), IntegerType)], None, BlockStmt([ForStmt(AssignStmt(Id(i), IntegerLit(0)), BinExpr(<, Id(i), BinExpr(/, Id(size), IntegerLit(2))), BinExpr(+, Id(i), IntegerLit(1)), BlockStmt([IfStmt(BinExpr(!=, ArrayCell(Id(head), [Id(i)]), ArrayCell(Id(tail), [Id(i)])), ReturnStmt(BooleanLit(True)))])), ReturnStmt(BooleanLit(True))]))
])"""
        self.assertTrue(TestAST.test(input, expect, 385))

    def test_funcdecls_72(self):
        input = r"""
checkElements: function boolean (arr: array[100] of integer, n: integer) {
  if ((n > 1000) || (n < 0))
    return false;
  for (i = 0, i < n - 1, i+1) {
    for (j = i + 1, j < n, j+1) {
      if (arr[i] == arr[j]/*)*/)
        return false;
    }
  }
  return true;
}
"""
        expect = r"""Program([
	FuncDecl(Id(checkElements), BooleanType, [Param(Id(arr), ArrayType([100], IntegerType)), Param(Id(n), IntegerType)], None, BlockStmt([IfStmt(BinExpr(||, BinExpr(>, Id(n), IntegerLit(1000)), BinExpr(<, Id(n), IntegerLit(0))), ReturnStmt(BooleanLit(True))), ForStmt(AssignStmt(Id(i), IntegerLit(0)), BinExpr(<, Id(i), BinExpr(-, Id(n), IntegerLit(1))), BinExpr(+, Id(i), IntegerLit(1)), BlockStmt([ForStmt(AssignStmt(Id(j), BinExpr(+, Id(i), IntegerLit(1))), BinExpr(<, Id(j), Id(n)), BinExpr(+, Id(j), IntegerLit(1)), BlockStmt([IfStmt(BinExpr(==, ArrayCell(Id(arr), [Id(i)]), ArrayCell(Id(arr), [Id(j)])), ReturnStmt(BooleanLit(True)))]))])), ReturnStmt(BooleanLit(True))]))
])"""
        self.assertTrue(TestAST.test(input, expect, 386))

    def test_funcdecls_73(self):
        input = r"""
binarySearch: function integer(arr: array[1000] of integer, left: integer, right: integer, x: integer) {
  if (right >= left) {
    mid:integer = left + (right - left) / 2;
    if (arr[mid] == x)
      return mid;
    if (arr[mid] > x)
      return binarySearch(arr, left, mid - 1, x);
    return binarySearch(arr, mid + 1, right, x);
  }
  return -1;
}
"""
        expect = r"""Program([
	FuncDecl(Id(binarySearch), IntegerType, [Param(Id(arr), ArrayType([1000], IntegerType)), Param(Id(left), IntegerType), Param(Id(right), IntegerType), Param(Id(x), IntegerType)], None, BlockStmt([IfStmt(BinExpr(>=, Id(right), Id(left)), BlockStmt([VarDecl(Id(mid), IntegerType, BinExpr(+, Id(left), BinExpr(/, BinExpr(-, Id(right), Id(left)), IntegerLit(2)))), IfStmt(BinExpr(==, ArrayCell(Id(arr), [Id(mid)]), Id(x)), ReturnStmt(Id(mid))), IfStmt(BinExpr(>, ArrayCell(Id(arr), [Id(mid)]), Id(x)), ReturnStmt(FuncCall(Id(binarySearch), [Id(arr), Id(left), BinExpr(-, Id(mid), IntegerLit(1)), Id(x)]))), ReturnStmt(FuncCall(Id(binarySearch), [Id(arr), BinExpr(+, Id(mid), IntegerLit(1)), Id(right), Id(x)]))])), ReturnStmt(UnExpr(-, IntegerLit(1)))]))
])"""
        self.assertTrue(TestAST.test(input, expect, 387))

    def test_funcdecls_74(self):
        input = r"""
x : array [0, 100] of integer;
main: function void(out x: array[0, 100] of integer) {
    for (i = 1, i < 100, i+1) {
        if (i % 2 == 0) {
            x[i, 0] = i;
        } else {
            x[0, i] = i + 1;
        }
    }
}
"""
        expect = r"""Program([
	VarDecl(Id(x), ArrayType([0, 100], IntegerType))
	FuncDecl(Id(main), VoidType, [OutParam(Id(x), ArrayType([0, 100], IntegerType))], None, BlockStmt([ForStmt(AssignStmt(Id(i), IntegerLit(1)), BinExpr(<, Id(i), IntegerLit(100)), BinExpr(+, Id(i), IntegerLit(1)), BlockStmt([IfStmt(BinExpr(==, BinExpr(%, Id(i), IntegerLit(2)), IntegerLit(0)), BlockStmt([AssignStmt(ArrayCell(Id(x), [Id(i), IntegerLit(0)]), Id(i))]), BlockStmt([AssignStmt(ArrayCell(Id(x), [IntegerLit(0), Id(i)]), BinExpr(+, Id(i), IntegerLit(1)))]))]))]))
])"""
        self.assertTrue(TestAST.test(input, expect, 388))

    def test_funcdecls_75(self):
        input = r"""
x :  integer = 1;
main: function void(out x: integer) {
    for (i = 1, i < 100, i+1) {
        for (j = 1, j < 200, j+1) {
            if (i + j >= 2) {
                foo(2, x + 1);
            }
        }
    }
}
"""
        expect = r"""Program([
	VarDecl(Id(x), IntegerType, IntegerLit(1))
	FuncDecl(Id(main), VoidType, [OutParam(Id(x), IntegerType)], None, BlockStmt([ForStmt(AssignStmt(Id(i), IntegerLit(1)), BinExpr(<, Id(i), IntegerLit(100)), BinExpr(+, Id(i), IntegerLit(1)), BlockStmt([ForStmt(AssignStmt(Id(j), IntegerLit(1)), BinExpr(<, Id(j), IntegerLit(200)), BinExpr(+, Id(j), IntegerLit(1)), BlockStmt([IfStmt(BinExpr(>=, BinExpr(+, Id(i), Id(j)), IntegerLit(2)), BlockStmt([CallStmt(Id(foo), IntegerLit(2), BinExpr(+, Id(x), IntegerLit(1)))]))]))]))]))
])"""
        self.assertTrue(TestAST.test(input, expect, 389))

    def test_funcdecls_76(self):
        input = r"""
main: function void() {
    for (i = 1, i < 100, i+1) {
        for (j = 1, j < 200, j+1) {
            if (i + j >= 2) {
                break;
            } else {
                continue;
            }
        }
    }
}
"""
        expect = r"""Program([
	FuncDecl(Id(main), VoidType, [], None, BlockStmt([ForStmt(AssignStmt(Id(i), IntegerLit(1)), BinExpr(<, Id(i), IntegerLit(100)), BinExpr(+, Id(i), IntegerLit(1)), BlockStmt([ForStmt(AssignStmt(Id(j), IntegerLit(1)), BinExpr(<, Id(j), IntegerLit(200)), BinExpr(+, Id(j), IntegerLit(1)), BlockStmt([IfStmt(BinExpr(>=, BinExpr(+, Id(i), Id(j)), IntegerLit(2)), BlockStmt([BreakStmt()]), BlockStmt([ContinueStmt()]))]))]))]))
])"""
        self.assertTrue(TestAST.test(input, expect, 390))

    def test_funcdecls_77(self):
        input = r"""
main: function void() {
    for (i = 1, i < 100, i+1) {
        j : integer = 0;
        while (j < 200) {
            if (i + j >= 20) {
                break;
            } else {
             j = j + 1;
            }
        }
    }
}
"""
        expect = r"""Program([
	FuncDecl(Id(main), VoidType, [], None, BlockStmt([ForStmt(AssignStmt(Id(i), IntegerLit(1)), BinExpr(<, Id(i), IntegerLit(100)), BinExpr(+, Id(i), IntegerLit(1)), BlockStmt([VarDecl(Id(j), IntegerType, IntegerLit(0)), WhileStmt(BinExpr(<, Id(j), IntegerLit(200)), BlockStmt([IfStmt(BinExpr(>=, BinExpr(+, Id(i), Id(j)), IntegerLit(20)), BlockStmt([BreakStmt()]), BlockStmt([AssignStmt(Id(j), BinExpr(+, Id(j), IntegerLit(1)))]))]))]))]))
])"""
        self.assertTrue(TestAST.test(input, expect, 391))

    def test_funcdecls_78(self):
        input = r"""
main: function void() {
    for (i = 1, i < 100, i+1) {
        j : integer = 0;
        while (j < 200) {j = j+1;}
        while (i != 20) {}
    }
}
"""
        expect = r"""Program([
	FuncDecl(Id(main), VoidType, [], None, BlockStmt([ForStmt(AssignStmt(Id(i), IntegerLit(1)), BinExpr(<, Id(i), IntegerLit(100)), BinExpr(+, Id(i), IntegerLit(1)), BlockStmt([VarDecl(Id(j), IntegerType, IntegerLit(0)), WhileStmt(BinExpr(<, Id(j), IntegerLit(200)), BlockStmt([AssignStmt(Id(j), BinExpr(+, Id(j), IntegerLit(1)))])), WhileStmt(BinExpr(!=, Id(i), IntegerLit(20)), BlockStmt([]))]))]))
])"""
        self.assertTrue(TestAST.test(input, expect, 392))

    def test_funcdecls_79(self):
        input = r"""
main: function void() {
    for (i = 1, i < 100, i+1) {
        j : integer = 0;
        while (j < 200) {j = j+1;}
        while (i != 20) {}
    }
}
"""
        expect = r"""Program([
	FuncDecl(Id(main), VoidType, [], None, BlockStmt([ForStmt(AssignStmt(Id(i), IntegerLit(1)), BinExpr(<, Id(i), IntegerLit(100)), BinExpr(+, Id(i), IntegerLit(1)), BlockStmt([VarDecl(Id(j), IntegerType, IntegerLit(0)), WhileStmt(BinExpr(<, Id(j), IntegerLit(200)), BlockStmt([AssignStmt(Id(j), BinExpr(+, Id(j), IntegerLit(1)))])), WhileStmt(BinExpr(!=, Id(i), IntegerLit(20)), BlockStmt([]))]))]))
])"""
        self.assertTrue(TestAST.test(input, expect, 393))

    def test_funcdecls_80(self):
        input = r"""
binarySearch: function integer(arr: array[100] of integer, left: integer, right: integer, x: integer) {
  if (right >= left) {
    mid:integer = left + (right - left) / 2;
    if (arr[mid] == x)
      return mid;
    if (arr[mid] > x)
      return binarySearch(arr, left, mid - 1, x);
    return binarySearch(arr, mid + 1, right, x);
  }
  return -1;
}
main: function void() {
    arr   : array [5] of integer = {1, 91, 0, -100, 100};
    binarySearch(arr, 0, 4, 0);
}
"""
        expect = r"""Program([
	FuncDecl(Id(binarySearch), IntegerType, [Param(Id(arr), ArrayType([100], IntegerType)), Param(Id(left), IntegerType), Param(Id(right), IntegerType), Param(Id(x), IntegerType)], None, BlockStmt([IfStmt(BinExpr(>=, Id(right), Id(left)), BlockStmt([VarDecl(Id(mid), IntegerType, BinExpr(+, Id(left), BinExpr(/, BinExpr(-, Id(right), Id(left)), IntegerLit(2)))), IfStmt(BinExpr(==, ArrayCell(Id(arr), [Id(mid)]), Id(x)), ReturnStmt(Id(mid))), IfStmt(BinExpr(>, ArrayCell(Id(arr), [Id(mid)]), Id(x)), ReturnStmt(FuncCall(Id(binarySearch), [Id(arr), Id(left), BinExpr(-, Id(mid), IntegerLit(1)), Id(x)]))), ReturnStmt(FuncCall(Id(binarySearch), [Id(arr), BinExpr(+, Id(mid), IntegerLit(1)), Id(right), Id(x)]))])), ReturnStmt(UnExpr(-, IntegerLit(1)))]))
	FuncDecl(Id(main), VoidType, [], None, BlockStmt([VarDecl(Id(arr), ArrayType([5], IntegerType), ArrayLit([IntegerLit(1), IntegerLit(91), IntegerLit(0), UnExpr(-, IntegerLit(100)), IntegerLit(100)])), CallStmt(Id(binarySearch), Id(arr), IntegerLit(0), IntegerLit(4), IntegerLit(0))]))
])"""
        self.assertTrue(TestAST.test(input, expect, 394))

    def test_funcdecls_81(self):
        input = r"""
checkElements: function boolean (arr: array[100] of integer, n: integer) {
  if ((n > 1000) || (n < 0))
    return false;
  for (i = 0, i < n - 1, i+1) {
    for (j = i + 1, j < n, j+1) {
      if (arr[i] == arr[j]/*)*/)
        return false;
    }
  }
  return true;
}
main: function void() {
    arr   : array [5] of integer = {1, 91, 0, -100, 100};
    checkElements(arr, 0);
}
"""
        expect = r"""Program([
	FuncDecl(Id(checkElements), BooleanType, [Param(Id(arr), ArrayType([100], IntegerType)), Param(Id(n), IntegerType)], None, BlockStmt([IfStmt(BinExpr(||, BinExpr(>, Id(n), IntegerLit(1000)), BinExpr(<, Id(n), IntegerLit(0))), ReturnStmt(BooleanLit(True))), ForStmt(AssignStmt(Id(i), IntegerLit(0)), BinExpr(<, Id(i), BinExpr(-, Id(n), IntegerLit(1))), BinExpr(+, Id(i), IntegerLit(1)), BlockStmt([ForStmt(AssignStmt(Id(j), BinExpr(+, Id(i), IntegerLit(1))), BinExpr(<, Id(j), Id(n)), BinExpr(+, Id(j), IntegerLit(1)), BlockStmt([IfStmt(BinExpr(==, ArrayCell(Id(arr), [Id(i)]), ArrayCell(Id(arr), [Id(j)])), ReturnStmt(BooleanLit(True)))]))])), ReturnStmt(BooleanLit(True))]))
	FuncDecl(Id(main), VoidType, [], None, BlockStmt([VarDecl(Id(arr), ArrayType([5], IntegerType), ArrayLit([IntegerLit(1), IntegerLit(91), IntegerLit(0), UnExpr(-, IntegerLit(100)), IntegerLit(100)])), CallStmt(Id(checkElements), Id(arr), IntegerLit(0))]))
])"""
        self.assertTrue(TestAST.test(input, expect, 395))

    def test_funcdecls_82(self):
        input = r"""
isSymmetry: function boolean(head: array[100] of integer, tail: array[100] of integer, size: integer) {
  for (i = 0, i < size / 2, i+1) {
    if (head[i] != tail[i])
      return false;
  }
  return true;
}
main: function void() {
    head, tail   : array [5] of integer = {1, 91, 0, -100, 100}, {10, 1, 1000, -100, 100};
    isSymmetry(head, tail, 5);
}
"""
        expect = r"""Program([
	FuncDecl(Id(isSymmetry), BooleanType, [Param(Id(head), ArrayType([100], IntegerType)), Param(Id(tail), ArrayType([100], IntegerType)), Param(Id(size), IntegerType)], None, BlockStmt([ForStmt(AssignStmt(Id(i), IntegerLit(0)), BinExpr(<, Id(i), BinExpr(/, Id(size), IntegerLit(2))), BinExpr(+, Id(i), IntegerLit(1)), BlockStmt([IfStmt(BinExpr(!=, ArrayCell(Id(head), [Id(i)]), ArrayCell(Id(tail), [Id(i)])), ReturnStmt(BooleanLit(True)))])), ReturnStmt(BooleanLit(True))]))
	FuncDecl(Id(main), VoidType, [], None, BlockStmt([VarDecl(Id(head), ArrayType([5], IntegerType), ArrayLit([IntegerLit(1), IntegerLit(91), IntegerLit(0), UnExpr(-, IntegerLit(100)), IntegerLit(100)])), VarDecl(Id(tail), ArrayType([5], IntegerType), ArrayLit([IntegerLit(10), IntegerLit(1), IntegerLit(1000), UnExpr(-, IntegerLit(100)), IntegerLit(100)])), CallStmt(Id(isSymmetry), Id(head), Id(tail), IntegerLit(5))]))
])"""
        self.assertTrue(TestAST.test(input, expect, 396))

    def test_funcdecls_83(self):
        input = r"""
n : integer = 10;
recursiveSearch: function integer(out n: integer, m: integer, arr: array[100] of integer, index: integer) {
  index = index + 1;
  if (index > n) {
    return -1;
  }
  if (arr[index - 1] == m) {
    for (i = index - 1, i < n - 1, i+1) {
      arr[i] = arr[i + 1];
    }
    n = n - 1;
    return index - 1;
  }
  return recursiveSearch(n, m, arr, index);
}
main: function void() {
    arr   : array [5] of integer = {1, 91, 0, -100, 100};
    recursiveSearch(n, 10, arr);
}
"""
        expect = r"""Program([
	VarDecl(Id(n), IntegerType, IntegerLit(10))
	FuncDecl(Id(recursiveSearch), IntegerType, [OutParam(Id(n), IntegerType), Param(Id(m), IntegerType), Param(Id(arr), ArrayType([100], IntegerType)), Param(Id(index), IntegerType)], None, BlockStmt([AssignStmt(Id(index), BinExpr(+, Id(index), IntegerLit(1))), IfStmt(BinExpr(>, Id(index), Id(n)), BlockStmt([ReturnStmt(UnExpr(-, IntegerLit(1)))])), IfStmt(BinExpr(==, ArrayCell(Id(arr), [BinExpr(-, Id(index), IntegerLit(1))]), Id(m)), BlockStmt([ForStmt(AssignStmt(Id(i), BinExpr(-, Id(index), IntegerLit(1))), BinExpr(<, Id(i), BinExpr(-, Id(n), IntegerLit(1))), BinExpr(+, Id(i), IntegerLit(1)), BlockStmt([AssignStmt(ArrayCell(Id(arr), [Id(i)]), ArrayCell(Id(arr), [BinExpr(+, Id(i), IntegerLit(1))]))])), AssignStmt(Id(n), BinExpr(-, Id(n), IntegerLit(1))), ReturnStmt(BinExpr(-, Id(index), IntegerLit(1)))])), ReturnStmt(FuncCall(Id(recursiveSearch), [Id(n), Id(m), Id(arr), Id(index)]))]))
	FuncDecl(Id(main), VoidType, [], None, BlockStmt([VarDecl(Id(arr), ArrayType([5], IntegerType), ArrayLit([IntegerLit(1), IntegerLit(91), IntegerLit(0), UnExpr(-, IntegerLit(100)), IntegerLit(100)])), CallStmt(Id(recursiveSearch), Id(n), IntegerLit(10), Id(arr))]))
])"""
        self.assertTrue(TestAST.test(input, expect, 397))

    def test_funcdecls_84(self):
        input = r"""
gcdIteration: function integer(p: integer, q: integer) {
  while (p * q != 0) {
    if (p > q) {
      p = p % q;
    } else {
      q = q % p;
    }
  }
  return p + q;
}
gcdRecursion: function integer(p: integer, q: integer) {
  if (q == 0)
    return p;
  return gcdRecursion(q, p % q);
}
main: function void() {
    gcdIteration(120, 5);
    gcdRecursion(120, 5);
}
"""
        expect = r"""Program([
	FuncDecl(Id(gcdIteration), IntegerType, [Param(Id(p), IntegerType), Param(Id(q), IntegerType)], None, BlockStmt([WhileStmt(BinExpr(!=, BinExpr(*, Id(p), Id(q)), IntegerLit(0)), BlockStmt([IfStmt(BinExpr(>, Id(p), Id(q)), BlockStmt([AssignStmt(Id(p), BinExpr(%, Id(p), Id(q)))]), BlockStmt([AssignStmt(Id(q), BinExpr(%, Id(q), Id(p)))]))])), ReturnStmt(BinExpr(+, Id(p), Id(q)))]))
	FuncDecl(Id(gcdRecursion), IntegerType, [Param(Id(p), IntegerType), Param(Id(q), IntegerType)], None, BlockStmt([IfStmt(BinExpr(==, Id(q), IntegerLit(0)), ReturnStmt(Id(p))), ReturnStmt(FuncCall(Id(gcdRecursion), [Id(q), BinExpr(%, Id(p), Id(q))]))]))
	FuncDecl(Id(main), VoidType, [], None, BlockStmt([CallStmt(Id(gcdIteration), IntegerLit(120), IntegerLit(5)), CallStmt(Id(gcdRecursion), IntegerLit(120), IntegerLit(5))]))
])"""
        self.assertTrue(TestAST.test(input, expect, 398))

    def test_funcdecls_85(self):
        input = r"""
isPalindrome: function boolean(strs: array[100] of string, strSize: integer) {
  for (i = 0, i < strSize / 2, i+1) {
    if (strs[i] != strs[strSize-i-1]) {
      return false;
    }
  }
  return true;
}
main: function void() {
    strs   : array [5] of string = {"hello", "world", "!!!", "", "test\n"};

    if(isPalindrome(strs, 5)) printString("Correct!!!");
    else printString("Wrong!!!");
}
"""
        expect = r"""Program([
	FuncDecl(Id(isPalindrome), BooleanType, [Param(Id(strs), ArrayType([100], StringType)), Param(Id(strSize), IntegerType)], None, BlockStmt([ForStmt(AssignStmt(Id(i), IntegerLit(0)), BinExpr(<, Id(i), BinExpr(/, Id(strSize), IntegerLit(2))), BinExpr(+, Id(i), IntegerLit(1)), BlockStmt([IfStmt(BinExpr(!=, ArrayCell(Id(strs), [Id(i)]), ArrayCell(Id(strs), [BinExpr(-, BinExpr(-, Id(strSize), Id(i)), IntegerLit(1))])), BlockStmt([ReturnStmt(BooleanLit(True))]))])), ReturnStmt(BooleanLit(True))]))
	FuncDecl(Id(main), VoidType, [], None, BlockStmt([VarDecl(Id(strs), ArrayType([5], StringType), ArrayLit([StringLit(hello), StringLit(world), StringLit(!!!), StringLit(), StringLit(test\n)])), IfStmt(FuncCall(Id(isPalindrome), [Id(strs), IntegerLit(5)]), CallStmt(Id(printString), StringLit(Correct!!!)), CallStmt(Id(printString), StringLit(Wrong!!!)))]))
])"""
        self.assertTrue(TestAST.test(input, expect, 399))
