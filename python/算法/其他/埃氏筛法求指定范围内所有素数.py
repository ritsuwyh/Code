
#! 复习使用generator 生成fib数

#!难理解的就是generator函数和普通函数的执行流程不一样。普通函数是顺序执行，
# !遇到return语句或者最后一行函数语句就返回。而变成generator的函数，在每次调用next()的时候执行，
# !遇到yield语句返回，再次执行时从上次返回的yield语句处继续执行


#!可以先构造一个从3开始的奇数序列：对于无限序列常常使用生成器 
def _odd_iter():
    n = 1
    while True:
        n = n + 2
        yield n
#! 定义一个筛选函数 
def _not_divisible(n):
    return lambda x: x % n > 0
#!最后，定义一个生成器，不断返回下一个素数：
def primes():
    yield 2
    it = _odd_iter() # 初始序列
    while True:
        n = next(it) # 返回序列的第一个数
        yield n
        it = filter(_not_divisible(n), it) # 构造新序列

#!注意到filter()函数返回的是一个Iterator，也就是一个惰性序列，所以要强迫filter()完成计算结果，需要用list()函数获得所有结果并返回list。
# 打印1000以内的素数:
for n in primes():
    #!由于primes()也是一个无限序列，所以调用时需要设置一个退出循环的条件：
    if n < 1000:
        print(n)
    else:
        break
    
    
#!不需要立刻求和，而是在后面的代码中，根据需要再计算怎么办？可以不返回求和的结果，而是返回求和的函数：
def lazy_sum(*args):
    def sum():
        ax = 0
        for n in args:
            ax = ax + n
        return ax
    return sum
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