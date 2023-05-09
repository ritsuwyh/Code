
# lst=list(map(int,input().split()))
# target=eval(input())
# #! 找准模型 背包恰好装满 最优化 把需要求最值的当做价值 此题为数量
# upbound=100000
# dp=[0]+[upbound for _ in range(target)]#! dp边界是0 因为0元不需要任何硬币就能凑出来
# #! 上面这个写成dp=[upbound for _ in range(target+1)] dp[0]=0 更好理解

# for i in range(len(lst)):#! 这里不用加1了 因为已经加了一个0元素
#     for j in range(1,target+1):
#         if j<lst[i]:
#             continue
        
#         #! 之前都是求最大值现在是求最小值
        
#         dp[j]=min(dp[j],dp[j-lst[i]]+1)
# if dp[target]>=upbound:
#     print(-1)
# else:
#     print(dp[target])
    
    
    

#! 在初始化的时候 物品list应该前面加上一个0元素 背包大小设为V+1 第一个元素是dp边界 遍历的时候从1开始遍历
#! 完全背包 恰好装满 最优化(最小)


class Solution:
    def coinChange(self, coins: list[int], amount: int) -> int:
        upbound=99999999
        dp=[upbound for _ in range(amount+1)]
        coins=[0]+coins
        dp[0]=0
        for i in range(1,len(coins)):
            for j in range(1,amount+1):
                if j<coins[i]:
                    continue
                dp[j]=min(dp[j],dp[j-coins[i]]+1)
        if dp[amount]==upbound:
            return -1
        else:
            return dp[amount]
