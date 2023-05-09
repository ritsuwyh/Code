
n,m=eval(input())
lst_stu_height=list(map(int,input().split()))
lst_ball_height=list(map(int,input().split()))

temp=lst_stu_height.copy()
temp.sort()

dic_stu=dict.fromkeys(lst_stu_height,0)
dic_ball=dict.fromkeys(lst_ball_height,1)

for i in temp:
    for j in lst_ball_height:
        if i>=j and dic_ball[j]==1:
            dic_stu[i]+=1
            dic_ball[j]=-1
for i in lst_stu_height:
    print(dic_stu[i])
            
            