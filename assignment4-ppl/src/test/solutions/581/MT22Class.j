.source MT22Class.java
.class public MT22Class
.super java.lang.Object

.method public static findMax([II)F
.var 0 is vals [I from Label0 to Label1
.var 1 is numEls I from Label0 to Label1
Label0:
.var 2 is max I from Label0 to Label1
	aload_0
	iconst_0
	iaload
	istore_2
.var 3 is i I from Label0 to Label1
	iconst_1
	istore_3
Label3:
	iload_3
	iload_1
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
	iload_2
	if_icmple Label8
	iconst_1
	goto Label9
Label8:
	iconst_0
Label9:
	ifgt Label10
	goto Label11
Label10:
	aload_0
	iload_3
	iaload
	istore_2
Label11:
Label4:
	iload_3
	iconst_1
	iadd
	istore_3
	goto Label3
Label5:
	iload_2
	i2f
	freturn
Label1:
.limit stack 10
.limit locals 4
.end method

.method public static main([Ljava/lang/String;)V
.var 0 is args [Ljava/lang/String; from Label0 to Label1
Label0:
.var 1 is arr [I from Label0 to Label1
	bipush 10
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
	dup
	iconst_5
	bipush 10
	iastore
	dup
	bipush 6
	iconst_1
	iastore
	dup
	bipush 7
	sipush 1000
	iastore
	dup
	bipush 8
	bipush 100
	ineg
	iastore
	dup
	bipush 9
	bipush 100
	iastore
	astore_1
	aload_1
	bipush 10
	invokestatic MT22Class/findMax([II)F
	invokestatic io/writeFloat(F)V
Label1:
	return
.limit stack 12
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
