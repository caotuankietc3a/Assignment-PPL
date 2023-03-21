.source MT22Class.java
.class public MT22Class
.super java.lang.Object

.method public static isSymmetry([I[II)Z
.var 0 is head [I from Label0 to Label1
.var 1 is tail [I from Label0 to Label1
.var 2 is size I from Label0 to Label1
Label0:
.var 3 is i I from Label0 to Label1
	iconst_0
	istore_3
Label3:
	iload_3
	iload_2
	if_icmpge Label6
	iconst_1
	goto Label7
Label6:
	iconst_0
Label7:
	ifle Label5
	aload_0
	iload_3
	iaload
	aload_1
	iload_2
	iload_3
	isub
	iconst_1
	isub
	iaload
	if_icmpeq Label8
	iconst_1
	goto Label9
Label8:
	iconst_0
Label9:
	ifgt Label10
	goto Label11
Label10:
	iconst_0
	ireturn
Label11:
Label4:
	iload_3
	iconst_1
	iadd
	istore_3
	goto Label3
Label5:
	iconst_1
	ireturn
Label1:
.limit stack 9
.limit locals 4
.end method

.method public static main([Ljava/lang/String;)V
.var 0 is args [Ljava/lang/String; from Label0 to Label1
Label0:
.var 1 is headf [I from Label0 to Label1
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
.var 2 is tailf [I from Label0 to Label1
	iconst_5
	newarray int
	dup
	iconst_0
	bipush 10
	iastore
	dup
	iconst_1
	iconst_1
	iastore
	dup
	iconst_2
	sipush 1000
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
	astore_2
.var 3 is headt [I from Label0 to Label1
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
	astore_3
.var 4 is tailt [I from Label0 to Label1
	iconst_5
	newarray int
	dup
	iconst_0
	bipush 100
	iastore
	dup
	iconst_1
	bipush 100
	ineg
	iastore
	dup
	iconst_2
	iconst_0
	iastore
	dup
	iconst_3
	bipush 91
	iastore
	dup
	iconst_4
	iconst_1
	iastore
	astore 4
	aload_1
	aload_2
	iconst_5
	invokestatic MT22Class/isSymmetry([I[II)Z
	invokestatic io/printBoolean(Z)V
	aload_3
	aload 4
	iconst_5
	invokestatic MT22Class/isSymmetry([I[II)Z
	invokestatic io/printBoolean(Z)V
Label1:
	return
.limit stack 13
.limit locals 5
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
