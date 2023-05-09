
from functools import reduce#
#! 三个函数的综合应用
#!描述：输入一些数，请去除可以被3整除的数，计算剩余数的平方之积。例如下面的输入样例中，首先去除3，剩余1,2,4，计算平方数得到1,4,16，计算它们的积得到64。要求使用map、filter、reduce函数实现上述功能
#! reduce的返回值是一个数
print(reduce(lambda a,b: a*b,list(map(lambda x: x*x,list(filter(lambda s: s%3!=0,list(map(int,input().split()))))))))