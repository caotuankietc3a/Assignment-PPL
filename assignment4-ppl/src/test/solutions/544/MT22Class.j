.source MT22Class.java
.class public MT22Class
.super java.lang.Object

.method public static main([Ljava/lang/String;)V
.var 0 is args [Ljava/lang/String; from Label0 to Label1
Label0:
.var 1 is i I from Label0 to Label1
	iconst_0
	istore_1
Label2:
Label5:
.var 2 is j I from Label5 to Label6
	iconst_0
	istore_2
Label9:
	iload_2
	bipush 20
	if_icmpge Label7
	iconst_1
	goto Label8
Label7:
	iconst_0
Label8:
	ifle Label11
	iload_1
	iload_2
	iadd
	bipush 20
	if_icmplt Label12
	iconst_1
	goto Label13
Label12:
	iconst_0
Label13:
	ifgt Label14
	iload_2
	iconst_1
	iadd
	istore_2
	goto Label15
Label14:
	goto Label11
Label15:
Label10:
	goto Label9
Label11:
	iload_2
	invokestatic io/printInteger(I)V
	iload_1
	iconst_1
	iadd
	istore_1
Label6:
Label3:
	iload_1
	bipush 10
	if_icmpge Label16
	iconst_1
	goto Label17
Label16:
	iconst_0
Label17:
	ifle Label4
	goto Label2
Label4:
Label1:
	return
.limit stack 9
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
