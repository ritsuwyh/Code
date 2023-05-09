
#todo 二维lst降维
lst=list(eval(input()))
nx=len(lst)
ny=len(lst[0])
temp=[]
for i in lst:
    for j in i:
        temp.append(j)

n,m=eval(input())
if n*m!=nx*ny:
    print('illgal')
    exit()
#todo 填充
new_lst=[[] for i in range(n)]
cnt=0
for i in range(n):
    for j in range(m):
        new_lst[i].append(temp[cnt])
        cnt+=1

print(new_lst)