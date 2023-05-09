
import sympy


#! 以后用的时候用 as sp
x=10
print(sympy.exp(x)/(1+sympy.exp(x*2)))

#! 括号里面的是变量的名称
x=sympy.Symbol('x')

a,b,c=sympy.symbols('a,b,c')

#! 常量

i=sympy.Integer(26)

f=sympy.Float(3.8)
#分数
r=sympy.Rational(11,13)

#!内建数值
print(sympy.pi,sympy.E,sympy.oo)

print(i**50)#! 可以表示超过inf 或者 sup 的数

print(sympy.Float(0.3,25))#! 0.3无法精确表示 25是有效位数
#0.2999999999999999888977698
print(sympy.Float('0.3',25))#! 可以用字符串
#0.3000000000000000000000000

#! 函数 
#自定义函数
f=sympy.Function('f')
print(type(f))

#内建函数
g=sympy.sin
print(type(g))

#! 表达式
print(sympy.sympify('2*x**2+3*x**3+1'))#! 高次幂到低次
print(sympy.sin(1))
print(sympy.sin(sympy.pi))


#todo 常用操作
expr = 3 * (x ** 2 - x) - x * (x + 1)
print(expr)
#化简
print(sympy.simplify(expr))


expr1 = 1 + 2 * x**2 + 3 * x**3
#展开
print(sympy.expand((x + 1) * (x + 2)))

#因式分解
print(sympy.factor(expr1))

x=sympy.Symbol('x')#! 在使用的时候应该后面的名称和前面的名称保持一致
y=sympy.Symbol('y')
z=sympy.Symbol('z')
print(sympy.sin(x + y).expand(trig=True))


#分式分解
sympy.apart( 1/ (x**2 + 5*x + 6) )
#通分
sympy.together(1/(y*x + x) + 1/(1 + x))
#消除公因子
sympy.cancel(x/ (x + x**2))

#求值
sympy.N(1 + sympy.pi)
sympy.N(sympy.pi, 50)
print((x + 1/sympy.pi).evalf())



# 用subs带入变量值(多个值可以使用字典)
#其实也可以带入函数
(x + 1/sympy.pi).subs(x, 3).evalf() #! 变量名:值
#3.31830988618379
expr = x * y + z**2 *x
values = {x: 1.25, y: 0.4, z: 3.2} 
expr.subs(values)#! 这个操作不会对expr改变 而是返回一个新的表达式
#13.3000000000000


#方程求解
sympy.solve(x**2 + 2*x - 3)
 #[-3, 1]
#通过第二个参数指定需求解的变量
sympy.solve(sympy.sin(x) - sympy.cos(x), x)

#如果方程是符号化的那么解也是符号化的
print(sympy.solve(a*x**2+b*x+c,x))


#方程组求解
#方程、变元都以列表形式提供
eq1 = x + 2 * y - 1
eq2 = x - y + 1
sympy.solve([eq1, eq2], [x, y], dict=True) 
# Out[108]: [{x: -1/3, y: 2/3}]

#sympy 和 矩阵 略

#!https://blog.csdn.net/weixin_28968285/article/details/113966634
#! 求解线性方程组 非线性方程组 微分方程
#数学分析

#计算给定表达式在某个给定点的极限
sympy.limit(sympy.sin(x) / x, x, 0)
#sympy.limit(expr/x, x, sympy.oo)

#级数
n=sympy.symbols('n',integer=True)
sumlist=sympy.Sum(1/(n**2),(n,1,sympy.oo))#!.Sum 是求和符号 第一个参数是求和表达式 右面的元组是指n 从 1 到 无穷
sumlist.doit()#求值

#泰勒展开
print(sympy.cos(x).series(n=10))
sympy.series(1/(1-x))
sympy.series(sympy.ln(1+x))

#导数和微分

f=sympy.Function('f')(x)# 声明一个以x为自变量的函数f

sympy.diff(f,x) #把函数f对x求导数

sympy.diff(f,x,3)# 求三阶导

g=sympy.Function('g')(x,y)#声明一个二元函数
sympy.diff(g,x,y)#g.diff(x,y) #! 先对x求偏导 再对y求偏导
g.diff(x,3,y,2)#对x求三阶偏导 再对y求二阶偏导

expr=x**4+x**3+x**2+1
expr.diff(x)#!对具体表达式求导
expr.diff(x,2)
expr=(x+1)**3*y**2*(z-1)
expr.diff(x,y,z)

#微分
expr=sympy.exp(sympy.cos(x))
d=sympy.Derivative(expr)#对表达式求微分

print(d.doit())# 求出具体值

#积分
sympy.integrate(f)#不定积分

sympy.integrate(f,(x,a,b))# a到b积分

expr=(x+y)**2
sympy.integrate(expr,x)# 对x不定积分
sympy.integrate(expr,(x,0,1),(y,0,1))


#!scipy 求解线性方程组
# #ri为四支股票的收益率矩阵，索引为交易日期，列为股票；
# #rp为四支股票每天的组合收益率，求每支股票的权重。
# ri=np.array([[ 0.003731,  0.021066, -0.004854,  0.006098],
#        [-0.001838,  0.001842, -0.016544, -0.003738],
#        [-0.003087, -0.000344, -0.033391,  0.007123],
#        [-0.024112,  0.011704, -0.029563, -0.01457]])
# rp=[0.00606,-0.003752,-0.004597,-0.016129]
# from scipy import linalg
# weight=linalg.solve(ri,rp)#求出来的是一个array
# stock=(['a','b','c','d'])
# for i in range(4):
#     print(stock[i],round(weight[i],2))

# a 0.44
# b 0.18
# c 0.15
# d 0.23
#!scipy 求极值

#!https://www.jb51.net/article/180064.htm

#!https://last2win.com/2020/04/11/scpiy-function-minimize/