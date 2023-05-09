
import numpy as np

a = np.random.randint(-100, 101, (3,4))
#step1
print(a)
print(a[0])

#step2
#! 第二列我理解为索引为2
#! 以列形式输出
# print(a[:,2:3])#print(a[:,2]) #!以行形式输出

#step3
print(a[:,2:4])
#step4
print(a[1:3,2:4])

