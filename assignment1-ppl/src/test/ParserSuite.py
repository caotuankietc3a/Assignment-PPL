import unittest
from TestUtils import TestParser


class ParserSuite(unittest.TestCase):
    #     def test_variable_decl_1(self):
    #         input = """
    # a, b, c : boolean;
    # """
    #         expect = "successful"
    #         self.assertTrue(TestParser.test(input, expect, 200))
    #
    #     def test_variable_decl_2(self):
    #         input = """
    # a,b,c,d: string;
    # """
    #         expect = "successful"
    #         self.assertTrue(TestParser.test(input, expect, 201))
    #
    #     def test_variable_decl_3(self):
    #         input = """
    # a,   b,   c   : auto = exprs , exprs , exprs;
    # """
    #         expect = "successful"
    #         self.assertTrue(TestParser.test(input, expect, 202))
    #
    #     def test_variable_decl_4(self):
    #         input = """
    # a,   b,   c   : auto = exprs , exprs;
    # """
    #         expect = "successful"
    #         self.assertTrue(TestParser.test(input, expect, 203))
    #
    #     def test_variable_decl_5(self):
    #         input = """
    # a,   b,   c   : auto;
    # """
    #         expect = "Error on line 2 col 20: ;"
    #         self.assertTrue(TestParser.test(input, expect, 204))
    #
    #     def test_variable_decl_6(self):
    #         input = """
    # a,   b,   c   : array [2, 3] of int;
    # """
    #         expect = "successful"
    #         self.assertTrue(TestParser.test(input, expect, 205))
    #
    #     def test_variable_decl_7(self):
    #         input = """
    # a, b, c : int = exprs;
    # """
    #         expect = "successful"
    #         self.assertTrue(TestParser.test(input, expect, 206))
    #
    #     def test_variable_decl_8(self):
    #         input = """
    # a,   b,   c   : array [2, 3] of int;
    # """
    #         expect = "successful"
    #         self.assertTrue(TestParser.test(input, expect, 207))
    #
    #     def test_variable_decl_9(self):
    #         input = """
    # a,   b,   c   : array [2, 3] of int = exprs, exprs;
    # """
    #         expect = "successful"
    #         self.assertTrue(TestParser.test(input, expect, 208))
    #
    #     def test_variable_decl_10(self):
    #         input = """
    # a,   b,   c   : array [2, 3] of int = exprs, exprs, exprs;
    # """
    #         expect = "successful"
    #         self.assertTrue(TestParser.test(input, expect, 209))

    #     def test_exprs_1(self):
    #         input = """
    # a + b, c + d - e,c + a[a+d]
    # """
    #         expect = "successful"
    #         self.assertTrue(TestParser.test(input, expect, 210))
    #
    #     def test_exprs_2(self):
    #         input = """
    # (c + e + d) >= 2,
    # (c >= 2) == true,
    # true && true,
    # b[a[2, 3],c[2, 5]] + d,
    # a::b::c,
    # 1 && 2 > 3,
    # -a,
    # !!true
    # """
    #         expect = "successful"
    #         self.assertTrue(TestParser.test(input, expect, 211))

    #     def test_stmts_1(self):
    #         input = """
    # b = a = arr[1, 2, 3] = 5;
    #
    # """
    #         expect = "successful"
    #         self.assertTrue(TestParser.test(input, expect, 212))

    def test_11(self):
        input = """
x : int = 65;
fact : function int (n : int) {
    if (n == 0) return 1;
    else return n*fact(n-1);
}
main : function void () {
    delta : int = fact(3);
    inc (x, delta);
    printint(x);
}
inc : function void (out n: int, delta : int) {
n = n + delta;
    }
    """
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 213))
