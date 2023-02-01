import unittest
from TestUtils import TestLexer


class LexerSuite(unittest.TestCase):

    """TEST COMMENT"""

    def test_comment_1(self):
        self.assertTrue(TestLexer.test(
            "/* A C-style comment */", "<EOF>", 101))

    def test_comment_2(self):
        self.assertTrue(TestLexer.test(
            "/* A C-sty\nle comment */", "<EOF>", 102))

    def test_comment_3(self):
        self.assertTrue(TestLexer.test(
            """// A C-style comment
""", "<EOF>", 103))

    def test_comment_4(self):
        self.assertTrue(TestLexer.test(
            "// A C-style\n /* comment */", "<EOF>", 104))

    def test_comment_5(self):
        self.assertTrue(TestLexer.test(
            "// A C-style/* comment */", "<EOF>", 105))

    def test_comment_6(self):
        self.assertTrue(TestLexer.test(
            "/* // A C-style comment */", "<EOF>", 106))

    def test_comment_7(self):
        self.assertTrue(TestLexer.test(
            "/* /* A C-style */ */", "*,/,<EOF>", 107))

    """TEST IDENTIFIERS"""

    def test_id_1(self):
        self.assertTrue(TestLexer.test("abc", "abc,<EOF>", 108))

    def test_id_2(self):
        self.assertTrue(TestLexer.test("abc a12", "abc,a12,<EOF>", 109))

    def test_id_3(self):
        self.assertTrue(TestLexer.test("abc A12", "abc,A12,<EOF>", 110))

    def test_id_4(self):
        self.assertTrue(TestLexer.test(
            "abc?svn", "abc,Error Token ?", 111))

    def test_id_5(self):
        self.assertTrue(TestLexer.test("0a12", "0,a12,<EOF>", 112))

    def test_id_6(self):
        self.assertTrue(TestLexer.test("abc_123", "abc_123,<EOF>", 113))

    def test_id_7(self):
        self.assertTrue(TestLexer.test("ABC_123", "ABC_123,<EOF>", 114))

    def test_id_8(self):
        self.assertTrue(TestLexer.test("aBc_d123", "aBc_d123,<EOF>", 115))

    def test_id_9(self):
        self.assertTrue(TestLexer.test("abC_D123", "abC_D123,<EOF>", 116))

    def test_id_10(self):
        self.assertTrue(TestLexer.test(
            "_abcABC__", "_abcABC__,<EOF>", 117))

    """TEST LITERALS"""

    def test_int_lit_1(self):
        self.assertTrue(
            TestLexer.test(
                r"""0""",
                "0,<EOF>",
                118,
            )
        )

    def test_int_lit_2(self):
        self.assertTrue(
            TestLexer.test(
                r"""123456789""",
                "123456789,<EOF>",
                119,
            )
        )

    def test_int_lit_3(self):
        self.assertTrue(
            TestLexer.test(
                r"""-1230""",
                "-,1230,<EOF>",
                120,
            )
        )

    def test_int_lit_4(self):
        self.assertTrue(
            TestLexer.test(
                r"""1_12""",
                "112,<EOF>",
                121,
            )
        )

    def test_int_lit_5(self):
        self.assertTrue(
            TestLexer.test(
                r"""123_456_789""",
                "123456789,<EOF>",
                122,
            )
        )

    def test_int_lit_6(self):
        self.assertTrue(
            TestLexer.test(
                r"""341_""",
                "341,_,<EOF>",
                123,
            )
        )

    def test_int_lit_7(self):
        self.assertTrue(
            TestLexer.test(
                r"""1_23_34_""",
                "12334,_,<EOF>",
                124,
            )
        )

    def test_float_lit_1(self):
        self.assertTrue(
            TestLexer.test(
                r"""0.0""",
                "0.0,<EOF>",
                125,
            )
        )

    def test_float_lit_2(self):
        self.assertTrue(
            TestLexer.test(
                r""".5555""",
                ".5555,<EOF>",
                126,
            )
        )

    def test_float_lit_3(self):
        self.assertTrue(
            TestLexer.test(
                r"""189.00000""",
                "189.00000,<EOF>",
                127,
            )
        )

    def test_float_lit_4(self):
        self.assertTrue(
            TestLexer.test(
                r"""157.""",
                "157.,<EOF>",
                128,
            )
        )

    def test_float_lit_5(self):
        self.assertTrue(
            TestLexer.test(
                r"""1_2_3_4.""",
                "1234.,<EOF>",
                129,
            )
        )

    def test_float_lit_6(self):
        self.assertTrue(
            TestLexer.test(
                r"""1_2_3_56.1234""",
                "12356.1234,<EOF>",
                130,
            )
        )

    def test_float_lit_7(self):
        self.assertTrue(
            TestLexer.test(
                r"""1_.34""",
                "1,_,.34,<EOF>",
                131,
            )
        )

    def test_float_lit_8(self):
        self.assertTrue(
            TestLexer.test(
                r"""12e8""",
                "12e8,<EOF>",
                132,
            )
        )

    def test_float_lit_9(self):
        self.assertTrue(
            TestLexer.test(
                r"""0.33E-3""",
                "0.33E-3,<EOF>",
                133,
            )
        )

    def test_float_lit_10(self):
        self.assertTrue(
            TestLexer.test(
                r"""128e+42""",
                "128e+42,<EOF>",
                134,
            )
        )

    def test_float_lit_11(self):
        self.assertTrue(
            TestLexer.test(
                r"""1_2_8e-42""",
                "128e-42,<EOF>",
                135,
            )
        )

    def test_boolean_lit(self):
        self.assertTrue(TestLexer.test(
            r"""true false""", "true,false,<EOF>", 136,))

    def test_string_lit_1(self):
        self.assertTrue(TestLexer.test(
            """\"This is \\t a string containing tab \t\"""", "This is \\t a string containing tab 	,<EOF>", 137,))

    def test_string_lit_2(self):
        self.assertTrue(TestLexer.test(
            """\"He asked me: \\\"Where is John?\\\"\"""", "He asked me: \\\"Where is John?\\\",<EOF>", 138,))

    def test_string_lit_3(self):
        self.assertTrue(TestLexer.test("\"He asked me: \'\"Where is John?\'\"\"",
                                       "He asked me: \'\"Where is John?\'\",<EOF>", 139))

    def test_string_lit_4(self):
        self.assertTrue(TestLexer.test(
            "\"\\b \\' He is my ex's man\"", "\\b \\' He is my ex's man,<EOF>", 140))

    def test_string_lit_5(self):
        self.assertTrue(TestLexer.test(
            "\"She is Tam\'s girlfriend.\"", "She is Tam\'s girlfriend.,<EOF>", 141))

    """TEST ERROR"""

    def test_string_unclose_1(self):
        self.assertTrue(TestLexer.test("\"He is a man",
                        "Unclosed String: He is a man", 142))

    def test_string_unclose_2(self):
        self.assertTrue(TestLexer.test("\"abc \\n \\f 's def",
                        "Unclosed String: abc \\n \\f 's def", 143))

    def test_string_unclose_3(self):
        self.assertTrue(TestLexer.test("\"He is \\b a man",
                        "Unclosed String: He is \\b a man", 144))

    def test_string_unclose_4(self):
        self.assertTrue(TestLexer.test("\"It is a unclosed \\n string",
                        "Unclosed String: It is a unclosed \\n string", 145))

    def test_string_unclose_5(self):
        self.assertTrue(TestLexer.test("\"This is a \\t string \\n containing tab \" \"He asked \\n me: '\"Where '\"is'\" John?'\"\" \"I am not closed",
                        "This is a \\t string \\n containing tab ,He asked \\n me: '\"Where '\"is'\" John?'\",Unclosed String: I am not closed", 146))

    def test_string_illegal_esc_1(self):
        self.assertTrue(TestLexer.test("\"I have an escape sequence \'\"Here it is \\k\'\"\"",
                        "Illegal Escape In String: I have an escape sequence \'\"Here it is \\k", 147))

    def test_string_illegal_esc_2(self):
        self.assertTrue(TestLexer.test("\"\\a He is a man\"",
                        "Illegal Escape In String: \\a", 148))

    def test_string_illegal_esc_3(self):
        self.assertTrue(TestLexer.test("\"\\\\ He is a \\\\ \\\' 19-year-old man \\a\"",
                        "Illegal Escape In String: \\\\ He is a \\\\ \\\' 19-year-old man \\a", 149))

    """TEST OPERATORS"""

    def test_operators_1(self):
        self.assertTrue(TestLexer.test("===", "==,=,<EOF>", 150))

    def test_operators_2(self):
        self.assertTrue(TestLexer.test("====", "==,==,<EOF>", 151))

    def test_operators_3(self):
        self.assertTrue(TestLexer.test("||||", "||,||,<EOF>", 152))

    def test_operators_4(self):
        self.assertTrue(TestLexer.test("[a,1,b]", "[,a,,,1,,,b,],<EOF>", 153))

    def test_operators_5(self):
        self.assertTrue(TestLexer.test("*/%::!=!<><===.+.",
                        "*,/,%,::,!=,!,<,>,<=,==,.,+,.,<EOF>", 154))

    def test_operators_6(self):
        self.assertTrue(TestLexer.test("&&&", "&&,Error Token &", 155))

    def test_operators_7(self):
        self.assertTrue(TestLexer.test("-12_3", "-,123,<EOF>", 156))

    """TEST KEYWORDS"""

    def test_keywords_1(self):
        self.assertTrue(TestLexer.test("auto break boolean do else",
                        "auto,break,boolean,do,else,<EOF>", 157))

    def test_keywords_2(self):
        self.assertTrue(TestLexer.test(
            "false float for function if", "false,float,for,function,if,<EOF>", 158))

    def test_keywords_3(self):
        self.assertTrue(TestLexer.test(
            "integer return string true void", "integer,return,string,true,void,<EOF>", 159))

    def test_keywords_4(self):
        self.assertTrue(TestLexer.test(
            "while out continue of inherit", "while,out,continue,of,inherit,<EOF>", 160))

    """TEST SEPERATORS"""

    def test_seperators_1(self):
        self.assertTrue(TestLexer.test(
            "() [] . , ; : {} =", "(,),[,],.,,,;,:,{,},=,<EOF>", 161))

    """OTHER TESTS"""

    def test_others_1(self):
        self.assertTrue(TestLexer.test("""
a abc a123 a_ a_bc a_bc123 a_123 a_123bc a_bc_123
_ _abc _123 _abc123 _abc_123 _123_abc
__ ____ ____123____
abc ABC aBC Abc _ABC __ABc __123ABc
h98f394__VWT_b5_VT_YGU87udhf__T_
        """, "a,abc,a123,a_,a_bc,a_bc123,a_123,a_123bc,a_bc_123,_,_abc,_123,_abc123,_abc_123,_123_abc,__,____,____123____,abc,ABC,aBC,Abc,_ABC,__ABc,__123ABc,h98f394__VWT_b5_VT_YGU87udhf__T_,<EOF>", 162))

    def test_others_2(self):
        self.assertTrue(TestLexer.test("""
e-12 e+12 . 1e 12e 12.05e .05e ee e01 .12 143e
        """, "e,-,12,e,+,12,.,1,e,12,e,12.05,e,.05,e,ee,e01,.12,143,e,<EOF>", 163))

    def test_others_3(self):
        self.assertTrue(TestLexer.test("""
integer[5] a;
{1, 2, 3}
{2.3, 4.2, 102e3}
        """, "integer,[,5,],a,;,{,1,,,2,,,3,},{,2.3,,,4.2,,,102e3,},<EOF>", 164))

    def test_others_4(self):
        self.assertTrue(TestLexer.test("""
" hello lexer \t "     asdf
        """, ' hello lexer 	 ,asdf,<EOF>', 165))

    def test_others_5(self):
        self.assertTrue(TestLexer.test("""
"Newline
	multiple lines
"
""", "Unclosed String: Newline", 166))

    def test_others_6(self):
        self.assertTrue(TestLexer.test("""
"abc" 123 __123 "abc xyz"
" abc\\m "
""", r"""abc,123,__123,abc xyz,Illegal Escape In String:  abc\m""", 167))

    def test_others_7(self):
        self.assertTrue(TestLexer.test("""
!== != &
""", r"""!=,=,!=,Error Token &""", 168))

    def test_others_8(self):
        self.assertTrue(TestLexer.test(r"""
^ % $ # ... \
""", r"""Error Token ^""", 169))

    def test_others_9(self):
        self.assertTrue(TestLexer.test(r"""
a := a && 1
""", r"""a,:,=,a,&&,1,<EOF>""", 170))

    def test_others_10(self):
        self.assertTrue(TestLexer.test(r"""
integer a = a|b;
""", r"""integer,a,=,a,Error Token |""", 171))

    def test_others_11(self):
        self.assertTrue(TestLexer.test(r"""
{1, 5, 7, 12}
""", r"""{,1,,,5,,,7,,,12,},<EOF>""", 172))

    def test_others_12(self):
        self.assertTrue(TestLexer.test(r"""
{"Kangxi", "Yongzheng", "Qianlong"}
""", r"""{,Kangxi,,,Yongzheng,,,Qianlong,},<EOF>""", 173))

    def test_others_13(self):
        self.assertTrue(TestLexer.test(r"""
00001.1111000000
0e-4
000000001e-40000
""", r"""0,0,0,0,1.1111000000,0e-4,0,0,0,0,0,0,0,0,1e-40000,<EOF>""", 174))

    def test_others_14(self):
        self.assertTrue(TestLexer.test(r"""
"abc - xyz"
"abc \ xyz"
""", r"""abc - xyz,Illegal Escape In String: abc \ """, 175))

    def test_others_15(self):
        self.assertTrue(TestLexer.test(r"""
"abc - xyz"
"abc \yyz"
""", r"""abc - xyz,Illegal Escape In String: abc \y""", 176))

    def test_others_16(self):
        self.assertTrue(TestLexer.test(r"""
"\"
""", r"""Unclosed String: \"""", 177))

    def test_others_17(self):
        self.assertTrue(TestLexer.test(r"""
s = "string
"
a = 4
g = 9
""", r"""s,=,Unclosed String: string""", 178))

    def test_others_18(self):
        self.assertTrue(TestLexer.test(r"""
s = "string "
a = 4
g = 9
""", r"""s,=,string ,a,=,4,g,=,9,<EOF>""", 179))

    def test_others_19(self):
        self.assertTrue(TestLexer.test(r"""
float a, b, c;
boolean x, y, z;
integer g, h, y;
""", r"""float,a,,,b,,,c,;,boolean,x,,,y,,,z,;,integer,g,,,h,,,y,;,<EOF>""", 180))

    def test_others_20(self):
        self.assertTrue(TestLexer.test(r"""
void nty() {
	// This is readLine()
}
""", r"""void,nty,(,),{,},<EOF>""", 181))

    def test_others_21(self):
        self.assertTrue(TestLexer.test(r"""
/*
    =======================================
    Comment here
    =======================================
*/
""", r"""<EOF>""", 182))

    def test_others_22(self):
        self.assertTrue(TestLexer.test(r"""
integer foo(){};
""", r"""integer,foo,(,),{,},;,<EOF>""", 183))

    def test_others_23(self):
        self.assertTrue(TestLexer.test(r"""
integer foo();
	while false{
		hard_work();
			if true then break;
		}
""", r"""integer,foo,(,),;,while,false,{,hard_work,(,),;,if,true,then,break,;,},<EOF>""", 184))

    def test_others_24(self):
        self.assertTrue(TestLexer.test(r"""
s = "abc,
""", r"""s,=,Unclosed String: abc,""", 185))

    def test_others_25(self):
        self.assertTrue(TestLexer.test(r"""
s = "abc                   ;
a = "xyz"
""", r"""s,=,Unclosed String: abc                   ;""", 186))

    def test_others_26(self):
        self.assertTrue(TestLexer.test(r"""
s = "abc            "       ;
a = "xyz"
""", r"""s,=,abc            ,;,a,=,xyz,<EOF>""", 187))

    def test_others_27(self):
        self.assertTrue(TestLexer.test(r"""
"\n\n\n\n\n\n\n\n\n"
""", r"""\n\n\n\n\n\n\n\n\n,<EOF>""", 188))

    def test_others_28(self):
        self.assertTrue(TestLexer.test(r"""
\r\r\r\r\r\r\r\r\r\
""", """Error Token \\""", 189))

    def test_others_29(self):
        self.assertTrue(TestLexer.test(r"""
// (,true,[ acb40 mod for,),with
= boolean .. p104c ] function do z71ae of < begin if break with of procedure b4169 break - of = = function div
/* <= : a41aa,while,m8bcd .. E8869,,,string*/
""", """=,boolean,.,.,p104c,],function,do,z71ae,of,<,begin,if,break,with,of,procedure,b4169,break,-,of,=,=,function,div,<EOF>""", 190))

    def test_others_30(self):
        self.assertTrue(TestLexer.test(r"""
: .. do n1afd then - of Be562 ] end * > .. string * + W0977 var function else or mod if not
""", """:,.,.,do,n1afd,then,-,of,Be562,],end,*,>,.,.,string,*,+,W0977,var,function,else,or,mod,if,not,<EOF>""", 191))

    def test_others_31(self):
        input = """
 powerFunc : function integer (base : integer, power : integer) {
  if (power == 0)
    return 1;
  else
    return (base * powerFunc(base, power - 1));
}

mod: function integer (num: array [5] of integer , a: integer) {
  res, i : integer  = 0, -1;

  for (i = 0; i < 5; i+1)
    res = (res * 10 + num[i] - "0") % a;

  return res;
}
"""
        expect = "powerFunc,:,function,integer,(,base,:,integer,,,power,:,integer,),{,if,(,power,==,0,),return,1,;,else,return,(,base,*,powerFunc,(,base,,,power,-,1,),),;,},mod,:,function,integer,(,num,:,array,[,5,],of,integer,,,a,:,integer,),{,res,,,i,:,integer,=,0,,,-,1,;,for,(,i,=,0,;,i,<,5,;,i,+,1,),res,=,(,res,*,10,+,num,[,i,],-,0,),%,a,;,return,res,;,},<EOF>"
        self.assertTrue(TestLexer.test(input, expect, 192))

    def test_others_32(self):
        input = """
mod: function integer (num: array [5] of integer , a: integer) {
  res, i : integer  = 0, -1;

  for (i = 0; i < 5; i+1)
    res = (res * 10 + num[i] - "0") % a;

  return res;
}
"""
        expect = "mod,:,function,integer,(,num,:,array,[,5,],of,integer,,,a,:,integer,),{,res,,,i,:,integer,=,0,,,-,1,;,for,(,i,=,0,;,i,<,5,;,i,+,1,),res,=,(,res,*,10,+,num,[,i,],-,0,),%,a,;,return,res,;,},<EOF>"
        self.assertTrue(TestLexer.test(input, expect, 193))

    def test_others_33(self):
        input = """
mod: function integer (num: array [5] of integer , a: integer) {
  res, i : integer  = 0, -1;
  return res;
}
"""
        expect = "mod,:,function,integer,(,num,:,array,[,5,],of,integer,,,a,:,integer,),{,res,,,i,:,integer,=,0,,,-,1,;,return,res,;,},<EOF>"
        self.assertTrue(TestLexer.test(input, expect, 194))

    def test_others_34(self):
        input = """
TESTFUNCTION: function integer (out num: array [5] of integer) {
  return 0;
}
"""
        expect = "TESTFUNCTION,:,function,integer,(,out,num,:,array,[,5,],of,integer,),{,return,0,;,},<EOF>"
        self.assertTrue(TestLexer.test(input, expect, 195))

    def test_others_35(self):
        input = """
return 0;
"""
        expect = "return,0,;,<EOF>"
        self.assertTrue(TestLexer.test(input, expect, 196))

    def test_others_36(self):
        input = """
break;
"""
        expect = "break,;,<EOF>"
        self.assertTrue(TestLexer.test(input, expect, 197))

    def test_others_37(self):
        input = """
do 
    statements
while()
"""
        expect = "do,statements,while,(,),<EOF>"
        self.assertTrue(TestLexer.test(input, expect, 198))

    def test_others_38(self):
        input = """
while(true) statements
"""
        expect = "while,(,true,),statements,<EOF>"
        self.assertTrue(TestLexer.test(input, expect, 199))

    def test_others_39(self):
        input = """
for(,,) statements
"""
        expect = "for,(,,,,,),statements,<EOF>"
        self.assertTrue(TestLexer.test(input, expect, 200))
