import numpy as np

# step1
a = np.random.randint(1, 6, (2, 3, 2))
print(a)
print()
b = np.random.randint(1, 6, (2, 3, 2))
print(b)
print()

# step2
# print(a+b)

c = np.zeros_like(a)
# print(c)
for i in range(2):
    for j in range(3):
        for k in range(2):
            c[i, j, k] = a[i, j, k] + b[i, j, k]
# print(c)

# step3
# ! 法1
# x=np.vstack((a,b))
# y=np.hstack((a,b))
# z=np.dstack((a,b))
# print(x)
# print('------------------------')
# print(y)
# print('------------------------')
# print(z)
# print('------------------------')

# ! 法2
print('************************')
xx = np.append(a, b, axis=0)
print(xx)
print('------------------------')
yy = np.append(a, b, axis=1)
print(yy)
print('------------------------')
zz = np.append(a, b, axis=2)
print(zz)

# ! 法3 zz=np.concatenate((a,b),axis=2)#! 不写的话默认axis=0 print(zz)#The axis along which the arrays will be joined. If
# axis is None, arrays are flattened before use. Default is 0.
