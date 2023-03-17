.source MT22Class.java
.class public MT22Class
.super java.lang.Object
.field static x I
.field static y I
.field static z I
.field static t I
.field static g F

.method public static main([Ljava/lang/String;)V
.var 0 is args [Ljava/lang/String; from Label0 to Label1
Label0:
.var 1 is x I from Label0 to Label1
	iconst_3
	istore_1
Label1:
	return
.limit stack 2
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
	bipush 10
	putstatic MT22Class.x I
	sipush 1023
	putstatic MT22Class.y I
	bipush 32
	putstatic MT22Class.z I
	bipush 123
	putstatic MT22Class.t I
Label1:
	return
.limit stack 4
.limit locals 0
.end method
