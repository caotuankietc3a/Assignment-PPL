import unittest
from TestUtils import TestCodeGen
from AST import *


class CheckCodeGenSuite(unittest.TestCase):
    #     def test_1(self):
    #         input = r"""
    #     x, y, z, t: integer;
    #     arr : array [2] of integer;
    #     main: function void(){
    #     }
    # """
    #         expect = ""
    #         self.assertTrue(TestCodeGen.test(input, expect, 501))

    #     def test_2(self):
    #         input = r"""
    #     x, y, z, t: integer = 10, 1023, 32, 123;
    #     // arr: array [2] of integer = {10, 1023};
    #     main: function void(){
    #     }
    # """
    #         expect = ""
    #         self.assertTrue(TestCodeGen.test(input, expect, 502))

    #     def test_3(self):
    #         input = r"""
    #     x, y, z, t: integer = 10, 1023, 32, 123;
    #     g: float;
    #     main: function void(){
    #         x: integer = 3;
    #     }
    # """
    #         expect = ""
    #         self.assertTrue(TestCodeGen.test(input, expect, 503))

    #     def test_4(self):
    #         input = r"""
    #     main: function void(){
    #         printInteger(10);
    #     }
    # """
    #         expect = "10"
    #         self.assertTrue(TestCodeGen.test(input, expect, 504))

    #     def test_5(self):
    #         input = r"""
    #     main: function void(){
    #         x: integer = 10;
    #         printInteger(x);
    #     }
    # """
    #         expect = "10"
    #         self.assertTrue(TestCodeGen.test(input, expect, 505))

    #     def test_6(self):
    #         input = r"""
    #     y: float = 10.123;
    #     main: function void(){
    #         x: integer = 10;
    #         printInteger(x);
    #         writeFloat(y);
    #         printInteger(z);
    #     }
    #     z: integer =  110;
    # """
    #         expect = "1010.123110"
    #         self.assertTrue(TestCodeGen.test(input, expect, 506))

    def test_7(self):
        input = r"""
    //b: boolean = false;
    z: integer =  110;
    main: function void(){
        //printBoolean(b);
        // printInteger(z);
    }
"""
        expect = ""
        self.assertTrue(TestCodeGen.test(input, expect, 507))
