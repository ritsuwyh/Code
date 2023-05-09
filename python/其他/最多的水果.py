
n=eval(input())
fruit_lst=[]
while n!=0:
    for i in range(n):
        x=input()
        fruit_lst.append(x)
    n=eval(input())
dic={}
for i in fruit_lst:
    dic[i]=fruit_lst.count(i)
lst=list(dic.items())
lst.sort(key=lambda x:(-x[1],fruit_lst.index(x[0])))
#! 不必用class 用index来记录谁先出线
#! 这里的排序技巧跟之前得类似 取决于两个条件 一个降序一个升序 "-"的使用
maxx=lst[0][1]
for i in lst:
    if i[1]==maxx:
        print(i[0]) 
