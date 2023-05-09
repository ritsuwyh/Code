import sympy

x = sympy.Symbol('x')
expr = sympy.exp(x) * sympy.sin(x)
ans1 = sympy.integrate(expr, x)  # 对x不定积分
print(ans1)
ans2 = sympy.Derivative(expr)  # 对表达式求微分
print(ans2.doit())
