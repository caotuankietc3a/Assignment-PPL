.source MT22Class.java
.class public MT22Class
.super java.lang.Object

.method public static gcdIteration(II)I
.var 0 is p I from Label0 to Label1
.var 1 is q I from Label0 to Label1
Label0:
Label4:
	iload_0
	iload_1
	imul
	iconst_0
	if_icmpeq Label2
	iconst_1
	goto Label3
Label2:
	iconst_0
Label3:
	ifle Label6
	iload_0
	iload_1
	if_icmple Label7
	iconst_1
	goto Label8
Label7:
	iconst_0
Label8:
	ifgt Label9
	iload_1
	iload_0
	irem
	istore_1
	goto Label10
Label9:
	iload_0
	iload_1
	irem
	istore_0
Label10:
Label5:
	goto Label4
Label6:
	iload_0
	iload_1
	iadd
	ireturn
Label1:
.limit stack 6
.limit locals 2
.end method

.method public static gcdRecursion(II)I
.var 0 is p I from Label0 to Label1
.var 1 is q I from Label0 to Label1
Label0:
	iload_1
	iconst_0
	if_icmpne Label2
	iconst_1
	goto Label3
Label2:
	iconst_0
Label3:
	ifgt Label4
	goto Label5
Label4:
	iload_0
	ireturn
Label5:
	iload_1
	iload_0
	iload_1
	irem
	invokestatic MT22Class/gcdRecursion(II)I
	ireturn
Label1:
.limit stack 5
.limit locals 2
.end method

.method public static main([Ljava/lang/String;)V
.var 0 is args [Ljava/lang/String; from Label0 to Label1
Label0:
	bipush 10
	bipush 15
	invokestatic MT22Class/gcdRecursion(II)I
	invokestatic io/printInteger(I)V
	bipush 10
	bipush 15
	invokestatic MT22Class/gcdIteration(II)I
	invokestatic io/printInteger(I)V
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
