# Generated from main/mt22/parser/MT22.g4 by ANTLR 4.11.1
# encoding: utf-8
from antlr4 import *
from io import StringIO
import sys
if sys.version_info[1] > 5:
	from typing import TextIO
else:
	from typing.io import TextIO

def serializedATN():
    return [
        4,1,59,437,2,0,7,0,2,1,7,1,2,2,7,2,2,3,7,3,2,4,7,4,2,5,7,5,2,6,7,
        6,2,7,7,7,2,8,7,8,2,9,7,9,2,10,7,10,2,11,7,11,2,12,7,12,2,13,7,13,
        2,14,7,14,2,15,7,15,2,16,7,16,2,17,7,17,2,18,7,18,2,19,7,19,2,20,
        7,20,2,21,7,21,2,22,7,22,2,23,7,23,2,24,7,24,2,25,7,25,2,26,7,26,
        2,27,7,27,2,28,7,28,2,29,7,29,2,30,7,30,2,31,7,31,2,32,7,32,2,33,
        7,33,2,34,7,34,2,35,7,35,2,36,7,36,2,37,7,37,2,38,7,38,2,39,7,39,
        2,40,7,40,2,41,7,41,2,42,7,42,2,43,7,43,2,44,7,44,2,45,7,45,2,46,
        7,46,2,47,7,47,2,48,7,48,2,49,7,49,2,50,7,50,2,51,7,51,2,52,7,52,
        1,0,1,0,1,0,1,1,1,1,1,1,1,1,3,1,114,8,1,1,2,1,2,1,2,3,2,119,8,2,
        1,3,1,3,3,3,123,8,3,1,3,1,3,1,4,1,4,1,4,1,4,1,4,3,4,132,8,4,1,4,
        1,4,3,4,136,8,4,1,4,1,4,1,4,1,5,1,5,1,5,1,5,1,5,5,5,146,8,5,10,5,
        12,5,149,9,5,1,6,1,6,1,6,1,6,1,6,1,6,1,6,3,6,158,8,6,1,6,1,6,3,6,
        162,8,6,1,6,1,6,1,6,3,6,167,8,6,1,6,1,6,1,7,1,7,1,7,1,7,1,7,3,7,
        176,8,7,1,8,3,8,179,8,8,1,8,3,8,182,8,8,1,8,1,8,1,8,1,8,1,8,3,8,
        189,8,8,1,9,1,9,1,10,1,10,1,11,1,11,1,11,1,11,1,11,3,11,200,8,11,
        1,12,1,12,1,12,1,12,1,12,3,12,207,8,12,1,13,1,13,1,13,1,13,1,13,
        1,13,5,13,215,8,13,10,13,12,13,218,9,13,1,14,1,14,1,14,1,14,1,14,
        1,14,5,14,226,8,14,10,14,12,14,229,9,14,1,15,1,15,1,15,1,15,1,15,
        1,15,5,15,237,8,15,10,15,12,15,240,9,15,1,16,1,16,1,16,3,16,245,
        8,16,1,17,1,17,1,17,3,17,250,8,17,1,18,1,18,1,18,3,18,255,8,18,1,
        19,1,19,1,19,1,19,1,20,1,20,1,20,1,20,1,20,3,20,266,8,20,1,21,1,
        21,1,21,3,21,271,8,21,1,22,1,22,1,22,3,22,276,8,22,1,22,1,22,1,23,
        1,23,1,23,1,23,1,23,3,23,285,8,23,1,24,1,24,1,24,1,24,1,24,1,24,
        1,24,1,24,3,24,295,8,24,1,25,1,25,1,25,1,25,1,25,3,25,302,8,25,1,
        26,1,26,3,26,306,8,26,1,26,1,26,1,26,1,26,3,26,312,8,26,3,26,314,
        8,26,1,27,1,27,1,27,1,27,1,27,1,27,1,27,1,27,1,27,1,27,3,27,326,
        8,27,1,28,1,28,1,28,1,28,1,28,1,29,1,29,1,29,3,29,336,8,29,1,30,
        1,30,1,31,1,31,1,31,1,31,1,31,1,31,1,31,3,31,347,8,31,1,32,1,32,
        1,32,1,32,1,32,1,32,1,32,1,32,1,32,1,32,1,33,1,33,1,33,1,33,1,34,
        1,34,1,35,1,35,1,36,1,36,1,36,1,36,1,36,1,36,1,37,1,37,1,37,1,37,
        1,37,1,37,1,37,1,37,1,38,1,38,1,38,1,39,1,39,1,39,1,40,1,40,3,40,
        389,8,40,1,40,1,40,1,41,1,41,1,41,1,42,1,42,3,42,398,8,42,1,42,1,
        42,1,43,1,43,1,44,1,44,1,45,1,45,1,46,1,46,1,47,1,47,1,48,1,48,1,
        49,1,49,1,50,1,50,1,50,1,50,1,50,1,50,1,50,1,51,1,51,1,51,5,51,426,
        8,51,10,51,12,51,429,9,51,1,52,1,52,1,52,1,52,3,52,435,8,52,1,52,
        0,3,26,28,30,53,0,2,4,6,8,10,12,14,16,18,20,22,24,26,28,30,32,34,
        36,38,40,42,44,46,48,50,52,54,56,58,60,62,64,66,68,70,72,74,76,78,
        80,82,84,86,88,90,92,94,96,98,100,102,104,0,4,1,0,9,14,1,0,7,8,1,
        0,1,2,1,0,3,5,439,0,106,1,0,0,0,2,113,1,0,0,0,4,118,1,0,0,0,6,120,
        1,0,0,0,8,126,1,0,0,0,10,140,1,0,0,0,12,150,1,0,0,0,14,175,1,0,0,
        0,16,178,1,0,0,0,18,190,1,0,0,0,20,192,1,0,0,0,22,199,1,0,0,0,24,
        206,1,0,0,0,26,208,1,0,0,0,28,219,1,0,0,0,30,230,1,0,0,0,32,244,
        1,0,0,0,34,249,1,0,0,0,36,254,1,0,0,0,38,256,1,0,0,0,40,265,1,0,
        0,0,42,270,1,0,0,0,44,272,1,0,0,0,46,284,1,0,0,0,48,294,1,0,0,0,
        50,301,1,0,0,0,52,313,1,0,0,0,54,325,1,0,0,0,56,327,1,0,0,0,58,335,
        1,0,0,0,60,337,1,0,0,0,62,339,1,0,0,0,64,348,1,0,0,0,66,358,1,0,
        0,0,68,362,1,0,0,0,70,364,1,0,0,0,72,366,1,0,0,0,74,372,1,0,0,0,
        76,380,1,0,0,0,78,383,1,0,0,0,80,386,1,0,0,0,82,392,1,0,0,0,84,395,
        1,0,0,0,86,401,1,0,0,0,88,403,1,0,0,0,90,405,1,0,0,0,92,407,1,0,
        0,0,94,409,1,0,0,0,96,411,1,0,0,0,98,413,1,0,0,0,100,415,1,0,0,0,
        102,422,1,0,0,0,104,434,1,0,0,0,106,107,3,2,1,0,107,108,5,0,0,1,
        108,1,1,0,0,0,109,110,3,4,2,0,110,111,3,2,1,0,111,114,1,0,0,0,112,
        114,3,4,2,0,113,109,1,0,0,0,113,112,1,0,0,0,114,3,1,0,0,0,115,119,
        3,8,4,0,116,119,3,12,6,0,117,119,3,16,8,0,118,115,1,0,0,0,118,116,
        1,0,0,0,118,117,1,0,0,0,119,5,1,0,0,0,120,122,5,20,0,0,121,123,3,
        50,25,0,122,121,1,0,0,0,122,123,1,0,0,0,123,124,1,0,0,0,124,125,
        5,21,0,0,125,7,1,0,0,0,126,127,3,10,5,0,127,131,5,25,0,0,128,132,
        3,104,52,0,129,132,3,100,50,0,130,132,3,98,49,0,131,128,1,0,0,0,
        131,129,1,0,0,0,131,130,1,0,0,0,132,135,1,0,0,0,133,134,5,26,0,0,
        134,136,3,48,24,0,135,133,1,0,0,0,135,136,1,0,0,0,136,137,1,0,0,
        0,137,138,6,4,-1,0,138,139,5,24,0,0,139,9,1,0,0,0,140,141,5,55,0,
        0,141,147,6,5,-1,0,142,143,5,22,0,0,143,144,5,55,0,0,144,146,6,5,
        -1,0,145,142,1,0,0,0,146,149,1,0,0,0,147,145,1,0,0,0,147,148,1,0,
        0,0,148,11,1,0,0,0,149,147,1,0,0,0,150,151,5,55,0,0,151,152,5,25,
        0,0,152,157,5,40,0,0,153,158,3,104,52,0,154,158,3,96,48,0,155,158,
        3,98,49,0,156,158,3,100,50,0,157,153,1,0,0,0,157,154,1,0,0,0,157,
        155,1,0,0,0,157,156,1,0,0,0,158,159,1,0,0,0,159,161,5,16,0,0,160,
        162,3,14,7,0,161,160,1,0,0,0,161,162,1,0,0,0,162,163,1,0,0,0,163,
        166,5,17,0,0,164,165,5,52,0,0,165,167,5,55,0,0,166,164,1,0,0,0,166,
        167,1,0,0,0,167,168,1,0,0,0,168,169,3,18,9,0,169,13,1,0,0,0,170,
        171,3,16,8,0,171,172,5,22,0,0,172,173,3,14,7,0,173,176,1,0,0,0,174,
        176,3,16,8,0,175,170,1,0,0,0,175,174,1,0,0,0,176,15,1,0,0,0,177,
        179,5,52,0,0,178,177,1,0,0,0,178,179,1,0,0,0,179,181,1,0,0,0,180,
        182,5,49,0,0,181,180,1,0,0,0,181,182,1,0,0,0,182,183,1,0,0,0,183,
        184,5,55,0,0,184,188,5,25,0,0,185,189,3,104,52,0,186,189,3,100,50,
        0,187,189,3,98,49,0,188,185,1,0,0,0,188,186,1,0,0,0,188,187,1,0,
        0,0,189,17,1,0,0,0,190,191,3,84,42,0,191,19,1,0,0,0,192,193,3,22,
        11,0,193,21,1,0,0,0,194,195,3,24,12,0,195,196,5,15,0,0,196,197,3,
        24,12,0,197,200,1,0,0,0,198,200,3,24,12,0,199,194,1,0,0,0,199,198,
        1,0,0,0,200,23,1,0,0,0,201,202,3,26,13,0,202,203,7,0,0,0,203,204,
        3,26,13,0,204,207,1,0,0,0,205,207,3,26,13,0,206,201,1,0,0,0,206,
        205,1,0,0,0,207,25,1,0,0,0,208,209,6,13,-1,0,209,210,3,28,14,0,210,
        216,1,0,0,0,211,212,10,2,0,0,212,213,7,1,0,0,213,215,3,28,14,0,214,
        211,1,0,0,0,215,218,1,0,0,0,216,214,1,0,0,0,216,217,1,0,0,0,217,
        27,1,0,0,0,218,216,1,0,0,0,219,220,6,14,-1,0,220,221,3,30,15,0,221,
        227,1,0,0,0,222,223,10,2,0,0,223,224,7,2,0,0,224,226,3,30,15,0,225,
        222,1,0,0,0,226,229,1,0,0,0,227,225,1,0,0,0,227,228,1,0,0,0,228,
        29,1,0,0,0,229,227,1,0,0,0,230,231,6,15,-1,0,231,232,3,32,16,0,232,
        238,1,0,0,0,233,234,10,2,0,0,234,235,7,3,0,0,235,237,3,32,16,0,236,
        233,1,0,0,0,237,240,1,0,0,0,238,236,1,0,0,0,238,239,1,0,0,0,239,
        31,1,0,0,0,240,238,1,0,0,0,241,242,5,6,0,0,242,245,3,32,16,0,243,
        245,3,34,17,0,244,241,1,0,0,0,244,243,1,0,0,0,245,33,1,0,0,0,246,
        247,5,2,0,0,247,250,3,34,17,0,248,250,3,36,18,0,249,246,1,0,0,0,
        249,248,1,0,0,0,250,35,1,0,0,0,251,252,5,55,0,0,252,255,3,38,19,
        0,253,255,3,40,20,0,254,251,1,0,0,0,254,253,1,0,0,0,255,37,1,0,0,
        0,256,257,5,18,0,0,257,258,3,50,25,0,258,259,5,19,0,0,259,39,1,0,
        0,0,260,266,3,42,21,0,261,262,5,16,0,0,262,263,3,20,10,0,263,264,
        5,17,0,0,264,266,1,0,0,0,265,260,1,0,0,0,265,261,1,0,0,0,266,41,
        1,0,0,0,267,271,3,46,23,0,268,271,3,44,22,0,269,271,5,55,0,0,270,
        267,1,0,0,0,270,268,1,0,0,0,270,269,1,0,0,0,271,43,1,0,0,0,272,273,
        5,55,0,0,273,275,5,16,0,0,274,276,3,50,25,0,275,274,1,0,0,0,275,
        276,1,0,0,0,276,277,1,0,0,0,277,278,5,17,0,0,278,45,1,0,0,0,279,
        285,5,28,0,0,280,285,5,29,0,0,281,285,5,30,0,0,282,285,5,31,0,0,
        283,285,3,6,3,0,284,279,1,0,0,0,284,280,1,0,0,0,284,281,1,0,0,0,
        284,282,1,0,0,0,284,283,1,0,0,0,285,47,1,0,0,0,286,287,3,20,10,0,
        287,288,6,24,-1,0,288,289,5,22,0,0,289,290,3,48,24,0,290,295,1,0,
        0,0,291,292,3,20,10,0,292,293,6,24,-1,0,293,295,1,0,0,0,294,286,
        1,0,0,0,294,291,1,0,0,0,295,49,1,0,0,0,296,297,3,20,10,0,297,298,
        5,22,0,0,298,299,3,50,25,0,299,302,1,0,0,0,300,302,3,20,10,0,301,
        296,1,0,0,0,301,300,1,0,0,0,302,51,1,0,0,0,303,306,3,54,27,0,304,
        306,3,8,4,0,305,303,1,0,0,0,305,304,1,0,0,0,306,307,1,0,0,0,307,
        308,3,52,26,0,308,314,1,0,0,0,309,312,3,54,27,0,310,312,3,8,4,0,
        311,309,1,0,0,0,311,310,1,0,0,0,312,314,1,0,0,0,313,305,1,0,0,0,
        313,311,1,0,0,0,314,53,1,0,0,0,315,326,3,56,28,0,316,326,3,62,31,
        0,317,326,3,64,32,0,318,326,3,72,36,0,319,326,3,74,37,0,320,326,
        3,76,38,0,321,326,3,78,39,0,322,326,3,80,40,0,323,326,3,82,41,0,
        324,326,3,84,42,0,325,315,1,0,0,0,325,316,1,0,0,0,325,317,1,0,0,
        0,325,318,1,0,0,0,325,319,1,0,0,0,325,320,1,0,0,0,325,321,1,0,0,
        0,325,322,1,0,0,0,325,323,1,0,0,0,325,324,1,0,0,0,326,55,1,0,0,0,
        327,328,3,58,29,0,328,329,5,26,0,0,329,330,3,60,30,0,330,331,5,24,
        0,0,331,57,1,0,0,0,332,336,3,86,43,0,333,334,5,55,0,0,334,336,3,
        38,19,0,335,332,1,0,0,0,335,333,1,0,0,0,336,59,1,0,0,0,337,338,3,
        20,10,0,338,61,1,0,0,0,339,340,5,41,0,0,340,341,5,16,0,0,341,342,
        3,20,10,0,342,343,5,17,0,0,343,346,3,54,27,0,344,345,5,36,0,0,345,
        347,3,54,27,0,346,344,1,0,0,0,346,347,1,0,0,0,347,63,1,0,0,0,348,
        349,5,39,0,0,349,350,5,16,0,0,350,351,3,66,33,0,351,352,5,22,0,0,
        352,353,3,68,34,0,353,354,5,22,0,0,354,355,3,70,35,0,355,356,5,17,
        0,0,356,357,3,54,27,0,357,65,1,0,0,0,358,359,3,86,43,0,359,360,5,
        26,0,0,360,361,3,20,10,0,361,67,1,0,0,0,362,363,3,20,10,0,363,69,
        1,0,0,0,364,365,3,20,10,0,365,71,1,0,0,0,366,367,5,48,0,0,367,368,
        5,16,0,0,368,369,3,20,10,0,369,370,5,17,0,0,370,371,3,54,27,0,371,
        73,1,0,0,0,372,373,5,35,0,0,373,374,3,84,42,0,374,375,5,48,0,0,375,
        376,5,16,0,0,376,377,3,20,10,0,377,378,5,17,0,0,378,379,5,24,0,0,
        379,75,1,0,0,0,380,381,5,33,0,0,381,382,5,24,0,0,382,77,1,0,0,0,
        383,384,5,50,0,0,384,385,5,24,0,0,385,79,1,0,0,0,386,388,5,43,0,
        0,387,389,3,20,10,0,388,387,1,0,0,0,388,389,1,0,0,0,389,390,1,0,
        0,0,390,391,5,24,0,0,391,81,1,0,0,0,392,393,3,44,22,0,393,394,5,
        24,0,0,394,83,1,0,0,0,395,397,5,20,0,0,396,398,3,52,26,0,397,396,
        1,0,0,0,397,398,1,0,0,0,398,399,1,0,0,0,399,400,5,21,0,0,400,85,
        1,0,0,0,401,402,5,55,0,0,402,87,1,0,0,0,403,404,5,34,0,0,404,89,
        1,0,0,0,405,406,5,42,0,0,406,91,1,0,0,0,407,408,5,38,0,0,408,93,
        1,0,0,0,409,410,5,44,0,0,410,95,1,0,0,0,411,412,5,47,0,0,412,97,
        1,0,0,0,413,414,5,32,0,0,414,99,1,0,0,0,415,416,5,46,0,0,416,417,
        5,18,0,0,417,418,3,102,51,0,418,419,5,19,0,0,419,420,5,51,0,0,420,
        421,3,104,52,0,421,101,1,0,0,0,422,427,5,28,0,0,423,424,5,22,0,0,
        424,426,5,28,0,0,425,423,1,0,0,0,426,429,1,0,0,0,427,425,1,0,0,0,
        427,428,1,0,0,0,428,103,1,0,0,0,429,427,1,0,0,0,430,435,3,88,44,
        0,431,435,3,90,45,0,432,435,3,92,46,0,433,435,3,94,47,0,434,430,
        1,0,0,0,434,431,1,0,0,0,434,432,1,0,0,0,434,433,1,0,0,0,435,105,
        1,0,0,0,37,113,118,122,131,135,147,157,161,166,175,178,181,188,199,
        206,216,227,238,244,249,254,265,270,275,284,294,301,305,311,313,
        325,335,346,388,397,427,434
    ]

