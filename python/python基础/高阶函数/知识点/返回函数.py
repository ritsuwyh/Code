

#! 把函数f 柯里化
def f1(a,b,c): 
    pass
#! 背下来
def g(x):#! 三层柯里化
    def temp1(y):
        def temp2(z):
            return f1(x,y,z)
        return temp2
        
    return temp1
# while True:
#     exec(input())
#!  这里f(x,y,z) 就是 g(x)(y)(z)、


# #! 形参是需要已经被柯里化的 需要去柯里化的函数 
# #! 返回去完柯里化的函数 使用是用 f=uncurry(g) 用f(x,y)即可正常调用f了
# def uncurry2(g):
#     def f(x,y):
#         return g(x)(y)
#     return f




##!不需要立刻求和，而是在后面的代码中，根据需要再计算怎么办？可以不返回求和的结果，而是返回求和的函数：
# def lazy_sum(*args):
#     def sum():
#         ax = 0
#         for n in args:
#             ax = ax + n
#         return ax
#     return sum
#!当我们调用lazy_sum()时，返回的并不是求和结果，而是求和函数：
# f = lazy_sum(1, 3, 5, 7, 9)
# >>> f
# <function lazy_sum.<locals>.sum at 0x101c6ed90>
# 调用函数f时，才真正计算求和的结果：

# >>> f()
# 25

# 在这个例子中，我们在函数lazy_sum中又定义了函数sum，并且，内部函数sum可以引用外部函数lazy_sum的参数和局部变量，当lazy_sum返回函数sum时，
# 相关参数和变量都保存在返回的函数中，这种称为“闭包（Closure）”的程序结构拥有极大的威力。

# 请再注意一点，当我们调用lazy_sum()时，每次调用都会返回一个新的函数，即使传入相同的参数：
#! 函数的柯里化 看网站收藏夹 定义一 定义二实际上就是偏函数的应用 而定义三一个函数有多个参数，将其拆分成几个函数，每一个函数只具有其中的部分参数，实现函数参数的拆分。
#! 不管是基于第一种、第二种定义，他更加侧重于将一个函数的多个参数中的其中几个先固定，这样减少参数的数量还是基于第三中定义，它更加侧重于将函数的多个参数拆分成少量几个参数的组成，其实它们的本质都是一样，它们的实现核心思想也是一样的，真正核心的地方就在于“高阶函数”。
#! 详情见收藏夹
# def add(x, y):
#     return x + y
 
# # 柯里化
# def currying_add(x):
#     def inc(y):
#         return x + y
#     return inc  # 返回函数
 
# result = currying_add(2)(3)
# print(result)   # 5


#! 写一个每次都加n的函数 n可以随便改  相当于把 函数 n+m 柯里化
# def add_print_cur(x):
#     def f(y):
#         return x+y
    
#     return f
# func=add_print_cur(3) 闭包内部的func这个函数已经记住了这个x=3这个值
# print(func(4),func(5),...)