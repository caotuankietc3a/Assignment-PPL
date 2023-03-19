.source MT22Class.java
.class public MT22Class
.super java.lang.Object
.field static arr [I

.method public static checkDuplicate([II)Z
.var 0 is ar [I from Label0 to Label1
.var 1 is size I from Label0 to Label1
Label0:
	iload_1
	iconst_1
	if_icmpgt Label2
	iconst_1
	goto Label3
Label2:
	iconst_0
Label3:
	ifle Label4
	iconst_1
	ireturn
Label4:
Label5:
.var 2 is less [I from Label0 to Label1
	bipush 100
	newarray int
	astore_2
.var 3 is greater [I from Label0 to Label1
	bipush 100
	newarray int
	astore_3
.var 4 is greater_size I from Label0 to Label1
	iconst_0
	istore 4
.var 5 is less_size I from Label0 to Label1
	iconst_0
	istore 5
.var 6 is i I from Label0 to Label1
	iconst_1
	istore 6
Label7:
	iload 6
	iload_1
	if_icmpge Label10
	iconst_1
	goto Label11
Label10:
	iconst_0
Label11:
	ifle Label9
	aload_0
	iload 6
	iaload
	aload_0
	iconst_0
	iaload
	if_icmpne Label12
	iconst_1
	goto Label13
Label12:
	iconst_0
Label13:
	ifle Label14
	iconst_0
	ireturn
Label14:
Label15:
	aload_0
	iload 6
	iaload
	aload_0
	iconst_0
	iaload
	if_icmpge Label16
	iconst_1
	goto Label17
Label16:
	iconst_0
Label17:
	ifle Label18
	aload_2
	iload 5
	aload_0
	iload 6
	iaload
	iastore
	iload 5
	iconst_1
	iadd
	istore 5
	goto Label19
Label18:
	aload_3
	iload 4
	aload_0
	iload 6
	iaload
	iastore
	iload 4
	iconst_1
	iadd
	istore 4
Label19:
Label8:
	iload 6
	iconst_1
	iadd
	istore 6
	goto Label7
Label9:
	aload_2
	iload 5
	invokestatic MT22Class/checkDuplicate([II)Z
	aload_3
	iload 4
	invokestatic MT22Class/checkDuplicate([II)Z
	iand
	ireturn
Label1:
.limit stack 25
.limit locals 7
.end method

.method public static main([Ljava/lang/String;)V
.var 0 is args [Ljava/lang/String; from Label0 to Label1
Label0:
	getstatic MT22Class.arr [I
	bipush 100
	invokestatic MT22Class/checkDuplicate([II)Z
	invokestatic io/printBoolean(Z)V
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
	bipush 100
	newarray int
	dup
	iconst_0
	iconst_1
	iastore
	dup
	iconst_1
	iconst_2
	iastore
	dup
	iconst_2
	iconst_3
	iastore
	dup
	iconst_3
	iconst_4
	iastore
	dup
	iconst_4
	iconst_5
	iastore
	dup
	iconst_5
	bipush 10
	iastore
	dup
	bipush 6
	bipush 12
	ineg
	iastore
	dup
	bipush 7
	bipush 23
	iastore
	dup
	bipush 8
	iconst_1
	iastore
	putstatic MT22Class.arr [I
Label1:
	return
.limit stack 11
.limit locals 0
.end method
