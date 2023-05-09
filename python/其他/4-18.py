#约瑟夫问题
#要灵活运用插件的性能 查看插件的提示
n,t=eval(input())
lst=[x for x in range(1,n+1)]
while len(lst)>1:
    for i in range(t-1):
        temp=lst.pop(0)
        lst.append(temp)
    lst.remove(lst[0])#删掉第一个元素
    #lst.pop(0)也可以
print(lst[0])
        
