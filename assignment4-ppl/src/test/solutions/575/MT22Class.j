.source MT22Class.java
.class public MT22Class
.super java.lang.Object
.field static a [I
.field static b [I

.method public static swap([I[II)V
.var 0 is a [I from Label0 to Label1
.var 1 is b [I from Label0 to Label1
.var 2 is n I from Label0 to Label1
Label0:
	iload_2
	bipush 10
	if_icmple Label2
	iconst_1
	goto Label3
Label2:
	iconst_0
Label3:
	ifgt Label4
.var 3 is temp I from Label0 to Label1
.var 4 is i I from Label0 to Label1
	iconst_0
	istore 4
Label7:
	iload 4
	iload_2
	if_icmpge Label10
	iconst_1
	goto Label11
Label10:
	iconst_0
Label11:
	ifle Label9
	aload_0
	iload 4
	iaload
	istore_3
	aload_0
	iload 4
	aload_1
	iload 4
	iaload
	iastore
	aload_1
	iload 4
	iload_3
	iastore
Label8:
	iload 4
	iconst_1
	iadd
	istore 4
	goto Label7
Label9:
	goto Label5
Label4:
	return
Label5:
Label1:
	return
.limit stack 13
.limit locals 5
.end method

.method public static main([Ljava/lang/String;)V
.var 0 is args [Ljava/lang/String; from Label0 to Label1
Label0:
	getstatic MT22Class.a [I
	getstatic MT22Class.b [I
	bipush 10
	invokestatic MT22Class/swap([I[II)V
.var 1 is i I from Label0 to Label1
	iconst_0
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
	getstatic MT22Class.a [I
	iload_1
	iaload
	invokestatic io/printInteger(I)V
Label4:
	iload_1
	iconst_1
	iadd
	istore_1
	goto Label3
Label5:
.var 2 is i I from Label0 to Label1
	iconst_0
	istore_2
Label9:
	iload_2
	bipush 10
	if_icmpge Label12
	iconst_1
	goto Label13
Label12:
	iconst_0
Label13:
	ifle Label11
	getstatic MT22Class.b [I
	iload_2
	iaload
	invokestatic io/printInteger(I)V
Label10:
	iload_2
	iconst_1
	iadd
	istore_2
	goto Label9
Label11:
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
	bipush 10
	newarray int
	dup
	iconst_0
	bipush 9
	iastore
	dup
	iconst_1
	bipush 8
	iastore
	dup
	iconst_2
	bipush 7
	iastore
	dup
	iconst_3
	bipush 6
	iastore
	dup
	iconst_4
	iconst_5
	iastore
	dup
	iconst_5
	iconst_4
	iastore
	dup
	bipush 6
	iconst_3
	iastore
	dup
	bipush 7
	iconst_2
	iastore
	dup
	bipush 8
	iconst_1
	iastore
	dup
	bipush 9
	iconst_0
	iastore
	putstatic MT22Class.a [I
	bipush 10
	newarray int
	dup
	iconst_0
	iconst_0
	iastore
	dup
	iconst_1
	iconst_1
	iastore
	dup
	iconst_2
	iconst_2
	iastore
	dup
	iconst_3
	iconst_3
	iastore
	dup
	iconst_4
	iconst_4
	iastore
	dup
	iconst_5
	iconst_5
	iastore
	dup
	bipush 6
	bipush 6
	iastore
	dup
	bipush 7
	bipush 7
	iastore
	dup
	bipush 8
	bipush 8
	iastore
	dup
	bipush 9
	bipush 9
	iastore
	putstatic MT22Class.b [I
Label1:
	return
.limit stack 12
.limit locals 0
.end method
