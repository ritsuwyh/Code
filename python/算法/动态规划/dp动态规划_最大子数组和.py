
#! 动态规划 选择子问题(状态) 把子问题定义的越清楚越好(加上一些条件限制 比如这道题 以nums[i]结尾的连续子数组最大和)
#!1. 定义状态 dp[i]：表示以 nums[i] 结尾 的 连续 子数组的最大和。
#!说明：「结尾」和「连续」是关键字。
#!2. 状态转移方程(描述子问题之间的联系) (思考dp[i]和dp[i-1]之间的联系?)  dp[i]=max{nums[i],dp[i−1]+nums[i]}
#! 友情提示：求解动态规划的问题经常要分类讨论，这是因为动态规划的问题本来就有「最优子结构」的特点，
#!即大问题的最优解通常由小问题的最优解得到。因此我们在设计子问题的时候，就需要把求解出所有子问题的结果，进而选出原问题的最优解。
#!3.思考初始值 dp[0] 就是 nums[0]
#!4.思考子问题怎么到所求问题 max(dp[i])即为所求
class Solution:
    def maxSubArray(self, nums):
        size = len(nums)
        if size == 0:
            return 0
        dp = [0 for _ in range(size)]

        dp[0] = nums[0]
        for i in range(1, size):
            if dp[i - 1] >= 0:
                dp[i] = dp[i - 1] + nums[i]
            else:
                dp[i] = nums[i]
        return max(dp)
