.source MT22Class.java
.class public MT22Class
.super java.lang.Object

.method public static main([Ljava/lang/String;)V
.var 0 is args [Ljava/lang/String; from Label0 to Label1
Label0:
.var 1 is i I from Label0 to Label1
	iconst_0
	istore_1
.var 2 is nE I from Label0 to Label1
	bipush 10
	istore_2
Label2:
Label5:
	iconst_0
	istore_1
Label8:
	iload_1
	iload_2
	if_icmpge Label11
	iconst_1
	goto Label12
Label11:
	iconst_0
Label12:
	ifle Label10
	iload_2
	bipush 10
	iconst_5
	iadd
	if_icmpne Label13
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
	goto Label9
Label16:
Label9:
	iload_1
	iconst_1
	iadd
	istore_1
	goto Label8
Label10:
	goto Label4
Label6:
Label3:
	iconst_1
	ifle Label4
	goto Label2
Label4:
	iload_2
	invokestatic io/printInteger(I)V
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
