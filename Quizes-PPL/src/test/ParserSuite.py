import unittest
from TestUtils import TestParser


class ParserSuite(unittest.TestCase):
    # def test_simple_program(self):
    #     """Simple program: int main() {} """
    #     input = """int main() {}"""
    #     expect = "successful"
    #     self.assertTrue(TestParser.test(input,expect,201))
    #
    # def test_more_complex_program(self):
    #     """More complex program"""
    #     input = """int main () {
    #         putIntLn(4);
    #     }"""
    #     expect = "successful"
    #     self.assertTrue(TestParser.test(input,expect,202))
    #
    # def test_wrong_miss_close(self):
    #     """Miss ) int main( {}"""
    #     input = """int main( {}"""
    #     expect = "Error on line 1 col 10: {"
    #     self.assertTrue(TestParser.test(input,expect,203))

    # def test_1(self):
    #     input = """vardecl"""
    #     expect = "successful"
    #     self.assertTrue(TestParser.test(input, expect, 801))
    #
    # def test_2(self):
    #     input = """funcdecl"""
    #     expect = "successful"
    #     self.assertTrue(TestParser.test(input, expect, 802))
    #
    # def test_3(self):
    #     input = """vardecl funcdecl vardecl"""
    #     expect = "successful"
    #     self.assertTrue(TestParser.test(input, expect, 803))
    #
    # def test_4(self):
    #     input = """vardecl vardecl vardecl"""
    #     expect = "successful"
    #     self.assertTrue(TestParser.test(input, expect, 804))
    #
    # def test_5(self):
    #     input = """funcdecl funcdecl funcdecl"""
    #     expect = "successful"
    #     self.assertTrue(TestParser.test(input, expect, 805))
    #
    # def test_6(self):
    #     input = """funcdecl
    #             vardecl
    #             vardecl
    #             funcdecl
    #             funcdecl
    #             vardecl
    #             funcdecl"""
    #     expect = "successful"
    #     self.assertTrue(TestParser.test(input, expect, 806))
    #
    # def test_7(self):
    #     input = """"""
    #     expect = "Error on line 1 col 0: <EOF>"
    #     self.assertTrue(TestParser.test(input, expect, 807))

    #     def test_8(self):
    #         input = """int a, b,c;
    #                 float foo(int a; float c, d) body
    #                 float goo (float a, b) body"""
    #         expect = "successful"
    #         self.assertTrue(TestParser.test(input, expect, 901))
    #
    #     def test_9(self):
    #         input = """int a, b,;"""
    #         expect = "Error on line 1 col 9: ;"
    #         self.assertTrue(TestParser.test(input, expect, 902))
    #
    #     def test_10(self):
    #         input = """float foo(int a, float c, d) body"""
    #         expect = "Error on line 1 col 17: float"
    #         self.assertTrue(TestParser.test(input, expect, 903))
    #
    #     def test_11(self):
    #         input = """float foo(int a; float c, d;) body"""
    #         expect = "Error on line 1 col 28: )"
    #         self.assertTrue(TestParser.test(input, expect, 904))
    #
    #     def test_12(self):
    #         input = """int c;
    # float A()"""
    #         expect = "Error on line 2 col 9: <EOF>"
    #         self.assertTrue(TestParser.test(input, expect, 905))
    #
    #     def test_13(self):
    #         input = """int c
    # float A() body"""
    #         expect = "Error on line 2 col 0: float"
    #         self.assertTrue(TestParser.test(input, expect, 906))
    #
    #     def test_14(self):
    #         input = """int a, b,c;
    # float foo(int a; float c, d) body
    # int c,d;
    # float goo (float a, b) body
    # int"""
    #         expect = "Error on line 5 col 3: <EOF>"
    #         self.assertTrue(TestParser.test(input, expect, 907))
    #
    #     def test_15(self):
    #         input = """float foo() body
    # int foo() body
    # float foo(int a) body"""
    #         expect = "successful"
    #         self.assertTrue(TestParser.test(input, expect, 908))
    #
    #     def test_16(self):
    #         input = """int a;
    # float b,c;
    # int a;"""
    #         expect = "successful"
    #         self.assertTrue(TestParser.test(input, expect, 909))
    #
    #     def test_17(self):
    #         input = "int a,b,c;"
    #         expect = "successful"
    #         self.assertTrue(TestParser.test(input, expect, 910))

    #     def test_18(self):
    #         input = """int a, b,c;
    #     float foo(int a; float c, d) {
    #        int e ;
    #        e = expr ;
    #        c = expr ;
    #        foo(expr);
    #        return expr;
    #     }
    #     float goo (float a, b) {
    #        return expr;
    #     }"""
    #         expect = "successful"
    #         self.assertTrue(TestParser.test(input, expect, 1000))
    #
    #     def test_19(self):
    #         input = """int a, b,;"""
    #         expect = "Error on line 1 col 9: ;"
    #         self.assertTrue(TestParser.test(input, expect, 1001))
    #
    #     def test_20(self):
    #         input = """float foo(int a, float c, d) {}"""
    #         expect = "Error on line 1 col 17: float"
    #         self.assertTrue(TestParser.test(input, expect, 1002))
    #
    #     def test_21(self):
    #         input = """float foo(int a; float c, d;) {}"""
    #         expect = "Error on line 1 col 28: )"
    #         self.assertTrue(TestParser.test(input, expect, 1003))
    #
    #     def test_22(self):
    #         input = """int c;
    # c = expr;"""
    #         expect = "Error on line 2 col 0: c"
    #         self.assertTrue(TestParser.test(input, expect, 1004))
    #
    #     def test_23(self):
    #         input = """int a, b,c;
    # float foo(int a; float c, d) {
    #    int e = expr;
    #    e = expr ;
    #    c = expr ;
    #    return expr;
    # }
    # float goo(float a, b) {
    #    return expr;
    # }"""
    #         expect = "Error on line 3 col 9: ="
    #         self.assertTrue(TestParser.test(input, expect, 1005))
    #
    #     def test_24(self):
    #         input = """int a, b,c;
    # float foo(int a; float c, d) {
    #    int e ;
    #    e = expr ;
    #    c = expr ;
    #    return expr
    # }
    # """
    #         expect = "Error on line 7 col 0: }"
    #         self.assertTrue(TestParser.test(input, expect, 1006))
    #
    #     def test_25(self):
    #         input = """float goo (float a, b) {
    #     foo(expr, expr, expr);
    #     return expr;
    # }
    #
    # c = expr;"""
    #         expect = "Error on line 6 col 0: c"
    #         self.assertTrue(TestParser.test(input, expect, 1007))
    #
    #     def test_26(self):
    #         input = """float goo (float a, b) {
    #    return expr;
    # }"""
    #         expect = "successful"
    #         self.assertTrue(TestParser.test(input, expect, 1008))
    #
    #     def test_27(self):
    #         input = """float goo (float a, b) {
    #    return expr;
    # }"""
    #         expect = "successful"
    #         self.assertTrue(TestParser.test(input, expect, 1009))

    def test_28(self):
        input = """int a, b,c;
float foo(int a; float c, d) {
   int e ;
   e = a + 4 ;
   c = a * d / 2.0 ;
   return c + 1;
}
float goo (float a, b) {
   return foo(1, a, b);
}"""
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 2000))

    def test_29(self):
        input = """int a, b,c;
float foo(int a; float c, d) {
   int e ;
   e = a + 4 ;
   c = a * d / 2.0 ;
   return c + 1;
}
float goo (float a, b) {
   return foo(1, a, b);
}"""
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 2001))

    def test_30(self):
        input = """int a, b,;"""
        expect = "Error on line 1 col 9: ;"
        self.assertTrue(TestParser.test(input, expect, 2002))

    def test_31(self):
        input = """float foo(int a, float c, d) {}"""
        expect = "Error on line 1 col 17: float"
        self.assertTrue(TestParser.test(input, expect, 2003))

    def test_32(self):
        input = """float foo(int a; float c, d;) {}"""
        expect = "Error on line 1 col 28: )"
        self.assertTrue(TestParser.test(input, expect, 2004))

    def test_33(self):
        input = """int c;
c = 4;"""
        expect = "Error on line 2 col 0: c"
        self.assertTrue(TestParser.test(input, expect, 2005))

    def test_34(self):
        input = """int a, b,c;
float foo(int a; float c, d) {
   int e = 5;
   e = a + 4 ;
   c = a * d / 2.0 ;
   return c + 1;
}
float goo(float a, b) {
   return foo(1, a, b);
}"""
        expect = "Error on line 3 col 9: ="
        self.assertTrue(TestParser.test(input, expect, 2006))

    def test_35(self):
        input = """int a, b,c;
float foo(int a; float c, d) {
   int e ;
   e = a + 4 ;
   c = a * d / 2.0 ;
   return c + 1
}
float goo (float a, b) {
   return foo(1, a, b);
}"""
        expect = "Error on line 7 col 0: }"
        self.assertTrue(TestParser.test(input, expect, 2007))

    def test_36(self):
        input = """float goo (float a, b) {
   return foo(1, a, b);
}

c = 5;"""
        expect = "Error on line 5 col 0: c"
        self.assertTrue(TestParser.test(input, expect, 2008))

    def test_37(self):
        input = """float goo (float a, b) {
   return foo(1, a, b) + 1;
}"""
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 2009))

    def test_38(self):
        input = """float goo (float a, b) {
   return 1 - foo(1, a, b);
}"""
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 410))

    def test_39(self):
        input = """int a, b,c;
float foo(int a; float c, d) {
   int e ;
   e = a + 4 ;
   c = a * d / 2.0 ;
   return c + 1;
}
float goo (float a, b) {
   return foo(1, a, b);
}"""
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 411))
