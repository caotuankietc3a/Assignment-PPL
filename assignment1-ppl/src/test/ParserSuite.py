import unittest
from TestUtils import TestParser


class ParserSuite(unittest.TestCase):
    def test_variable_decl_1(self):
        input = """
a, b, c : boolean;
"""
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 200))

    def test_variable_decl_2(self):
        input = """
a,b,c,d: string;
"""
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 201))

    def test_variable_decl_3(self):
        input = r"""
a,b,c,d: string = "12345", "test", "0000000", "Hello World\n";
"""
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 202))

    def test_variable_decl_4(self):
        input = """
a, b, c : boolean = false, true, false;
"""
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 203))

    def test_variable_decl_5(self):
        input = """
a,   b,   c   : auto;
"""
        expect = "Error on line 2 col 20: ;"
        self.assertTrue(TestParser.test(input, expect, 204))

    def test_variable_decl_6(self):
        input = """
a,   b,   c   : array [2, 3] of int;
"""
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 205))

    def test_variable_decl_7(self):
        input = """
a, b, c : int;
"""
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 206))

    def test_variable_decl_8(self):
        input = """
a,   b,   c   : array [2, 3] of int;
"""
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 207))

    def test_variable_decl_9(self):
        input = """
a,   b,   c   : array[2] of int = {1, 2}, {8, 9};
"""
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 208))

    def test_variable_decl_10(self):
        input = """
a,   b,   c   : array [2] of int = {1, 3}, {9}, {};
"""
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 209))

    def test_variable_decl_11(self):
        input = """
a,   b,   c   : array [2, 3] of int = {{1, 2, 3}, {0, 5, 6}}, {{}, {}}, {{2, 3}, {}};
    """
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 210))

    def test_variable_decl_12(self):
        input = """
found : boolean = true;
is_Num, is_String: string = "", "";
is_String = "TEST";
"""
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 211))

    def test_stmts_1(self):
        input = """
nE : int = 0;
for (i = 0, i < nE, i + 1) {
    if (nE == 10 + 5) {
        return nE;
    }
}
"""
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 212))

    def test_stmts_2(self):
        input = """
nE : int = 0;
for (i = 0, i < nE, i + 1) 
    if (nE == 10 + 5) 
        return nE;
    

"""
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 213))

    def test_stmts_3(self):
        input = """
nE : int = 0;
for (i = 0, i < nE,) 
    if (nE == 10 + 5) 
        return nE;
    else i = i + 1;
"""
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 214))

    def test_stmts_4(self):
        input = """
nE : int = 0;
for (i = 0,,) 
    if (nE == 10 + 5) 
        return nE;
    else i = i + 1;
"""
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 215))

    def test_stmts_5(self):
        input = """
nE : int = 0;
for (,,) 
    if (nE == 10 + 5) 
        return nE;
    else nE = nE + 1;
"""
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 216))

    def test_stmts_6(self):
        input = """
nE : int = 0;
while (true){
    if (nE == 10) 
        break;
    else {
        nE = nE + 1;
        continue;
    }
}
"""
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 217))

    def test_stmts_7(self):
        input = """
nE : int = 0;
do {
    if (nE == 10) 
        break;
    else {
        nE = nE + 1;
        continue;
    }
} while(true);
"""
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 218))

    def test_stmts_8(self):
        input = """
nE : int = 0;
do 
    if (nE == 10) 
        break;
    else {
        nE = nE + 1;
        continue;
    }
 while(true);
"""
        expect = "Error on line 4 col 4: if"
        self.assertTrue(TestParser.test(input, expect, 219))

    def test_functions_1(self):
        input = """
x : int = 65;
fact : function int (n : int) {
    if (n == 0) return 1;
    else return n*fact(n-1);
}
main : function void () {
    delta : int = fact(3);
    inc (x, delta);
    printint(x);
}
inc : function void (out n: int, delta : int) {
n = n + delta;
    }
    """
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 220))

    def test_functions_2(self):
        input = """
x : int = 65;
fact : function int (n : int) {
    if (n == 0) return 1;
    else return n*fact(n-1);
}
main : function void () {
    delta : int = fact(3);
    inc (x, delta);
    printint(x);

    arr : array [2, 3] of int;
    arr[1][2] = 10
}
inc : function void (out n: int, delta : int) {
    nE : int = 0;
    do {
        for (i = 0, i < nE, i + 1) 
            if (nE == 10 + 5) 
                return nE;
            else 
                nE = nE + 1;
            continue;
    } while(true);
}
    """
        expect = "Error on line 14 col 0: }"
        self.assertTrue(TestParser.test(input, expect, 221))

    def test_functions_3(self):
        input = """
x : int = 65;
main : function void () {
    arr : array [2, 3] of int;
    if(check_prime(7)){
        arr[1][2] = 10;
    }
}
check_prime: function boolean (n : int) {
  if (n < 2)
    return false;

  for (i = 2, i <= sqrt(n), i+1) {
    if (n % i == 0)
      return false;
  }
  return true;
}
    """
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 222))

    def test_functions_4(self):
        input = """
x : int = 65;
main : function void () {
    arr : array [2, 3] of int;
    if(check_prime(7)){
        arr[1][2] = Fibonacci(10);
    }

}
Fibonacci: function int(n: int) {
    f0,   f1,   fn: auto = 0, 1, 1;
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
check_prime: function boolean (n : int) {
  if (n < 2)
    return false;

  for (i = 2, i <= sqrt(n), i+1) {
    if (n % i == 0)
      return false;
  }
  return true;
}
    """
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 223))

    def test_functions_5(self):
        input = """
Fibonacci: function int(n: int) {
    f0,   f1,   fn: auto = 0, 1, 1;
    if (n < 0) {
        return -1
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
"""
        expect = "Error on line 6 col 4: }"
        self.assertTrue(TestParser.test(input, expect, 224))

    def test_functions_6(self):
        input = """
Fibonacci: function int(n: int) {
    f0,   f1,   fn: auto = 0, 1, 1;
    if (n < 0) {
        return -1;
    }
    if ((n == 0 || (n == 1)) {
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
"""
        expect = "Error on line 7 col 29: {"
        self.assertTrue(TestParser.test(input, expect, 225))

    def test_functions_7(self):
        input = """
Fibonacci: function int(n: int) {
    f0,   f1,   fn: auto = 0, 1, 1;
    if (n < 0) {
        return -1;
    }
    if ((n == 0) || (n == 1)) {
        return n;
    } else {
        for (i = 2; i < n; i + 1) {
          f0 = f1;
          f1 = fn;
          fn = f0 + f1;
        }
    }
    return fn;
}
"""
        expect = "Error on line 10 col 18: ;"
        self.assertTrue(TestParser.test(input, expect, 226))

    def test_functions_8(self):
        input = """
Fibonacci: function int(n: int) {
    f0,   f1,   fn: auto = 0, 1, 1;
    if (n < 0) {
        return -1;
    }
    if ((n == 0) || (n == 1)) {
        return n;
    } else {
        for (i = 2, i < n, i + 1) {
          f0 = f1,
          f1 = fn,
          fn = f0 + f1,
        }
    }
    return fn;
}
"""
        expect = "Error on line 11 col 17: ,"
        self.assertTrue(TestParser.test(input, expect, 227))

    def test_functions_9(self):
        input = """
check_str_code: function boolean (code : string, size: int) {
    if (code == "")
    return false;
    for (i = 0, i < size, i+ 1) {
        if (!(((code[i] >= "a") && (code[i] <= "z")) ||
              ((code[i] >= "A") && (code[i] <= "Z")))) {
            return false;
        }
    }
    return true;
}
"""
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 228))

    def test_functions_10(self):
        input = """
check_str_code: function boolean (code : string, size: int) {
    if (code == "")
    return false;
    for (i = 0, i < size, i+ 1) {
        if (!(((code[i] >= "a") && (code[i] <= "z")) ||
              ((code[i] >= "A") && (code[i] <= "Z"))) {
            return false;
        }
    }
    return true;
}
"""
        expect = "Error on line 7 col 54: {"
        self.assertTrue(TestParser.test(input, expect, 229))

    def test_functions_11(self):
        input = """
check_str_code: function boolean (code : string, size: int) {
    if (code == "")
    return false;
    for (i = 0, i < size, i + 6 - 3) {
        if (!(((code[i] >= "a") && (code[i] <= "z")) ||
              ((code[i] >= "A") && (code[i] <= "Z")))) {
            break;
        }
    }
    return true;
}
"""
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 230))

    def test_functions_12(self):
        input = """
reverse_string: function string(str: string, size: int) {
    for (i = 0, i < size / 2, i+1) {
        x : string = str[i];
        str[i] = str[size - i - 1];
        str[size - i - 1] = x;
    }
    return str;
}
"""
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 231))

    def test_functions_13(self):
        input = """
reverse_string: function string(str: string, size: int) {
    for (i = 0, i < size / 2, i+1) {
        x : string = str[i];
        str[i] = str[size - i - 1];
        str[size - i - 1] = x;
    }
    return str;
}
main : function void () {
    reverse_string("Hello World!", 12);
}
"""
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 232))

    def test_functions_14(self):
        input = """
Recursive: function void (nums: array[100] of int, size: int, index: int , count: int, sum: int , minjump: int) {
    if (sum >= size) {
        if (minjump > count)
            minjump = count;
    } else {
        for (i = 1, i <= nums[index], i + 1) {
          Recursive(nums, index + i, count + 1, sum + i, minjump);
        }
    }
}
"""
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 233))

    def test_functions_15(self):
        input = """
Recursive: function void (nums: array[100] of int, size: int, index: int , count: int, sum: int , minjump: int) {
    if (sum >= size) {
        if (minjump > count)
            minjump = count;
    } else {
        for (i = 1, i <= nums[index], i + 1) {
          Recursive(nums, index + i, count + 1, sum + i, minjump);
        }
    }
}
main : function void () {
    nums: array[100] of int;
    Recursive(nums, 1 + 2, 1 / 2, 1 % 31, 1, -1);
}
"""
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 234))

    def test_functions_16(self):
        input = """
Recursive: function void (nums: array[100] of int, size: int, index: int , count: int, sum: int , minjump: int) {
    if (sum >= size) {
        if (minjump > count)
            minjump = count;
    } else {
        for (i = 1, i <= nums[index], i + 1) {
          Recursive(nums, index + i, count + 1, sum + i, minjump);
        }
    }
}
main : function void () {
    nums: array[100] of int;
    Recursive(nums, 1 + 2, 1 / 2, 1 % 31, 1, -1);
}
"""
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 235))

    def test_functions_17(self):
        input = """
Recursive: function void (nums: array[100] of int, size: int, index: int , count: int, sum: int , minjump: int) {
    if (sum >= size) {
        nums[10] = sum;
    } else {
        Recursive(nums, index + i, count + 1, sum + i, minjump);
    }
}
main : function void () {
    nums: array[100] of int;
    Recursive(nums, 1 + 2, 1 / 2, 1 % 31, 1, -1);
}
"""
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 236))

    def test_functions_18(self):
        input = """
lookUp: function boolean (name: string, scopeFounded: int) { 
    // Undeclared
    for (, scopeFounded >= 0, scopeFounded-1) {
        if (isExist(name, scopeFounded)) {
            return true; 
        }
    }
    return false;
} 
"""
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 237))

    def test_functions_19(self):
        input = """
lookUp: function boolean (name: string, scopeFounded: int) { 
    // Undeclared
    for (, scopeFounded >= 0, scopeFounded-1) {
        if (isExist(name, scopeFounded)) {
            return true; 
        }
    }
    return false;
} 
main : function void () {
    lookUp("test", 1);
}
"""
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 238))

    def test_functions_20(self):
        input = """
longestSublist: function int (words: array[100] of string, size: int) {
    if(!size) return 0;
    result : int = 1;
    for (i = 0, i < size - 1, i + 1) {
        if (words[i][0] == words[i + 1][0]) {
          pre_result, j: int  = 2 , i + 1;
          while (j < size - 1) {
            if (words[j][0] == words[j + 1][0]) {
              pre_result = pre_result + 1;
              j = j + 1;
            } else {
              break;
            }
          }
          if(pre_result > result) result = pre_result;
        }
    }
    return result;
}
"""
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 239))

    def test_functions_21(self):
        input = """
longestSublist: function int (words: array[100] of string, size: int) {
    if(!size) return 0;
    result : int = 1;
    for (i = 0, i < size - 1, i + 1) {
        if (words[i][0] == words[i + 1][0]) {
          pre_result, j: int  = 2 , i + 1
          while (j < size - 1) {
            if (words[j][0] == words[j + 1][0]) {
              pre_result = pre_result + 1;
              j = j + 1;
            } else {
              break;
            }
          }
          if(pre_result > result) result = pre_result;
        }
    }
    return result;
}
"""
        expect = "Error on line 8 col 10: while"
        self.assertTrue(TestParser.test(input, expect, 240))

    def test_functions_22(self):
        input = """
longestSublist: function int (words: array[100] of string, size: int) {
    if(!size) return 0;
    result : int = 1;
    for (i = 0, i < size - 1, i + 1) {
        if (!(words[i][0] == words[i + 1][0])) {
          pre_result, j: int  = 2 , i + 1;
          while (true) {
            if (words[j][0] != words[j + 1][0]) {
              pre_result = pre_result + 1;
              j = j + 1;
            } else {
              continue;
            }
          }
          if(pre_result > result) result = result / pre_result;
        }
    }
    return result;
}
"""
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 241))

    def test_functions_23(self):
        input = """
equalSumIndex: function int (words: array[100] of string, size: int) {
    if(!size) return 0;
    result : int = 1;
    if(size == 1) return 0;
    sumRight, sumLeft, j: int = 0, 0, 1;

    for (i = 1, i < size, i * 2) {
        sumRight = sumRight + nums[i];
    }

    for (i = 0, j < size, i + 1) {
        sumRight = sumRight - nums[j];
        sumLeft = sumLeft + nums[i];
        if (sumLeft == sumRight) return i+1;
        j = j + 1;
    }
    return -1;
}
"""
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 242))

    def test_functions_24(self):
        input = """
findGCD: function int (a: int, b: int)
{
    if(b){
        return findGCD(b, a % b);
    }
    return a;
}
"""
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 243))

    def test_functions_25(self):
        input = """
n: int = 10;
reverseFactorial: function int (out n: int, i: int) {
    if(n == 1){
        return i - 1;
    }
    if(n % i){
        return -1;
    }
    return reverseFactorial(n / i, i + 1);
}
"""
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 244))

    def test_functions_26(self):
        input = """
n: int = 10;
reverseFactorial: function int (out n: int, i: int) {
    if(n == 1){
        return i - 1;
    }
    if(n % i){
        return -1;
    }
    return reverseFactorial(n / i, i + 1);
}
main : function void () {
    reverseFactorial(n, 2);
}
"""
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 245))

    def test_functions_27(self):
        input = """
findGCD: function int (a: int, b: int) {
  if(b){
    return findGCD(b, a % b);
  }
  return a;
}

findLCM: function int (a: int, b: int){
  return (a*b)/findGCD(a, b);
}

main : function void () {
    findLCM(144, 12);
}
"""
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 246))

    def test_functions_28(self):
        input = """
isZero, no_count : boolean = 0, 0;

printPattern: function void (n: int) {
  if (n <= 0)
    isZero = 1;
  if (isZero) {
    no_count = no_count - 1;
    if (no_count == -1)
      return;
    else {
      print(" ");
    }
    printPattern(n + 5);
  } else {
    print(" ");
    no_count = no_count + 1;
    printPattern(n - 5);
  }
}

main : function void () {
    printPattern(10);
}
"""
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 247))

    def test_functions_29(self):
        input = """
isZero, no_count : boolean = 0, 0;

printPattern: function void (n: int) {
  if (n <= 0)
    isZero = 1;
  if (isZero) {
    no_count --;
    if (no_count == -1)
      return;
    else {
      print(" ");
    }
    printPattern(n + 5);
  } else {
    print(" ");
    no_count = no_count + 1;
    printPattern(n - 5);
  }
}

main : function void () {
    printPattern(10);
}
"""
        expect = "Error on line 8 col 15: ;"
        self.assertTrue(TestParser.test(input, expect, 248))

    def test_functions_29(self):
        input = """
isZero, no_count : boolean = 0, 0;

printPattern: function void (n: int) {
  if (n <= 0)
    isZero = 1;
  if (isZero) {
    no_count = no_count - 1;
    if (no_count = -1)
      return;
    else {
      print(" ");
    }
    printPattern(n + 5);
  } else {
    print(" ");
    no_count = no_count + 1;
    printPattern(n - 5);
  }
}

main : function void () {
    printPattern(10);
}
"""
        expect = "Error on line 9 col 17: ="
        self.assertTrue(TestParser.test(input, expect, 249))

    def test_functions_30(self):
        input = """
countWaysUtil: function int (x: int, n: int, num: int)
{
    // Base cases
    val: int = (x - pow(num, n));
    if (val == 0)
        return 1;
    if (val < 0)
        return 0;

    return countWaysUtil(val, n, num + 1) +
           countWaysUtil(x, n, num + 1);
}

countWaySumOfSquare: function int (x: int)
{
    return countWaysUtil(x, 2, 1);
}
"""
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 250))

    def test_functions_31(self):
        input = """
countWaysUtil: function int (x: int, n: int, num: int)
{
    // Base cases
    val: int = (x - pow(num, n));
    if (val == 0)
        return 1;
    if (val < 0)
        return 0;

    return countWaysUtil(val, n, num + 1) +
           countWaysUtil(x, n, num + 1);
}

countWaySumOfSquare: function int (x: int)
{
    return countWaysUtil(x, 2, 1);
}

main: function void(){
    print(countWaySumOfSquare(100));
}
"""
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 251))

    def test_functions_32(self):
        input = """
countWaysUtil: function int (x: int, n: int, num: int)
{
    // Base cases
    val: int = (x - pow(num, n));
    if (val == 0)
        return 1;
    if (val < 0)
        return 0;

    return countWaysUtil(val, n, num + 1) +
           countWaysUtil(x, n, num + 1);
}

countWaySumOfSquare: function int (x: int)
{
    return countWaysUtil(x, 2, 1);
}

main: function void(){
    print(countWaySumOfSquare(100));
}
"""
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 251))

    def test_functions_33(self):
        input = """
countWaysUtil: function int (x: int, n: int, num: int)
{
    // Base cases
    val: int = (x - pow(num, n));
    if (val == 0);
        return 1;
    if (val < 0)
        return 0;

    return countWaysUtil(val, n, num + 1) +
           countWaysUtil(x, n, num + 1);
}

countWaySumOfSquare: function int (x: int)
{
    return countWaysUtil(x, 2, 1);
}

main: function void(){
    print(countWaySumOfSquare(100));
}
"""
        expect = "Error on line 6 col 17: ;"
        self.assertTrue(TestParser.test(input, expect, 252))

    def test_functions_34(self):
        input = """
buyCar: function int (nums : array [200] of int, length: int, k: int) {
  sort(nums, nums + length);
  result, i: int = 0, 0;
  while ((k > 0) && (k - nums[i] >= 0)) {
    result = result + 1;
    k = k - nums[i];
    i = i + 1;
  }
  return result;
}
"""
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 253))

    def test_functions_35(self):
        input = """
buyCar: function int (nums : array [200] of int, length: int, k: int) {
  sort(nums, nums + length);
  result, i: int = 0, 0;
  while ((k > 0) && (k - nums[i] >= 0)) {
    result = result + 1;
    k = k - nums[i];
    i = i + 1;
  }
  return result;
}
main: function void(){
    nums: array [] of int = {90,30,40,90,20};
    length : int = sizeof(nums)/sizeof(nums[0]);
    print(buyCar(nums, length, 90));
}
"""
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 254))

    def test_functions_36(self):
        input = """
buyCar: function int (nums : array [200] of int, length: int, k: int) {
  sort(nums, nums + length);
  result, i: int = 0, 0;
  while ((k > 0) | (k - nums[i] >= 0)) {
    result = result + 1;
    k = k - nums[i];
    i = i + 1;
  }
  return result;
}
main: function void(){
    nums: array [5] of int = {90,30,40,90,20};
    length : int = sizeof(nums)/sizeof(nums[0]);
    print(buyCar(nums, length, 90));
}
"""
        expect = "|"
        self.assertTrue(TestParser.test(input, expect, 255))

    def test_functions_37(self):
        input = """
consecutiveOnes: function boolean(nums : array [200] of int, size: int) {
    found: boolean = false;
    for (i = 0, i < size,) {
        if (nums[i] == 1) {
            if(found) return false;
            while (i < size) {
                if(nums[i] != 1){
                    found = true;
                    break;
                }
                i = i+1;
            }
        }

        i = i+1;
    }
    return true;
}
"""
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 256))

    def test_functions_38(self):
        input = """
consecutiveOnes: function boolean(nums : array [200] of int, size: int) {
    found: boolean = false;
    for (i = 0; i < size;) {
        if (nums[i] == 1) {
            if(found) return false;
            while (i < size) {
                if(nums[i] != 1){
                    found = true;
                    break;
                }
                i = i+1;
            }
        }

        i = i+1;
    }
    return true;
}
"""
        expect = "Error on line 4 col 14: ;"
        self.assertTrue(TestParser.test(input, expect, 257))

    def test_functions_39(self):
        input = """
consecutiveOnes: function boolean(nums : array [200] of int, size: int) {
    found: boolean = false;
    for (i = 0, i < size,) {
        if (nums[i] == 1) {
            if(found) return false;
            while (i < size) {
                if(nums[i] != 1){
                    found = true;
                    break;
                }
                i += 1;
            }
        }

        i = i+1;
    }
    return true;
}
"""
        expect = "Error on line 12 col 18: +"
        self.assertTrue(TestParser.test(input, expect, 258))

    def test_functions_40(self):
        input = """
consecutiveOnes: function boolean(nums : array [200] of int, size: int) {
    found: boolean = false;
    for (i = 0, i < size,) {
        if (nums[i] == 1) {
            if(found) return false;
            while (i < size) {
                if(nums[i] != 1){
                    found = true;
                    break;
                }
                i = i + 1;
            }
        }

        i = i+1;
    }
    return true;

"""
        expect = "Error on line 20 col 0: <EOF>"
        self.assertTrue(TestParser.test(input, expect, 259))

    def test_functions_41(self):
        input = """
check_str_code: function boolean (code : string, size: int) {
    if (code == "")
        return false;
    for (i = 0, i < size, i+ 1) {
        if (!(((code[i] >= 'a") && (code[i] <= "z")) ||
              ((code[i] >= "A") && (code[i] <= "Z")))) {
            return false;
        }
    }
    return true;
}
"""
        expect = "'"
        self.assertTrue(TestParser.test(input, expect, 260))

    def test_functions_42(self):
        input = """
check_str_code: function boolean (code : string, size: int) {
    if (code == "")
        return false;
    for (i = 0, i < size, i+ 1) {
        if (!(((code[i] >= "a") && (code[i <= "z")) ||
              ((code[i] >= "A") && (code[i] <= "Z")))) {
            return false;
        }
    }
    return true;
}
"""
        expect = "Error on line 6 col 49: )"
        self.assertTrue(TestParser.test(input, expect, 261))

    def test_functions_43(self):
        input = """
reverse_string: function string(str: string, size: int) {
    for (i = 0, i < size / 2, i+1) {
        x : string = str[i];
        str[i] = str[size - i - 1];
        str[size - i - 1] = x;
    }
    return str
}
"""
        expect = "Error on line 9 col 0: }"
        self.assertTrue(TestParser.test(input, expect, 262))

    def test_functions_44(self):
        input = """
reverse_string: function string(str: string, size: int) {
    for (,,) {
        x : string = str[i];
        str[i] = str[size - i - 1];
        str[size - i - 1] = x;
        break
    }
    return str;
}
"""
        expect = "Error on line 8 col 4: }"
        self.assertTrue(TestParser.test(input, expect, 263))

    def test_functions_45(self):
        input = """
void reverse(s: string, from: int, to: int) {
  temp: string = s;
  for (i = 0, i < to - from, i++) {
    s[from + i] = temp[to - 1 - i];
  }
}
"""
        expect = "Error on line 2 col 0: void"
        self.assertTrue(TestParser.test(input, expect, 264))

    def test_functions_46(self):
        input = """
reverse: function void(s: string, from: int, to: int) {
  temp: string = s;
  for (i = 0, i < to - from, i++) {
    s[from + i] = temp[to - 1 - i];
  }
}
"""
        expect = "Error on line 4 col 31: +"
        self.assertTrue(TestParser.test(input, expect, 265))

    def test_functions_47(self):
        input = """
reverse: function void(s: string, from: int, to: int) {
  temp: string = s;
  for (i = 0, i < to - from, i+1) {
    s[from + i] = temp[to - 1 - i];
  }
}
"""
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 266))

    def test_functions_48(self):
        input = """
removeDuplicates: function string (S: string, length: int){
  ans: string;
  push_back(ans, S[0]);
  for (i = 1, i < length; i+1) {

    if (S[i] == back(ans)) {
      pop_back(ans);
    } else {
      push_back(ans, S[i]);
    }
  }

  return ans;
}
"""
        expect = "Error on line 5 col 24: ;"
        self.assertTrue(TestParser.test(input, expect, 267))

    def test_functions_49(self):
        input = """
removeDuplicates: function string (S: string, length: int){
  ans: string;
  push_back(ans, S[0]);
  for (i = 1, i < length, i+1) {

    if (S[i] == back(ans)) {
      pop_back(ans);
    } else {
      push_back(ans, S[i]);
    }
  }

  return ans;
}
"""
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 268))

    def test_functions_50(self):
        input = """
removeDuplicates: function string (S: string, length: int){
  // ans: string;
  push_back(ans, S[0]);
  for (i = 1, i < length, i+1)
    if (S[i] == back(ans)) {
      pop_back(ans);
    } else push_back(ans, S[i]);

  return ans;
}
"""
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 269))

    def test_functions_51(self):
        input = """
midSquare: function int (seed: int) {
  newSeed: int = pow(seed, 2);
  s: string = to_string(newSeed);
  erase(s, begin() + size(s) - 2, end(s));
  return stoi(substr(s, size(s) - 4));
}
"""
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 270))

    def test_functions_52(self):
        input = """
midSquare: function int (seed: int) {
  newSeed: int = pow(seed, 2);
  s: string = to_string(newSeed);
  erase(s, begin() + (int)s.size() - 2, end(s));
  return stoi(substr(s, size(s) - 4));
}
"""
        expect = "Error on line 5 col 22: int"
        self.assertTrue(TestParser.test(input, expect, 271))

    def test_functions_53(self):
        input = """
moduloDivision: function int (seed: int, mod: int) { return seed % mod; }
"""
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 272))

    def test_functions_54(self):
        input = """
moduloDivision function int (seed: int, mod: int) { return seed % mod; }
"""
        expect = "Error on line 2 col 15: function"
        self.assertTrue(TestParser.test(input, expect, 273))

    def test_functions_55(self):
        input = """
long int digitExtraction(seed: int, extractDigits: array[100] of int, size: int) {
  s, strSeed: string = "", to_string(seed);
  for (int i = 0; i < size; i++) {
    s += strSeed[extractDigits[i]];
  }
  return stoi(s);
}
"""
        expect = "Error on line 2 col 5: int"
        self.assertTrue(TestParser.test(input, expect, 274))

    def test_functions_56(self):
        input = """
digitExtraction: function int (seed: int, extractDigits: array[100] of int, size: int) {
  s, strSeed: string = "", to_string(seed);
  for (i = 0, i < size, i+1) {
    s += strSeed[extractDigits[i]];
  }
  return stoi(s);
}
"""
        expect = "Error on line 5 col 7: ="
        self.assertTrue(TestParser.test(input, expect, 275))

    def test_functions_57(self):
        input = """
digitExtraction: function int (seed: int, extractDigits: array[100] of int, size: int) {
  s, strSeed: string = "", to_string(seed);
  for (i = 0, i < size, i+1) {
    s = s + strSeed[extractDigits[i]];
  }
  return stoi(s);
}
"""
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 276))

    def test_functions_58(self):
        input = """
foldShift: function int (key: int, addressSize: int)
{
    x: string = to_string(key);
    sum: int = 0;
  for (i = 0, i < length(x),) {
    s: string = substr(x, i, addressSize);
    i = i + addressSize;
    sum = sum + stoi(s);
  }
  test : int = pow(10, addressSize);
  return sum % (test);
}
"""
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 277))

    def test_functions_59(self):
        input = """
foldShift: function int (key: int, addressSize: int)
{
    x: string = to_string(key)
    sum: int = 0;
  for (i = 0, i < length(x),) {
    s: string = substr(x, i, addressSize);
    i = i + addressSize;
    sum = sum + stoi(s);
  }
  test : int = pow(10, addressSize);
  return sum % (test);
}
"""
        expect = "Error on line 5 col 4: sum"
        self.assertTrue(TestParser.test(input, expect, 278))

    def test_functions_60(self):
        input = """
foldShift: function int (key: int, addressSize: int)
{
    x: string = to_string(key);
    sum: int = 0;
  for (i = 0, i < length(x)) {
    s: string = substr(x, i, addressSize);
    i = i + addressSize;
    sum = sum + stoi(s);
  }
  test : int = pow(10, addressSize);
  return sum % (test);
}
"""
        expect = "Error on line 6 col 27: )"
        self.assertTrue(TestParser.test(input, expect, 279))

    def test_functions_61(self):
        input = """
foldShift: function int (key: int, addressSize: int)
{
    x: string = to_string(key);
    sum: int = 0;
  for (i = 0, i < length(x),) {
    s: string = substr(x, i, addressSize);
    i = i + addressSize;
    sum = sum + stoi(s);
  }
  int test = pow(10, addressSize);
  return sum % (test);
}
"""
        expect = "Error on line 11 col 2: int"
        self.assertTrue(TestParser.test(input, expect, 280))

    def test_functions_62(self):
        input = """
rotation: function int (key: int, addressSize: int)
{
  x: string = to_string(key);
  temp: string = x[x.length() - 1];
  for (int i = (int)x.length() - 1; i > 0; i--) {
    x[i] = x[i - 1];
  }
  x[0] = temp;
    return foldShift(stoll(x), addressSize);
}
"""
        expect = "Error on line 5 col 20: ."
        self.assertTrue(TestParser.test(input, expect, 281))

    def test_functions_63(self):
        input = """
rotation: function int (key: int, addressSize: int)
{
  x: string = to_string(key);
  temp: string = x[length(x) - 1];
  for (i = length(x) - 1, i > 0, i-1) {
    x[i] = x[i - 1];
  }
  x[0] = temp;
  return foldShift(stoll(x), addressSize);
}
"""
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 282))

    def test_functions_64(self):
        input = """
left: function int (i: int) { return (2 * i + 1); }
right: function int (i: int) { return (2 * i + 2); }
parent: function int (i: int) { return (i - 1) / 2; }
swap: function void(x: int,y: int) {
  k: int = x;
  x = y
  y = k;
}
"""
        expect = "Error on line 8 col 2: y"
        self.assertTrue(TestParser.test(input, expect, 283))

    def test_functions_65(self):
        input = """
left: function int (i: int) { return (2 * i + 1); }
right: function int (i: int) { return (2 * i + 2); }
parent: function int (i: int) { return (i - 1) / 2; }
swap: function void(x: int,y: int) {
  k: int = x;
  x = y;
  y = k;
}
"""
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 284))

    def test_functions_66(self):
        input = """
left: function int (i: int) { return (2 * i + 1); }
right: function int (i: int) { return (2 * i + 2); }
parent: function int (i: int) { return (i - 1) / 2; }
swap: function void(x: int,y: int) {
  k: int = x;
  x = y;
  y = k;
}
reheapUp: function void(maxHeap: array[100] of int, numberOfElements: int , index: int ) {
  if (index < numberOfElements) {
    if (index && maxHeap[parent(index)] < maxHeap[index]) {
      swap(maxHeap[index], maxHeap[parent(index)]);
      reheapUp(maxHeap, numberOfElements, parent(index));
    }
  }

}
"""
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 285))

    def test_functions_67(self):
        input = """
left: function int (i: int) { return (2 * i + 1); }
right: function int (i: int) { return (2 * i + 2); }
parent: function int (i: int) { return (i - 1) / 2; }
swap: function void(x: int,y: int) {
  k: int = x;
  x = y;
  y = k;
}
reheapUp: function void(maxHeap: array[100] of int, numberOfElements: int , index: int ) {
  if (index < numberOfElements) {
    if (index && maxHeap[parent(index)] < maxHeap[index]) {
      swap(maxHeap[index], maxHeap[parent(index)]);
      reheapUp(maxHeap numberOfElements, parent(index));
    }
  }

}
"""
        expect = "Error on line 14 col 23: numberOfElements"
        self.assertTrue(TestParser.test(input, expect, 286))

    def test_functions_68(self):
        input = """
left: function int (i: int) { return (2 * i + 1); }
right: function int (i: int) { return (2 * i + 2); }
parent: function int (i: int) { return (i - 1) / 2; }
swap: function void(x: int,y: int) {
  k: int = x;
  x = y;
  y = k;
}
reheapDown: function void (maxHeap: array[100] of int, numberOfElements: int , index: int ) {
    if (index < numberOfElements) {
          l, r, largest: int = left(index), right(index), index;
          if (l < numberOfElements && maxHeap[l] > maxHeap[index]) {
            largest = l;
          }
        
          if (r < numberOfElements && maxHeap[r] > maxHeap[largest]) {
            largest = r;
          }
        
          if (largest != index) {
            swap(maxHeap[index], maxHeap[largest]);
            reheapDown(maxHeap, numberOfElements, largest);
          }
    }
  
}
"""
        expect = "Error on line 13 col 49: >"
        self.assertTrue(TestParser.test(input, expect, 287))

    def test_functions_69(self):
        input = """
left: function int (i: int) { return (2 * i + 1); }
right: function int (i: int) { return (2 * i + 2); }
parent: function int (i: int) { return (i - 1) / 2; }
swap: function void(x: int,y: int) {
  k: int = x;
  x = y;
  y = k;
}
reheapDown: function void (maxHeap: array[100] of int, numberOfElements: int , index: int ) {
    if (index < numberOfElements) {
          l, r, largest: int = left(index), right(index), index;
          if ((l < numberOfElements) && (maxHeap[l] > maxHeap[index])) {
            largest = l;
          }
        
          if ((r < numberOfElements) && (maxHeap[r] > maxHeap[largest])) {
            largest = r;
          }
        
          if (largest != index) {
            swap(maxHeap[index], maxHeap[largest]);
            reheapDown(maxHeap, numberOfElements, largest);
          }
    }
  
}
"""
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 288))

    def test_functions_70(self):
        input = """
left: function int (i: int) { return (2 * i + 1); }
right: function int (i: int) { return (2 * i + 2); }
parent: function int (i: int) { return (i - 1) / 2; }
swap: function void(x: int,y: int) {
  k: int = x;
  x = y;
  y = k;
}
reheapDown: function void (maxHeap: array[100] of int, numberOfElements: int , index: int ) {
    if (index < numberOfElements) {
          l, r, largest: int = left(index)right(index), index;
          if ((l < numberOfElements) && (maxHeap[l] > maxHeap[index])) {
            largest = l;
          }
        
          if ((r < numberOfElements) && (maxHeap[r] > maxHeap[largest])) {
            largest = r;
          }
        
          if (largest != index) {
            swap(maxHeap[index], maxHeap[largest]);
            reheapDown(maxHeap, numberOfElements, largest);
          }
    }
  
}
"""
        expect = "Error on line 12 col 42: right"
        self.assertTrue(TestParser.test(input, expect, 289))

    def test_functions_71(self):
        input = """
buildMaxHeap: function void (arr: array[100] of int, numOfEl: int) {
    for (i = numOfEl / 2 - 1, i >= 0, i-1) {
      heapify(arr, numOfEl, i);
    }
}
"""
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 290))

    def test_functions_72(self):
        input = """
buildMaxHeap: function (arr: array[100] of int, numOfEl: int) {
    for (i = numOfEl / 2 - 1, i >= 0, i-1) {
      heapify(arr, numOfEl, i);
    }
}
"""
        expect = "Error on line 2 col 23: ("
        self.assertTrue(TestParser.test(input, expect, 291))

    def test_functions_73(self):
        input = """
buildMaxHeap: function void (arr: array[100] of int, numOfEl: int) {
    for (i = numOfEl / 2 - 1, i >= 0, i-1) {
      heapify(arr, numOfEl, i);
    }
}
heapSort: function void (start: array[] of int, end: array[100] of int) {
    numOfEl: int = end - start;
    buildMaxHeap(start, numOfEl);
    for (i = numOfEl - 1, i >= 0, i-1) {
      temp: int = start[0];
      start[0] = start[i];
      start[i] = temp;
      heapify(start, i, 0);
    }
    printArray(start, end);
  }
"""
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 292))

    def test_functions_74(self):
        input = """
buildMaxHeap: function void (arr: array[100] of int, numOfEl: int) {
    for (i = numOfEl / 2 - 1, i >= 0, i-1) {
      heapify(arr, numOfEl, i);
    }
}
heapSort: function void (start: array[] of int, end: array[100] of int) {
    numOfEl: int = end - start;
    buildMaxHeap(start, numOfEl);
    for (i = numOfEl - 1, i >= 0, i-1) {
      temp: int = start[0];
      start[0] = start[i];
      start[i] = temp;
      heapify(start, i, 0);
    }
    printArray(start; end);
  }
"""
        expect = "Error on line 16 col 20: ;"
        self.assertTrue(TestParser.test(input, expect, 293))

    def test_functions_75(self):
        input = """
heapify: function void(arr: array[100] of int, numOfEl: int, i: int) {
    left, right, largest: int = 2 * i + 1, 2 * i + 2, i;
    if ((left < numOfEl) && (arr[left] > arr[largest]))
      largest = left;

    if ((right < numOfEl) && (arr[right] > arr[largest]))
      largest = right;

    // Swap and continue heapifying if root is not largest
    if (largest != i) {
      temp: int = arr[i];
      arr[i] = arr[largest];
      arr[largest] = temp;
      heapify(arr, numOfEl, largest);
    }
  }
"""
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 294))

    def test_functions_76(self):
        input = """
heapify: function void(arr: array[100] of int, numOfEl: int, i: int) {
    left, right, largest: int = 2 * i + 1, 2 * i + 2, i;
    if ((left < numOfEl) && (arr[left] > arr[largest]))
      largest = left;

    if ((right < numOfEl) && (arr[right] > arr[largest]))
      largest = right;

    // Swap and continue heapifying if root is not largest
    if (largest != i) {
      temp: int = arr[i];
      arr[i] = arr[largest;
      arr[largest] = temp;
      heapify(arr, numOfEl, largest);
    }
  }
"""
        expect = "Error on line 13 col 26: ;"
        self.assertTrue(TestParser.test(input, expect, 295))

    def test_functions_77(self):
        input = """
heapify: function void(arr: array[100] of int, numOfEl: int, i: int) {
    left, right, largest: int = 2 * i + 1, 2 * i + 2, i;
    if ((left < numOfEl) && (arr[left] > arr[largest]))
      largest = left;

    if ((right < numOfEl) && (arr[right] > arr[largest]))
      largest = right;

    // Swap and continue heapifying if root is not largest
    if (largest != i) {
      temp: int = arr[i];
      arr[i] = arr[largest]
      arr[largest] = temp;
      heapify(arr, numOfEl, largest);
    }
  }
"""
        expect = "Error on line 14 col 6: arr"
        self.assertTrue(TestParser.test(input, expect, 296))

    def test_functions_78(self):
        input = """
minWaitingTime: function int (n: int, arrvalTime: array[] of int, completeTime: array[] of int) {
    sort(a, a + n, greater());
    minTime : int = 0;

    // Iterate through the groups
    for (i = 0, i < n, i + k)
        // Update the time taken for each group
        minTime = minTime + (2 * a[i]);

    // Return the total time taken
    return minTime;
}
"""
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 297))

    def test_functions_79(self):
        input = """
minWaitingTime: function int (n: int, arrvalTime: array[1000] of int, completeTime: array[] of int) {
    sort(a, a + n, greater());
    minTime : int = 0

    // Iterate through the groups
    for (i = 0, i < n, i + k)
        // Update the time taken for each group
        minTime = minTime + (2 * a[i]);

    // Return the total time taken
    return minTime;
}
"""
        expect = "Error on line 7 col 4: for"
        self.assertTrue(TestParser.test(input, expect, 298))

    def test_functions_80(self):
        input = """
minWaitingTime: function int (n: int, arrvalTime: array[1000] of int, completeTime: array[] of int) {
    sort(a, a + n, greater());
    minTime : int = 0;

    // Iterate through the groups
    for (i = 0, i < n, i + k)
        // Update the time taken for each group
        minTime = minTime + (2 * a[i]);

    // Return the total time taken
    return minTime
}
"""
        expect = "Error on line 13 col 0: }"
        self.assertTrue(TestParser.test(input, expect, 299))
