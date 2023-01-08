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

    def test_boolean_lit(self):
        self.assertTrue(TestLexer.test(
            r"""true false""", "true,false,<EOF>", 121,))

    def test_string_lit_1(self):
        self.assertTrue(TestLexer.test(
            """\"This is \\t a string containing tab \t\"""", "This is \\t a string containing tab 	,<EOF>", 122,))

    def test_string_lit_2(self):
        self.assertTrue(TestLexer.test(
            """\"He asked me: \\\"Where is John?\\\"\"""", "He asked me: \\\"Where is John?\\\",<EOF>", 123,))

    def test_string_lit_3(self):
        self.assertTrue(TestLexer.test("\"He asked me: \'\"Where is John?\'\"\"",
                                       "He asked me: \'\"Where is John?\'\",<EOF>", 124))

    def test_string_lit_4(self):
        self.assertTrue(TestLexer.test(
            "\"\\b \\' He is my ex's man\"", "\\b \\' He is my ex's man,<EOF>", 125))

    def test_string_lit_5(self):
        self.assertTrue(TestLexer.test(
            "\"She is Tam\'s girlfriend.\"", "She is Tam\'s girlfriend.,<EOF>", 126))

    def test_string_unclose_1(self):
        self.assertTrue(TestLexer.test("\"He is a man",
                        "Unclosed String: He is a man", 127))

    def test_string_unclose_2(self):
        self.assertTrue(TestLexer.test("\"abc \\n \\f 's def",
                        "Unclosed String: abc \\n \\f 's def", 128))

    def test_string_unclose_3(self):
        self.assertTrue(TestLexer.test("\"He is \\b a man",
                        "Unclosed String: He is \\b a man", 129))

    def test_string_unclose_4(self):
        self.assertTrue(TestLexer.test("\"It is a unclosed \\n string",
                        "Unclosed String: It is a unclosed \\n string", 130))

    def test_string_unclose_5(self):
        self.assertTrue(TestLexer.test("\"This is a \\t string \\n containing tab \" \"He asked \\n me: '\"Where '\"is'\" John?'\"\" \"I am not closed",
                        "This is a \\t string \\n containing tab ,He asked \\n me: '\"Where '\"is'\" John?'\",Unclosed String: I am not closed", 131))

    def test_string_illegal_esc_1(self):
        self.assertTrue(TestLexer.test("\"I have an escape sequence \'\"Here it is \\k\'\"\"",
                        "Illegal Escape In String: I have an escape sequence \'\"Here it is \\k", 132))

    def test_string_illegal_esc_2(self):
        self.assertTrue(TestLexer.test("\"\\a He is a man\"",
                        "Illegal Escape In String: \\a", 133))

    def test_string_illegal_esc_3(self):
        self.assertTrue(TestLexer.test("\"\\\\ He is a \\\\ \\\' 19-year-old man \\a\"",
                        "Illegal Escape In String: \\\\ He is a \\\\ \\\' 19-year-old man \\a", 134))
