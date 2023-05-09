
import numpy as np

# x=np.arange(30)
# yy=np.reshape(x,(2,3,5))
# print(yy)
# print(yy.sum(axis=(0,2)))#! 相当于先按层求和(把层合并) 然后再按行求和 把行合并

# a = np.array([[100, 3, 5, 7],[5, 7, 2, 2],[4, 6, 8, 1]])
# print(a.argmax())

#print(np.outer(x,x))
# x=np.arange(10)

# y=x.reshape(2,5)
# print(y)
# print(y[:,])
# print(y[:,0:1])
#todo ipython 的使用 终端输入ipython
#!https://blog.csdn.net/qq_39362996/article/details/82892671
#!https://www.dune9.com/post/7133
# %timeit  %%timeit 单行多行计算时间
# %paste#! 完美 复制




# 1、如何创建定义ufunc
# 要创建自己的ufunc，必须定义一个函数，就像使用Python中的普通函数一样，然后使用frompyfunc()方法将其添加到NumPy ufunc库中。

# frompyfunc()方法采用以下参数：

# function- 函数的名称。
# inputs- 输入参数(数组)的数目。
# outputs- 输出数组的数目。

 

# def myadd(x):
#     return x*x

# myadd = np.frompyfunc(myadd, 1, 1)
# print(myadd([1, 2, 3, 4]))



#todo np.nonzero()
#!https://www.cnblogs.com/1zhk/articles/4782812.html

#! 用法见网站和插件注解
#todo np.where()
#!https://blog.csdn.net/lens___/article/details/83896645

#* 注意当只有condition参数时,就相当于调用了nonzero函数
#np.nonzero 见官方文档 
#np.count_nonzero

# np.where([[True,False], [True,True]],    # 官网上的例子
#              [[1,2], [3,4]],
#              [[9,8], [7,6]])

# array([[1, 8],
#        [3, 4]])
# ``
# `
# 上面这个例子的条件为[[True,False], [True,False]]，分别对应最后输出结果的四个值。第一个值从[1,9]中选，因为条件为True，所以是选1。第二个值从[2,8]中选，因为条件为False，所以选8，后面的以此类推。

# 同理，再看下面的一个例子：

# ```python
# a = 10
# np.where([[a > 5,a < 5], [a == 10,a == 7]],
#              [["chosen","not chosen"], ["chosen","not chosen"]],
#              [["not chosen","chosen"], ["not chosen","chosen"]])

# array([['chosen', 'chosen'],
#        ['chosen', 'chosen']], dtype='<U10')

#todo np.choose(a,choices)
#!https://blog.csdn.net/jydpd_2008/article/details/79501873
#! 其实就是按照a数组的选法 在choices中选择元素重新构造数组a
# a=[[1,0,2],[2,1,0],[2,0,1]]
# c1=[[1,2,3],[4,5,6],[7,8,9]]
# c2=[[11,22,33],[44,55,66],[77,88,99]]
# choices=[c1,100,c2]
# result=np.choose(a,choices)
# print(result)
#np.choose()#! 注意官方给的例子


#todo np.select()
#!https://blog.csdn.net/qq_27825451/article/details/82698929
# np.select()

# a=np.array([1,2,3,4,5,6,7,8,9,10])
# print(a<6)
# condlist=[a<6]      #第一个参数，必须用【】括起来，列表形式
# print(condlist)
# choicelist=[a+10]   #第二个参数，必须用【】括起来，列表形式
# print(choicelist)
# aa=np.select(condlist,choicelist,default=100)
# print(aa)

# 什么意思呢？可以这样理解，对于第一个参数condlist=[ a<6 ]，我们将a<6看成是一个条件，只不过这个条件是针对array类型的a的，
# 第二个参数choicelist所要执行的操作是依据condlist而言的，即这里的  [a+10]里面的a+10这个操作，和 [a<6]这个里面的，
# a<6是对应关系的，即当第一条件里的每个元素满足条件的时候，即为True的时候，就执行相应的操作，如果为false，那么久不执行，
# 而对于不满足的元素，则执行默认的值，即default。

