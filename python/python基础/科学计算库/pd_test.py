import pandas as pd
import numpy as np

#lst=list(map(int,input().split()))

#! 创建 series 对象

#从ndarray对象创建
s=pd.Series([1,2,3])
s1=pd.Series([1,2,3],index=['a','b','c'])
print(s1)
s3 = pd.Series(np.random.rand(5), index = list("abcde"))

#从dict
pd.Series({"b": 1, "a": 0, "c": 2})
pd.Series(dict(zip(list("abcde"), np.arange(5))))

#广播
pd.Series(10, index = list("abc"))

#可以给series命名，以表示特定的数值关系
test1=pd.Series([1,2,3],index=list('abc'),name='test1')
print(test1)

test1.rename('xx',inplace=True)#! 如果指定参数inplace==True 那么函数返回None
#并直接在原来series的基础上进行修改 如果不指定参数inplace 那么返回一个新的serise对象
print(test1)


#! series 的操作
#dict操作：series对象可以像dict一样参与运算和使用
s['a']=0
s.get('g',default=np.nan)


#! 合并
s1 = pd.Series([1.0, 2.0, 3.0], index=["a", "b", "c"])
s3 = pd.Series([4.0, 5.0, 6.0], index=["b", "c", "a"])
print(s1+s3)
#运算中默认将不能对应的index值视为NaN
s4 = pd.Series([4.0, 5.0, 6.0], index=["b", "c", "d"])
print(s1+s4)

s5 = pd.Series([4.0, 5.0], index=["b", "c"])#! 因为s1里面有a 而s5里面没有 所以 s1+s5里面 a的值是NAN

print(s1+s5)


#! 实例 为若干成员发工资

salaries = [3000, 4500, 8000]
names = ['Mayue', 'Lilin', 'Wuyun']
salaries_list = pd.Series(salaries, index = names)
bonus = pd.Series({'Mayue': 500, 'Wuyun': 1000})

#! 我们现在不能直接把两个series直接加到一起 因为bonus 里面确实Lilin的数据 会导致Lilin对应的数为Nan

# 方法一
salaries_list.add(bonus, fill_value = 0) #在函数中指定缺失值的处理策略

# 方法二 预处理缺失值
#bonus = bonus.reindex(names)#! 重新设置index 
#bonus = bonus.fillna(0)
bonus = bonus.reindex(names,fill_value=0)
print(bonus)

# series reindex
# s1 = pd.Series([1, 2, 3, 4], index=['A', 'B', 'C', 'D'])
# print(s1)
# '''
# A    1
# B    2
# C    3
# D    4
# dtype: int64
# '''


# # 重新指定 index， 多出来的index，可以使用fill_value 填充 少的就相当于切片
# print(s1.reindex(index=['A', 'B', 'C', 'D', 'E'], fill_value = 10))
# '''
# A     1
# B     2
# C     3
# D     4
# E    10
# dtype: int64
# '''
# print(s1.reindex(index=['A', 'B','E'], fill_value = 10))
# '''
# A     1
# B     2
# E    10
# dtype: int64
# '''

#方法三 bonus.index 利用切片
salaries_list[bonus.index] += bonus
print(salaries_list)


#! dataframe
#from series 

# – 构建一个单列的DataFrame
# – Series的index会成为表格的index
# – 默认的列名（column name）为数值索引 如果series 指定name了 那么colunm name 就是 series 的name
s = pd.Series([4, 5, 6], index = list("bca"),name='wyh')
x=pd.DataFrame(s)
print(x)


#! from dict of series
# – series的index将被自动对齐一致，作为index
# – dict的index将作为column name
# In [53]: s = pd.Series([4, 5, 6], index = list("bca"))
# In [63]: s2 = pd.Series([1, 2, 3], index = list("abc"))
# In [65]: pd.DataFrame({"one":s, "two":s2})



#! from np.array  可以创建多列的 dataframe
# In [66]: data = np.array([(1, 2.0, "Hello"), (2, 3.0, "World")])
# #默认的index和column name都为数值索引
# In [67]: pd.DataFrame(data)

# #指定index和columns
# In [68]: pd.DataFrame(data, index = ["first","second"], columns = 
# ["id","value", "string"])


#! from a list of dicts

# dict 的key 就是Column 的名字
# In [69]: data2 = [{"a": 1, "b": 2}, {"a": 5, "b": 10, "c": 20}] 

# In [70]: pd.DataFrame(data2)
# Out[70]:
# a b c
# 0 1 2 NaN
# 1 5 10 20.0

#!pd.DataFrame 的操作



#! 使用numpy的函数来加载 txt文件
# data=np.loadtxt('word_embedding.txt')