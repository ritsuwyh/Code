
import sympy as sp
import scipy as cp
import numpy as np
x, y, z = sp.symbols("x y z")

# 默认等式为0的形式

eq = [x+3*y+z-10,2*x+y+3*z-13,2*x+2*y+z-9]#!"======默认等式为0的形式 ======="

result = sp.linsolve(eq, [x, y, z])

print(result)


x=np.array([[1,3,1],[2,1,3],[2,2,1]])
y=np.array([10,13,9])
ans=np.linalg.solve(x,y)
print(ans)