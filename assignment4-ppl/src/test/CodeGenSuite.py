import unittest
from TestUtils import TestCodeGen
from AST import *


class CheckCodeGenSuite(unittest.TestCase):
    def test_1(self):
        input = r"""
        x, y, z, t: integer;
        arr : array [2] of integer;
        main: function void(){
        }
    """
        expect = ""
        self.assertTrue(TestCodeGen.test(input, expect, 501))

    def test_2(self):
        input = r"""
    x, y, z, t: integer = 10, 1023, 32, 123;
    // arr: array [2] of integer = {10, 1023};
    main: function void(){
    }
"""
        expect = ""
        self.assertTrue(TestCodeGen.test(input, expect, 502))

    def test_3(self):
        input = r"""
    x, y, z, t: integer = 10, 1023, 32, 123;
    g: float;
    main: function void(){
        x: integer = 3;
    }
"""
        expect = ""
        self.assertTrue(TestCodeGen.test(input, expect, 503))

    def test_4(self):
        input = r"""
    main: function void(){
        printInteger(10);
    }
"""
        expect = "10"
        self.assertTrue(TestCodeGen.test(input, expect, 504))

    def test_5(self):
        input = r"""
    main: function void(){
        x: integer = 10;
        printInteger(x);
    }
"""
        expect = "10"
        self.assertTrue(TestCodeGen.test(input, expect, 505))

    def test_6(self):
        input = r"""
        main: function void(){
            x: integer = 10;
            printInteger(x);
            y: float = 10.123;
            writeFloat(y);
        }
    """
        expect = "1010.123"
        self.assertTrue(TestCodeGen.test(input, expect, 506))

    def test_7(self):
        input = r"""
    main: function void(){
        printInteger(z);
    }
    z: integer =  110;
"""
        expect = "110"
        self.assertTrue(TestCodeGen.test(input, expect, 507))

    def test_8(self):
        input = r"""
    b: boolean = false;
    main: function void(){
        printBoolean(b);
    }
"""
        expect = "false"
        self.assertTrue(TestCodeGen.test(input, expect, 508))

    def test_9(self):
        input = r"""
    t: float = 129.12;
    main: function void(){
        writeFloat(t);
    }
"""
        expect = "129.12"
        self.assertTrue(TestCodeGen.test(input, expect, 509))

    def test_10(self):
        input = r"""
    s: string = "Hello";
    main: function void(){
        printString(s);
    }
"""
        expect = "Hello"
        self.assertTrue(TestCodeGen.test(input, expect, 510))

    def test_11(self):
        input = r"""
    main: function void(){
        s: string = "Hello";
        printString(s);
    }
"""
        expect = "Hello"
        self.assertTrue(TestCodeGen.test(input, expect, 511))

    def test_12(self):
        input = r"""
    main: function void(){
        writeFloat(1 + 2.2);
        writeFloat(2.2 + 1);
        writeFloat(2.2 + 2.2);
        printInteger(1 + 2);
    }
"""
        expect = "3.23.24.43"
        self.assertTrue(TestCodeGen.test(input, expect, 512))

    def test_13(self):
        input = r"""
    main: function void(){
        writeFloat(1 - 2.2);
        writeFloat(2.2 - 1);
        writeFloat(2.2 - 2.2);
        printInteger(1 - 2);
    }
"""
        expect = "-1.21.20.0-1"
        self.assertTrue(TestCodeGen.test(input, expect, 513))

    def test_14(self):
        input = r"""
    main: function void(){
        writeFloat(1000 * 2.2);
        writeFloat(2.2 * 1000);
        writeFloat(2200 * 22.2);
        printInteger(10000 * 2);
    }
"""
        expect = "2200.02200.048840.020000"
        self.assertTrue(TestCodeGen.test(input, expect, 514))

    def test_15(self):
        input = r"""
    main: function void(){
        writeFloat(1000 / 2.2);
        writeFloat(2.2 / 1000);
        writeFloat(2200 / 22.2);
        writeFloat(10000 / 2);
    }
"""
        expect = "454.545440.002299.09915000.0"
        self.assertTrue(TestCodeGen.test(input, expect, 515))

    def test_16(self):
        input = r"""
    main: function void(){
        printInteger(1000 % 2);
        printInteger(1001 % 2);
    }
"""
        expect = "01"
        self.assertTrue(TestCodeGen.test(input, expect, 516))

    def test_17(self):
        input = r"""
    main: function void(){
        printString("Hello"::" World!");
        printString(("Hello"::" World!")::"KietCaoC3a");
        printString("KietCaoC3a"::("Hello"::" World!"));
        printString(("Kiet"::"CaoC3a")::("Hello"::" World!"));
    }
"""
        expect = "Hello World!Hello World!KietCaoC3aKietCaoC3aHello World!KietCaoC3aHello World!"
        self.assertTrue(TestCodeGen.test(input, expect, 517))

    def test_18(self):
        input = r"""
    main: function void(){
        printBoolean((12 > 20) && (50 <= 100));
        printBoolean((12 < 20) && (50 <= 100));
        printBoolean((12 <= 12) && (50 > 100));
        printBoolean((12 == 12) || (50 != 100));
    }
"""
        expect = "falsetruefalsetrue"
        self.assertTrue(TestCodeGen.test(input, expect, 518))

    def test_19(self):
        input = r"""
    main: function void(){
        printBoolean((12.123 > 20.23) && (50.1123 <= 100.344));
        printBoolean((12.23121 < 20.3444) && (50.4444 <= 100));
        printBoolean((12 <= 12) && (50 > 100.532));
        printBoolean((12 == 12) || (50 != 100));
    }
"""
        expect = "falsetruefalsetrue"
        self.assertTrue(TestCodeGen.test(input, expect, 519))

    def test_20(self):
        input = r"""
    main: function void(){
        a: integer = 10;
        b: float = 10.12;
        printBoolean(!(!false && true));
        printInteger(-(1+3));
        printInteger(-1+3);
    }
"""
        expect = "false-42"
        self.assertTrue(TestCodeGen.test(input, expect, 520))

    def test_21(self):
        input = r"""
    main: function void(){
        printBoolean(1.5*2 + 2 - 5.3*2.1 > 3*5 + 2*3/2 - 4*7.2/14 + 1);
        printBoolean(1.5*2 + 2 - 5.3*2.1 < 3*5 + 2*3/2 - 4*7.2/14 + 1);

        printBoolean(1.5*2 + 2 - 5.3*2.1 == 3*5 + 2*3/2 - 4*7.2/14 + 1);

        printBoolean(1.5*2 + 2 - 5.3*2.1 >= 3*5 + 2*3/2 - 4*7.2/14 + 1);
        printBoolean(1.5*2 + 2 - 5.3*2.1 <= 3*5 + 2*3/2 - 4*7.2/14 + 1);
        printBoolean(1.5*2 + 2 - 5.3*2.1 != 3*5 + 2*3/2 - 4*7.2/14 + 1);
    }
"""
        expect = "falsetruefalsefalsetruetrue"
        self.assertTrue(TestCodeGen.test(input, expect, 521))

    def test_22(self):
        input = r"""
    main: function void(){
        printBoolean(1.5*2 + 2 - 5.3*2.1 - (3*5 + 2*3/2 - 4*7.2/14 + 1) > 0);
        printBoolean(1.5*2 + 2 - 5.3*2.1 - (3*5 + 2*3/2 - 4*7.2/14 + 1) < 0);
        printBoolean(1.5*2 + 2 - 5.3*2.1 - (3*5 + 2*3/2 - 4*7.2/14 + 1) == 0);
        printBoolean(1.5*2 + 2 - 5.3*2.1 - (3*5 + 2*3/2 - 4*7.2/14 + 1) >= 0);
        printBoolean(1.5*2 + 2 - 5.3*2.1 - (3*5 + 2*3/2 - 4*7.2/14 + 1) <= 0);
        printBoolean(1.5*2 + 2 - 5.3*2.1 - (3*5 + 2*3/2 - 4*7.2/14 + 1) != 0);
    }
"""
        expect = "falsetruefalsefalsetruetrue"
        self.assertTrue(TestCodeGen.test(input, expect, 522))

    def test_23(self):
        input = r"""
    arr : array [2] of integer = {0, 1};
    main: function void(){
        printInteger(arr[0]);
        printInteger(arr[1]);
    }
"""
        expect = "01"
        self.assertTrue(TestCodeGen.test(input, expect, 523))

    def test_24(self):
        input = r"""
    main: function void(){
        arr : array [2] of integer = {0, 1};
        printInteger(arr[0]);
        printInteger(arr[1]);
    }
"""
        expect = "01"
        self.assertTrue(TestCodeGen.test(input, expect, 524))

    def test_25(self):
        input = r"""
    arr1 : array [2, 2] of integer = {{1, 3}, {123, 1238}};
    main: function void(){
        printInteger(arr1[0, 0]);
        printInteger(arr1[0, 1]);
        printInteger(arr1[1, 0]);
        printInteger(arr1[1, 1]);
    }
"""
        expect = "131231238"
        self.assertTrue(TestCodeGen.test(input, expect, 525))

    def test_26(self):
        input = r"""
    main: function void(){
        arr1 : array [2, 2] of integer = {{1, 3}, {123, 1238}};
        printInteger(arr1[0, 0]);
        printInteger(arr1[0, 1]);
        printInteger(arr1[1, 0]);
        printInteger(arr1[1, 1]);
    }
"""
        expect = "131231238"
        self.assertTrue(TestCodeGen.test(input, expect, 526))

    def test_27(self):
        input = r"""
    arr3 : array [2, 3, 2] of integer = {{{1, 3}, {12, 13}, {123, 321}}, {{2, 41}, {123, 123}, {923, 32}}};
    main: function void(){
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
        expect = "13121312332124112312392332"
        self.assertTrue(TestCodeGen.test(input, expect, 527))

    def test_28(self):
        input = r"""
    x: integer = 3 + 100;
    y: float = 100.3243 + 123;
    main: function void(){
        /*printInteger(x);
        writeFloat(y);
        y = 10000;
        printInteger(x);
        writeFloat(y);*/
        x = 6;
        y = x;
        writeFloat(y);
    }
