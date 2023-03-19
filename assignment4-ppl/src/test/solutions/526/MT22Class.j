.source MT22Class.java
.class public MT22Class
.super java.lang.Object

.method public static main([Ljava/lang/String;)V
.var 0 is args [Ljava/lang/String; from Label0 to Label1
Label0:
.var 1 is arr1 [I from Label0 to Label1
	iconst_4
	newarray int
	dup
	iconst_0
	iconst_1
	iastore
	dup
	iconst_1
	iconst_3
	iastore
	dup
	iconst_2
	bipush 123
	iastore
	dup
	iconst_3
	sipush 1238
	iastore
	astore_1
	aload_1
	iconst_2
	iconst_0
	imul
	iconst_0
	iadd
	iaload
	invokestatic io/printInteger(I)V
	aload_1
	iconst_2
	iconst_0
	imul
	iconst_1
	iadd
	iaload
	invokestatic io/printInteger(I)V
	aload_1
	iconst_2
	iconst_1
	imul
	iconst_0
	iadd
	iaload
	invokestatic io/printInteger(I)V
	aload_1
	iconst_2
	iconst_1
	imul
	iconst_1
	iadd
	iaload
	invokestatic io/printInteger(I)V
Label1:
	return
.limit stack 10
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
