.source MT22Class.java
.class public MT22Class
.super java.lang.Object
.field static s Ljava/lang/String;

.method public static random(I)Ljava/lang/String;
.var 0 is n I from Label0 to Label1
Label0:
	ldc ""
	putstatic MT22Class.s Ljava/lang/String;
.var 1 is i I from Label0 to Label1
	iconst_0
	istore_1
Label3:
	iload_1
	iload_0
	if_icmpge Label6
	iconst_1
	goto Label7
Label6:
	iconst_0
Label7:
	ifle Label5
	getstatic MT22Class.s Ljava/lang/String;
	ldc "!"
	invokevirtual java/lang/String/concat(Ljava/lang/String;)Ljava/lang/String;
	putstatic MT22Class.s Ljava/lang/String;
Label4:
	iload_1
	iconst_1
	iadd
	istore_1
	goto Label3
Label5:
	getstatic MT22Class.s Ljava/lang/String;
	areturn
Label1:
.limit stack 4
.limit locals 2
.end method

.method public static main([Ljava/lang/String;)V
.var 0 is args [Ljava/lang/String; from Label0 to Label1
Label0:
.var 1 is n I from Label0 to Label1
	bipush 10
	istore_1
	ldc "The random string length n is "
	iload_1
	invokestatic MT22Class/random(I)Ljava/lang/String;
	invokevirtual java/lang/String/concat(Ljava/lang/String;)Ljava/lang/String;
	invokestatic io/printString(Ljava/lang/String;)V
Label1:
	return
.limit stack 3
.limit locals 2
.end method

.method public <init>()V
.var 0 is this LMT22Class; from Label0 to Label1
Label0:
	aload_0
	invokespecial java/lang/Object/<init>()V
Label1:
	return
.limit stack 1
.limit locals 1
.end method

.method public static <clinit>()V
Label0:
Label1:
	return
.limit stack 0
.limit locals 0
.end method
