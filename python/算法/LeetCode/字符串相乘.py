from functools import reduce

dic = dict(zip('0123456789', range(10)))
# print(dic) #!不让用字符串转数字 那就用dic打一个数字对照表

num1, num2 = input().split()
num1_lst = list(num1)
num2_lst = list(num2)

for i in range(len(num1_lst)):
    num1_lst[i] = dic[num1_lst[i]]
for i in range(len(num2_lst)):
    num2_lst[i] = dic[num2_lst[i]]
x1 = reduce(lambda x, y: 10*x+y, num1_lst)
x2 = reduce(lambda x, y: 10*x+y, num2_lst)
print(x1*x2)
