
#todo输入一个整数n，使用lambda, all, map, filter 等函数，从小到大顺序输出[2,n]区间的所有质数。
#* all(iterable) all函数
# >>> all(['a', 'b', 'c', 'd'])  # 列表list，元素都不为空或0
# True
# >>> all(['a', 'b', '', 'd'])   # 列表list，存在一个为空的元素
# False
# >>> all([0, 1，2, 3])          # 列表list，存在一个为0的元素
# False
   
# >>> all(('a', 'b', 'c', 'd'))  # 元组tuple，元素都不为空或0
# True
# >>> all(('a', 'b', '', 'd'))   # 元组tuple，存在一个为空的元素
# False
# >>> all((0, 1, 2, 3))          # 元组tuple，存在一个为0的元素
# False
   
# >>> all([])             # 空列表
# True
# >>> all(())             # 空元组
# True
# !如果iterable的所有元素不为0、''、False或者iterable为空，all(iterable)返回True，否则返回False；
# !注意：空元组、空列表返回值为True，这里要特别注意。
# def is_prime(num):
#     for i in range(2,num):
#         if num%i==0:
#             return False
#     return True
n=eval(input())
#! all的用法 int(x**0.5)+1的用法
print(list(filter(lambda x: all([x%i for i in range(2,int(x**0.5)+1)]) ,[i for i in range(2,n+1)])))


# for i in range(2,1):#! 不会报错
#     print(i)