.source MT22Class.java
.class public MT22Class
.super java.lang.Object
.field static x I
.field static y I
.field static z I
.field static t I

.method public static main([Ljava/lang/String;)V
.var 0 is args [Ljava/lang/String; from Label0 to Label1
Label0:
Label1:
	return
.limit stack 0
.limit locals 1
.end method

.method public <init>()V
.var 0 is this LMT22Class; from Label0 to Label1
Label0:
	aload_0
	invokespecial java/lang/Object/<init>()V
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
.limit stack 9
.limit locals 1
.end method
