import unittest
from TestUtils import TestLexer


class LexerSuite(unittest.TestCase):

    def test_1(self):
        self.assertTrue(TestLexer.test("abc", "abc,<EOF>", 101))

    def test_2(self):
        self.assertTrue(TestLexer.test("abc a12", "abc,a12,<EOF>", 102))

    def test_3(self):
        self.assertTrue(TestLexer.test("abc A12", "abc,Error Token A", 103))

    def test_4(self):
        self.assertTrue(TestLexer.test("abc?svn", "abc,Error Token ?", 104))

    def test_5(self):
        self.assertTrue(TestLexer.test("0a12", "Error Token 0", 105))
