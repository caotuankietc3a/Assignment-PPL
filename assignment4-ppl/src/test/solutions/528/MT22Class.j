.source MT22Class.java
.class public MT22Class
.super java.lang.Object
.field static x I
.field static y F

.method public static main([Ljava/lang/String;)V
.var 0 is args [Ljava/lang/String; from Label0 to Label1
Label0:
	bipush 6
	putstatic MT22Class.x I
	getstatic MT22Class.x I
	i2f
	putstatic MT22Class.y F
	getstatic MT22Class.y F
	invokestatic io/writeFloat(F)V
Label1:
	return
.limit stack 1
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
	iconst_3
	bipush 100
	iadd
	putstatic MT22Class.x I
	ldc 100.3243
	bipush 123
	i2f
	fadd
	putstatic MT22Class.y F
Label1:
	return
.limit stack 3
.limit locals 0
.end method
