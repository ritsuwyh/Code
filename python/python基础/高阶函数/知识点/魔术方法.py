
# __init__ : 构造函数，在生成对象时自动调用
# __del__ : 析构函数，在释放对象时自动调用
# __repr__ : 当repr()调用时被自动调用
# __str__: 当str()调用时被自动调用 或者print()
# __len__: 当len()调用时被自动调用
#! 见双向字典
# __delitem__ ...
# __setitem__ : 按照索引[]赋值时被调用
# __getitem__: 按照索引[]获取值时被调用

#__bool__函数 在bool()的时候自动调用
# Account.__bool__ = lambda self: self.balance != 0
# bool(Account('Jack'))

#todo 自己生成一个range类
#! 方法1
class MyRange(object):
        def __init__(self, end):
            self.start = 0
            self.end = end
#         #! 可迭代对象必须要有 __iter__ 和 __next__ 
# 什么是迭代器？
# – 具有__next__()方法的对象
#  什么是可迭代对象？
# – 具有__iter__()方法，且返回的是迭代器的对象
        def __iter__(self):
            return self
        def __next__(self):
            if self.start < self.end:
                ret = self.start
                self.start += 1
                return ret
            else:
                raise StopIteration#! 以抛出异常的形式表示遍历结束

for i in MyRange(10):
    print(i)
# #!方法2
class MyRange:
    def __init__(self,end):
        self.start=0
        self.end=end
        self.step=1
    def __iter__(self):
        return MyIter(self)
class MyIter:
    def __init__(self,my_range:MyRange) -> None:
        self.range=my_range
        self.cur=self.range.start
    def __next__(self):
        return_val=self.start
        if return_val==self.end:
            raise StopIteration
        self.cur+=self.range.step
        return return_val
        



#todo class里面重写以下方法类似于c++里面的操作符重载 
#用于比较的特殊方法：
# __cmp__: 返回比较的结果
# __eq__: ==
# __ne__: !=
# __lt__: <
# __gt__: >=
# 用于运算的特殊方法：
# __add__: +
# __sub__: -
# __mul__: *
# __truediv__: \
# __mod__: %
# __pow__:**
# class MyNumber():
#     def __init__(self, value):
#         self.value = value
#     def __add__(self, other):
#         return MyNumber(self.value + other.value)
#     def __str__(self):
#         return str(self.value)
# #! 可以实现自定义类对象的运算 注意在print的时候会自动调用__str__函数
# n1 = MyNumber(10)
# n2 = MyNumber(15)
# print(n1 + n2)

#?对于MyNumber与int的混合运算，应该如何实现？
class MyNumber():
    def __init__(self, value):
        self.value = value
    def __add__(self, other:any)->int:#! 注意这里自定义类对象只能在+的左面
        if isinstance(other,int):
            return self.value+other
        else:
            return self.value + other.value
    def __str__(self):
        return str(self.value)
#! 可以实现自定义类对象的运算 注意在print的时候会自动调用__str__函数
n1 = MyNumber(10)
n2 = MyNumber(15)
n3=100
print(type(n1 + n2),n1+n2)
print(type(n1+n3),n1+n3)

#todo我们都知道在 Python 中，两个字符串相加会自动拼接字符串，但遗憾的是两个字符串相减却抛出异常。
# todo因此，现在我们要求定义一个 Nstr 类，支持字符串的相减操作：A – B，从 A 中去除所有 B 的子字符串。
#* 我们可以继承str类 然后重写 __sub__ 方法

#__call__ 在对象出现在函数调用语句中时自动被调用
# class Adder():
#     def __init__(self, n):
#         self.n = n
#     def __call__(self, k):
#         return self.n + k
# #! 这样写比函数的闭包更加灵活 
# add_three_obj = Adder(3)
# add_three_obj(4)
# add_four_obj = Adder(4)
# ...