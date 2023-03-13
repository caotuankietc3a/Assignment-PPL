.source MT22Class.java
.class public MT22Class
.super java.lang.Object

.method public static main([Ljava/lang/String;)V
.var 0 is args [Ljava/lang/String; from Label0 to Label1
Label0:
	bipush 12
	bipush 20
	if_icmple Label2
	iconst_1
	goto Label3
Label2:
	iconst_0
Label3:
	bipush 50
	bipush 100
	if_icmpgt Label4
	iconst_1
	goto Label5
Label4:
	iconst_0
Label5:
	iand
	invokestatic io/printBoolean(Z)V
	bipush 12
	bipush 20
	if_icmpge Label6
	iconst_1
	goto Label7
Label6:
	iconst_0
Label7:
	bipush 50
	bipush 100
	if_icmpgt Label8
	iconst_1
	goto Label9
Label8:
	iconst_0
Label9:
	iand
	invokestatic io/printBoolean(Z)V
	bipush 12
	bipush 12
	if_icmpgt Label10
	iconst_1
	goto Label11
Label10:
	iconst_0
Label11:
	bipush 50
	bipush 100
	if_icmple Label12
	iconst_1
	goto Label13
Label12:
	iconst_0
Label13:
	iand
	invokestatic io/printBoolean(Z)V
	bipush 12
	bipush 12
	iconst_1
	goto Label15
Label14:
	iconst_0
Label15:
	bipush 50
	bipush 100
	iconst_1
	goto Label17
Label16:
	iconst_0
Label17:
	ior
	invokestatic io/printBoolean(Z)V
Label1:
	return
.limit stack 34
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
