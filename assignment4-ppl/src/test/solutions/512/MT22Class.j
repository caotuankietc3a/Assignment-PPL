.source MT22Class.java
.class public MT22Class
.super java.lang.Object

.method public static main([Ljava/lang/String;)V
.var 0 is args [Ljava/lang/String; from Label0 to Label1
Label0:
	iconst_1
	i2f
	ldc 2.2
	fadd
	invokestatic io/writeFloat(F)V
	ldc 2.2
	iconst_1
	i2f
	fadd
	invokestatic io/writeFloat(F)V
	ldc 2.2
	ldc 2.2
	fadd
	invokestatic io/writeFloat(F)V
	iconst_1
	iconst_2
	iadd
	invokestatic io/printInteger(I)V
Label1:
	return
.limit stack 6
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
