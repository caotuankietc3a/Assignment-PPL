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
.var 2 is j I from Label0 to Label1
	iconst_0
	istore_2
Label7:
	iload_2
	bipush 20
	if_icmpge Label5
	iconst_1
	goto Label6
Label5:
	iconst_0
Label6:
	ifle Label9
	iload_1
	iload_2
	iadd
	bipush 20
	if_icmplt Label10
	iconst_1
	goto Label11
Label10:
	iconst_0
Label11:
	ifle Label12
	goto Label9
	goto Label13
Label12:
	iload_2
	iconst_1
	iadd
	istore_2
Label13:
	goto Label7
Label8:
Label9:
	iload_2
	invokestatic io/printInteger(I)V
	iload_1
	iconst_1
	iadd
	istore_1
	iload_1
	bipush 10
	if_icmpge Label14
	iconst_1
	goto Label15
Label14:
	iconst_0
Label15:
	ifgt Label2
Label3:
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
