import unittest
from TestUtils import TestCodeGen
from AST import *


class CheckCodeGenSuite(unittest.TestCase):
    def test_1(self):
        input = r"""
    // x, y, z, t: integer = 10, 1023, 32, -123;
    // arr: array [2] of integer = {10, 1023};
     x, y, z, t: integer;
    arr : array [2] of integer;
    main: function void(){
    }
"""
        expect = ""
        self.assertTrue(TestCodeGen.test(input, expect, 501))
