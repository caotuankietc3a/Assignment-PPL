.source MT22Class.java
.class public MT22Class
.super java.lang.Object
.field static x I
.field static y F
.field static arr [I

.method public static main([Ljava/lang/String;)V
.var 0 is args [Ljava/lang/String; from Label0 to Label1
Label0:
.var 1 is arr3 [F from Label0 to Label1
	bipush 12
	newarray float
	dup
	iconst_0
	iconst_1
	i2f
	fastore
	dup
	iconst_1
	iconst_3
	i2f
	fastore
	dup
	iconst_2
	bipush 12
	i2f
	fastore
	dup
	iconst_3
	bipush 13
	i2f
	fastore
	dup
	iconst_4
	bipush 123
	i2f
	fastore
	dup
	iconst_5
	sipush 321
	i2f
	fastore
	dup
	bipush 6
	iconst_2
	i2f
	fastore
	dup
	bipush 7
	bipush 41
	i2f
	fastore
	dup
	bipush 8
	bipush 123
	i2f
	fastore
	dup
	bipush 9
	bipush 123
	i2f
	fastore
	dup
	bipush 10
	sipush 923
	i2f
	fastore
	dup
	bipush 11
	bipush 32
	i2f
	fastore
	astore_1
	aload_1
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
	getstatic MT22Class.y F
	fastore
	aload_1
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
	faload
	aload_1
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
	faload
	fadd
	invokestatic io/writeFloat(F)V
	aload_1
	iconst_2
	iconst_3
	iconst_0
	imul
	imul
	iconst_2
	iconst_0
	imul
	iadd
	getstatic MT22Class.x I
	iadd
	faload
	aload_1
	iconst_2
	iconst_3
	iconst_0
	imul
	imul
	iconst_2
	iconst_1
	imul
	iadd
	getstatic MT22Class.arr [I
	iconst_1
	iaload
	iadd
	faload
	fadd
	invokestatic io/writeFloat(F)V
Label1:
	return
.limit stack 14
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
	iconst_1
	putstatic MT22Class.x I
	ldc 100.3243
	getstatic MT22Class.x I
	i2f
	fadd
	putstatic MT22Class.y F
	iconst_2
	newarray int
	dup
	iconst_0
	iconst_0
	iastore
	dup
	iconst_1
	getstatic MT22Class.x I
	iastore
	putstatic MT22Class.arr [I
Label1:
	return
.limit stack 6
.limit locals 0
.end method
