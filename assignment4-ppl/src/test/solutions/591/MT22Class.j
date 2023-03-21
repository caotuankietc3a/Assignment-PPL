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
	bipush 10
	if_icmpge Label6
	iconst_1
	goto Label7
Label6:
	iconst_0
Label7:
	ifle Label5
.var 2 is j I from Label0 to Label1
	iconst_0
	istore_2
Label10:
	iload_2
	bipush 20
	if_icmpge Label8
	iconst_1
	goto Label9
Label8:
	iconst_0
Label9:
	ifle Label12
	iload_1
	iload_2
	iadd
	bipush 20
	if_icmplt Label13
	iconst_1
	goto Label14
Label13:
	iconst_0
Label14:
	ifgt Label15
	iload_2
	iconst_1
	iadd
	istore_2
	goto Label16
Label15:
	goto Label12
Label16:
Label11:
	goto Label10
Label12:
	iload_2
	invokestatic io/printInteger(I)V
Label4:
	iload_1
	iconst_1
	iadd
	istore_1
	goto Label3
Label5:
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