"""
        expect = "6.0"
        self.assertTrue(TestCodeGen.test(input, expect, 528))

    def test_29(self):
        input = r"""
    arr : array [2] of integer = {0, 1};
    arr3 : array [2, 3, 2] of float = {{{1, 3}, {12, 13}, {123, 321}}, {{2, 41}, {123, 123}, {923, 32}}};
    y: float = 100.3243 + 123;
    main: function void(){
        x: integer = 100;
        y = arr[1] + 10 - arr3[1, 2, 0]; // 1 + 10 -32
        writeFloat(y);
    }
"""
        expect = "-912.0"
        self.assertTrue(TestCodeGen.test(input, expect, 529))

    def test_30(self):
        input = r"""
    x: integer = 1;
    y: float = 100.3243 + x;
    arr : array [2] of integer = {0, x};
    main: function void(){
        arr3 : array [2, 3, 2] of float = {{{1, 3}, {12, 13}, {123, 321}}, {{2, 41}, {123, 123}, {923, 32}}};
        arr3[0, 0, 1] = y;
        writeFloat(arr3[0, 0, 1] + arr3[0, 1, 1]);
        writeFloat(arr3[0, 0, x] + arr3[0, 1, arr[1]]);
    }
"""
        expect = "114.3243114.3243"
        self.assertTrue(TestCodeGen.test(input, expect, 530))

    def test_31(self):
        input = """
        main: function void() {
            if (1 < 2) {
                printBoolean(true);
            } else {
                printBoolean(false);
            }
        }
        """
        expect = "true"
        self.assertTrue(TestCodeGen.test(input, expect, 531))

    def test_32(self):
        input = """
        main: function void() {
            if (1 > 2) {
                printBoolean(true);
            } else {
                printBoolean(false);
            }
            printBoolean(false);
        }
        """
        expect = "falsefalse"
        self.assertTrue(TestCodeGen.test(input, expect, 532))

    def test_33(self):
        input = """
        main: function void() {
            if (!(1 > 2)) {
                printBoolean(true);
            } else {
                printBoolean(false);
            }
            printBoolean(false);
        }
        """
        expect = "truefalse"
        self.assertTrue(TestCodeGen.test(input, expect, 533))

    def test_34(self):
        input = """
        main: function void() {
            i: integer = 1;
            x: array[10, 10] of integer;
            if (i % 2 == 0) {
                x[i, 0] = i;
                printInteger(x[i, 0]);
            } else {
                x[0, i] = i + 1;
                printInteger(x[0, i]);
            }
        }
        """
        expect = "2"
        self.assertTrue(TestCodeGen.test(input, expect, 534))

    def test_35(self):
        input = r"""
    x: integer = 1;
    y: float = 100.3243 + x;
    arr : array [2] of integer = {0, x};
    main: function void(){
        arr3 : array [2, 3, 2] of float = {{{1, 3}, {12, 13}, {123, 321}}, {{2, 41}, {123, 123}, {923, 32}}};
        arr[1] = x;
        arr3[0, 1, 1] = arr[1];
        writeFloat(arr3[0, 0, 1]);
        writeFloat(arr3[0, 0, arr[1]]);
        writeFloat(arr3[0, 0, x]);
        writeFloat(arr3[0, 1, x]);
    }
