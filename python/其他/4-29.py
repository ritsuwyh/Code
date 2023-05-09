lst1=input().split()#这么写是为了符合输入规则
lst1.pop(0) #删去个数 因为无用
lst2=input().split()
lst2.pop(0)
ans_lst=[]
for i in lst1:
    if i not in lst2 and i not in ans_lst:
        ans_lst.append(i)
for j in lst2:
    if j not in lst1 and j not in ans_lst:
        ans_lst.append(j)
for k in ans_lst:
    print(k,end=" ")