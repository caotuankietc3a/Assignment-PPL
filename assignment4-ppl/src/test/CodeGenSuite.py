import unittest
from TestUtils import TestCodeGen
from AST import *


class CheckCodeGenSuite(unittest.TestCase):
    #     def test_1(self):
    #         input = r"""
    #         x, y, z, t: integer;
    #         arr : array [2] of integer;
    #         main: function void(){
    #         }
    #     """
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
    #         main: function void(){
    #             x: integer = 10;
    #             printInteger(x);
    #             y: float = 10.123;
    #             writeFloat(y);
    #         }
    #     """
    #         expect = "1010.123"
    #         self.assertTrue(TestCodeGen.test(input, expect, 506))

    #     def test_7(self):
    #         input = r"""
    #     main: function void(){
    #         printInteger(z);
    #     }
    #     z: integer =  110;
    # """
    #         expect = "110"
    #         self.assertTrue(TestCodeGen.test(input, expect, 507))

    #     def test_8(self):
    #         input = r"""
    #     b: boolean = false;
    #     main: function void(){
    #         printBoolean(b);
    #     }
    # """
    #         expect = "false"
    #         self.assertTrue(TestCodeGen.test(input, expect, 508))

    #     def test_9(self):
    #         input = r"""
    #     t: float = 129.12;
    #     main: function void(){
    #         writeFloat(t);
    #     }
    # """
    #         expect = "129.12"
    #         self.assertTrue(TestCodeGen.test(input, expect, 509))

    #     def test_10(self):
    #         input = r"""
    #     s: string = "Hello";
    #     main: function void(){
    #         printString(s);
    #     }
    # """
    #         expect = "Hello"
    #         self.assertTrue(TestCodeGen.test(input, expect, 510))

    #     def test_11(self):
    #         input = r"""
    #     main: function void(){
    #         s: string = "Hello";
    #         printString(s);
    #     }
    # """
    #         expect = "Hello"
    #         self.assertTrue(TestCodeGen.test(input, expect, 511))

    #     def test_12(self):
    #         input = r"""
    #     main: function void(){
    #         writeFloat(1 + 2.2);
    #         writeFloat(2.2 + 1);
    #         writeFloat(2.2 + 2.2);
    #         printInteger(1 + 2);
    #     }
    # """
    #         expect = "3.23.24.43"
    #         self.assertTrue(TestCodeGen.test(input, expect, 512))

    #     def test_13(self):
    #         input = r"""
    #     main: function void(){
    #         writeFloat(1 - 2.2);
    #         writeFloat(2.2 - 1);
    #         writeFloat(2.2 - 2.2);
    #         printInteger(1 - 2);
    #     }
    # """
    #         expect = "-1.21.20.0-1"
    #         self.assertTrue(TestCodeGen.test(input, expect, 513))

    #     def test_14(self):
    #         input = r"""
    #     main: function void(){
    #         writeFloat(1000 * 2.2);
    #         writeFloat(2.2 * 1000);
    #         writeFloat(2200 * 22.2);
    #         printInteger(10000 * 2);
    #     }
    # """
    #         expect = "2200.02200.048840.020000"
    #         self.assertTrue(TestCodeGen.test(input, expect, 514))

    #     def test_15(self):
    #         input = r"""
    #     main: function void(){
    #         writeFloat(1000 / 2.2);
    #         writeFloat(2.2 / 1000);
    #         writeFloat(2200 / 22.2);
    #         writeFloat(10000 / 2);
    #     }
    # """
    #         expect = "454.545440.002299.09915000.0"
    #         self.assertTrue(TestCodeGen.test(input, expect, 515))

    #     def test_16(self):
    #         input = r"""
    #     main: function void(){
    #         printInteger(1000 % 2);
    #         printInteger(1001 % 2);
    #     }
    # """
    #         expect = "01"
    #         self.assertTrue(TestCodeGen.test(input, expect, 516))

    #     def test_17(self):
    #         input = r"""
    #     main: function void(){
    #         printString("Hello"::" World!");
    #         printString(("Hello"::" World!")::"KietCaoC3a");
    #         printString("KietCaoC3a"::("Hello"::" World!"));
    #         printString(("Kiet"::"CaoC3a")::("Hello"::" World!"));
    #     }
    # """
    #         expect = "Hello World!Hello World!KietCaoC3aKietCaoC3aHello World!KietCaoC3aHello World!"
    #         self.assertTrue(TestCodeGen.test(input, expect, 517))

    #     def test_18(self):
    #         input = r"""
    #     main: function void(){
    #         printBoolean((12 > 20) && (50 <= 100));
    #         printBoolean((12 < 20) && (50 <= 100));
    #         printBoolean((12 <= 12) && (50 > 100));
    #         printBoolean((12 == 12) || (50 != 100));
    #     }
    # """
    #         expect = "falsetruefalsetrue"
    #         self.assertTrue(TestCodeGen.test(input, expect, 518))

    #     def test_19(self):
    #         input = r"""
    #     main: function void(){
    #         printBoolean((12.123 > 20.23) && (50.1123 <= 100.344));
    #         printBoolean((12.23121 < 20.3444) && (50.4444 <= 100));
    #         printBoolean((12 <= 12) && (50 > 100.532));
    #         printBoolean((12 == 12) || (50 != 100));
    #     }
    # """
    #         expect = "falsetruefalsetrue"
    #         self.assertTrue(TestCodeGen.test(input, expect, 519))

    #     def test_20(self):
    #         input = r"""
    #     main: function void(){
    #         a: integer = 10;
    #         b: float = 10.12;
    #         printBoolean(!(!false && true));
    #         printInteger(-(1+3));
    #         printInteger(-1+3);
    #     }
    # """
    #         expect = "false-42"
    #         self.assertTrue(TestCodeGen.test(input, expect, 520))

    #     def test_21(self):
    #         input = r"""
    #     main: function void(){
    #         printBoolean(1.5*2 + 2 - 5.3*2.1 > 3*5 + 2*3/2 - 4*7.2/14 + 1);
    #         printBoolean(1.5*2 + 2 - 5.3*2.1 < 3*5 + 2*3/2 - 4*7.2/14 + 1);

    #         printBoolean(1.5*2 + 2 - 5.3*2.1 == 3*5 + 2*3/2 - 4*7.2/14 + 1);

    #         printBoolean(1.5*2 + 2 - 5.3*2.1 >= 3*5 + 2*3/2 - 4*7.2/14 + 1);
    #         printBoolean(1.5*2 + 2 - 5.3*2.1 <= 3*5 + 2*3/2 - 4*7.2/14 + 1);
    #         printBoolean(1.5*2 + 2 - 5.3*2.1 != 3*5 + 2*3/2 - 4*7.2/14 + 1);
    #     }
    # """
    #         expect = "falsetruetruefalsetruetrue"
    #         self.assertTrue(TestCodeGen.test(input, expect, 521))

    #     def test_22(self):
    #         input = r"""
    #     main: function void(){
    #         printBoolean(1.5*2 + 2 - 5.3*2.1 - (3*5 + 2*3/2 - 4*7.2/14 + 1) > 0);
    #         printBoolean(1.5*2 + 2 - 5.3*2.1 - (3*5 + 2*3/2 - 4*7.2/14 + 1) < 0);
    #         printBoolean(1.5*2 + 2 - 5.3*2.1 - (3*5 + 2*3/2 - 4*7.2/14 + 1) == 0);
    #         printBoolean(1.5*2 + 2 - 5.3*2.1 - (3*5 + 2*3/2 - 4*7.2/14 + 1) >= 0);
    #         printBoolean(1.5*2 + 2 - 5.3*2.1 - (3*5 + 2*3/2 - 4*7.2/14 + 1) <= 0);
    #         printBoolean(1.5*2 + 2 - 5.3*2.1 - (3*5 + 2*3/2 - 4*7.2/14 + 1) != 0);
    #     }
    # """
    #         expect = "falsetruetruefalsetruetrue"
    #         self.assertTrue(TestCodeGen.test(input, expect, 522))

    def test_23(self):
        input = r"""
    arr : array [2] of integer = {0, 1};
    arr1 : array [2, 2] of integer = {{1, 3}, {123, 1238}};
    arr3 : array [2, 3, 2] of integer = {{{1, 3}, {12, 13}, {123, 321}}, {{2, 41}, {123, 123}, {923, 32}}};
    main: function void(){
        printInteger(arr[0]);
        printInteger(arr[1]);
        printInteger(arr1[0, 0]);
        printInteger(arr1[0, 1]);
        printInteger(arr1[1, 0]);
        printInteger(arr1[1, 1]);
        printInteger(arr3[0, 0, 0]);
        printInteger(arr3[0, 0, 1]);
        printInteger(arr3[0, 1, 0]);
        printInteger(arr3[0, 1, 1]);
        printInteger(arr3[0, 2, 0]);
        printInteger(arr3[0, 2, 1]);
        printInteger(arr3[1, 0, 0]);
        printInteger(arr3[1, 0, 1]);
        printInteger(arr3[1, 1, 0]);
        printInteger(arr3[1, 1, 1]);
        printInteger(arr3[1, 2, 0]);
        printInteger(arr3[1, 2, 1]);
    }
"""
        expect = "1238"
        self.assertTrue(TestCodeGen.test(input, expect, 523))
