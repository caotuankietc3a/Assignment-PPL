.source MT22Class.java
.class public MT22Class
.super java.lang.Object

.method public static isPalindrome([II)Z
.var 0 is strs [I from Label0 to Label1
.var 1 is strSize I from Label0 to Label1
Label0:
.var 2 is i I from Label0 to Label1
	iconst_0
	istore_2
Label3:
	iload_2
	i2f
	iload_1
	i2f
	iconst_2
	i2f
	fdiv
	fcmpl
	ifge Label6
	iconst_1
	goto Label7
Label6:
	iconst_0
Label7:
	ifle Label5
	aload_0
	iload_2
	iaload
	aload_0
	iload_1
	iload_2
	isub
	iconst_1
	isub
	iaload
	if_icmpeq Label8
	iconst_1
	goto Label9
Label8:
	iconst_0
Label9:
	ifgt Label10
	goto Label11
Label10:
	iconst_0
	ireturn
Label11:
Label4:
	iload_2
	iconst_1
	iadd
	istore_2
	goto Label3
Label5:
	iconst_1
	ireturn
Label1:
.limit stack 9
.limit locals 3
.end method

.method public static main([Ljava/lang/String;)V
.var 0 is args [Ljava/lang/String; from Label0 to Label1
Label0:
.var 1 is strs [I from Label0 to Label1
	iconst_5
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
	iconst_2
	iastore
	dup
	iconst_4
	iconst_1
	iastore
	astore_1
	aload_1
	iconst_5
	invokestatic MT22Class/isPalindrome([II)Z
	ifgt Label2
	ldc "Wrong!!!"
	invokestatic io/printString(Ljava/lang/String;)V
	goto Label3
Label2:
	ldc "Correct!!!"
	invokestatic io/printString(Ljava/lang/String;)V
Label3:
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
Label1:
	return
.limit stack 0
.limit locals 0
.end method