# a=np.array([[1,2,3,4,5],[6,7,8,9,10],[11,12,13,14,15],[16,17,18,19,20],[21,22,23,24,25]])
# condlist=[a<6,np.logical_and(a>10,a<16),a>20]  #参数一，定义三个限制条件
# print(condlist)
# condlist=[a<6,(a>10) & (a<16), a>20]#! 这里不能用 and   

# print(condlist)
# choicelist=[a+10,a**2,a*10]                    #参数二，定义三个不同的操作
# print(choicelist)
# aa=np.select(condlist,choicelist)
# print(aa)
 
# print('=======================================')

#! boolean array可以进行逻辑运算
# （1）np.logical_and(array1, array2)

# （2）np.logical_or(array1, array2)

# （3）np.logical_xor(array1, array2)

# （4）np.logical_not(array1)

# np.mean()
# np.average()
# mean和average都是计算均值的函数，在不指定权重的时候average和mean是一样的。
# 指定权重后，average可以计算一维的加权平均值
# b = np.array([1, 2, 3, 4])
# wts = np.array([4, 3, 2, 1])
# print('不指定权重\n', np.average(b))
# print('指定权重\n', np.average(b, weights=wts))




#!关于np.delete() 
# x=np.array([[1,2,3],[4,5,6]])
# print(np.delete(x,0,0))
#[[4 5 6]]
#!https://blog.csdn.net/qq_18351157/article/details/104014933




#!np.insert()
#!https://www.cjavapy.com/article/908/
#a = np.array([[1, 1], [2, 2], [3, 3]])
# print(np.insert(a, 1, 5, axis=0))#! 这里的1 理解为在第一个数字之后插入
#输出结果#! 相当于对数字5进行了广播操作
# [[1 1]
#  [5 5]
#  [2 2]
#  [3 3]]
# print(np.insert(a, 1, 5, axis=1))
# 输出结果
# [[1 5 1]
#  [2 5 2]
#  [3 5 3]]
# a = np.array([[1, 1], [2, 2], [3, 3]])
# print(np.sum(a,0))
# [6 6]

# a=np.array([[[1,2,3],[4,5,6]],[[1,2,3],[4,5,6]],[[1,2,3],[4,5,6]]])
# print(a)
# print(np.sum(a,axis=2))
#print(np.insert(a,1,[1],axis=1))
# [[1 1 1]
#  [2 1 2]
#  [3 1 3]]
#print(np.insert(a,1,[4,5,6],axis=1))#! 相当于在第一个元素之后分别插入4 5 6
# [[1 4 1]
#  [2 5 2]
#  [3 6 3]]

#! np数学运算  
#! 理解out参数
# x=np.array([1,2,3,4,5,6])
# y=np.add(x,5,where=(x%2==0))
# print(y)
# z=np.add(x,5,where=(x%2==0),out=x)
# print(z)
# print(x)
#!https://blog.csdn.net/weixin_42575020/article/details/106947188



#! np 比较运算
# x = np.arange(10)
# x    # array([0, 1, 2, 3, 4, 5, 6, 7, 8, 9])
 
# x < 5    # array([ True,  True,  True,  True,  True, False, False, False, False, False])
# x[x<5]    # array([0, 1, 2, 3, 4])
# x >= 5    # array([False, False, False, False, False,  True,  True,  True,  True, True])
# x == 5    # array([False, False, False, False, False,  True, False, False, False, False])
# x != 5    # array([ True,  True,  True,  True,  True, False,  True,  True,  True, True])
 
# x - 1 != x // 2    # array([ True, False, False,  True,  True,  True,  True,  True,  True, True])
 
# x + 2 == x // 2 + 3    # array([ True, False, False,  True,  True,  True,  True,  True,  True, True])
 
# x[x + 2 == x // 2 + 3]    # array([1, 2])

