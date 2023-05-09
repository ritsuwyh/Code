import sympy

a,b,c,x=sympy.symbols('a,b,c,x')
expr=a*x**2+b*x+c

#1
values1={a:1,b:2,c:-3}
test1=expr.subs(values1)
print(test1)
ans1=sympy.solve(test1)#! 默认右侧为0
print(ans1)

print('-------------')

#2
values2={a:1,b:0,c:2}
test2=expr.subs(values2)
print(test2)
ans2=sympy.solve(test2)
print(ans2)

#! 程序会输出复数解

