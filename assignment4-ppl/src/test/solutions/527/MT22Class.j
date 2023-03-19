.source MT22Class.java
.class public MT22Class
.super java.lang.Object
.field static arr3 [I

.method public static main([Ljava/lang/String;)V
.var 0 is args [Ljava/lang/String; from Label0 to Label1
Label0:
	getstatic MT22Class.arr3 [I
	iconst_2
	iconst_3
	iconst_0
	imul
	imul
	iconst_2
	iconst_0
	imul
	iadd
	iconst_0
	iadd
	iaload
	invokestatic io/printInteger(I)V
	getstatic MT22Class.arr3 [I
	iconst_2
	iconst_3
	iconst_0
	imul
	imul
	iconst_2
	iconst_0
	imul
	iadd
	iconst_1
	iadd
	iaload
	invokestatic io/printInteger(I)V
	getstatic MT22Class.arr3 [I
	iconst_2
	iconst_3
	iconst_0
	imul
	imul
	iconst_2
	iconst_1
	imul
	iadd
	iconst_0
	iadd
	iaload
	invokestatic io/printInteger(I)V
	getstatic MT22Class.arr3 [I
	iconst_2
	iconst_3
	iconst_0
	imul
	imul
	iconst_2
	iconst_1
	imul
	iadd
	iconst_1
	iadd
	iaload
	invokestatic io/printInteger(I)V
	getstatic MT22Class.arr3 [I
	iconst_2
	iconst_3
	iconst_0
	imul
	imul
	iconst_2
	iconst_2
	imul
	iadd
	iconst_0
	iadd
	iaload
	invokestatic io/printInteger(I)V
	getstatic MT22Class.arr3 [I
	iconst_2
	iconst_3
	iconst_0
	imul
	imul
	iconst_2
	iconst_2
	imul
	iadd
	iconst_1
	iadd
	iaload
	invokestatic io/printInteger(I)V
	getstatic MT22Class.arr3 [I
	iconst_2
	iconst_3
	iconst_1
	imul
	imul
	iconst_2
	iconst_0
	imul
	iadd
	iconst_0
	iadd
	iaload
	invokestatic io/printInteger(I)V
	getstatic MT22Class.arr3 [I
	iconst_2
	iconst_3
	iconst_1
	imul
	imul
	iconst_2
	iconst_0
	imul
	iadd
	iconst_1
	iadd
	iaload
	invokestatic io/printInteger(I)V
	getstatic MT22Class.arr3 [I
	iconst_2
	iconst_3
	iconst_1
	imul
	imul
	iconst_2
	iconst_1
	imul
	iadd
	iconst_0
	iadd
	iaload
	invokestatic io/printInteger(I)V
	getstatic MT22Class.arr3 [I
	iconst_2
	iconst_3
	iconst_1
	imul
	imul
	iconst_2
	iconst_1
	imul
	iadd
	iconst_1
	iadd
	iaload
	invokestatic io/printInteger(I)V
	getstatic MT22Class.arr3 [I
	iconst_2
	iconst_3
	iconst_1
	imul
	imul
	iconst_2
	iconst_2
	imul
	iadd
	iconst_0
	iadd
	iaload
	invokestatic io/printInteger(I)V
	getstatic MT22Class.arr3 [I
	iconst_2
	iconst_3
	iconst_1
	imul
	imul
	iconst_2
	iconst_2
	imul
	iadd
	iconst_1
	iadd
	iaload
	invokestatic io/printInteger(I)V
Label1:
	return
.limit stack 7
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
Label1:
	return
.limit stack 14
.limit locals 0
.end method
