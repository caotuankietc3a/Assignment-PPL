.source MT22Class.java
.class public MT22Class
.super java.lang.Object

.method public static completeNum(I)Z
.var 0 is N I from Label0 to Label1
Label0:
.var 1 is sum I from Label0 to Label1
	iconst_0
	istore_1
.var 2 is i I from Label0 to Label1
	iconst_1
	istore_2
Label3:
	iload_2
	iload_0
	if_icmpge Label6
	iconst_1
	goto Label7
Label6:
	iconst_0
Label7:
	ifle Label5
	iload_0
	iload_2
	irem
	iconst_0
	if_icmpne Label8
	iconst_1
	goto Label9
Label8:
	iconst_0
Label9:
	ifgt Label10
	goto Label11
Label10:
	iload_1
	iload_2
	iadd
	istore_1
Label11:
Label4:
	iload_2
	iconst_1
	iadd
	istore_2
	goto Label3
Label5:
	iload_1
	iload_0
	if_icmpne Label12
	iconst_1
	goto Label13
Label12:
	iconst_0
Label13:
	ifgt Label14
	goto Label15
Label14:
	iconst_1
	ireturn
Label15:
	iconst_0
	ireturn
Label1:
.limit stack 10
.limit locals 3
.end method

.method public static main([Ljava/lang/String;)V
.var 0 is args [Ljava/lang/String; from Label0 to Label1
Label0:
	bipush 6
	invokestatic MT22Class/completeNum(I)Z
	invokestatic io/printBoolean(Z)V
	bipush 10
	invokestatic MT22Class/completeNum(I)Z
	invokestatic io/printBoolean(Z)V
Label1:
	return
.limit stack 1
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
Label1:
	return
.limit stack 0
.limit locals 0
.end method
