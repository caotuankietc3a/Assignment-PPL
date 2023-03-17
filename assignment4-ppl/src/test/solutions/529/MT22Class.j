.source MT22Class.java
.class public MT22Class
.super java.lang.Object
.field static arr [I
.field static arr3 [I
.field static y F

.method public static main([Ljava/lang/String;)V
.var 0 is args [Ljava/lang/String; from Label0 to Label1
Label0:
	getstatic MT22Class.arr [I
	iconst_0
	sipush 999
	iastore
	getstatic MT22Class.arr [I
	iconst_0
	iaload
	invokestatic io/printInteger(I)V
Label1:
	return
.limit stack 4
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
	iconst_2
	newarray int
	dup
	iconst_0
	iconst_0
	iastore
	dup
	iconst_1
	iconst_1
	iastore
	putstatic MT22Class.arr [I
	bipush 12
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
	bipush 12
	iastore
	dup
	iconst_3
	bipush 13
	iastore
	dup
	iconst_4
	bipush 123
	iastore
	dup
	iconst_5
	sipush 321
	iastore
	dup
	bipush 6
	iconst_2
	iastore
	dup
	bipush 7
	bipush 41
	iastore
	dup
	bipush 8
	bipush 123
	iastore
	dup
	bipush 9
	bipush 123
	iastore
	dup
	bipush 10
	sipush 923
	iastore
	dup
	bipush 11
	bipush 32
	iastore
	putstatic MT22Class.arr3 [I
	ldc 100.3243
	bipush 123
	i2f
	fadd
	putstatic MT22Class.y F
Label1:
	return
.limit stack 14
.limit locals 0
.end method
