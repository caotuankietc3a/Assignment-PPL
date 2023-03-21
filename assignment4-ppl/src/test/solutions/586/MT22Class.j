.source MT22Class.java
.class public MT22Class
.super java.lang.Object

.method public static findGCD(II)I
.var 0 is a I from Label0 to Label1
.var 1 is b I from Label0 to Label1
Label0:
	iload_1
	ifgt Label2
	goto Label3
Label2:
	iload_1
	iload_0
	iload_1
	irem
	invokestatic MT22Class/findGCD(II)I
	ireturn
Label3:
	iload_0
	ireturn
Label1:
.limit stack 3
.limit locals 2
.end method

.method public static findLCM(II)F
.var 0 is a I from Label0 to Label1
.var 1 is b I from Label0 to Label1
Label0:
	iload_0
	iload_1
	imul
	i2f
	iload_0
	iload_1
	invokestatic MT22Class/findGCD(II)I
	i2f
	fdiv
	freturn
Label1:
.limit stack 3
.limit locals 2
.end method

.method public static main([Ljava/lang/String;)V
.var 0 is args [Ljava/lang/String; from Label0 to Label1
Label0:
	sipush 144
	bipush 12
	invokestatic MT22Class/findLCM(II)F
	invokestatic io/writeFloat(F)V
	sipush 144
	bipush 12
	invokestatic MT22Class/findGCD(II)I
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
