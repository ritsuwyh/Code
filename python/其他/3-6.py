n=int(input())
l=[]
for i in range(n):
    x=int(input())
    l.append(x)
num=l[0]
times=l.count(l[0])
for j in l:
    if l.count(j)>times:
        times=l.count(j)
        num=j# 遍历中的同步更新 
print(num,times)