.source MT22Class.java
.class public MT22Class
.super java.lang.Object

.method public static main([Ljava/lang/String;)V
.var 0 is args [Ljava/lang/String; from Label0 to Label1
Label0:
.var 1 is i I from Label0 to Label1
	iconst_1
	istore_1
Label3:
	iload_1
	iconst_3
	if_icmpge Label6
	iconst_1
	goto Label7
Label6:
	iconst_0
Label7:
	ifle Label5
.var 2 is j I from Label0 to Label1
	iconst_1
	istore_2
Label9:
	iload_2
	iconst_3
	if_icmpge Label12
	iconst_1
	goto Label13
Label12:
	iconst_0
Label13:
	ifle Label11
	iload_1
	iload_2
	iadd
	iconst_2
	if_icmplt Label14
	iconst_1
	goto Label15
Label14:
	iconst_0
Label15:
	ifle Label16
	iload_1
	iload_2
	iadd
	invokestatic io/printInteger(I)V
	goto Label11
	goto Label17
Label16:
	iload_1
	iload_2
	isub
	invokestatic io/printInteger(I)V
Label17:
Label10:
	iload_2
	iconst_1
	iadd
	istore_2
	goto Label9
Label11:
Label4:
	iload_1
	iconst_1
	iadd
	istore_1
	goto Label3
Label5:
Label1:
	return
.limit stack 8
.limit locals 3
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
