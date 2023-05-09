lst=list(eval(input()))
if len(lst)==0:
    print('None')
elif len(lst)==1:
    print(lst)
    exit()#! 特判之后要记得退出程序 ！！！！ 防止重复输出
else:
    for i in range(len(lst)-1,-1,-1):
        if i==0:
            if lst==sorted(lst,reverse=True):
                lst.sort()
                break
            else:
                lst[i+1:]=sorted(lst[i+1:])
                for j in range(i+1,len(lst)):
                    if lst[j]>lst[i]:
                        lst[i],lst[j]=lst[j],lst[i]
                        break
                lst[i+1:]=sorted(lst[i+1:])
                break
        else:
            if lst[i:]==sorted(lst[i:],reverse=True):
                continue
            else:
                lst[i+1:]=sorted(lst[i+1:])
                for j in range(i+1,len(lst)):
                    if lst[j]>lst[i]:
                        lst[i],lst[j]=lst[j],lst[i]
                        break
                lst[i+1:]=sorted(lst[i+1:])
                break

if lst[0]==0:
    lst[0],lst[1]=lst[1],lst[0]
print(lst)