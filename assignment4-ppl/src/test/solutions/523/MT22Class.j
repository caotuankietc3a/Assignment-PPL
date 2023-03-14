.source MT22Class.java
.class public MT22Class
.super java/lang/Object
.field static arr3 [[I

.method public static main([Ljava/lang/String;)V
    .limit stack 10
    .limit locals 1

    getstatic MT22Class/arr3 [[I ; load the 2-dimensional array
    ldc 1                       ; index of first dimension
    ldc 2                       ; index of second dimension
    iaload                      ; load the value at index [1][2]
    invokestatic java/lang/System/out.println(I)V ; print the value to the console

    return
.end method

.method public <init>()V
    aload_0
    invokenonvirtual java/lang/Object/<init>()V
    return
.end method

.method public static <clinit>()V
    .limit stack 10
    .limit locals 2

    ldc 3                       ; size of first dimension
    anewarray [I                ; create a new integer array of size 3 for the first dimension

    ; initialize each element in the first dimension with a new integer array of size 4 for the second dimension
    dup                         ; duplicate the first dimension array reference on the stack
    iconst_0                    ; index of the first element in the first dimension
    ldc 4                       ; size of the second dimension
    newarray int                ; create a new integer array of size 4 for the second dimension
    aastore                     ; store the second dimension array in the first dimension array
    dup                         ; duplicate the first dimension array reference on the stack
    iconst_1                    ; index of the second element in the first dimension
    ldc 4                       ; size of the second dimension
    newarray int                ; create a new integer array of size 4 for the second dimension
    aastore                     ; store the second dimension array in the first dimension array
    dup                         ; duplicate the first dimension array reference on the stack
    iconst_2                    ; index of the third element in the first dimension
    ldc 4                       ; size of the second dimension
    newarray int                ; create a new integer array of size 4 for the second dimension
    aastore                     ; store the second dimension array in the first dimension array

    ; assign value to one element
    getstatic MT22Class/arr3 [[I ; load the 2-dimensional array
    dup                         ; duplicate the array reference on the stack
    ldc 1                       ; index of first dimension
    aaload                      ; load the array at index 1
    ldc 2                       ; index of second dimension
    iconst_5                    ; value to assign to the element
    iastore                     ; store the value in the array

    putstatic MT22Class/arr3 [[I ; store the 2-dimensional array in the field

    return
.end method
