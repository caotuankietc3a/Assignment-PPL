.source MT22Class.java
.class public MT22Class
.super java.lang.Object
.field static y F
.field static z I

.method public <init>()V
.var 0 is this LMT22Class; from Label0 to Label1
Label0:
	aload_0
	invokespecial java/lang/Object/<init>()V
Label1:
	return
.limit stack 4
.limit locals 1
.end method

.method public static main([Ljava/lang/String;)V
.var 0 is args [Ljava/lang/String; from Label2 to Label3
Label2:
	ldc 10.123
	putstatic MT22Class.y F
	bipush 110
	putstatic MT22Class.z I
.var 1 is x I from Label2 to Label3
	bipush 10
	istore_1
	iload_1
	invokestatic io/printInteger(I)V
	getstatic MT22Class.y F
	invokestatic io/writeFloat(F)V
	getstatic MT22Class.z I
	invokestatic io/printInteger(I)V
Label3:
	return
.limit stack 3
.limit locals 2
.end method
