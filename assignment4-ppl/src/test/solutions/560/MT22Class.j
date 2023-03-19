.source MT22Class.java
.class public MT22Class
.super java.lang.Object

.method public static foo(Ljava/lang/String;F)Ljava/lang/String;
.var 0 is a Ljava/lang/String; from Label0 to Label1
.var 1 is b F from Label0 to Label1
Label0:
.var 2 is c I from Label0 to Label1
	iconst_2
	istore_2
.var 3 is d F from Label0 to Label1
	iload_2
	iconst_1
	iadd
	i2f
	fstore_3
.var 4 is f [Ljava/lang/String; from Label0 to Label1
	iconst_5
	anewarray java/lang/String
	astore 4
	aload 4
	iconst_1
	aaload
	areturn
Label1:
.limit stack 5
.limit locals 5
.end method

.method public static bar(ILjava/lang/String;)V
.var 0 is a I from Label0 to Label1
.var 1 is b Ljava/lang/String; from Label0 to Label1
Label0:
	ldc "Hello"
	ldc 1.2312
	invokestatic MT22Class/foo(Ljava/lang/String;F)Ljava/lang/String;
	invokestatic io/printString(Ljava/lang/String;)V
Label1:
	return
.limit stack 2
.limit locals 2
.end method

.method public static main([Ljava/lang/String;)V
.var 0 is args [Ljava/lang/String; from Label0 to Label1
Label0:
Label1:
	return
.limit stack 0
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
