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

    def test_18(self):
        input = """int a, b,c;
float foo(int a; float c, d) {
   int e ;
   e = expr ;
   c = expr ;
   foo(expr);
   return expr;
}
float goo (float a, b) {
   return expr;
}"""
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 1000))
