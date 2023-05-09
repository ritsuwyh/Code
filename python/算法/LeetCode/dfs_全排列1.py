

#from itertools import combinations
#复习combinations 需要使用list才能迫使其完成计算

ans_lst=[]
temp=[]
#todo 给当一个不含重复数字的数组nums 返回其可能的全排列
def dfs(step):
    if step==len(nums):
        ans_lst.append(temp.copy())
        
        return 
    for i in range(len(nums)):
        if vis[i]:
            continue
        vis[i]=True
        temp.append(nums[i])
        dfs(step+1)
        temp.pop()
        vis[i]=False

nums=list(eval(input()))
vis=[False for i in range(len(nums))]
dfs(0)
print(ans_lst)
#! leetcode 答题模板
# class Solution:
#     def permute(self, nums):
#         ans_lst=[]
#         temp=[]
#         vis=[False for i in range(len(nums))]
#         def dfs(step):
#             if step==len(nums):
#                 ans_lst.append(temp.copy())
        
#                 return 
#             for i in range(len(nums)):
#                 if vis[i]:
#                     continue
#                 vis[i]=True
#                 temp.append(nums[i])
#                 dfs(step+1)
#                 temp.pop()
#                 vis[i]=False
#         dfs(0)
#         return ans_lst