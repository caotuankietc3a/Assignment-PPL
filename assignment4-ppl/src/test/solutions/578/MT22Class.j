.source MT22Class.java
.class public MT22Class
.super java.lang.Object
.field static n I

.method public static recursiveSearch(II[II)I
.var 0 is n I from Label0 to Label1
.var 1 is m I from Label0 to Label1
.var 2 is arr [I from Label0 to Label1
.var 3 is index I from Label0 to Label1
Label0:
	iload_3
	iconst_1
	iadd
	istore_3
	iload_3
	iload_0
	if_icmple Label2
	iconst_1
	goto Label3
Label2:
	iconst_0
Label3:
	ifgt Label4
	goto Label5
Label4:
	iconst_1
	ineg
	ireturn
Label5:
	aload_2
	iload_3
	iconst_1
	isub
	iaload
	iload_1
	if_icmpne Label6
	iconst_1
	goto Label7
Label6:
	iconst_0
Label7:
	ifgt Label8
	goto Label9
Label8:
.var 4 is i I from Label0 to Label1
	iload_3
	iconst_1
	isub
	istore 4
Label11:
	iload 4
	iload_0
	iconst_1
	isub
	if_icmpge Label14
	iconst_1
	goto Label15
Label14:
	iconst_0
Label15:
	ifle Label13
	aload_2
	iload 4
	aload_2
	iload 4
	iconst_1
	iadd
	iaload
	iastore
Label12:
	iload 4
	iconst_1
	iadd
	istore 4
	goto Label11
Label13:
	iload_0
	iconst_1
	isub
	istore_0
	iload_3
	iconst_1
	isub
	ireturn
Label9:
	iload_0
	iload_1
	aload_2
	iload_3
	invokestatic MT22Class/recursiveSearch(II[II)I
	ireturn
Label1:
.limit stack 14
.limit locals 5
.end method

.method public static main([Ljava/lang/String;)V
.var 0 is args [Ljava/lang/String; from Label0 to Label1
Label0:
.var 1 is arr [I from Label0 to Label1
	iconst_5
	newarray int
	dup
	iconst_0
	iconst_1
	iastore
	dup
	iconst_1
	bipush 91
	iastore
	dup
	iconst_2
	iconst_0
	iastore
	dup
	iconst_3
	bipush 100
	ineg
	iastore
	dup
	iconst_4
	bipush 100
	iastore
	astore_1
	getstatic MT22Class.n I
	bipush 10
	aload_1
	iconst_0
	invokestatic MT22Class/recursiveSearch(II[II)I
	invokestatic io/printInteger(I)V
	getstatic MT22Class.n I
	bipush 100
	ineg
	aload_1
	iconst_0
	invokestatic MT22Class/recursiveSearch(II[II)I
	invokestatic io/printInteger(I)V
Label1:
	return
.limit stack 7
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
	iconst_5
	putstatic MT22Class.n I
Label1:
	return
.limit stack 1
.limit locals 0
.end method
