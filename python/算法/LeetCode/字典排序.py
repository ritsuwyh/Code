

#! 像这种指定输出格式的 我们最好先把原来的所有元素取出来!!!!!!!!
lst=list(map(int,input().split()))
#! 使用set去重
lstx=sorted(list(set(lst)),key=lambda x: lst.count(x))
#print(lstx)
s='{'
for i in lstx:
    #! 这里加空格纯属是为了符合题意
    
    s=s+str(i)+':'+' '+str(lst.count(i))+','+' '
    
s=s[:len(s)-2]+'}'
print(s)

