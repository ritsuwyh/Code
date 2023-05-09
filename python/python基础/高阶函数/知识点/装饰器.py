


# def hi(name="yasoob"):
#     return "hi " + name
 
# print(hi())
# # output: 'hi yasoob'
 
# # 我们甚至可以将一个函数赋值给一个变量，比如
# greet = hi
# # 我们这里没有在使用小括号，因为我们并不是在调用hi函数
# # 而是在将它放在greet变量里头。我们尝试运行下这个
 
# print(greet())
# # output: 'hi yasoob'
 
# # 如果我们删掉旧的hi函数，看看会发生什么！
# del hi
# print(hi())
# #outputs: NameError
 
# print(greet())
#outputs: 'hi yasoob' #! 删去hi函数 但是greet仍然可以调用

#! 函数中定义函数(闭包) 函数作为返回值 惰性函数 将函数作为参数传给另一个函数--抽象函数 函数可以指向变量 函数可以指向函数(装饰器)

#todo 装饰器例子
# def a_new_decorator(a_func):
 
#     def wrapTheFunction():
#         print("I am doing some boring work before executing a_func()")
 
#         a_func()
 
#         print("I am doing some boring work after executing a_func()")
 
#     return wrapTheFunction

# @a_new_decorator #!the @a_new_decorator is just a short way of saying:
# #!a_function_requiring_decoration = a_new_decorator(a_function_requiring_decoration)
# def a_function_requiring_decoration():
#     """Hey you! Decorate me!"""
#     print("I am the function which needs some decoration to "
#           "remove my foul smell")
 
# a_function_requiring_decoration()
# #outputs: I am doing some boring work before executing a_func()
# #         I am the function which needs some decoration to remove my foul smell
# #         I am doing some boring work after executing a_func()
 


# #todo用 funA() 函数装饰器去装饰 funB() 函数
# #funA 作为装饰器函数
# def funA(fn):
#     #...
#     fn() # 执行传入的fn参数
#     #...
#     return '...'

# @funA
# def funB():
    #...

#todo 带参数的装饰器 比较简单的解决方法就是在函数装饰器中嵌套一个函数，该函数带有的参数个数和被装饰器修饰的函数相同。
# def funA(fn):
#     # 定义一个嵌套函数
#     def say(arc):
#         print("Python教程:",arc)
#     return say

# @funA
# def funB(arc):
#     print("funB():", a)
# funB("http://c.biancheng.net/python")

#!exec 执行储存在字符串或文件中的Python语句，相比于 eval，exec可以执行更复杂的 Python 代码。
#todo 例子
# input_str = "@say_hi\ndef add(a,b):\n\tprint(a+b)\nadd(1,2)"
# exec(input_str)
#todo 例子
# >>>exec 'print "Hello World"'
# Hello World
# # 单行语句字符串
# >>> exec "print 'runoob.com'"
# runoob.com
 
# #  多行语句字符串
# >>> exec """for i in range(5):
# ...   print "iter time: %d" % i
# ... """
# iter time: 0
# iter time: 1
# iter time: 2
# iter time: 3
# iter time: 4


#todo
def say_hi(func):
    def sayx(*x):#!必须传入可变参数 这里的函数变量个数要和你要装饰的函数参数的个数保持一致!!!!
        print("Hello World")
        func(*x)
    return sayx

@say_hi
#! 相当于执行 add=say_hi(add)!!!
def add(a,b):
    print(a+b)
    
add(1,2)    