# X < 5    # array([[ True,  True,  True,  True],
#                   [ True, False, False, False],
#                   [False, False, False, False],
#                   [False, False, False, False]])
# x = x + 2    # 执行2次
# x    # array([ 4,  5,  6,  7,  8,  9, 10, 11, 12, 13])
# np.sum(x < 8)    # 4
# np.count_nonzero(x < 8)    # 4
# np.any(x < 4)    # False
# np.any(x <= 4)    # True
# np.all(x > 4)    # False
# np.all(x >= 4)    # True
 
# np.sum(X % 2 == 0)    # 8
# np.sum(X % 2 == 0, axis=0)    # array([4, 0, 4, 0])
# np.sum(X % 2 == 0, axis=1)    # array([2, 2, 2, 2])
# np.sum((X > 2) & (X < 10))    # 7
# np.sum((X == 2) | (X == 10))    # 2
# np.sum(~(X == 2))    # 15
# X[(X > 2) & (X < 10)]    # array([3, 4, 5, 6, 7, 8, 9])
 
# X[:, -1]    # array([ 3,  7, 11, 15])，最后1列
# X[:, -2]    # array([ 2,  6, 10, 14])，倒数第2列
# X[:, -1] % 3 == 0    # array([ True, False, False,  True])
# X[X[:, -1] % 3 == 0]    # array([[ 0,  1,  2,  3],
#                                  [12, 13, 14, 15]])
# X[X[:, -1] % 3 == 0, :]    # array([[ 0,  1,  2,  3],
#                                     [12, 13, 14, 15]])
# X[X[:, -1] % 3 == 0, -1]    # array([ 3, 15])
# X[X[:, -1] % 3 == 0, 1:3]    # array([[ 1,  2],
#                                       [13, 14]])


# np.greater
# np.greater_equal
# np.less
# np.less_equal
# np.equal
# np.not_equal


# #! 前缀和的应用
# def my_average(arr,win_len:int):
#     x=np.cumsum(arr)
#     print(x)
#     sumx=0
#     for i in range(win_len-1,len(x)):
#         if i==win_len-1:
#             sumx+=x[i]
#         else:
#             sumx+=x[i]-x[i-win_len]
#     return sumx/(len(x)-win_len+1)

# print(my_average(np.arange(6),3))


# 计算给定矩阵的平方根矩阵。其中，负数的平方根为其绝对值的平方根的相反数。

x=np.random.randint(-100,101,(5,5))
print(x)
#! 重新构建x矩阵
z=np.select([x<0,x>=0],[-np.sqrt(np.abs(x)),np.sqrt(x)])
print(z)


# 局部极大值#! 利用错位的思想
x=np.array([2,3,1,4,3,5,5,4,3,2,5])
temp=x[1:-1]
temp_l=x[:-2]
temp_r=x[2:]
print(temp[np.logical_and (temp>temp_r,temp>temp_l )])



#!np.squeeze
# numpy.squeeze(a, axis=None)

# squeeze()函数的功能是：从矩阵shape中，去掉维度为1的。例如一个矩阵是的shape是（5， 1），使用过这个函数后，结果为（5，）。

# 参数：
# a是输入的矩阵
# axis : 选择shape中的一维条目的子集。如果在shape大于1的情况下设置axis，则会引发错误。
# ————————————————

# print(np.ones((3)))
#! 复习笔记 广播
A=np.ones((3,1,2))
B= np.ones((3,1))
print(np.squeeze(A)*B)
A=np.ones((3,1,2))
B= np.ones((3,1))
print(np.shape(A*B))


# np.maximum
# np.minimum
z=np.arange(10).reshape((5,2))
print(z[z>5])


#  创建一个2维数组，该数组边界值为1，内部的值为0 
# Z = np.ones((10, 10))
# Z[1:-1, 1:-1] = 0
# print (Z)


# Z = np.ones((10, 10))
# Z = np.pad(Z, pad_width=1, mode='constant', constant_values=0)
# print (Z)

