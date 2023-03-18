.source MT22Class.java
.class public MT22Class
.super java.lang.Object

.method public static checkElements([II)Z
.var 0 is arr [I from Label0 to Label1
	bipush 100
	newarray int
	astore_0
.var 1 is n I from Label0 to Label1
Label0:
	aload_0
	iconst_0
	iaload
	invokestatic io/printInteger(I)V
	iconst_0
	ireturn
Label1:
.limit stack 3
.limit locals 2
.end method

.method public static main([Ljava/lang/String;)V
.var 0 is args [Ljava/lang/String; from Label0 to Label1
Label0:
.var 1 is arr [I from Label0 to Label1
	iconst_5
	newarray int
	dup
	iconst_0
	iconst_1
	iastore
	dup
	iconst_1
	bipush 91
	iastore
	dup
	iconst_2
	iconst_0
	iastore
	dup
	iconst_3
	bipush 100
	ineg
	iastore
	dup
	iconst_4
	bipush 100
	iastore
	astore_1
	aload_1
	iconst_0
	invokestatic MT22Class/checkElements([II)Z
	invokestatic io/printBoolean(Z)V
Label1:
	return
.limit stack 7
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
