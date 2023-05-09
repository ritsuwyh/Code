import os
#不用创建 水果：单价对照表 因为根本用不到水果 
#创建一个字典 编号:单价
dic={}#懒得打了 
lst=input().split()
cnt=0
for i in lst:
    if cnt>5 or i=='0':
        exit(0) #os.exit()
    elif i not in dic.keys():
        print("0.00")
    else:
        print(dic[i])
        