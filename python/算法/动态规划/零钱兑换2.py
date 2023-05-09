
# #! 模型 必须装满 统计方案数 完全背包
# amount=eval(input())
# coins=list(map(int,input().split()))

# dp=[0 for _ in range(amount+1)]
# dp[0]=1
# for i in range(len(coins)):
#     for j in range(1,amount+1):
#         if j<coins[i]:
#             continue
#         dp[j]+=dp[j-coins[i]]

# print(dp[amount])

#! 完全背包 组合问题 (求方案数) 这种求方案数的问题和正常的最优化问题初始化不一样 求方案数除了dp边界其余应该初始化为0
class Solution:
    def change(self, amount: int, coins: list[int]) -> int:
        dp=[0 for _ in range(amount+1)]#! 其他元素初始化为0
        dp[0]=1#! 总金额为0 方案数只有一个那就是什么也不选
        coins=[0]+coins
        for i in range(1,len(coins)):
            for j in range(1,amount+1):
                if j<coins[i]:
                    continue
                dp[j]+=dp[j-coins[i]]
        return dp[amount]