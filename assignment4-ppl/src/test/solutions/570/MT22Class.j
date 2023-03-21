.source MT22Class.java
.class public MT22Class
.super java.lang.Object

.method public static foo(ILjava/lang/String;)Ljava/lang/String;
.var 0 is a I from Label0 to Label1
.var 1 is b Ljava/lang/String; from Label0 to Label1
Label0:
.var 2 is f [Ljava/lang/String; from Label0 to Label1
	iconst_5
	anewarray java/lang/String
	dup
	iconst_0
	aload_1
	aastore
	astore_2
	aload_2
	iconst_0
	aaload
	areturn
Label1:
.limit stack 5
.limit locals 3
.end method

.method public static foo1(Ljava/lang/String;ILjava/lang/String;)Ljava/lang/String;
.var 0 is a Ljava/lang/String; from Label0 to Label1
.var 1 is b I from Label0 to Label1
.var 2 is c Ljava/lang/String; from Label0 to Label1
.var 3 is a I from Label0 to Label1
	iload_1
	istore_3
.var 4 is b Ljava/lang/String; from Label0 to Label1
	aload_0
	astore 4
Label0:
.var 5 is f [Ljava/lang/String; from Label0 to Label1
	iconst_5
	anewarray java/lang/String
	dup
	iconst_0
	aload_0
	aastore
	astore 5
	aload 5
	iconst_0
	aaload
	areturn
Label1:
.limit stack 7
.limit locals 6
.end method

.method public static bar(ILjava/lang/String;)V
.var 0 is a I from Label0 to Label1
.var 1 is b Ljava/lang/String; from Label0 to Label1
.var 2 is a Ljava/lang/String; from Label0 to Label1
	ldc "Hello"
	aload_1
	invokevirtual java/lang/String/concat(Ljava/lang/String;)Ljava/lang/String;
	astore_2
.var 3 is b I from Label0 to Label1
	iload_0
	istore_3
.var 4 is c Ljava/lang/String; from Label0 to Label1
	ldc "Hello"
	aload_1
	invokevirtual java/lang/String/concat(Ljava/lang/String;)Ljava/lang/String;
	astore 4
.var 5 is a I from Label0 to Label1
	iload_3
	istore 5
.var 6 is b Ljava/lang/String; from Label0 to Label1
	aload_2
	astore 6
Label0:
.var 7 is i I from Label0 to Label1
	iconst_1
	istore 7
Label3:
	iload 7
	bipush 10
	if_icmpge Label6
	iconst_1
	goto Label7
Label6:
	iconst_0
Label7:
	ifle Label5
	iload_0
	i2f
	invokestatic io/writeFloat(F)V
Label4:
	iload 7
	iconst_1
	iadd
	istore 7
	goto Label3
Label5:
	iload_0
	iconst_2
	if_icmpne Label8
	iconst_1
	goto Label9
Label8:
	iconst_0
Label9:
	ifgt Label10
	goto Label11
Label10:
	return
Label11:
	bipush 111
	ldc "Hello"
	aload_1
	invokevirtual java/lang/String/concat(Ljava/lang/String;)Ljava/lang/String;
	invokestatic MT22Class/foo(ILjava/lang/String;)Ljava/lang/String;
	invokestatic io/printString(Ljava/lang/String;)V
	aload 4
	invokestatic io/printString(Ljava/lang/String;)V
Label1:
	return
.limit stack 12
.limit locals 8
.end method

.method public static main([Ljava/lang/String;)V
.var 0 is args [Ljava/lang/String; from Label0 to Label1
Label0:
	bipush 10
	ldc "World!"
	invokestatic MT22Class/bar(ILjava/lang/String;)V
Label1:
	return
.limit stack 2
.limit locals 1
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
