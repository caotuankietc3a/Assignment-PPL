import unittest
from TestUtils import TestLexer


class LexerSuite(unittest.TestCase):

    # def test_1(self):
    #     self.assertTrue(TestLexer.test("abc", "abc,<EOF>", 101))
    #
    # def test_2(self):
    #     self.assertTrue(TestLexer.test("abc a12", "abc,a12,<EOF>", 102))
    #
    # def test_3(self):
    #     self.assertTrue(TestLexer.test("abc A12", "abc,Error Token A", 103))
    #
    # def test_4(self):
    #     self.assertTrue(TestLexer.test("abc?svn", "abc,Error Token ?", 104))
    #
    # def test_5(self):
    #     self.assertTrue(TestLexer.test("0a12", "Error Token 0", 105))

    # def test_6(self):
    #     self.assertTrue(TestLexer.test("1.0", "1.0,<EOF>", 201))
    #
    # def test_7(self):
    #     self.assertTrue(TestLexer.test("1e-12", "1e-12,<EOF>", 202))
    #
    # def test_8(self):
    #     self.assertTrue(TestLexer.test("1.0e-12", "1.0e-12,<EOF>", 203))
    #
    # def test_9(self):
    #     self.assertTrue(TestLexer.test(".01", "Error Token .", 204))
    #
    # def test_10(self):
    #     self.assertTrue(TestLexer.test("'0.01'", "Error Token '", 205))
    #
    # def test_11(self):
    #     self.assertTrue(TestLexer.test("1.0e", "1.0,Error Token e", 206))
    #
    # def test_12(self):
    #     self.assertTrue(TestLexer.test("0e123", "0e123,<EOF>", 207))
    #
    # def test_13(self):
    #     self.assertTrue(TestLexer.test(".e123", "Error Token .", 208))
    #
    # def test_14(self):
    #     self.assertTrue(TestLexer.test("e123", "Error Token e", 209))

    def test_15(self):
        self.assertTrue(TestLexer.test("'Yanxi Palace - 2018'",
                        "'Yanxi Palace - 2018',<EOF>", 301))

    def test_16(self):
        self.assertTrue(TestLexer.test("'abc?svn'",
                        "'abc?svn',<EOF>", 302))

    def test_17(self):
        self.assertTrue(TestLexer.test("'1.0e-12'",
                                       "'1.0e-12',<EOF>", 303))

    def test_18(self):
        self.assertTrue(TestLexer.test("'0.001''",
                        "'0.001',Error Token '", 304))

    def test_19(self):
        self.assertTrue(TestLexer.test("'0.001'''",
                        "'0.001''',<EOF>", 305))
