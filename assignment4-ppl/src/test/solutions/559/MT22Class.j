.source MT22Class.java
.class public MT22Class
.super java.lang.Object
.field static b Z

.method public static main([Ljava/lang/String;)V
.var 0 is args [Ljava/lang/String; from Label0 to Label1
Label0:
.var 1 is f [Z from Label0 to Label1
	iconst_5
	newarray boolean
	dup
	iconst_0
	iconst_1
	bastore
	dup
	iconst_1
	iconst_0
	bastore
	dup
	iconst_2
	iconst_1
	bastore
	astore_1
	aload_1
	iconst_0
	baload
	aload_1
	iconst_1
	baload
	iand
	aload_1
	iconst_2
	baload
	iand
	invokestatic io/printBoolean(Z)V
	aload_1
	iconst_0
	aload_1
	iconst_0
	baload
	aload_1
	iconst_1
	baload
	ior
	bastore
	aload_1
	iconst_0
	baload
	invokestatic io/printBoolean(Z)V
	aload_1
	iconst_1
	bipush 100
	bipush 10
	if_icmple Label2
	iconst_1
	goto Label3
Label2:
	iconst_0
Label3:
	bastore
	aload_1
	iconst_1
	baload
	invokestatic io/printBoolean(Z)V
Label1:
	return
.limit stack 20
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
	iconst_0
	putstatic MT22Class.b Z
Label1:
	return
.limit stack 2
.limit locals 0
.end method
