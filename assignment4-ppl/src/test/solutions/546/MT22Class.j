.source MT22Class.java
.class public MT22Class
.super java.lang.Object
.field static x I

.method public static inc(II)V
.var 0 is n I from Label0 to Label1
.var 1 is delta I from Label0 to Label1
Label0:
	iload_0
	iload_1
	iadd
	istore_0
	iload_0
	invokestatic io/printInteger(I)V
Label1:
	return
.limit stack 2
.limit locals 2
.end method

.method public static main([Ljava/lang/String;)V
.var 0 is args [Ljava/lang/String; from Label0 to Label1
Label0:
.var 1 is delta I from Label0 to Label1
	iconst_3
	istore_1
	getstatic MT22Class.x I
	iload_1
	invokestatic MT22Class/inc(II)V
	getstatic MT22Class.x I
	invokestatic io/printInteger(I)V
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
	bipush 65
	putstatic MT22Class.x I
Label1:
	return
.limit stack 1
.limit locals 0
.end method
