import numpy as np
#给定两个int型list，长度分别为n,m。请编写程序完成以下功能：
# 1）将这两个list分别转换成1xn和1xm的numpy向量N,M。
# 2）计算N^TxM（N的转置矩阵乘上M，输出维度应为nxm）的结果

#1
n,m=4,5
lst1=[0 for i in range(n)]
lst2=[0 for i in range(m)]
arr1=np.array(lst1)#! 这是向量 [0 0 0 0]
arr1=np.reshape(arr1,(1,4))#! 这是矩阵[[0 0 0 0]]
print(arr1)
arr2=np.array(lst2).reshape((1,-1))
print(arr2)

# print(arr1.transpose())#![0 0 0 0]转置 就是本身
# li = [i for i in range(10)]
# print(li)        # 输出的结果是  [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]`


#2
#!print(arr1.T*arr2) 这个会进行广播 然后对应元素进行相乘 与下面有本质的区别
print(arr1.T.dot(arr2))#! 向量没法转置 