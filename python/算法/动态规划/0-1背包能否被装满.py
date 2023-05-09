

#! dp动态规划 '能不能' '0-1背包'
# item_lst=[0]+list(map(int,input().split()))
# target=eval(input())

# dp=[False for _ in range(target+1)]
# dp[0]=True#! dp边界
# for i in range(1,len(item_lst)):#! 这里不用再加1了
#     for j in range(target,0,-1):
#         if j<item_lst[i]:
#             break
#         dp[j]=dp[j] or dp[j-item_lst[i]]
        
# print(dp[target])  

#! 求子集 找子集中有没有和为target的 这样可以输出所有的可能方案

item_lst=list(map(int,input().split()))
target=eval(input())
lst=[[]]
for x in item_lst:
    lst+=[temp+[x] for temp in lst]#! 这里最好写成temp+[x] 而不是写成[x]+temp
#*print(lst)
flag=False
for xx in lst:
    if sum(xx)==target:
        flag=True
        break
if flag:
    print(True)
else:
    print(False)