import unittest
from TestUtils import TestLexer


class LexerSuite(unittest.TestCase):

    """TEST COMMENT"""

    def test_comment_1(self):
        self.assertTrue(TestLexer.test(
            "/* A C-style comment */", "<EOF>", 101))

    def test_comment_2(self):
        self.assertTrue(TestLexer.test(
            "/* A C-sty\nle comment */", "<EOF>", 102))

    def test_comment_3(self):
        self.assertTrue(TestLexer.test(
            """// A C-style comment
""", "<EOF>", 103))

    def test_comment_4(self):
        self.assertTrue(TestLexer.test(
            "// A C-style\n /* comment */", "<EOF>", 104))

    def test_comment_5(self):
        self.assertTrue(TestLexer.test(
            "// A C-style/* comment */", "<EOF>", 105))

    def test_comment_6(self):
        self.assertTrue(TestLexer.test(
            "/* // A C-style comment */", "<EOF>", 106))

    def test_comment_7(self):
        self.assertTrue(TestLexer.test(
            "/* /* A C-style */ */", "*,/,<EOF>", 107))

    """TEST IDENTIFIERS"""

    def test_id_1(self):
        self.assertTrue(TestLexer.test("abc", "abc,<EOF>", 108))

    def test_id_2(self):
        self.assertTrue(TestLexer.test("abc a12", "abc,a12,<EOF>", 109))

    def test_id_3(self):
        self.assertTrue(TestLexer.test("abc A12", "abc,A12,<EOF>", 110))

    def test_id_4(self):
        self.assertTrue(TestLexer.test("abc?svn", "abc,Error Token ?", 111))

    def test_id_5(self):
        self.assertTrue(TestLexer.test("0a12", "0,a12,<EOF>", 112))

    def test_id_6(self):
        self.assertTrue(TestLexer.test("abc_123", "abc_123,<EOF>", 113))

    def test_id_7(self):
        self.assertTrue(TestLexer.test("ABC_123", "ABC_123,<EOF>", 114))

    def test_id_8(self):
        self.assertTrue(TestLexer.test("aBc_d123", "aBc_d123,<EOF>", 115))

    def test_id_9(self):
        self.assertTrue(TestLexer.test("abC_D123", "abC_D123,<EOF>", 116))

    def test_id_10(self):
        self.assertTrue(TestLexer.test("_abcABC__", "_abcABC__,<EOF>", 117))

    """TEST LITERALS"""

    def test_int_lit_1(self):
        self.assertTrue(
            TestLexer.test(
                r"""
0 1 2 3 4 123 123456789
""",
                "0,1,2,3,4,123,123456789,<EOF>",
                118,
            )
        )

    def test_int_lit_2(self):
        self.assertTrue(
            TestLexer.test(
                r"""
-1230 1_12 123_456_789 1_123 1_4 1_55 341_
""",
                "-,1230,112,123456789,1123,14,155,341,_,<EOF>",
                119,
            )
        )

    def test_float_lit(self):
        self.assertTrue(
            TestLexer.test(
                r"""
9.0 12e8 1. 0.33E-3 128e+42 1_2_3_4. 1_2_3_56.1234 1_.34 1_2_8e-42
""",
                "9.0,12e8,1.,0.33E-3,128e+42,1_2_3_4.,1_2_3_56.1234,1,_,.34,1_2_8e-42,<EOF>",
                120,
            )
        )
