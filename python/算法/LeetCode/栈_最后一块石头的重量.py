
lst=list(map(int,input().split()))
while len(lst)>=2:
    lst.sort()
    temp=lst[-1]-lst[-2]
    lst=lst[:len(lst)-2]
    if temp==0:
        continue
    else:
        lst.append(temp)

if len(lst)==0:
    print(0)
else:
    print(lst[-1])

    