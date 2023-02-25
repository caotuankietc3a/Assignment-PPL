import sys
import os
from antlr4 import *
from antlr4.error.ErrorListener import ConsoleErrorListener
from StaticCheck import StaticChecker
from StaticError import *
from CodeGenerator import CodeGenerator
import subprocess

JASMIN_JAR = "./external/jasmin.jar"
TEST_DIR = "./test/testcases/"
SOL_DIR = "./test/solutions/"


class TestUtil:
    @staticmethod
    def makeSource(inputStr, num):
        filename = TEST_DIR + str(num) + ".txt"
        file = open(filename, "w")
        file.write(inputStr)
        file.close()
        return FileStream(filename)


class NewErrorListener(ConsoleErrorListener):
    INSTANCE = None

    def syntaxError(self, recognizer, offendingSymbol, line, column, msg, e):
        raise SyntaxException("Error on line " + str(line) +
                              " col " + str(column) + ": " + offendingSymbol.text)


NewErrorListener.INSTANCE = NewErrorListener()


class SyntaxException(Exception):
    def __init__(self, msg):
        self.message = msg


class TestCodeGen():
    @staticmethod
    def test(input, expect, num):
        if type(input) is str:
            # inputfile = TestUtil.makeSource(input, num)
            # lexer = Lexer(inputfile)
            # tokens = CommonTokenStream(lexer)
            # parser = Parser(tokens)
            # tree = parser.program()
            # asttree = ASTGeneration().visit(tree)
            pass
        else:
            inputfile = TestUtil.makeSource(str(input), num)
            asttree = input

        TestCodeGen.check(SOL_DIR, asttree, num)

        dest = open(os.path.join(SOL_DIR, str(num) + ".txt"), "r")
        line = dest.read()
        return line == expect

    @staticmethod
    def check(soldir, asttree, num):
        print("num:", num)
        codeGen = CodeGenerator()
        path = os.path.join(soldir, str(num))
        if not os.path.isdir(path):
            os.mkdir(path)
        f = open(os.path.join(soldir, str(num) + ".txt"), "w")
        try:
            codeGen.gen(asttree, path)

            subprocess.call("java  -jar " + JASMIN_JAR + " " + path +
                            "/BKOOLClass.j", shell=True, stderr=subprocess.STDOUT)

            subprocess.run("java -cp ./lib:. BKOOLClass",
                           shell=True, stdout=f, timeout=10)
        except StaticError as e:
            f.write(str(e))
        except subprocess.TimeoutExpired:
            f.write("Time out\n")
        except subprocess.CalledProcessError as e:
            raise RuntimeError("command '{}' return with error (code {}): {}".format(
                e.cmd, e.returncode, e.output))
        finally:
            f.close()
