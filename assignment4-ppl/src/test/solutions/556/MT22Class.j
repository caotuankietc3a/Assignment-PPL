.source MT22Class.java
.class public MT22Class
.super java.lang.Object

.method public static checkElements([II)Z
.var 0 is arr [I from Label0 to Label1
.var 1 is n I from Label0 to Label1
Label0:
	iload_1
	sipush 1000
	if_icmple Label2
	iconst_1
	goto Label3
Label2:
	iconst_0
Label3:
	iload_1
	iconst_0
	if_icmpge Label4
	iconst_1
	goto Label5
Label4:
	iconst_0
Label5:
	ior
	ifgt Label6
	goto Label7
Label6:
	iconst_0
	ireturn
Label7:
.var 2 is i I from Label0 to Label1
	iconst_0
	istore_2
Label9:
	iload_2
	iload_1
	iconst_1
	isub
	if_icmpge Label12
	iconst_1
	goto Label13
Label12:
	iconst_0
Label13:
	ifle Label11
.var 3 is j I from Label0 to Label1
	iload_2
	iconst_1
	iadd
	istore_3
Label15:
	iload_3
	iload_1
	if_icmpge Label18
	iconst_1
	goto Label19
Label18:
	iconst_0
Label19:
	ifle Label17
	aload_0
	iload_2
	iaload
	aload_0
	iload_3
	iaload
	if_icmpne Label20
	iconst_1
	goto Label21
Label20:
	iconst_0
Label21:
	ifgt Label22
	goto Label23
Label22:
	iconst_0
	ireturn
Label23:
Label16:
	iload_3
	iconst_1
	iadd
	istore_3
	goto Label15
Label17:
Label10:
	iload_2
	iconst_1
	iadd
	istore_2
	goto Label9
Label11:
	iconst_1
	ireturn
Label1:
.limit stack 16
.limit locals 4
.end method

.method public static main([Ljava/lang/String;)V
.var 0 is args [Ljava/lang/String; from Label0 to Label1
Label0:
.var 1 is arr [I from Label0 to Label1
	bipush 6
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
	sipush 200
	iastore
	astore_1
	aload_1
	bipush 6
	invokestatic MT22Class/checkElements([II)Z
	invokestatic io/printBoolean(Z)V
Label1:
	return
.limit stack 8
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
