
# 4. 求出函数 f(x,y,z) = x**2 + 3*x + 2*y**2 + 2*y + 3*z**2 - 4*z + 5 的极小值，并输出结果和取到最小值的x,y,z的值，手算结果验证输出的正确性。
# 目标：熟悉scipy的 求极值 操作。
#! 课件 只能一个变量
# from scipy import optimize as opt
# # def objective_function(x):
#     return 4 * x ** 4 - 3 * x + 1 
# res=opt.minimize_scalar(objective_function)
# print(res)


import scipy.optimize as opt
import numpy as np

fun = lambda x:  x[0]**2 + 3* x[0] +2* x[1]**2 + 2*x[1] + 3*x[2]**2 - 4*x[2]+5
bnds = ((0, 5), (0, 5),(0,5))  # 定义域
#           fun为函数名，x0为函数参数的起始点，bounds为每个变量的定义域范围
res = opt.minimize(fun=fun, x0=np.array([1,1,1]))
print(res.x)

