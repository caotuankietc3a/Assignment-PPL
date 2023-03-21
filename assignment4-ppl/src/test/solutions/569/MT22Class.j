.source MT22Class.java
.class public MT22Class
.super java.lang.Object

.method public static foo1(Ljava/lang/String;IFZ)I
.var 0 is a Ljava/lang/String; from Label0 to Label1
.var 1 is b I from Label0 to Label1
.var 2 is c F from Label0 to Label1
.var 3 is d Z from Label0 to Label1
Label0:
	iload_1
	iconst_1
	iadd
	ireturn
Label1:
.limit stack 2
.limit locals 4
.end method

.method public static foo(Ljava/lang/String;I)Ljava/lang/String;
.var 0 is a Ljava/lang/String; from Label0 to Label1
.var 1 is b I from Label0 to Label1
.var 2 is a Ljava/lang/String; from Label0 to Label1
	ldc "Hello"
	aload_0
	invokevirtual java/lang/String/concat(Ljava/lang/String;)Ljava/lang/String;
	astore_2
.var 3 is b I from Label0 to Label1
	sipush 134
	istore_3
.var 4 is c F from Label0 to Label1
	ldc 12.0
	fstore 4
.var 5 is d Z from Label0 to Label1
	iconst_0
	istore 5
Label0:
.var 6 is f [Ljava/lang/String; from Label0 to Label1
	iconst_5
	anewarray java/lang/String
	dup
	iconst_0
	ldc "a"
	aastore
	astore 6
	aload 6
	iconst_0
	aaload
	areturn
Label1:
.limit stack 10
.limit locals 7
.end method

.method public static bar(ILjava/lang/String;)V
.var 0 is a I from Label0 to Label1
.var 1 is x Ljava/lang/String; from Label0 to Label1
.var 2 is a Ljava/lang/String; from Label0 to Label1
	ldc "Hello"
	aload_1
	invokevirtual java/lang/String/concat(Ljava/lang/String;)Ljava/lang/String;
	astore_2
.var 3 is b I from Label0 to Label1
	bipush 123
	istore_3
.var 4 is a Ljava/lang/String; from Label0 to Label1
	ldc "Hello"
	aload_2
	invokevirtual java/lang/String/concat(Ljava/lang/String;)Ljava/lang/String;
	astore 4
.var 5 is b I from Label0 to Label1
	sipush 134
	istore 5
.var 6 is c F from Label0 to Label1
	ldc 12.0
	fstore 6
.var 7 is d Z from Label0 to Label1
	iconst_0
	istore 7
Label0:
	iload_0
	iload_3
	iadd
	i2f
	fload 6
	fadd
	invokestatic io/writeFloat(F)V
Label1:
	return
.limit stack 9
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
