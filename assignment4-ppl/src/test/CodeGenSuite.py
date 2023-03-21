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

    def test_43(self):
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
        inc: function float(n: integer, delta: integer) {
            n = n + delta;
            for (i = 1, i < n, i+1) {
                for (j = 1, j < n, j+1) {
                    if (i + j >= 5) {
                        return i + j;
                    } else {
                        printInteger(i-j);
                    }
                }
            }
            return 10;
        }
        main: function void() {
            writeFloat(inc(2, 2));
        }
        """
        expect = "0-1-2105.0"
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
                /*printInteger(arr[i]);
                printString("&&");
                printInteger(arr[j]);
                printString("\n");*/
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