"""
        expect = "3.03.03.01.0"
        self.assertTrue(TestCodeGen.test(input, expect, 535))

    def test_36(self):
        input = """
        main: function void() {
            i: integer = 5;
            x: array[10, 10] of integer = {{101, 202}, {i}};
            printInteger(x[1, 0]);
            if (i % 2 != 0) {
                x[i, 0] = i;
            }
            /*else {
                x[0, i] = i + 1;
            }*/
            printInteger(x[i, 0]);
        }
        """
        expect = "55"
        self.assertTrue(TestCodeGen.test(input, expect, 536))

    def test_37(self):
        input = """
        main: function void() {
            i: integer;
            for (i = 0, i < 10, i + 1){
                printInteger(i);
            }
        }
        """
        expect = "0123456789"
        self.assertTrue(TestCodeGen.test(input, expect, 537))

    def test_38(self):
        input = """
        main: function void() {
            i: integer;
            for (i = 0, i < 10, i + 1){
                printInteger(i);
            }
        }
        """
        expect = "0123456789"
        self.assertTrue(TestCodeGen.test(input, expect, 538))

    def test_39(self):
        input = """
    main: function void() {
        // i, j: integer;
        for (i = 1, i < 2, i+1) {
            for (j = 1, j < 2, j+1) {
                if (i + j >= 2) {
                    printInteger(i+j);
                } else {
                    printInteger(i-j);
                }
            }
        }
    }
        """
        expect = "2"
        self.assertTrue(TestCodeGen.test(input, expect, 539))

    def test_40(self):
        input = """
    main: function void() {
        for (i = 1, i < 3, i+1) {
            for (j = 1, j < 3, j+1) {
                if (i + j >= 2) {
                    printInteger(i+j);
                    break;
                } else {
                    printInteger(i-j);
                }
            }
        }
    }
        """
        expect = "23"
        self.assertTrue(TestCodeGen.test(input, expect, 540))

    def test_41(self):
        input = """
    main: function void() {
        for (i = 1, i < 3, i+1) {
            for (j = 1, j < 3, j+1) {
                if (i + j >= 2) {
                    continue;
                    printInteger(i+j);
                } else {
                    printInteger(i-j);
                }
            }
            printInteger(i);
        }
    }
        """
        expect = "12"
        self.assertTrue(TestCodeGen.test(input, expect, 541))

    def test_42(self):
        input = """
    main: function void() {
        i: integer = 0;
        while(i < 10){
            printInteger(i);
            i = i + 1;
        }
        printInteger(i);
    }
        """
        expect = "012345678910"
        self.assertTrue(TestCodeGen.test(input, expect, 542))

    def test_43(self):
        input = """
        main: function void() {
           writeFloat(5 / 4);
           writeFloat(15 / 4);
           writeFloat(52 / 6);
           writeFloat(56 / 5);
           writeFloat(9 / 12);
           writeFloat(1998 / 46);
           writeFloat(1998 / 54);
           writeFloat(1998 / 87);
           writeFloat(1998 / 42);
           writeFloat(1998 / 16);
           writeFloat(1998 / 19);
           writeFloat(1998 / 24);
        }
    """
        expect = "1.253.758.66666711.20.7543.43478437.022.96551747.57143124.875105.157983.25"
        self.assertTrue(TestCodeGen.test(input, expect, 543))

    def test_43(self):
        input = """
    main: function void() {
        for (i = 1, i < 10, i+1) {
            j : integer = 0;
            while (j < 20) {
                if (i + j >= 20) {
                    break;
                } else {
                    j = j + 1;
                }
            }
            printInteger(j);
        }
    }
        """
        expect = "191817161514131211"
        self.assertTrue(TestCodeGen.test(input, expect, 543))

    def test_44(self):
        input = """
    main: function void() {
        i: integer = 0;
        do{
            j : integer = 0;
            while (j < 20) {
                if (i + j >= 20) {
                    break;
                } else {
                    j = j + 1;
                }
            }
            printInteger(j);
            i = i + 1;
        }while(i < 10);
    }
        """
        expect = "20191817161514131211"
        self.assertTrue(TestCodeGen.test(input, expect, 544))

    def test_45(self):
        input = """
        main: function void() {
            i, nE: integer = 0, 10;
            do {
                for (i = 0, i < nE, i+1)
                    if (nE == 10 + 5)
                        continue;
                    else
                        nE = nE + 1;
                break;
            } while(true);
            printInteger(nE);
        }
        """
        expect = "15"
        self.assertTrue(TestCodeGen.test(input, expect, 545))

    def test_46(self):
        input = """
            x: integer = 65;
            inc: function void(n: integer, delta: integer) {
                n = n + delta;
                printInteger(n);
            }
            main: function void() {
                delta: integer = 3;
                inc(x, delta);
                printInteger(x);
            }
        """
        expect = "6865"
        self.assertTrue(TestCodeGen.test(input, expect, 546))

    def test_47(self):
        input = """
            x: integer = 65;
            fact: function integer (n: integer) {
                if (n == 0) return 1;
                else return n * fact(n - 1);
            }
            inc: function void(n: integer, delta: integer) {
                n = n + delta;
                printInteger(n);
            }
            main: function void() {
                delta: integer = fact(3); // = 3!
                inc(x, delta); // x = 65 -> pass by value
                printInteger(x);
            }
        """
        expect = "7165"
        self.assertTrue(TestCodeGen.test(input, expect, 547))

    def test_48(self):
        input = """
        main: function void() {
            printBoolean(!false);
            printBoolean(!true);
            printBoolean(!!false);
            printBoolean(!!true);
            printBoolean(!!!false);
            printBoolean(!!!true);
            printBoolean(!false && true);
            printBoolean(!true && false);
            printBoolean(!!false && !!!true || false && true);
            printBoolean(!!true || false);
        }
    """
        expect = "truefalsefalsetruetruefalsetruefalsefalsetrue"
        self.assertTrue(TestCodeGen.test(input, expect, 548))

    def test_49(self):
        input = """
        inc: function integer(n: integer, delta: integer) {
            n = n + delta;
            for (i = 1, i < 10, i+1) {
                return i;
            }
            return 10;
        }
        main: function void() {
            printInteger(inc(1, 1));
        }
            """
        expect = "1"
        self.assertTrue(TestCodeGen.test(input, expect, 549))

    def test_50(self):
        input = """
        main: function void() {
            printInteger(5 % 4);
            printInteger(15 % 4);
            printInteger(52 % 6);
            printInteger(56 % 5);
            printInteger(9 % 12);
            printInteger(1998 % 46);
            printInteger(1998 % 54);
            printInteger(1998 % 87);
            printInteger(1998 % 42);
            printInteger(1998 % 16);
            printInteger(1998 % 19);
            printInteger(1998 % 24);
        }
    """
        expect = "1341920084241436"
        self.assertTrue(TestCodeGen.test(input, expect, 550))

    def test_51(self):
        input = """
        inc: function float(n: integer, delta: integer) {
            n = n + delta;
            for (i = 1, i < n, i+1) {
                j: integer = 1;
                while(j < n){
                    if (i + j >= 5) {
                        return i + j;
                    } else {
                        printInteger(i-j);
                    }
                    j = j + 1;
                }
            }
            return 10;
        }
        main: function void() {
            writeFloat(inc(2, 2));
        }
        """
        expect = "0-1-2105.0"
        self.assertTrue(TestCodeGen.test(input, expect, 551))

    def test_52(self):
        input = """
        inc: function float(n: integer, delta: integer) {
            n = n + delta;
            for (i = 1, i < n, i+1) {
                j: integer = 1;
                do{
                    if (i + j >= 5) {
                        return i + j;
                    }
                    j = j + 1;
                }while(j < n);
            }
            return 10;
        }
        main: function void() {
            writeFloat(inc(2, 2));
        }
        """
        expect = "5.0"
        self.assertTrue(TestCodeGen.test(input, expect, 552))

    # Cut
    def test_53(self):
        input = """
        arr: array[100] of integer = {1, 2, 3, 4,  5,  10, -12, 23, 1};
        checkDuplicate: function boolean(ar: array[100] of integer, size: integer) {
          if (size <= 1)
            return true;
          less, greater: array[100] of integer;
          greater_size, less_size: integer  = 0, 0;

          for (i = 1, i < size, i+1) {
            if (ar[i] == ar[0]) {
              return false;
            }

            if (ar[i] < ar[0]) {
              less[less_size] = ar[i];
              less_size = less_size + 1;
            } else {
              greater[greater_size] = ar[i];
              greater_size = greater_size + 1;
            }
          }

          return checkDuplicate(less, less_size) && checkDuplicate(greater, greater_size);
        }

        main: function void() {
            printBoolean(checkDuplicate(arr, 100));
        }
            """
        expect = "false"
        self.assertTrue(TestCodeGen.test(input, expect, 553))

    def test_54(self):
        input = """
        less_zero: boolean = false;
        c: integer = 0;

        printPattern: function void(out n: integer) {
          if (n <= 0) {
            less_zero = true;
          }

          if (less_zero) {
            c = c - 1;
            if (c == -1) {
                printInteger(n);
                return;
            }
            printInteger(c);
            printPattern(n + 5);
          } else {
            c = c + 1;
            printInteger(c);
            printPattern(n - 5);
          }
        }
        main: function void() {
            printPattern(5);
        }
            """
        expect = "105"
        self.assertTrue(TestCodeGen.test(input, expect, 554))

    def test_55(self):
        input = """
        less_zero: boolean = false;
        c: integer = 0;

        printPattern: function void(out n: integer) {
          if (n <= 0) {
            less_zero = true;
          }

          if (less_zero) {
            c = c - 1;
            if (c == -1) {
                printInteger(n);
                return;
            }
            printInteger(c);
            printPattern(n + 5);
          } else {
            c = c + 1;
            printInteger(c);
            printPattern(n - 5);
          }
        }
        main: function void() {
            printPattern(5);
        }
            """
        expect = "105"
        self.assertTrue(TestCodeGen.test(input, expect, 555))

    def test_56(self):
        input = r"""
    checkElements: function boolean (arr: array[100] of integer, n: integer) {
        if ((n > 1000) || (n < 0))
            return false;
        for (i = 0, i < n - 1, i+1) {
            for (j = i + 1, j < n, j+1) {
              if (arr[i] == arr[j])
                  return false;
            }
        }
        return true;
    }
    main: function void() {
        arr   : array [6] of integer = {1, 91, 0, -100, 100, 200};
        printBoolean(checkElements(arr, 6));
    }
            """
        expect = "true"
        self.assertTrue(TestCodeGen.test(input, expect, 556))

    def test_57(self):
        input = r"""
    main: function void() {
        s: string = "Hello World";
        arr   : array [3] of string = {"Cao", "Tuan", "Kiet "};
        /*printString(arr[0]);
        printString(arr[1]);
        printString(arr[2]);*/
        arr[0] = (arr[0]::arr[1])::arr[2];
        printString(arr[0]);
        printString("\n");
        arr[1] = arr[0]::s;
        printString(arr[1]);
    }
            """
        expect = "CaoTuanKiet \nCaoTuanKiet Hello World"
        self.assertTrue(TestCodeGen.test(input, expect, 557))

    def test_58(self):
        input = """
        b: boolean = false;
        main : function void () {
            f : array [5] of boolean = {true, false, true};
            printBoolean(f[0] && f[1] && f[2]);
            f[0] = f[0] || f[1];
            printBoolean(f[0]);
            f[1] = 100 > 10;
            printBoolean(f[1]);
        }
            """
        expect = "falsetruetrue"
        self.assertTrue(TestCodeGen.test(input, expect, 558))

    def test_59(self):
        input = """
        b: boolean = false;
        main : function void () {
            f : array [5] of boolean = {true, false, true};
            printBoolean(f[0] && f[1] && f[2]);
            f[0] = f[0] || f[1];
            printBoolean(f[0]);
            f[1] = 100 > 10;
            printBoolean(f[1]);
        }
            """
        expect = "falsetruetrue"
        self.assertTrue(TestCodeGen.test(input, expect, 559))

    def test_60(self):
        input = """
        foo: function string (inherit a: string, b: float) {
            return "Hello foo";
        }
        foo1: function void (inherit z: string, t: string) inherit foo{
            //super("Hello"::t, 123.123);
            super("Hello", 123.123);
            printString(a);
        }
        /*bar: function void (inherit out x: integer, inherit out y: string) inherit foo1 {
            super("Hello", "!!!!");
            printString(a::z);
        }*/
        main: function void() {
            foo1("CaoTuanKiet", "!!!!");
        }
    """
        expect = "Hello"
        self.assertTrue(TestCodeGen.test(input, expect, 560))

    def test_61(self):
        input = """
        foo: function string (inherit a: string, b: float) {
            return "Hello foo";
        }
        foo1: function void (inherit z: string, t: string) inherit foo{
            super(("Hello"::z)::t, 123.123);
            printString(a);
        }
        main: function void() {
            foo1(" CaoTuanKiet", "!!!!");
        }
    """
        expect = "Hello CaoTuanKiet!!!!"
        self.assertTrue(TestCodeGen.test(input, expect, 561))

    def test_62(self):
        input = """
        foo: function string (inherit a: string, b: float) {
            return "Hello foo";
        }
        foo1: function void (inherit z: string, t: string) inherit foo{
            super(("Hello"::z)::t, 123.123);
            printString(a);
        }
        bar: function void (inherit out x: integer, inherit out y: string) inherit foo1 {
            super("Hello", y);
        }
        main: function void() {
            foo1(" CaoTuanKiet", "!!!!");
        }
    """
        expect = "Hello CaoTuanKiet!!!!"
        self.assertTrue(TestCodeGen.test(input, expect, 562))

    def test_63(self):
        input = """
        foo1: function string (inherit c: string, d: float) {
            return "foo1";
        }
        foo: function string (inherit a: string, b: string) inherit foo1 {
            super("World!"::b, 123.0);
            return "foo";
        }
        bar: function void (inherit x: integer, inherit y: string) inherit foo {
            super("Hello", "Kiet");
            printString(c);
        }
        main : function void () {
            bar(1, "Hello");
        }
            """
        expect = "World!Kiet"
        self.assertTrue(TestCodeGen.test(input, expect, 563))

    def test_64(self):
        input = """
        foo1: function string (inherit c: string, d: float) {
            return "foo1";
        }
        foo: function string (inherit a: string, b: string) inherit foo1 {
            super("World!"::b, 123.0);
            return "foo";
        }
        bar: function void (inherit x: integer, inherit y: string) inherit foo {
            preventDefault();
            c: string = y::" Kiet";
            printString(c);
        }
        main : function void () {
            bar(1, "Hello");
        }
            """
        expect = "Hello Kiet"
        self.assertTrue(TestCodeGen.test(input, expect, 564))

    def test_65(self):
        input = """
        foo1: function string (inherit c: string, d: float) {
            return "foo1";
        }
        foo: function string () inherit foo1 {
            super("World!", 123.0);
            return "foo";
        }
        bar: function void (inherit x: integer, inherit y: string) inherit foo {
            printString(c);
        }
        main : function void () {
            bar(1, "Hello");
        }
            """
        expect = "World!"
        self.assertTrue(TestCodeGen.test(input, expect, 565))

    def test_66(self):
        input = """
        foo: function integer(inherit x: integer){
            return 1;
        }

        foo1: function float() inherit foo{
            super(100);
            return 1;
        }
        main: function void() inherit foo1 {
            printInteger(x);
        }
            """
        expect = "100"
        self.assertTrue(TestCodeGen.test(input, expect, 566))

    def test_67(self):
        input = r"""
        main: function void() {
            b: integer = 10;
            f : array [5] of integer = {b};
            writeFloat(b);
            writeFloat(f[0]);
    }
    """
        expect = "10.010.0"
        self.assertTrue(TestCodeGen.test(input, expect, 567))

    def test_68(self):
        input = r"""
        foo: function string (a: integer, b: string) {
            f : array [5] of string = {b};
            return f[0];
        }
        foo1: function string (a: string, b: integer, inherit c: string) inherit foo{
            super(b, a);
            f : array [5] of string = {a};
            return f[0];
        }
        bar: function void (inherit out a: integer, inherit out b: string) inherit foo1 {
            super("Hello"::b, a, "Hello"::b);
            for (i = 1, i < 10, i + 1)
            {
                writeFloat(a);
            }
            if (a==2)
                return;
            printString(foo(111, "Hello"::b));
            printString(c);
        }
        main: function void() {
            bar(10, "World!");
        }
    """
        expect = "10.010.010.010.010.010.010.010.010.0HelloWorld!HelloWorld!"
        self.assertTrue(TestCodeGen.test(input, expect, 568))

    def test_69(self):
        input = """
        foo1: function integer (a: string, b: integer, inherit c: float, inherit d: boolean) {
            return b + 1;
        }
        foo: function string (a: string, inherit b: integer) inherit foo1{
            super("Hello"::a, 134, 12.0, false);
            f : array [5] of string = {"a"};
            return f[0];
        }
        bar: function void (inherit a: integer, x: string) inherit foo {
            super("Hello"::x, 123);
            writeFloat((a + b) + c);
        }
        main: function void() {
            bar(10, "World!");
        }
    """
        expect = "145.0"
        self.assertTrue(TestCodeGen.test(input, expect, 569))

    def test_70(self):
        input = """
        foo1: function integer (a: string, b: integer, inherit c: float, inherit d: boolean) {
            printString(a);
            return b + 1;
        }
        foo: function string (a: string, inherit b: integer) inherit foo1{
            super("Hello"::a, 134, 12.0, false);
            f : array [5] of string = {"a"};
            return f[0];
        }
        bar: function void (inherit a: integer, x: string) inherit foo {
            super("Hello"::x, 123);
            writeFloat((a + b) + c);
        }
        main: function void() {
            bar(10, "World!");
            printInteger(foo1("", 1, 1.0, false));
        }
    """
        expect = "145.02"
        self.assertTrue(TestCodeGen.test(input, expect, 570))

    def test_71(self):
        input = """
        foo1: function integer (a: string, b: integer, inherit c: float, inherit d: boolean) {
            printString(a);
            return b + 1;
        }
        foo: function string (a: string, inherit b: integer) inherit foo1{
            super("Hello"::a, 134, 12.0, false);
            writeFloat(c);
            f : array [5] of string = {"a"};
            return f[0]::a;
        }
        bar: function void (inherit a: integer, x: string) inherit foo {
            super("Hello"::x, 123);
            writeFloat((a + b) + c);
        }
        main: function void() {
            bar(10, "World!");
            printString(foo("", 1));
            printInteger(foo1("", 1, 1.0, false));
        }
    """
        expect = "145.012.0a2"
        self.assertTrue(TestCodeGen.test(input, expect, 571))

    def test_72(self):
        input = """
        foo1: function integer (a: string, b: integer, inherit c: float, inherit d: boolean) {
            printString(a);
            return b + 1;
        }
        foo: function string (a: string, inherit b: integer) inherit foo1{
            super("Hello"::a, 134, 12.0, false);
            writeFloat(c);
            f : array [5] of string = {"a"};
            return f[0]::a;
        }
        bar: function void (inherit a: integer, x: string) inherit foo {
            super("Hello"::x, 123);
            writeFloat((a + b) + c);
        }
        main: function void() {
            bar(10, "World!");
            printString(foo("", 1));
            printInteger(foo1("", 1, 1.0, false));
        }
    """
        expect = "145.012.0a2"
        self.assertTrue(TestCodeGen.test(input, expect, 572))

    def test_73(self):
        input = """
        count: function boolean(n: integer)
        {
            i: integer;
            c: integer = 0;
            for (i=1,i<n,i+1)
                if (n%i==0)
                    c = c + 1;
            if (c == 2)
                return true;
            else
                return false;
        }
        main: function void() {
            n : integer = 10;
            if (count(n) == true)
                printString("n is prime number");
            else
                printString("n is not prime number");
        }
    """
        expect = "n is not prime number"
        self.assertTrue(TestCodeGen.test(input, expect, 573))

    def test_74(self):
        input = """
        s : string;
        random: function string(n: integer)
        {
            s = "";
            for (i = 0,i < n,i+1)
                s = s::"!";
            return s;
        }
        main: function void() {
            n : integer = 10;
            printString("The random string length n is "::random(n));
        }
    """
        expect = "The random string length n is !!!!!!!!!!"
        self.assertTrue(TestCodeGen.test(input, expect, 574))

    def test_75(self):
        input = r"""
        a: array[10] of integer = {9, 8, 7, 6, 5, 4, 3, 2, 1, 0};
        b: array[10] of integer = {0, 1, 2, 3, 4, 5, 6, 7, 8, 9};
        swap: function void(out a: array[10] of integer, out b: array[10] of integer, n: integer)
        {
            if (n>10)
                return;
            else
            {
                temp,i : integer;
                for (i=0,i<n,i+1)
                {
                    temp=a[i];
                    a[i]=b[i];
                    b[i]=temp;
                }
            }
        }
        main: function void() {
            swap(a, b, 10);
            for(i = 0, i < 10, i + 1){
                printInteger(a[i]);
            }
            for(i = 0, i < 10, i + 1){
                printInteger(b[i]);
            }
        }
    """
        expect = "01234567899876543210"
        self.assertTrue(TestCodeGen.test(input, expect, 575))

    def test_76(self):
        input = r"""
        isPalindrome: function boolean(strs: array[100] of integer, strSize: integer) {
          for (i = 0, i < strSize / 2, i+1) {
            if (strs[i] != strs[strSize-i-1]) {
              return false;
            }
          }
          return true;
        }
        main: function void() {
            strs   : array [5] of integer = {1, 2, 3, 2 ,1};
            if(isPalindrome(strs, 5)) printString("Correct!!!");
            else printString("Wrong!!!");
        }
    """
        expect = "Correct!!!"
        self.assertTrue(TestCodeGen.test(input, expect, 576))

    def test_77(self):
        input = r"""
        gcdIteration: function integer(p: integer, q: integer) {
          while (p * q != 0) {
            if (p > q) {
              p = p % q;
            } else {
              q = q % p;
            }
          }
          return p + q;
        }
        gcdRecursion: function integer(p: integer, q: integer) {
          if (q == 0)
            return p;
          return gcdRecursion(q, p % q);
        }
        main: function void() {
            printInteger(gcdRecursion(10, 15));
            printInteger(gcdIteration(10, 15));
        }
    """
        expect = "55"
        self.assertTrue(TestCodeGen.test(input, expect, 577))

    def test_78(self):
        input = r"""
        n : integer = 5;
        recursiveSearch: function integer(out n: integer, m: integer, arr: array[100] of integer, index: integer) {
          index = index + 1;
          if (index > n) {
            return -1;
          }
          if (arr[index - 1] == m) {
            for (i = index - 1, i < n - 1, i+1) {
              arr[i] = arr[i + 1];
            }
            n = n - 1;
            return index - 1;
          }
          return recursiveSearch(n, m, arr, index);
        }
        main: function void() {
            arr   : array [5] of integer = {1, 91, 0, -100, 100};
            printInteger(recursiveSearch(n, 10, arr, 0));
            printInteger(recursiveSearch(n, -100, arr, 0));
        }
    """
        expect = "-13"
        self.assertTrue(TestCodeGen.test(input, expect, 578))

    def test_79(self):
        input = r"""
        isSymmetry: function boolean(head: array[100] of integer, tail: array[100] of integer, size: integer) {
          for (i = 0, i < size, i+1) {
            if (head[i] != tail[size - i - 1])
              return false;
          }
          return true;
        }
        main: function void() {
            headf, tailf: array [5] of integer = {1, 91, 0, -100, 100}, {10, 1, 1000, -100, 100};
            headt, tailt: array [5] of integer = {1, 91, 0, -100, 100}, {100, -100, 0, 91, 1};
            printBoolean(isSymmetry(headf, tailf, 5));
            printBoolean(isSymmetry(headt, tailt, 5));
        }
    """
        expect = "falsetrue"
        self.assertTrue(TestCodeGen.test(input, expect, 579))

    def test_80(self):
        input = r"""
        findMin: function integer(vals: array[100] of integer, numEls: integer) {
          min: integer = vals[0];
          for (i = 1, i < numEls, i+1) {
            if (vals[i] < min) {
              min = vals[i];
            }
          }
          return min;
        }
        main: function void() {
            arr: array [10] of integer = {1, 91, 0, -100, 100, 10, 1, 1000, -100, 100};
            printInteger(findMin(arr, 10));
        }
    """
        expect = "-100"
        self.assertTrue(TestCodeGen.test(input, expect, 580))

    def test_81(self):
        input = r"""
        findMax: function float(vals: array[100] of integer, numEls: integer) {
          max: integer = vals[0];
          for (i = 1, i < numEls, i+1) {
            if (vals[i] > max) {
              max = vals[i];
            }
          }
          return max;
        }
        main: function void() {
            arr: array [10] of integer = {1, 91, 0, -100, 100, 10, 1, 1000, -100, 100};
            writeFloat(findMax(arr, 10));
        }
    """
        expect = "1000.0"
        self.assertTrue(TestCodeGen.test(input, expect, 581))

    def test_82(self):
        input = r"""
        min_two_nums: function float (a: integer, b: integer) {
            if (a < b) {
                return a;
            }
            return b;
        }
        max_two_nums: function integer (a: integer, b: integer) {
            if (a > b) {
                return a;
            }
            return b;
        }
        main: function void() {
            writeFloat(min_two_nums(-123, 10));
            printInteger(max_two_nums(-123, 10));
        }
    """
        expect = "-123.010"
        self.assertTrue(TestCodeGen.test(input, expect, 582))

    def test_83(self):
        input = r"""
        completeNum: function boolean(N: integer) {
          sum: integer = 0;
          for (i = 1, i < N, i + 1) {
            if (N % i == 0) {
              sum = sum + i;
            }
          }
          if (sum == N) {
            return true;
          }
          return false;
        }
        main: function void() {
            printBoolean(completeNum(6));
            printBoolean(completeNum(10));
        }
    """
        expect = "truefalse"
        self.assertTrue(TestCodeGen.test(input, expect, 583))

    def test_84(self):
        input = r"""
        Checkzero: function boolean(nums: array[100] of integer, size: integer) {
          found: boolean = false;
          for (i = 0, (i < size) && !found, i + 1) {
            if (nums[i] == 0)
              found = true;
          }
          return found;
        }
        main: function void() {
            arr: array [10] of integer = {1, 91, 90, -90, 100, 10, 1, 1000, -100, 100};
            printBoolean(Checkzero(arr, 10));
            arr[0] = 0;
            printBoolean(Checkzero(arr, 10));
        }
    """
        expect = "falsetrue"
        self.assertTrue(TestCodeGen.test(input, expect, 584))

    def test_85(self):
        input = r"""
        Check: function boolean (nums: array[100] of integer, size: integer) {
          count: integer  = 0;
          for (i = 0, i < size, i + 1) {
            if (nums[i] < 0)
              count = count + 1;
          }
          if (count % 2 == 0)
            return true;
          else
            return false;
        }
        main: function void() {
            arr: array [10] of integer = {1, 91, 90, -90, 100, 10, 1, 1000, -100, 100};
            printBoolean(Check(arr, 10));
        }
    """
        expect = "true"
        self.assertTrue(TestCodeGen.test(input, expect, 585))

    def test_86(self):
        input = r"""
    findGCD: function integer (a: integer, b: integer) {
        if(b){
            return findGCD(b, a % b);
        }
        return a;
    }

    findLCM: function float (a: integer, b: integer){
        return (a*b)/findGCD(a, b);
    }

    main : function void () {
        writeFloat(findLCM(144, 12));
        printInteger(findGCD(144, 12));
    }
    """
        expect = "144.012"
        self.assertTrue(TestCodeGen.test(input, expect, 586))

    def test_87(self):
        input = r"""
        Fibonacci: function integer(n: integer) {
            f0,   f1,   fn: integer = 0, 1, 1;
            if (n < 0) {
                return -1;
            }
            if ((n == 0) || (n == 1)) {
                return n;
            } else {
                for (i = 2, i < n, i + 1) {
                  f0 = f1;
                  f1 = fn;
                  fn = f0 + f1;
                }
            }
            return fn;
        }
        main : function void () {
            printInteger(Fibonacci(10));
        }
    """
        expect = "55"
        self.assertTrue(TestCodeGen.test(input, expect, 587))

    def test_88(self):
        input = r"""
        main : function void () {
            nE : integer = 0;
            do {
                if (nE == 10)
                    break;
                else {
                    nE = nE + 1;
                    continue;
                }
            } while(true);
            printInteger(nE);
        }
    """
        expect = "10"
        self.assertTrue(TestCodeGen.test(input, expect, 588))

    def test_89(self):
        input = """
        main: function void() {
            printInteger(--1);
            printInteger(--100);
            writeFloat(--1.0);
            writeFloat(--10000.0);
            printInteger(---1);
            printInteger(---100);
            writeFloat(---1.0);
            writeFloat(---10000.0);
        }
    """
        expect = "11001.010000.0-1-100-1.0-10000.0"
        self.assertTrue(TestCodeGen.test(input, expect, 589))

    def test_90(self):
        input = """
        inc: function float(n: integer, delta: integer) {
            n = n + delta;
            for (i = 1, i < n, i+1) {
                j: integer = 1;
                while(j < n){
                    if (i + j >= 5) {
                        return i + j;
                    } else {
                        printInteger(i-j);
                    }
                    j = j + 1;
                }
            }
            return 10;
        }
        main: function void() {
            writeFloat(inc(2, 2));
        }
        """
        expect = "0-1-2105.0"
        self.assertTrue(TestCodeGen.test(input, expect, 590))

    def test_91(self):
        input = """
    main: function void() {
        for (i = 1, i < 10, i+1) {
            j : integer = 0;
            while (j < 20) {
                if (i + j >= 20) {
                    break;
                } else {
                    j = j + 1;
                }
            }
            printInteger(j);
        }
    }
        """
        expect = "191817161514131211"
        self.assertTrue(TestCodeGen.test(input, expect, 591))

    def test_92(self):
        input = """
        main: function void() {
            writeFloat(1.5*2 + 2 - 5.3*2.1);
            writeFloat(3*5 + 2*3/2 - 4*7.2/14 + 1);
            writeFloat(1.5*2 + 2 - 5.3*2.1 - (3*5 + 2*3/2 - 4*7.2/14 + 1));
        }
    """
        expect = "-6.1316.942858-23.072857"
        self.assertTrue(TestCodeGen.test(input, expect, 592))

    def test_93(self):
        input = """
    main: function void() {
        i: integer = 0;
        do{
            printInteger(i);
            i = i + 1;
        }while(i < 10);

        printInteger(i);
    }
        """
        expect = "012345678910"
        self.assertTrue(TestCodeGen.test(input, expect, 593))

    def test_94(self):
        input = """
        main: function void() {
            writeFloat(-(1.5*2 + 2 - 5.3*2.1 - (3*5 + 2*3/2 - 4*7.2/14 + 1)));
            writeFloat(-(1.5*2 + 2 - 5.3*2.1) - (3*5 + 2*3/2 - 4*7.2/14 + 1));
            writeFloat(--(1.5*2 + 2 - 5.3*2.1) --- (3*5 + 2*3/2 - 4*7.2/14 + 1));
            writeFloat(-(-(-(-(1.5*2 + 2 - 5.3*2.1)))) ---- (3*5 + 2*3/2 - 4*7.2/14 + 1));
        }
    """
        expect = "23.072857-10.812858-23.07285710.812858"
        self.assertTrue(TestCodeGen.test(input, expect, 594))

    def test_95(self):
        input = """
            x: integer = 65;
            fact: function integer (n: integer) {
                if (n == 0) {return 1;}
                else {return n * fact(n - 1);}
            }
            //inc: function void(out n: integer, delta: integer) {
            inc: function void(n: integer, delta: integer) {
                n = n + delta;
                printInteger(n);
            }
            main: function void() {
                /*delta: integer = fact(3); // = 3!
                printInteger(delta);
                inc(x, delta); // x = 65 + 3! -> pass by ref
                printInteger(x);*/

                delta: integer = fact(3); // = 3!
                inc(x, delta); // x = 65 -> pass by value
                printInteger(x);
            }
        """
        expect = "7165"
        self.assertTrue(TestCodeGen.test(input, expect, 595))
