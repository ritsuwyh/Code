import numpy as np
# 实现一个卷积运算：卷积运算是指从输入矩阵的左上角开始，开一个与模板矩阵（卷积核）同样大小的活动窗口，窗口矩阵元素与模板矩阵元素对应起来相乘再相加，并用计算结果代替窗口中心的值。然后，活动窗口向右移动一列，并作同样的运算。以此类推，从左到右、从上到下，即可得到一个新的矩阵即为卷积的结果。
# 请编程实现卷积运算，输入为两个numpy矩阵，M,N，维度分别为mxm和nxn（m>n）。要求以M为输入矩阵，N为模板矩阵（卷积核）进行卷积操作，输出卷积得到的新矩阵，维度应该为（(m-n+1)x(m-n+1)）。
#     现在需要通过两种方式实现卷积运算，并且比对两种方式的效率。
#     提示：一种是不改变输入，用for循环来不停移动窗口和模板进行卷积。
#     另一种是预先将输入矩阵处理成更大的矩阵（可以扩展维度，也可以将每次卷积需要的输入   reshape成1维然后拼接），然后再用模板利用广播机制去卷积。

import time


arr1=np.array([[0., 1., 2., 3., 4.],
 [0. ,1., 2. ,3., 4.],
 [0., 1., 2., 3. ,4.],
 [0., 1., 2., 3., 4.],
 [0. ,1., 2., 3., 4.]])
arr2=np.array([[1., 1., 1.],
 [1., 1., 1.],
 [1., 1., 1.]])


strde=1
m1,n1=np.shape(arr1)
m2,n2=np.shape(arr2)

#! 实际上 x y 移动的次数就是所求结果的行数和列数
x=(m1-m2)//strde+1#! 行数
y=(n1-n2)//strde+1#! 列数


start = time.perf_counter()
#方法1
ans=np.zeros((x,y))
for i in range(x):
    for j in range(y):
        print(arr1[strde*i:strde*i+m2,strde*j:strde*j+n2]*arr2)
        print('---------------------------------------')
        temp=np.sum(arr1[strde*i:strde*i+m2,strde*j:strde*j+n2]*arr2)
        ans[i,j]=temp
        
end = time.perf_counter()
print("运行时间为", end-start, 'seconds')  

print('**************************')
print(ans)

# arr1=np.arange(9).reshape((1,3,3))
# print(arr1)
# arr1=np.vstack((arr1,np.arange(9).reshape(1,3,3)))
# print(arr1)

#方法2 对原矩阵进行预处理 变为三维矩阵
temp=None
flag=True

start = time.perf_counter()
for i in range(x):
    for j in range(y):
        if flag:
            temp=arr1[strde*i:strde*i+m2,strde*j:strde*j+n2].reshape(1,m2,n2)
            flag=False
        else:
            temp=np.vstack((temp,arr1[strde*i:strde*i+m2,strde*j:strde*j+n2].reshape(1,m2,n2)))
# print(temp)
end = time.perf_counter()
print("运行时间为", end-start, 'seconds')  
print('************')
print(np.sum(temp*arr2,axis=(1,2)).reshape(x,y))#! arr2 进行广播 然后1，2维度求和 得到一维数组 然后reshape得到答案


#! 我们利用reshape可以对一个矩阵进行升维度操作 sum函数可以同时合并多个维度

#! 统计某一段程序的运行时间
# import time
# start = time.perf_counter()
# ######## 实际程序开始 ##########
# for i in range(10000):
# 	for j in range(10000):
# 		pass
# ######## 实际程序结束 ##########
# end = time.perf_counter()
# print("运行时间为", (end-start), 'seconds')