class MT22Parser ( Parser ):

    grammarFileName = "MT22.g4"

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    sharedContextCache = PredictionContextCache()

    literalNames = [ "<INVALID>", "'+'", "'-'", "'*'", "'/'", "'%'", "'!'", 
                     "'&&'", "'||'", "'=='", "'!='", "'<'", "'<='", "'>'", 
                     "'>='", "'::'", "'('", "')'", "'['", "']'", "'{'", 
                     "'}'", "','", "'.'", "';'", "':'", "'='", "'_'", "<INVALID>", 
                     "<INVALID>", "<INVALID>", "<INVALID>", "'auto'", "'break'", 
                     "'boolean'", "'do'", "'else'", "'false'", "'float'", 
                     "'for'", "'function'", "'if'", "'integer'", "'return'", 
                     "'string'", "'true'", "'array'", "'void'", "'while'", 
                     "'out'", "'continue'", "'of'", "'inherit'" ]

    symbolicNames = [ "<INVALID>", "ADD", "MINUS", "MUL", "DIV", "MOD", 
                      "NOT", "AND", "OR", "EQ", "NOT_EQ", "LT", "LT_EQ", 
                      "GT", "GT_EQ", "SR", "LEFT_PAREN", "RIGHT_PAREN", 
                      "LEFT_BRACK", "RIGHT_BRACK", "LEFT_BRACE", "RIGHT_BRACE", 
                      "COMMA", "DOT", "SEMI_COLON", "COLON", "ASSIGN", "UNDERSCORE", 
                      "INTEGER_LIT", "FLOAT_LIT", "BOOLEAN_LIT", "STRING_LIT", 
                      "AUTO", "BREAK", "BOOLEAN", "DO", "ELSE", "FALSE", 
                      "FLOAT", "FOR", "FUNCTION", "IF", "INTEGER", "RETURN", 
                      "STRING", "TRUE", "ARRAY", "VOID", "WHILE", "OUT", 
                      "CONTINUE", "OF", "INHERIT", "BLOCK_COMMENT", "LINE_COMMENT", 
                      "ID", "WS", "UNCLOSE_STRING", "ILLEGAL_ESCAPE", "ERROR_CHAR" ]

    RULE_program = 0
    RULE_decls = 1
    RULE_decl = 2
    RULE_array_lit = 3
    RULE_variable_decl = 4
    RULE_identifiers_list = 5
    RULE_function_decl = 6
    RULE_params_list = 7
    RULE_parameter_decl = 8
    RULE_body = 9
    RULE_expr = 10
    RULE_string_expr = 11
    RULE_relational_expr = 12
    RULE_logical_expr_1 = 13
    RULE_adding_expr = 14
    RULE_multiplying_expr = 15
    RULE_logical_expr_2 = 16
    RULE_sign_expr = 17
    RULE_index_expr = 18
    RULE_index_operator = 19
    RULE_operand_expr = 20
    RULE_operand = 21
    RULE_func_call = 22
    RULE_literal = 23
    RULE_exprs_list_var_decl = 24
    RULE_exprs_list = 25
    RULE_statements_list = 26
    RULE_statement = 27
    RULE_assign_stmt = 28
    RULE_assign_stmt_lhs = 29
    RULE_assign_stmt_rhs = 30
    RULE_if_stmt = 31
    RULE_for_stmt = 32
    RULE_init_expr = 33
    RULE_condition_expr = 34
    RULE_update_expr = 35
    RULE_while_stmt = 36
    RULE_do_while_stmt = 37
    RULE_break_stmt = 38
    RULE_continue_stmt = 39
    RULE_return_stmt = 40
    RULE_call_stmt = 41
    RULE_block_stmt = 42
    RULE_scalar_var = 43
    RULE_boolean_type = 44
    RULE_int_type = 45
    RULE_float_type = 46
    RULE_string_type = 47
    RULE_void_type = 48
    RULE_auto_type = 49
    RULE_array_type = 50
    RULE_dimensions = 51
    RULE_atomic_type = 52

    ruleNames =  [ "program", "decls", "decl", "array_lit", "variable_decl", 
                   "identifiers_list", "function_decl", "params_list", "parameter_decl", 
                   "body", "expr", "string_expr", "relational_expr", "logical_expr_1", 
                   "adding_expr", "multiplying_expr", "logical_expr_2", 
                   "sign_expr", "index_expr", "index_operator", "operand_expr", 
                   "operand", "func_call", "literal", "exprs_list_var_decl", 
                   "exprs_list", "statements_list", "statement", "assign_stmt", 
                   "assign_stmt_lhs", "assign_stmt_rhs", "if_stmt", "for_stmt", 
                   "init_expr", "condition_expr", "update_expr", "while_stmt", 
                   "do_while_stmt", "break_stmt", "continue_stmt", "return_stmt", 
                   "call_stmt", "block_stmt", "scalar_var", "boolean_type", 
                   "int_type", "float_type", "string_type", "void_type", 
                   "auto_type", "array_type", "dimensions", "atomic_type" ]

    EOF = Token.EOF
    ADD=1
    MINUS=2
    MUL=3
    DIV=4
    MOD=5
    NOT=6
    AND=7
    OR=8
    EQ=9
    NOT_EQ=10
    LT=11
    LT_EQ=12
    GT=13
    GT_EQ=14
    SR=15
    LEFT_PAREN=16
    RIGHT_PAREN=17
    LEFT_BRACK=18
    RIGHT_BRACK=19
    LEFT_BRACE=20
    RIGHT_BRACE=21
    COMMA=22
    DOT=23
    SEMI_COLON=24
    COLON=25
    ASSIGN=26
    UNDERSCORE=27
    INTEGER_LIT=28
    FLOAT_LIT=29
    BOOLEAN_LIT=30
    STRING_LIT=31
    AUTO=32
    BREAK=33
    BOOLEAN=34
    DO=35
    ELSE=36
    FALSE=37
    FLOAT=38
    FOR=39
    FUNCTION=40
    IF=41
    INTEGER=42
    RETURN=43
    STRING=44
    TRUE=45
    ARRAY=46
    VOID=47
    WHILE=48
    OUT=49
    CONTINUE=50
    OF=51
    INHERIT=52
    BLOCK_COMMENT=53
    LINE_COMMENT=54
    ID=55
    WS=56
    UNCLOSE_STRING=57
    ILLEGAL_ESCAPE=58
    ERROR_CHAR=59

    def __init__(self, input:TokenStream, output:TextIO = sys.stdout):
        super().__init__(input, output)
        self.checkVersion("4.11.1")
        self._interp = ParserATNSimulator(self, self.atn, self.decisionsToDFA, self.sharedContextCache)
        self._predicates = None



    @property
    def ids_size(self):
        try:
            return self._ids_size
        except AttributeError: 
            self._ids_size = -1
            return self._ids_size

    @property
    def exprs_size(self):
        try:
            return self._exprs_size
        except AttributeError:
            self._exprs_size = -1
            return self._exprs_size

    @ids_size.setter
    def ids_size(self, value):
        self._ids_size = value

    @exprs_size.setter
    def exprs_size(self, value):
        self._exprs_size = value


    def check(self, flag):
        if flag: 
            if self.exprs_size != -1 and self.exprs_size != self.ids_size: 
                raise NoViableAltException(self)
            else:
                self.ids_size = -1
                self.exprs_size = -1
        else:
            if self.exprs_size + 2 >= self.ids_size:
                raise NoViableAltException(self)
            else:
                self.exprs_size += 1
        



    class ProgramContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def decls(self):
            return self.getTypedRuleContext(MT22Parser.DeclsContext,0)


        def EOF(self):
            return self.getToken(MT22Parser.EOF, 0)

        def getRuleIndex(self):
            return MT22Parser.RULE_program

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitProgram" ):
                return visitor.visitProgram(self)
            else:
                return visitor.visitChildren(self)




    def program(self):

        localctx = MT22Parser.ProgramContext(self, self._ctx, self.state)
        self.enterRule(localctx, 0, self.RULE_program)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 106
            self.decls()
            self.state = 107
            self.match(MT22Parser.EOF)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class DeclsContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def decl(self):
            return self.getTypedRuleContext(MT22Parser.DeclContext,0)


        def decls(self):
            return self.getTypedRuleContext(MT22Parser.DeclsContext,0)


        def getRuleIndex(self):
            return MT22Parser.RULE_decls

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitDecls" ):
                return visitor.visitDecls(self)
            else:
                return visitor.visitChildren(self)




    def decls(self):

        localctx = MT22Parser.DeclsContext(self, self._ctx, self.state)
        self.enterRule(localctx, 2, self.RULE_decls)
        try:
            self.state = 113
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,0,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 109
                self.decl()
                self.state = 110
                self.decls()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 112
                self.decl()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class DeclContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def variable_decl(self):
            return self.getTypedRuleContext(MT22Parser.Variable_declContext,0)


        def function_decl(self):
            return self.getTypedRuleContext(MT22Parser.Function_declContext,0)


        def parameter_decl(self):
            return self.getTypedRuleContext(MT22Parser.Parameter_declContext,0)


        def getRuleIndex(self):
            return MT22Parser.RULE_decl

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitDecl" ):
                return visitor.visitDecl(self)
            else:
                return visitor.visitChildren(self)




    def decl(self):

        localctx = MT22Parser.DeclContext(self, self._ctx, self.state)
        self.enterRule(localctx, 4, self.RULE_decl)
        try:
            self.state = 118
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,1,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 115
                self.variable_decl()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 116
                self.function_decl()
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 117
                self.parameter_decl()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Array_litContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def LEFT_BRACE(self):
            return self.getToken(MT22Parser.LEFT_BRACE, 0)

        def RIGHT_BRACE(self):
            return self.getToken(MT22Parser.RIGHT_BRACE, 0)

        def exprs_list(self):
            return self.getTypedRuleContext(MT22Parser.Exprs_listContext,0)


        def getRuleIndex(self):
            return MT22Parser.RULE_array_lit

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitArray_lit" ):
                return visitor.visitArray_lit(self)
            else:
                return visitor.visitChildren(self)




    def array_lit(self):

        localctx = MT22Parser.Array_litContext(self, self._ctx, self.state)
        self.enterRule(localctx, 6, self.RULE_array_lit)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 120
            self.match(MT22Parser.LEFT_BRACE)
            self.state = 122
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if ((_la) & ~0x3f) == 0 and ((1 << _la) & 36028801046609988) != 0:
                self.state = 121
                self.exprs_list()


            self.state = 124
            self.match(MT22Parser.RIGHT_BRACE)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Variable_declContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def identifiers_list(self):
            return self.getTypedRuleContext(MT22Parser.Identifiers_listContext,0)


        def COLON(self):
            return self.getToken(MT22Parser.COLON, 0)

        def SEMI_COLON(self):
            return self.getToken(MT22Parser.SEMI_COLON, 0)

        def atomic_type(self):
            return self.getTypedRuleContext(MT22Parser.Atomic_typeContext,0)


        def array_type(self):
            return self.getTypedRuleContext(MT22Parser.Array_typeContext,0)


        def auto_type(self):
            return self.getTypedRuleContext(MT22Parser.Auto_typeContext,0)


        def ASSIGN(self):
            return self.getToken(MT22Parser.ASSIGN, 0)

        def exprs_list_var_decl(self):
            return self.getTypedRuleContext(MT22Parser.Exprs_list_var_declContext,0)


        def getRuleIndex(self):
            return MT22Parser.RULE_variable_decl

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitVariable_decl" ):
                return visitor.visitVariable_decl(self)
            else:
                return visitor.visitChildren(self)




    def variable_decl(self):

        localctx = MT22Parser.Variable_declContext(self, self._ctx, self.state)
        self.enterRule(localctx, 8, self.RULE_variable_decl)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 126
            self.identifiers_list()
            self.state = 127
            self.match(MT22Parser.COLON)
            self.state = 131
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [34, 38, 42, 44]:
                self.state = 128
                self.atomic_type()
                pass
            elif token in [46]:
                self.state = 129
                self.array_type()
                pass
            elif token in [32]:
                self.state = 130
                self.auto_type()
                pass
            else:
                raise NoViableAltException(self)

            self.state = 135
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==26:
                self.state = 133
                self.match(MT22Parser.ASSIGN)
                self.state = 134
                self.exprs_list_var_decl()



            self.check(True)

            self.state = 138
            self.match(MT22Parser.SEMI_COLON)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Identifiers_listContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ID(self, i:int=None):
            if i is None:
                return self.getTokens(MT22Parser.ID)
            else:
                return self.getToken(MT22Parser.ID, i)

        def COMMA(self, i:int=None):
            if i is None:
                return self.getTokens(MT22Parser.COMMA)
            else:
                return self.getToken(MT22Parser.COMMA, i)

        def getRuleIndex(self):
            return MT22Parser.RULE_identifiers_list

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitIdentifiers_list" ):
                return visitor.visitIdentifiers_list(self)
            else:
                return visitor.visitChildren(self)




    def identifiers_list(self):

        localctx = MT22Parser.Identifiers_listContext(self, self._ctx, self.state)
        self.enterRule(localctx, 10, self.RULE_identifiers_list)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 140
            self.match(MT22Parser.ID)
            self.ids_size += 2
            self.state = 147
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==22:
                self.state = 142
                self.match(MT22Parser.COMMA)
                self.state = 143
                self.match(MT22Parser.ID)
                self.ids_size += 1
                self.state = 149
                self._errHandler.sync(self)
                _la = self._input.LA(1)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Function_declContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ID(self, i:int=None):
            if i is None:
                return self.getTokens(MT22Parser.ID)
            else:
                return self.getToken(MT22Parser.ID, i)

        def COLON(self):
            return self.getToken(MT22Parser.COLON, 0)

        def FUNCTION(self):
            return self.getToken(MT22Parser.FUNCTION, 0)

        def LEFT_PAREN(self):
            return self.getToken(MT22Parser.LEFT_PAREN, 0)

        def RIGHT_PAREN(self):
            return self.getToken(MT22Parser.RIGHT_PAREN, 0)

        def body(self):
            return self.getTypedRuleContext(MT22Parser.BodyContext,0)


        def atomic_type(self):
            return self.getTypedRuleContext(MT22Parser.Atomic_typeContext,0)


        def void_type(self):
            return self.getTypedRuleContext(MT22Parser.Void_typeContext,0)


        def auto_type(self):
            return self.getTypedRuleContext(MT22Parser.Auto_typeContext,0)


        def array_type(self):
            return self.getTypedRuleContext(MT22Parser.Array_typeContext,0)


        def params_list(self):
            return self.getTypedRuleContext(MT22Parser.Params_listContext,0)


        def INHERIT(self):
            return self.getToken(MT22Parser.INHERIT, 0)

        def getRuleIndex(self):
            return MT22Parser.RULE_function_decl

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitFunction_decl" ):
                return visitor.visitFunction_decl(self)
            else:
                return visitor.visitChildren(self)




    def function_decl(self):

        localctx = MT22Parser.Function_declContext(self, self._ctx, self.state)
        self.enterRule(localctx, 12, self.RULE_function_decl)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 150
            self.match(MT22Parser.ID)
            self.state = 151
            self.match(MT22Parser.COLON)
            self.state = 152
            self.match(MT22Parser.FUNCTION)
            self.state = 157
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [34, 38, 42, 44]:
                self.state = 153
                self.atomic_type()
                pass
            elif token in [47]:
                self.state = 154
                self.void_type()
                pass
            elif token in [32]:
                self.state = 155
                self.auto_type()
                pass
            elif token in [46]:
                self.state = 156
                self.array_type()
                pass
            else:
                raise NoViableAltException(self)

            self.state = 159
            self.match(MT22Parser.LEFT_PAREN)
            self.state = 161
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if ((_la) & ~0x3f) == 0 and ((1 << _la) & 41095346599755776) != 0:
                self.state = 160
                self.params_list()


            self.state = 163
            self.match(MT22Parser.RIGHT_PAREN)
            self.state = 166
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==52:
                self.state = 164
                self.match(MT22Parser.INHERIT)
                self.state = 165
                self.match(MT22Parser.ID)


            self.state = 168
            self.body()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Params_listContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def parameter_decl(self):
            return self.getTypedRuleContext(MT22Parser.Parameter_declContext,0)


        def COMMA(self):
            return self.getToken(MT22Parser.COMMA, 0)

        def params_list(self):
            return self.getTypedRuleContext(MT22Parser.Params_listContext,0)


        def getRuleIndex(self):
            return MT22Parser.RULE_params_list

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitParams_list" ):
                return visitor.visitParams_list(self)
            else:
                return visitor.visitChildren(self)




    def params_list(self):

        localctx = MT22Parser.Params_listContext(self, self._ctx, self.state)
        self.enterRule(localctx, 14, self.RULE_params_list)
        try:
            self.state = 175
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,9,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 170
                self.parameter_decl()
                self.state = 171
                self.match(MT22Parser.COMMA)
                self.state = 172
                self.params_list()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 174
                self.parameter_decl()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Parameter_declContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ID(self):
            return self.getToken(MT22Parser.ID, 0)

        def COLON(self):
            return self.getToken(MT22Parser.COLON, 0)

        def atomic_type(self):
            return self.getTypedRuleContext(MT22Parser.Atomic_typeContext,0)


        def array_type(self):
            return self.getTypedRuleContext(MT22Parser.Array_typeContext,0)


        def auto_type(self):
            return self.getTypedRuleContext(MT22Parser.Auto_typeContext,0)


        def INHERIT(self):
            return self.getToken(MT22Parser.INHERIT, 0)

        def OUT(self):
            return self.getToken(MT22Parser.OUT, 0)

        def getRuleIndex(self):
            return MT22Parser.RULE_parameter_decl

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitParameter_decl" ):
                return visitor.visitParameter_decl(self)
            else:
                return visitor.visitChildren(self)




    def parameter_decl(self):

        localctx = MT22Parser.Parameter_declContext(self, self._ctx, self.state)
        self.enterRule(localctx, 16, self.RULE_parameter_decl)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 178
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==52:
                self.state = 177
                self.match(MT22Parser.INHERIT)


            self.state = 181
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==49:
                self.state = 180
                self.match(MT22Parser.OUT)


            self.state = 183
            self.match(MT22Parser.ID)
            self.state = 184
            self.match(MT22Parser.COLON)
            self.state = 188
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [34, 38, 42, 44]:
                self.state = 185
                self.atomic_type()
                pass
            elif token in [46]:
                self.state = 186
                self.array_type()
                pass
            elif token in [32]:
                self.state = 187
                self.auto_type()
                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class BodyContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def block_stmt(self):
            return self.getTypedRuleContext(MT22Parser.Block_stmtContext,0)


        def getRuleIndex(self):
            return MT22Parser.RULE_body

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitBody" ):
                return visitor.visitBody(self)
            else:
                return visitor.visitChildren(self)




    def body(self):

        localctx = MT22Parser.BodyContext(self, self._ctx, self.state)
        self.enterRule(localctx, 18, self.RULE_body)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 190
            self.block_stmt()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ExprContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def string_expr(self):
            return self.getTypedRuleContext(MT22Parser.String_exprContext,0)


        def getRuleIndex(self):
            return MT22Parser.RULE_expr

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitExpr" ):
                return visitor.visitExpr(self)
            else:
                return visitor.visitChildren(self)




    def expr(self):

        localctx = MT22Parser.ExprContext(self, self._ctx, self.state)
        self.enterRule(localctx, 20, self.RULE_expr)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 192
            self.string_expr()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class String_exprContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def relational_expr(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(MT22Parser.Relational_exprContext)
            else:
                return self.getTypedRuleContext(MT22Parser.Relational_exprContext,i)


        def SR(self):
            return self.getToken(MT22Parser.SR, 0)

        def getRuleIndex(self):
            return MT22Parser.RULE_string_expr

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitString_expr" ):
                return visitor.visitString_expr(self)
            else:
                return visitor.visitChildren(self)




    def string_expr(self):

        localctx = MT22Parser.String_exprContext(self, self._ctx, self.state)
        self.enterRule(localctx, 22, self.RULE_string_expr)
        try:
            self.state = 199
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,13,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 194
                self.relational_expr()
                self.state = 195
                self.match(MT22Parser.SR)
                self.state = 196
                self.relational_expr()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 198
                self.relational_expr()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Relational_exprContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def logical_expr_1(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(MT22Parser.Logical_expr_1Context)
            else:
                return self.getTypedRuleContext(MT22Parser.Logical_expr_1Context,i)


        def EQ(self):
            return self.getToken(MT22Parser.EQ, 0)

        def NOT_EQ(self):
            return self.getToken(MT22Parser.NOT_EQ, 0)

        def GT(self):
            return self.getToken(MT22Parser.GT, 0)

        def LT(self):
            return self.getToken(MT22Parser.LT, 0)

        def LT_EQ(self):
            return self.getToken(MT22Parser.LT_EQ, 0)

        def GT_EQ(self):
            return self.getToken(MT22Parser.GT_EQ, 0)

        def getRuleIndex(self):
            return MT22Parser.RULE_relational_expr

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitRelational_expr" ):
                return visitor.visitRelational_expr(self)
            else:
                return visitor.visitChildren(self)




    def relational_expr(self):

        localctx = MT22Parser.Relational_exprContext(self, self._ctx, self.state)
        self.enterRule(localctx, 24, self.RULE_relational_expr)
        self._la = 0 # Token type
        try:
            self.state = 206
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,14,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 201
                self.logical_expr_1(0)
                self.state = 202
                _la = self._input.LA(1)
                if not(((_la) & ~0x3f) == 0 and ((1 << _la) & 32256) != 0):
                    self._errHandler.recoverInline(self)
                else:
                    self._errHandler.reportMatch(self)
                    self.consume()
                self.state = 203
                self.logical_expr_1(0)
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 205
                self.logical_expr_1(0)
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Logical_expr_1Context(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def adding_expr(self):
            return self.getTypedRuleContext(MT22Parser.Adding_exprContext,0)


        def logical_expr_1(self):
            return self.getTypedRuleContext(MT22Parser.Logical_expr_1Context,0)


        def AND(self):
            return self.getToken(MT22Parser.AND, 0)

        def OR(self):
            return self.getToken(MT22Parser.OR, 0)

        def getRuleIndex(self):
            return MT22Parser.RULE_logical_expr_1

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitLogical_expr_1" ):
                return visitor.visitLogical_expr_1(self)
            else:
                return visitor.visitChildren(self)



    def logical_expr_1(self, _p:int=0):
        _parentctx = self._ctx
        _parentState = self.state
        localctx = MT22Parser.Logical_expr_1Context(self, self._ctx, _parentState)
        _prevctx = localctx
        _startState = 26
        self.enterRecursionRule(localctx, 26, self.RULE_logical_expr_1, _p)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 209
            self.adding_expr(0)
            self._ctx.stop = self._input.LT(-1)
            self.state = 216
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,15,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    localctx = MT22Parser.Logical_expr_1Context(self, _parentctx, _parentState)
                    self.pushNewRecursionContext(localctx, _startState, self.RULE_logical_expr_1)
                    self.state = 211
                    if not self.precpred(self._ctx, 2):
                        from antlr4.error.Errors import FailedPredicateException
                        raise FailedPredicateException(self, "self.precpred(self._ctx, 2)")
                    self.state = 212
                    _la = self._input.LA(1)
                    if not(_la==7 or _la==8):
                        self._errHandler.recoverInline(self)
                    else:
                        self._errHandler.reportMatch(self)
                        self.consume()
                    self.state = 213
                    self.adding_expr(0) 
                self.state = 218
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,15,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.unrollRecursionContexts(_parentctx)
        return localctx


    class Adding_exprContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def multiplying_expr(self):
            return self.getTypedRuleContext(MT22Parser.Multiplying_exprContext,0)


        def adding_expr(self):
            return self.getTypedRuleContext(MT22Parser.Adding_exprContext,0)


        def ADD(self):
            return self.getToken(MT22Parser.ADD, 0)

        def MINUS(self):
            return self.getToken(MT22Parser.MINUS, 0)

        def getRuleIndex(self):
            return MT22Parser.RULE_adding_expr

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitAdding_expr" ):
                return visitor.visitAdding_expr(self)
            else:
                return visitor.visitChildren(self)



    def adding_expr(self, _p:int=0):
        _parentctx = self._ctx
        _parentState = self.state
        localctx = MT22Parser.Adding_exprContext(self, self._ctx, _parentState)
        _prevctx = localctx
        _startState = 28
        self.enterRecursionRule(localctx, 28, self.RULE_adding_expr, _p)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 220
            self.multiplying_expr(0)
            self._ctx.stop = self._input.LT(-1)
            self.state = 227
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,16,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    localctx = MT22Parser.Adding_exprContext(self, _parentctx, _parentState)
                    self.pushNewRecursionContext(localctx, _startState, self.RULE_adding_expr)
                    self.state = 222
                    if not self.precpred(self._ctx, 2):
                        from antlr4.error.Errors import FailedPredicateException
                        raise FailedPredicateException(self, "self.precpred(self._ctx, 2)")
                    self.state = 223
                    _la = self._input.LA(1)
                    if not(_la==1 or _la==2):
                        self._errHandler.recoverInline(self)
                    else:
                        self._errHandler.reportMatch(self)
                        self.consume()
                    self.state = 224
                    self.multiplying_expr(0) 
                self.state = 229
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,16,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.unrollRecursionContexts(_parentctx)
        return localctx


    class Multiplying_exprContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def logical_expr_2(self):
            return self.getTypedRuleContext(MT22Parser.Logical_expr_2Context,0)


        def multiplying_expr(self):
            return self.getTypedRuleContext(MT22Parser.Multiplying_exprContext,0)


        def MUL(self):
            return self.getToken(MT22Parser.MUL, 0)

        def DIV(self):
            return self.getToken(MT22Parser.DIV, 0)

        def MOD(self):
            return self.getToken(MT22Parser.MOD, 0)

        def getRuleIndex(self):
            return MT22Parser.RULE_multiplying_expr

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitMultiplying_expr" ):
                return visitor.visitMultiplying_expr(self)
            else:
                return visitor.visitChildren(self)



    def multiplying_expr(self, _p:int=0):
        _parentctx = self._ctx
        _parentState = self.state
        localctx = MT22Parser.Multiplying_exprContext(self, self._ctx, _parentState)
        _prevctx = localctx
        _startState = 30
        self.enterRecursionRule(localctx, 30, self.RULE_multiplying_expr, _p)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 231
            self.logical_expr_2()
            self._ctx.stop = self._input.LT(-1)
            self.state = 238
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,17,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    localctx = MT22Parser.Multiplying_exprContext(self, _parentctx, _parentState)
                    self.pushNewRecursionContext(localctx, _startState, self.RULE_multiplying_expr)
                    self.state = 233
                    if not self.precpred(self._ctx, 2):
                        from antlr4.error.Errors import FailedPredicateException
                        raise FailedPredicateException(self, "self.precpred(self._ctx, 2)")
                    self.state = 234
                    _la = self._input.LA(1)
                    if not(((_la) & ~0x3f) == 0 and ((1 << _la) & 56) != 0):
                        self._errHandler.recoverInline(self)
                    else:
                        self._errHandler.reportMatch(self)
                        self.consume()
                    self.state = 235
                    self.logical_expr_2() 
                self.state = 240
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,17,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.unrollRecursionContexts(_parentctx)
        return localctx


    class Logical_expr_2Context(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def NOT(self):
            return self.getToken(MT22Parser.NOT, 0)

        def logical_expr_2(self):
            return self.getTypedRuleContext(MT22Parser.Logical_expr_2Context,0)


        def sign_expr(self):
            return self.getTypedRuleContext(MT22Parser.Sign_exprContext,0)


        def getRuleIndex(self):
            return MT22Parser.RULE_logical_expr_2

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitLogical_expr_2" ):
                return visitor.visitLogical_expr_2(self)
            else:
                return visitor.visitChildren(self)




    def logical_expr_2(self):

        localctx = MT22Parser.Logical_expr_2Context(self, self._ctx, self.state)
        self.enterRule(localctx, 32, self.RULE_logical_expr_2)
        try:
            self.state = 244
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [6]:
                self.enterOuterAlt(localctx, 1)
                self.state = 241
                self.match(MT22Parser.NOT)
                self.state = 242
                self.logical_expr_2()
                pass
            elif token in [2, 16, 20, 28, 29, 30, 31, 55]:
                self.enterOuterAlt(localctx, 2)
                self.state = 243
                self.sign_expr()
                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Sign_exprContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def MINUS(self):
            return self.getToken(MT22Parser.MINUS, 0)

        def sign_expr(self):
            return self.getTypedRuleContext(MT22Parser.Sign_exprContext,0)


        def index_expr(self):
            return self.getTypedRuleContext(MT22Parser.Index_exprContext,0)


        def getRuleIndex(self):
            return MT22Parser.RULE_sign_expr

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitSign_expr" ):
                return visitor.visitSign_expr(self)
            else:
                return visitor.visitChildren(self)




    def sign_expr(self):

        localctx = MT22Parser.Sign_exprContext(self, self._ctx, self.state)
        self.enterRule(localctx, 34, self.RULE_sign_expr)
        try:
            self.state = 249
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [2]:
                self.enterOuterAlt(localctx, 1)
                self.state = 246
                self.match(MT22Parser.MINUS)
                self.state = 247
                self.sign_expr()
                pass
            elif token in [16, 20, 28, 29, 30, 31, 55]:
                self.enterOuterAlt(localctx, 2)
                self.state = 248
                self.index_expr()
                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Index_exprContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ID(self):
            return self.getToken(MT22Parser.ID, 0)

        def index_operator(self):
            return self.getTypedRuleContext(MT22Parser.Index_operatorContext,0)


        def operand_expr(self):
            return self.getTypedRuleContext(MT22Parser.Operand_exprContext,0)


        def getRuleIndex(self):
            return MT22Parser.RULE_index_expr

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitIndex_expr" ):
                return visitor.visitIndex_expr(self)
            else:
                return visitor.visitChildren(self)




    def index_expr(self):

        localctx = MT22Parser.Index_exprContext(self, self._ctx, self.state)
        self.enterRule(localctx, 36, self.RULE_index_expr)
        try:
            self.state = 254
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,20,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 251
                self.match(MT22Parser.ID)
                self.state = 252
                self.index_operator()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 253
                self.operand_expr()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Index_operatorContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def LEFT_BRACK(self):
            return self.getToken(MT22Parser.LEFT_BRACK, 0)

        def exprs_list(self):
            return self.getTypedRuleContext(MT22Parser.Exprs_listContext,0)


        def RIGHT_BRACK(self):
            return self.getToken(MT22Parser.RIGHT_BRACK, 0)

        def getRuleIndex(self):
            return MT22Parser.RULE_index_operator

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitIndex_operator" ):
                return visitor.visitIndex_operator(self)
            else:
                return visitor.visitChildren(self)




    def index_operator(self):

        localctx = MT22Parser.Index_operatorContext(self, self._ctx, self.state)
        self.enterRule(localctx, 38, self.RULE_index_operator)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 256
            self.match(MT22Parser.LEFT_BRACK)
            self.state = 257
            self.exprs_list()
            self.state = 258
            self.match(MT22Parser.RIGHT_BRACK)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Operand_exprContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def operand(self):
            return self.getTypedRuleContext(MT22Parser.OperandContext,0)


        def LEFT_PAREN(self):
            return self.getToken(MT22Parser.LEFT_PAREN, 0)

        def expr(self):
            return self.getTypedRuleContext(MT22Parser.ExprContext,0)


        def RIGHT_PAREN(self):
            return self.getToken(MT22Parser.RIGHT_PAREN, 0)

        def getRuleIndex(self):
            return MT22Parser.RULE_operand_expr

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitOperand_expr" ):
                return visitor.visitOperand_expr(self)
            else:
                return visitor.visitChildren(self)




    def operand_expr(self):

        localctx = MT22Parser.Operand_exprContext(self, self._ctx, self.state)
        self.enterRule(localctx, 40, self.RULE_operand_expr)
        try:
            self.state = 265
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [20, 28, 29, 30, 31, 55]:
                self.enterOuterAlt(localctx, 1)
                self.state = 260
                self.operand()
                pass
            elif token in [16]:
                self.enterOuterAlt(localctx, 2)
                self.state = 261
                self.match(MT22Parser.LEFT_PAREN)
                self.state = 262
                self.expr()
                self.state = 263
                self.match(MT22Parser.RIGHT_PAREN)
                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class OperandContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def literal(self):
            return self.getTypedRuleContext(MT22Parser.LiteralContext,0)


        def func_call(self):
            return self.getTypedRuleContext(MT22Parser.Func_callContext,0)


        def ID(self):
            return self.getToken(MT22Parser.ID, 0)

        def getRuleIndex(self):
            return MT22Parser.RULE_operand

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitOperand" ):
                return visitor.visitOperand(self)
            else:
                return visitor.visitChildren(self)




    def operand(self):

        localctx = MT22Parser.OperandContext(self, self._ctx, self.state)
        self.enterRule(localctx, 42, self.RULE_operand)
        try:
            self.state = 270
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,22,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 267
                self.literal()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 268
                self.func_call()
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 269
                self.match(MT22Parser.ID)
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Func_callContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ID(self):
            return self.getToken(MT22Parser.ID, 0)

        def LEFT_PAREN(self):
            return self.getToken(MT22Parser.LEFT_PAREN, 0)

        def RIGHT_PAREN(self):
            return self.getToken(MT22Parser.RIGHT_PAREN, 0)

        def exprs_list(self):
            return self.getTypedRuleContext(MT22Parser.Exprs_listContext,0)


        def getRuleIndex(self):
            return MT22Parser.RULE_func_call

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitFunc_call" ):
                return visitor.visitFunc_call(self)
            else:
                return visitor.visitChildren(self)




    def func_call(self):

        localctx = MT22Parser.Func_callContext(self, self._ctx, self.state)
        self.enterRule(localctx, 44, self.RULE_func_call)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 272
            self.match(MT22Parser.ID)
            self.state = 273
            self.match(MT22Parser.LEFT_PAREN)
            self.state = 275
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if ((_la) & ~0x3f) == 0 and ((1 << _la) & 36028801046609988) != 0:
                self.state = 274
                self.exprs_list()


            self.state = 277
            self.match(MT22Parser.RIGHT_PAREN)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class LiteralContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def INTEGER_LIT(self):
            return self.getToken(MT22Parser.INTEGER_LIT, 0)

        def FLOAT_LIT(self):
            return self.getToken(MT22Parser.FLOAT_LIT, 0)

        def BOOLEAN_LIT(self):
            return self.getToken(MT22Parser.BOOLEAN_LIT, 0)

        def STRING_LIT(self):
            return self.getToken(MT22Parser.STRING_LIT, 0)

        def array_lit(self):
            return self.getTypedRuleContext(MT22Parser.Array_litContext,0)


        def getRuleIndex(self):
            return MT22Parser.RULE_literal

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitLiteral" ):
                return visitor.visitLiteral(self)
            else:
                return visitor.visitChildren(self)




    def literal(self):

        localctx = MT22Parser.LiteralContext(self, self._ctx, self.state)
        self.enterRule(localctx, 46, self.RULE_literal)
        try:
            self.state = 284
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [28]:
                self.enterOuterAlt(localctx, 1)
                self.state = 279
                self.match(MT22Parser.INTEGER_LIT)
                pass
            elif token in [29]:
                self.enterOuterAlt(localctx, 2)
                self.state = 280
                self.match(MT22Parser.FLOAT_LIT)
                pass
            elif token in [30]:
                self.enterOuterAlt(localctx, 3)
                self.state = 281
                self.match(MT22Parser.BOOLEAN_LIT)
                pass
            elif token in [31]:
                self.enterOuterAlt(localctx, 4)
                self.state = 282
                self.match(MT22Parser.STRING_LIT)
                pass
            elif token in [20]:
                self.enterOuterAlt(localctx, 5)
                self.state = 283
                self.array_lit()
                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Exprs_list_var_declContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def expr(self):
            return self.getTypedRuleContext(MT22Parser.ExprContext,0)


        def COMMA(self):
            return self.getToken(MT22Parser.COMMA, 0)

        def exprs_list_var_decl(self):
            return self.getTypedRuleContext(MT22Parser.Exprs_list_var_declContext,0)


        def getRuleIndex(self):
            return MT22Parser.RULE_exprs_list_var_decl

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitExprs_list_var_decl" ):
                return visitor.visitExprs_list_var_decl(self)
            else:
                return visitor.visitChildren(self)




    def exprs_list_var_decl(self):

        localctx = MT22Parser.Exprs_list_var_declContext(self, self._ctx, self.state)
        self.enterRule(localctx, 48, self.RULE_exprs_list_var_decl)
        try:
            self.state = 294
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,25,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 286
                self.expr()

                self.check(False)

                self.state = 288
                self.match(MT22Parser.COMMA)
                self.state = 289
                self.exprs_list_var_decl()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 291
                self.expr()
                self.exprs_size += 2
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Exprs_listContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def expr(self):
            return self.getTypedRuleContext(MT22Parser.ExprContext,0)


        def COMMA(self):
            return self.getToken(MT22Parser.COMMA, 0)

        def exprs_list(self):
            return self.getTypedRuleContext(MT22Parser.Exprs_listContext,0)


        def getRuleIndex(self):
            return MT22Parser.RULE_exprs_list

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitExprs_list" ):
                return visitor.visitExprs_list(self)
            else:
                return visitor.visitChildren(self)




    def exprs_list(self):

        localctx = MT22Parser.Exprs_listContext(self, self._ctx, self.state)
        self.enterRule(localctx, 50, self.RULE_exprs_list)
        try:
            self.state = 301
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,26,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 296
                self.expr()
                self.state = 297
                self.match(MT22Parser.COMMA)
                self.state = 298
                self.exprs_list()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 300
                self.expr()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Statements_listContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def statements_list(self):
            return self.getTypedRuleContext(MT22Parser.Statements_listContext,0)


        def statement(self):
            return self.getTypedRuleContext(MT22Parser.StatementContext,0)


        def variable_decl(self):
            return self.getTypedRuleContext(MT22Parser.Variable_declContext,0)


        def getRuleIndex(self):
            return MT22Parser.RULE_statements_list

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitStatements_list" ):
                return visitor.visitStatements_list(self)
            else:
                return visitor.visitChildren(self)




    def statements_list(self):

        localctx = MT22Parser.Statements_listContext(self, self._ctx, self.state)
        self.enterRule(localctx, 52, self.RULE_statements_list)
        try:
            self.state = 313
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,29,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 305
                self._errHandler.sync(self)
                la_ = self._interp.adaptivePredict(self._input,27,self._ctx)
                if la_ == 1:
                    self.state = 303
                    self.statement()
                    pass

                elif la_ == 2:
                    self.state = 304
                    self.variable_decl()
                    pass


                self.state = 307
                self.statements_list()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 311
                self._errHandler.sync(self)
                la_ = self._interp.adaptivePredict(self._input,28,self._ctx)
                if la_ == 1:
                    self.state = 309
                    self.statement()
                    pass

                elif la_ == 2:
                    self.state = 310
                    self.variable_decl()
                    pass


                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class StatementContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def assign_stmt(self):
            return self.getTypedRuleContext(MT22Parser.Assign_stmtContext,0)


        def if_stmt(self):
            return self.getTypedRuleContext(MT22Parser.If_stmtContext,0)


        def for_stmt(self):
            return self.getTypedRuleContext(MT22Parser.For_stmtContext,0)


        def while_stmt(self):
            return self.getTypedRuleContext(MT22Parser.While_stmtContext,0)


        def do_while_stmt(self):
            return self.getTypedRuleContext(MT22Parser.Do_while_stmtContext,0)


        def break_stmt(self):
            return self.getTypedRuleContext(MT22Parser.Break_stmtContext,0)


        def continue_stmt(self):
            return self.getTypedRuleContext(MT22Parser.Continue_stmtContext,0)


        def return_stmt(self):
            return self.getTypedRuleContext(MT22Parser.Return_stmtContext,0)


        def call_stmt(self):
            return self.getTypedRuleContext(MT22Parser.Call_stmtContext,0)


        def block_stmt(self):
            return self.getTypedRuleContext(MT22Parser.Block_stmtContext,0)


        def getRuleIndex(self):
            return MT22Parser.RULE_statement

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitStatement" ):
                return visitor.visitStatement(self)
            else:
                return visitor.visitChildren(self)




    def statement(self):

        localctx = MT22Parser.StatementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 54, self.RULE_statement)
        try:
            self.state = 325
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,30,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 315
                self.assign_stmt()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 316
                self.if_stmt()
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 317
                self.for_stmt()
                pass

            elif la_ == 4:
                self.enterOuterAlt(localctx, 4)
                self.state = 318
                self.while_stmt()
                pass

            elif la_ == 5:
                self.enterOuterAlt(localctx, 5)
                self.state = 319
                self.do_while_stmt()
                pass

            elif la_ == 6:
                self.enterOuterAlt(localctx, 6)
                self.state = 320
                self.break_stmt()
                pass

            elif la_ == 7:
                self.enterOuterAlt(localctx, 7)
                self.state = 321
                self.continue_stmt()
                pass

            elif la_ == 8:
                self.enterOuterAlt(localctx, 8)
                self.state = 322
                self.return_stmt()
                pass

            elif la_ == 9:
                self.enterOuterAlt(localctx, 9)
                self.state = 323
                self.call_stmt()
                pass

            elif la_ == 10:
                self.enterOuterAlt(localctx, 10)
                self.state = 324
                self.block_stmt()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Assign_stmtContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def assign_stmt_lhs(self):
            return self.getTypedRuleContext(MT22Parser.Assign_stmt_lhsContext,0)


        def ASSIGN(self):
            return self.getToken(MT22Parser.ASSIGN, 0)

        def assign_stmt_rhs(self):
            return self.getTypedRuleContext(MT22Parser.Assign_stmt_rhsContext,0)


        def SEMI_COLON(self):
            return self.getToken(MT22Parser.SEMI_COLON, 0)

        def getRuleIndex(self):
            return MT22Parser.RULE_assign_stmt

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitAssign_stmt" ):
                return visitor.visitAssign_stmt(self)
            else:
                return visitor.visitChildren(self)




    def assign_stmt(self):

        localctx = MT22Parser.Assign_stmtContext(self, self._ctx, self.state)
        self.enterRule(localctx, 56, self.RULE_assign_stmt)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 327
            self.assign_stmt_lhs()
            self.state = 328
            self.match(MT22Parser.ASSIGN)
            self.state = 329
            self.assign_stmt_rhs()
            self.state = 330
            self.match(MT22Parser.SEMI_COLON)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Assign_stmt_lhsContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def scalar_var(self):
            return self.getTypedRuleContext(MT22Parser.Scalar_varContext,0)


        def ID(self):
            return self.getToken(MT22Parser.ID, 0)

        def index_operator(self):
            return self.getTypedRuleContext(MT22Parser.Index_operatorContext,0)


        def getRuleIndex(self):
            return MT22Parser.RULE_assign_stmt_lhs

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitAssign_stmt_lhs" ):
                return visitor.visitAssign_stmt_lhs(self)
            else:
                return visitor.visitChildren(self)




    def assign_stmt_lhs(self):

        localctx = MT22Parser.Assign_stmt_lhsContext(self, self._ctx, self.state)
        self.enterRule(localctx, 58, self.RULE_assign_stmt_lhs)
        try:
            self.state = 335
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,31,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 332
                self.scalar_var()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 333
                self.match(MT22Parser.ID)
                self.state = 334
                self.index_operator()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Assign_stmt_rhsContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def expr(self):
            return self.getTypedRuleContext(MT22Parser.ExprContext,0)


        def getRuleIndex(self):
            return MT22Parser.RULE_assign_stmt_rhs

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitAssign_stmt_rhs" ):
                return visitor.visitAssign_stmt_rhs(self)
            else:
                return visitor.visitChildren(self)




    def assign_stmt_rhs(self):

        localctx = MT22Parser.Assign_stmt_rhsContext(self, self._ctx, self.state)
        self.enterRule(localctx, 60, self.RULE_assign_stmt_rhs)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 337
            self.expr()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class If_stmtContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def IF(self):
            return self.getToken(MT22Parser.IF, 0)

        def LEFT_PAREN(self):
            return self.getToken(MT22Parser.LEFT_PAREN, 0)

        def expr(self):
            return self.getTypedRuleContext(MT22Parser.ExprContext,0)


        def RIGHT_PAREN(self):
            return self.getToken(MT22Parser.RIGHT_PAREN, 0)

        def statement(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(MT22Parser.StatementContext)
            else:
                return self.getTypedRuleContext(MT22Parser.StatementContext,i)


        def ELSE(self):
            return self.getToken(MT22Parser.ELSE, 0)

        def getRuleIndex(self):
            return MT22Parser.RULE_if_stmt

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitIf_stmt" ):
                return visitor.visitIf_stmt(self)
            else:
                return visitor.visitChildren(self)




    def if_stmt(self):

        localctx = MT22Parser.If_stmtContext(self, self._ctx, self.state)
        self.enterRule(localctx, 62, self.RULE_if_stmt)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 339
            self.match(MT22Parser.IF)
            self.state = 340
            self.match(MT22Parser.LEFT_PAREN)
            self.state = 341
            self.expr()
            self.state = 342
            self.match(MT22Parser.RIGHT_PAREN)
            self.state = 343
            self.statement()
            self.state = 346
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,32,self._ctx)
            if la_ == 1:
                self.state = 344
                self.match(MT22Parser.ELSE)
                self.state = 345
                self.statement()


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class For_stmtContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def FOR(self):
            return self.getToken(MT22Parser.FOR, 0)

        def LEFT_PAREN(self):
            return self.getToken(MT22Parser.LEFT_PAREN, 0)

        def init_expr(self):
            return self.getTypedRuleContext(MT22Parser.Init_exprContext,0)


        def COMMA(self, i:int=None):
            if i is None:
                return self.getTokens(MT22Parser.COMMA)
            else:
                return self.getToken(MT22Parser.COMMA, i)

        def condition_expr(self):
            return self.getTypedRuleContext(MT22Parser.Condition_exprContext,0)


        def update_expr(self):
            return self.getTypedRuleContext(MT22Parser.Update_exprContext,0)


        def RIGHT_PAREN(self):
            return self.getToken(MT22Parser.RIGHT_PAREN, 0)

        def statement(self):
            return self.getTypedRuleContext(MT22Parser.StatementContext,0)


        def getRuleIndex(self):
            return MT22Parser.RULE_for_stmt

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitFor_stmt" ):
                return visitor.visitFor_stmt(self)
            else:
                return visitor.visitChildren(self)




    def for_stmt(self):

        localctx = MT22Parser.For_stmtContext(self, self._ctx, self.state)
        self.enterRule(localctx, 64, self.RULE_for_stmt)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 348
            self.match(MT22Parser.FOR)
            self.state = 349
            self.match(MT22Parser.LEFT_PAREN)
            self.state = 350
            self.init_expr()
            self.state = 351
            self.match(MT22Parser.COMMA)
            self.state = 352
            self.condition_expr()
            self.state = 353
            self.match(MT22Parser.COMMA)
            self.state = 354
            self.update_expr()
            self.state = 355
            self.match(MT22Parser.RIGHT_PAREN)
            self.state = 356
            self.statement()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Init_exprContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def scalar_var(self):
            return self.getTypedRuleContext(MT22Parser.Scalar_varContext,0)


        def ASSIGN(self):
            return self.getToken(MT22Parser.ASSIGN, 0)

        def expr(self):
            return self.getTypedRuleContext(MT22Parser.ExprContext,0)


        def getRuleIndex(self):
            return MT22Parser.RULE_init_expr

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitInit_expr" ):
                return visitor.visitInit_expr(self)
            else:
                return visitor.visitChildren(self)




    def init_expr(self):

        localctx = MT22Parser.Init_exprContext(self, self._ctx, self.state)
        self.enterRule(localctx, 66, self.RULE_init_expr)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 358
            self.scalar_var()
            self.state = 359
            self.match(MT22Parser.ASSIGN)
            self.state = 360
            self.expr()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Condition_exprContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def expr(self):
            return self.getTypedRuleContext(MT22Parser.ExprContext,0)


        def getRuleIndex(self):
            return MT22Parser.RULE_condition_expr

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitCondition_expr" ):
                return visitor.visitCondition_expr(self)
            else:
                return visitor.visitChildren(self)




    def condition_expr(self):

        localctx = MT22Parser.Condition_exprContext(self, self._ctx, self.state)
        self.enterRule(localctx, 68, self.RULE_condition_expr)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 362
            self.expr()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Update_exprContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def expr(self):
            return self.getTypedRuleContext(MT22Parser.ExprContext,0)


        def getRuleIndex(self):
            return MT22Parser.RULE_update_expr

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitUpdate_expr" ):
                return visitor.visitUpdate_expr(self)
            else:
                return visitor.visitChildren(self)




    def update_expr(self):

        localctx = MT22Parser.Update_exprContext(self, self._ctx, self.state)
        self.enterRule(localctx, 70, self.RULE_update_expr)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 364
            self.expr()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class While_stmtContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def WHILE(self):
            return self.getToken(MT22Parser.WHILE, 0)

        def LEFT_PAREN(self):
            return self.getToken(MT22Parser.LEFT_PAREN, 0)

        def expr(self):
            return self.getTypedRuleContext(MT22Parser.ExprContext,0)


        def RIGHT_PAREN(self):
            return self.getToken(MT22Parser.RIGHT_PAREN, 0)

        def statement(self):
            return self.getTypedRuleContext(MT22Parser.StatementContext,0)


        def getRuleIndex(self):
            return MT22Parser.RULE_while_stmt

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitWhile_stmt" ):
                return visitor.visitWhile_stmt(self)
            else:
                return visitor.visitChildren(self)




    def while_stmt(self):

        localctx = MT22Parser.While_stmtContext(self, self._ctx, self.state)
        self.enterRule(localctx, 72, self.RULE_while_stmt)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 366
            self.match(MT22Parser.WHILE)
            self.state = 367
            self.match(MT22Parser.LEFT_PAREN)
            self.state = 368
            self.expr()
            self.state = 369
            self.match(MT22Parser.RIGHT_PAREN)
            self.state = 370
            self.statement()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Do_while_stmtContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def DO(self):
            return self.getToken(MT22Parser.DO, 0)

        def block_stmt(self):
            return self.getTypedRuleContext(MT22Parser.Block_stmtContext,0)


        def WHILE(self):
            return self.getToken(MT22Parser.WHILE, 0)

        def LEFT_PAREN(self):
            return self.getToken(MT22Parser.LEFT_PAREN, 0)

        def expr(self):
            return self.getTypedRuleContext(MT22Parser.ExprContext,0)


        def RIGHT_PAREN(self):
            return self.getToken(MT22Parser.RIGHT_PAREN, 0)

        def SEMI_COLON(self):
            return self.getToken(MT22Parser.SEMI_COLON, 0)

        def getRuleIndex(self):
            return MT22Parser.RULE_do_while_stmt

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitDo_while_stmt" ):
                return visitor.visitDo_while_stmt(self)
            else:
                return visitor.visitChildren(self)




    def do_while_stmt(self):

        localctx = MT22Parser.Do_while_stmtContext(self, self._ctx, self.state)
        self.enterRule(localctx, 74, self.RULE_do_while_stmt)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 372
            self.match(MT22Parser.DO)
            self.state = 373
            self.block_stmt()
            self.state = 374
            self.match(MT22Parser.WHILE)
            self.state = 375
            self.match(MT22Parser.LEFT_PAREN)
            self.state = 376
            self.expr()
            self.state = 377
            self.match(MT22Parser.RIGHT_PAREN)
            self.state = 378
            self.match(MT22Parser.SEMI_COLON)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Break_stmtContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def BREAK(self):
            return self.getToken(MT22Parser.BREAK, 0)

        def SEMI_COLON(self):
            return self.getToken(MT22Parser.SEMI_COLON, 0)

        def getRuleIndex(self):
            return MT22Parser.RULE_break_stmt

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitBreak_stmt" ):
                return visitor.visitBreak_stmt(self)
            else:
                return visitor.visitChildren(self)




    def break_stmt(self):

        localctx = MT22Parser.Break_stmtContext(self, self._ctx, self.state)
        self.enterRule(localctx, 76, self.RULE_break_stmt)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 380
            self.match(MT22Parser.BREAK)
            self.state = 381
            self.match(MT22Parser.SEMI_COLON)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Continue_stmtContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def CONTINUE(self):
            return self.getToken(MT22Parser.CONTINUE, 0)

        def SEMI_COLON(self):
            return self.getToken(MT22Parser.SEMI_COLON, 0)

        def getRuleIndex(self):
            return MT22Parser.RULE_continue_stmt

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitContinue_stmt" ):
                return visitor.visitContinue_stmt(self)
            else:
                return visitor.visitChildren(self)




    def continue_stmt(self):

        localctx = MT22Parser.Continue_stmtContext(self, self._ctx, self.state)
        self.enterRule(localctx, 78, self.RULE_continue_stmt)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 383
            self.match(MT22Parser.CONTINUE)
            self.state = 384
            self.match(MT22Parser.SEMI_COLON)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Return_stmtContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def RETURN(self):
            return self.getToken(MT22Parser.RETURN, 0)

        def SEMI_COLON(self):
            return self.getToken(MT22Parser.SEMI_COLON, 0)

        def expr(self):
            return self.getTypedRuleContext(MT22Parser.ExprContext,0)


        def getRuleIndex(self):
            return MT22Parser.RULE_return_stmt

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitReturn_stmt" ):
                return visitor.visitReturn_stmt(self)
            else:
                return visitor.visitChildren(self)




    def return_stmt(self):

        localctx = MT22Parser.Return_stmtContext(self, self._ctx, self.state)
        self.enterRule(localctx, 80, self.RULE_return_stmt)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 386
            self.match(MT22Parser.RETURN)
            self.state = 388
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if ((_la) & ~0x3f) == 0 and ((1 << _la) & 36028801046609988) != 0:
                self.state = 387
                self.expr()


            self.state = 390
            self.match(MT22Parser.SEMI_COLON)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Call_stmtContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def func_call(self):
            return self.getTypedRuleContext(MT22Parser.Func_callContext,0)


        def SEMI_COLON(self):
            return self.getToken(MT22Parser.SEMI_COLON, 0)

        def getRuleIndex(self):
            return MT22Parser.RULE_call_stmt

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitCall_stmt" ):
                return visitor.visitCall_stmt(self)
            else:
                return visitor.visitChildren(self)




    def call_stmt(self):

        localctx = MT22Parser.Call_stmtContext(self, self._ctx, self.state)
        self.enterRule(localctx, 82, self.RULE_call_stmt)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 392
            self.func_call()
            self.state = 393
            self.match(MT22Parser.SEMI_COLON)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Block_stmtContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def LEFT_BRACE(self):
            return self.getToken(MT22Parser.LEFT_BRACE, 0)

        def RIGHT_BRACE(self):
            return self.getToken(MT22Parser.RIGHT_BRACE, 0)

        def statements_list(self):
            return self.getTypedRuleContext(MT22Parser.Statements_listContext,0)


        def getRuleIndex(self):
            return MT22Parser.RULE_block_stmt

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitBlock_stmt" ):
                return visitor.visitBlock_stmt(self)
            else:
                return visitor.visitChildren(self)




    def block_stmt(self):

        localctx = MT22Parser.Block_stmtContext(self, self._ctx, self.state)
        self.enterRule(localctx, 84, self.RULE_block_stmt)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 395
            self.match(MT22Parser.LEFT_BRACE)
            self.state = 397
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if ((_la) & ~0x3f) == 0 and ((1 << _la) & 37447759725330432) != 0:
                self.state = 396
                self.statements_list()


            self.state = 399
            self.match(MT22Parser.RIGHT_BRACE)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Scalar_varContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ID(self):
            return self.getToken(MT22Parser.ID, 0)

        def getRuleIndex(self):
            return MT22Parser.RULE_scalar_var

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitScalar_var" ):
                return visitor.visitScalar_var(self)
            else:
                return visitor.visitChildren(self)




    def scalar_var(self):

        localctx = MT22Parser.Scalar_varContext(self, self._ctx, self.state)
        self.enterRule(localctx, 86, self.RULE_scalar_var)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 401
            self.match(MT22Parser.ID)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Boolean_typeContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def BOOLEAN(self):
            return self.getToken(MT22Parser.BOOLEAN, 0)

        def getRuleIndex(self):
            return MT22Parser.RULE_boolean_type

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitBoolean_type" ):
                return visitor.visitBoolean_type(self)
            else:
                return visitor.visitChildren(self)




    def boolean_type(self):

        localctx = MT22Parser.Boolean_typeContext(self, self._ctx, self.state)
        self.enterRule(localctx, 88, self.RULE_boolean_type)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 403
            self.match(MT22Parser.BOOLEAN)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Int_typeContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def INTEGER(self):
            return self.getToken(MT22Parser.INTEGER, 0)

        def getRuleIndex(self):
            return MT22Parser.RULE_int_type

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitInt_type" ):
                return visitor.visitInt_type(self)
            else:
                return visitor.visitChildren(self)




    def int_type(self):

        localctx = MT22Parser.Int_typeContext(self, self._ctx, self.state)
        self.enterRule(localctx, 90, self.RULE_int_type)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 405
            self.match(MT22Parser.INTEGER)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Float_typeContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def FLOAT(self):
            return self.getToken(MT22Parser.FLOAT, 0)

        def getRuleIndex(self):
            return MT22Parser.RULE_float_type

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitFloat_type" ):
                return visitor.visitFloat_type(self)
            else:
                return visitor.visitChildren(self)




    def float_type(self):

        localctx = MT22Parser.Float_typeContext(self, self._ctx, self.state)
        self.enterRule(localctx, 92, self.RULE_float_type)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 407
            self.match(MT22Parser.FLOAT)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class String_typeContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def STRING(self):
            return self.getToken(MT22Parser.STRING, 0)

        def getRuleIndex(self):
            return MT22Parser.RULE_string_type

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitString_type" ):
                return visitor.visitString_type(self)
            else:
                return visitor.visitChildren(self)




    def string_type(self):

        localctx = MT22Parser.String_typeContext(self, self._ctx, self.state)
        self.enterRule(localctx, 94, self.RULE_string_type)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 409
            self.match(MT22Parser.STRING)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Void_typeContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def VOID(self):
            return self.getToken(MT22Parser.VOID, 0)

        def getRuleIndex(self):
            return MT22Parser.RULE_void_type

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitVoid_type" ):
                return visitor.visitVoid_type(self)
            else:
                return visitor.visitChildren(self)




    def void_type(self):

        localctx = MT22Parser.Void_typeContext(self, self._ctx, self.state)
        self.enterRule(localctx, 96, self.RULE_void_type)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 411
            self.match(MT22Parser.VOID)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Auto_typeContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def AUTO(self):
            return self.getToken(MT22Parser.AUTO, 0)

        def getRuleIndex(self):
            return MT22Parser.RULE_auto_type

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitAuto_type" ):
                return visitor.visitAuto_type(self)
            else:
                return visitor.visitChildren(self)




    def auto_type(self):

        localctx = MT22Parser.Auto_typeContext(self, self._ctx, self.state)
        self.enterRule(localctx, 98, self.RULE_auto_type)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 413
            self.match(MT22Parser.AUTO)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Array_typeContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ARRAY(self):
            return self.getToken(MT22Parser.ARRAY, 0)

        def LEFT_BRACK(self):
            return self.getToken(MT22Parser.LEFT_BRACK, 0)

        def dimensions(self):
            return self.getTypedRuleContext(MT22Parser.DimensionsContext,0)


        def RIGHT_BRACK(self):
            return self.getToken(MT22Parser.RIGHT_BRACK, 0)

        def OF(self):
            return self.getToken(MT22Parser.OF, 0)

        def atomic_type(self):
            return self.getTypedRuleContext(MT22Parser.Atomic_typeContext,0)


        def getRuleIndex(self):
            return MT22Parser.RULE_array_type

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitArray_type" ):
                return visitor.visitArray_type(self)
            else:
                return visitor.visitChildren(self)




    def array_type(self):

        localctx = MT22Parser.Array_typeContext(self, self._ctx, self.state)
        self.enterRule(localctx, 100, self.RULE_array_type)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 415
            self.match(MT22Parser.ARRAY)
            self.state = 416
            self.match(MT22Parser.LEFT_BRACK)
            self.state = 417
            self.dimensions()
            self.state = 418
            self.match(MT22Parser.RIGHT_BRACK)
            self.state = 419
            self.match(MT22Parser.OF)
            self.state = 420
            self.atomic_type()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class DimensionsContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def INTEGER_LIT(self, i:int=None):
            if i is None:
                return self.getTokens(MT22Parser.INTEGER_LIT)
            else:
                return self.getToken(MT22Parser.INTEGER_LIT, i)

        def COMMA(self, i:int=None):
            if i is None:
                return self.getTokens(MT22Parser.COMMA)
            else:
                return self.getToken(MT22Parser.COMMA, i)

        def getRuleIndex(self):
            return MT22Parser.RULE_dimensions

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitDimensions" ):
                return visitor.visitDimensions(self)
            else:
                return visitor.visitChildren(self)




    def dimensions(self):

        localctx = MT22Parser.DimensionsContext(self, self._ctx, self.state)
        self.enterRule(localctx, 102, self.RULE_dimensions)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 422
            self.match(MT22Parser.INTEGER_LIT)
            self.state = 427
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==22:
                self.state = 423
                self.match(MT22Parser.COMMA)
                self.state = 424
                self.match(MT22Parser.INTEGER_LIT)
                self.state = 429
                self._errHandler.sync(self)
                _la = self._input.LA(1)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Atomic_typeContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def boolean_type(self):
            return self.getTypedRuleContext(MT22Parser.Boolean_typeContext,0)


        def int_type(self):
            return self.getTypedRuleContext(MT22Parser.Int_typeContext,0)


        def float_type(self):
            return self.getTypedRuleContext(MT22Parser.Float_typeContext,0)


        def string_type(self):
            return self.getTypedRuleContext(MT22Parser.String_typeContext,0)


        def getRuleIndex(self):
            return MT22Parser.RULE_atomic_type

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitAtomic_type" ):
                return visitor.visitAtomic_type(self)
            else:
                return visitor.visitChildren(self)




    def atomic_type(self):

        localctx = MT22Parser.Atomic_typeContext(self, self._ctx, self.state)
        self.enterRule(localctx, 104, self.RULE_atomic_type)
        try:
            self.state = 434
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [34]:
                self.enterOuterAlt(localctx, 1)
                self.state = 430
                self.boolean_type()
                pass
            elif token in [42]:
                self.enterOuterAlt(localctx, 2)
                self.state = 431
                self.int_type()
                pass
            elif token in [38]:
                self.enterOuterAlt(localctx, 3)
                self.state = 432
                self.float_type()
                pass
            elif token in [44]:
                self.enterOuterAlt(localctx, 4)
                self.state = 433
                self.string_type()
                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx



    def sempred(self, localctx:RuleContext, ruleIndex:int, predIndex:int):
        if self._predicates == None:
            self._predicates = dict()
        self._predicates[13] = self.logical_expr_1_sempred
        self._predicates[14] = self.adding_expr_sempred
        self._predicates[15] = self.multiplying_expr_sempred
        pred = self._predicates.get(ruleIndex, None)
        if pred is None:
            raise Exception("No predicate with index:" + str(ruleIndex))
        else:
            return pred(localctx, predIndex)

    def logical_expr_1_sempred(self, localctx:Logical_expr_1Context, predIndex:int):
            if predIndex == 0:
                return self.precpred(self._ctx, 2)
         

    def adding_expr_sempred(self, localctx:Adding_exprContext, predIndex:int):
            if predIndex == 1:
                return self.precpred(self._ctx, 2)
         

    def multiplying_expr_sempred(self, localctx:Multiplying_exprContext, predIndex:int):
            if predIndex == 2:
                return self.precpred(self._ctx, 2)
         




