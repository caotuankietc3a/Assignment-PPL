.source MT22Class.java
.class public MT22Class
.super java.lang.Object

.method public static main([Ljava/lang/String;)V
.var 0 is args [Ljava/lang/String; from Label0 to Label1
Label0:
.var 1 is nE I from Label0 to Label1
	iconst_0
	istore_1
Label2:
Label5:
	iload_1
	bipush 10
	if_icmpne Label7
	iconst_1
	goto Label8
Label7:
	iconst_0
Label8:
	ifgt Label9
	iload_1
	iconst_1
	iadd
	istore_1
	goto Label3
	goto Label10
Label9:
	goto Label4
Label10:
Label6:
Label3:
	iconst_1
	ifle Label4
	goto Label2
Label4:
	iload_1
	invokestatic io/printInteger(I)V
Label1:
	return
.limit stack 5
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
