.source MT22Class.java
.class public MT22Class
.super java.lang.Object

.method public static inc(II)F
.var 0 is n I from Label0 to Label1
.var 1 is delta I from Label0 to Label1
Label0:
	iload_0
	iload_1
	iadd
	istore_0
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
.var 3 is j I from Label0 to Label1
	iconst_1
	istore_3
Label9:
	iload_3
	iload_0
	if_icmpge Label12
	iconst_1
	goto Label13
Label12:
	iconst_0
Label13:
	ifle Label11
	iload_2
	iload_3
	iadd
	iconst_5
	if_icmplt Label14
	iconst_1
	goto Label15
Label14:
	iconst_0
Label15:
	ifle Label16
	iload_2
	iload_3
	iadd
	i2f
	freturn
Label16:
	iload_2
	iload_3
	isub
	invokestatic io/printInteger(I)V
Label17:
Label10:
	iload_3
	iconst_1
	iadd
	istore_3
	goto Label9
Label11:
Label4:
	iload_2
	iconst_1
	iadd
	istore_2
	goto Label3
Label5:
	bipush 10
	i2f
	freturn
Label1:
.limit stack 7
.limit locals 4
.end method

.method public static main([Ljava/lang/String;)V
.var 0 is args [Ljava/lang/String; from Label0 to Label1
Label0:
	iconst_2
	iconst_2
	invokestatic MT22Class/inc(II)F
	invokestatic io/writeFloat(F)V
Label1:
	return
.limit stack 2
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
