import sys
import os
import subprocess
import unittest
from antlr4 import *

for path in ['./test/', './main/bkool/utils/', './main/bkool/checker/', './main/bkool/codegen/']:
    sys.path.append(path)
# ANTLR_JAR = os.environ.get('ANTLR_JAR')
ANTLR_JAR = './lib/antlr-4.11.1-complete.jar'
TARGET_DIR = '../target'
GENERATE_DIR = 'main/bkool/parser'


def main(argv):
    if len(argv) < 1:
        printUsage()
    elif argv[0] == 'clean':
        subprocess.run(["rm", "-rf", TARGET_DIR + "/*"])

    elif argv[0] == 'test':
        if len(argv) < 2:
            printUsage()
        elif argv[1] == 'CodeGenSuite':
            from CodeGenSuite import CheckCodeGenSuite
            getAndTest(CheckCodeGenSuite)
        else:
            printUsage()
    else:
        printUsage()


def getAndTest(cls):
    suite = unittest.makeSuite(cls)
    test(suite)


def test(suite):
    from pprint import pprint
    from io import StringIO
    stream = StringIO()
    runner = unittest.TextTestRunner(stream=stream)
    result = runner.run(suite)
    print('Tests run ', result.testsRun)
    print('Errors ', result.errors)
    pprint(result.failures)
    stream.seek(0)
    print('Test output\n', stream.read())


def printUsage():
    print("python3 run.py test CodeGenSuite")


if __name__ == "__main__":
    main(sys.argv[1:])
