.source MT22Class.java
.class public MT22Class
.super java.lang.Object

.method public static foo(Ljava/lang/String;F)Ljava/lang/String;
.var 0 is a Ljava/lang/String; from Label0 to Label1
.var 1 is b F from Label0 to Label1
Label0:
	ldc "Hello foo"
	areturn
Label1:
.limit stack 1
.limit locals 2
.end method

.method public static foo1(Ljava/lang/String;Ljava/lang/String;)V
.var 0 is z Ljava/lang/String; from Label0 to Label1
.var 1 is t Ljava/lang/String; from Label0 to Label1
.var 2 is a Ljava/lang/String; from Label0 to Label1
	ldc "Hello"
	aload_0
	invokevirtual java/lang/String/concat(Ljava/lang/String;)Ljava/lang/String;
	aload_1
	invokevirtual java/lang/String/concat(Ljava/lang/String;)Ljava/lang/String;
	astore_2
.var 3 is b F from Label0 to Label1
	ldc 123.123
	fstore_3
Label0:
	aload_2
	invokestatic io/printString(Ljava/lang/String;)V
Label1:
	return
.limit stack 3
.limit locals 4
.end method

.method public static main([Ljava/lang/String;)V
.var 0 is args [Ljava/lang/String; from Label0 to Label1
Label0:
	ldc " CaoTuanKiet"
	ldc "!!!!"
	invokestatic MT22Class/foo1(Ljava/lang/String;Ljava/lang/String;)V
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