#创建一个8x8的国际象棋棋盘矩阵（黑块为0，白块为1） (★☆☆)
# Z = np.zeros((8, 8), dtype=int)
# Z[1::2, ::2] = 1
# Z[::2, 1::2] = 1
# print (Z)


# # 给定一个一维数组把元素值从3到8的元素求相反数 (★☆☆)
# Z = np.arange(11)
# Z[(3 <= Z) & (Z < 8)] *= -1#! 求相反数 *=-1
# print (Z)

# #创建一个5x5的矩阵且每一行的值范围为从0到4 (★★☆)
# #! 利用广播
# Z = np.zeros((5, 5))
# Z += np.arange(5)
# print (Z)

# #! 掐头去尾用切片
# Z = np.linspace(0, 1, 12, endpoint=True)[1: -1]
# print (Z)


#对一个小数组进行求和有没有办法比np.sum更快?
# Z = np.arange(10)
# np.add.reduce(Z)
# np.add.reduce 是numpy.add模块中的一个ufunc(universal function)函数,C语言实现


#如何在数组中找到与给定标量接近的值? 
# Z = np.arange(100)
# v = np.random.uniform(0, 100)
# index = (np.abs(Z-v)).argmin()
# print(Z[index])


# 创建一个大小为10的随机向量并且将该向量中最大的值替换为0**(★★☆)
# (提示: argmax)
# Z = np.random.random(10)
# Z[Z.argmax()] = 0
# print (Z)


#减去矩阵每一行的平均值 (★★☆)
#! 使用reshape 调整形状 进行广播
# X = np.random.rand(5, 10)
 
# # 新
# Y = X - X.mean(axis=1, keepdims=True)
 
# # 旧
# Y = X - X.mean(axis=1).reshape(-1, 1)
 
# print(Y)

#70.考虑向量[1,2,3,4,5]，如何建立一个新的向量，在每个值之间交错有3个连续的零？ (★★★)
#! 我们预先求出新向量的大小 然后修改对应位置的元素即可
arr=np.array([1,2,3,4,5])
lenx=len(arr)
new_arr=np.zeros(4*(lenx-1)+1)#! 长度为4*(lenx-1)+1的向量
#arr=np.zeros((1,10)) 这是矩阵 不是向量
new_arr[::4]=arr
print(new_arr)


#交换两行
# arr=np.arange(10).reshape((5,2))
# arr[[0,1]]=arr[[1,0]]#! 交换两行
# arr[:,[0,1]]=arr[:,[1,0]]#! 交换两列
# print(arr)

#第n个最大的数
# x=np.arange(10).reshape((5,2))
# x=np.sort(x)
# print(x.flatten()[4])


#! 不用库函数的矩阵旋转操作
# matrix=[[1,2,3],[4,5,6],[7,8,9]]
# matrix=list(zip(*matrix))
# print(matrix[::-1])#! 逆时针转90

# matrix=[list(col)[::-1] for col in matrix]#! 顺时针旋转90
# print(matrix)

class Solution:
    def rotate(self, matrix: list[list[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        # matrix[:]=list(zip(*matrix))
        # matrix[:]=[list(col)[::-1] for col in matrix]
        matrix[:]=[list(col)[::-1] for col in list(zip(*matrix))]
solution=Solution()
matrix=[[1,2,3],[4,5,6],[7,8,9]]
solution.rotate(matrix)
print(matrix)



# def func(lst):
#     lst.append(1)
    
# lst=[1,2,3]
# func(lst)
# print(lst)#[1, 2, 3, 1]

# def funcx(x):
#     x=2
# number=6
# funcx(number)
# print(number)#输出 2

#!叉乘 点乘的资料

#!https://blog.csdn.net/weixin_39571403/article/details/110695950

# x=np.array([1,2,4,5,6])
# print(np.shape(x))#(5,)
# y=np.random.rand(5,3)
# #print(x*y)#operands could not be broadcast together with shapes (5,) (5,3)
# print(x*y.T)#在广播的时候会把向量当成1*5的
# print(np.dot(x,y))#向量点乘矩阵

