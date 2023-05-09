
#todo  1.给你一个整数数组 nums 和一个整数 k ，请你统计并返回 该数组中和为 k 的子数组的个数

#! 可以不连续 我只能想到回溯dfs加去重(直接pass掉 时间复杂度太高)    转化为背包问题 ？多重背包?
#! 注意下面这个方法 [1,1,1] 只要取了两个1 就算是一种
class Solution:
    def subarraySum(self, nums, k):
#todo 利用字典生成式来统计list中每个数字出现的次数
# nums=[1,2,3,3,4,4,5,5,5]
# dic={num:nums.count(num) for num in nums}
# print(dic)
        dic={num:nums.count(num) for num in nums}
        w=[0]+list(dic.keys())
        s=[0]+list(dic.values())
        dp=[0 for _ in range(k+1)]
        dp[0]=1
        for i in range(1,len(w)):
            for j in range(k,-1,-1):
                if j<w[i]:
                    break
                for z in range(1,min(s[i],j//w[i])+1):
                    dp[j]=dp[j]+dp[j-z*w[i]]
                    
        return dp[k]

solution=Solution()
print(solution.subarraySum([1,2,3,1],6))    
               



#todo 剑指 Offer II 010. 和为 k 的子数组   2.给定一个整数数组和一个整数 k ，请找到该数组中和为 k 的连续子数组的个数 这道题目非常简洁，就是求数组中和为整数k的连续子数组个数。
#!如果这道题的取值没有负数，那就是标准的滑窗问题，但因为有了负数，滑窗思想不能用了。
#!因为连续 所以想 朴素前缀和 加变长度窗口

# 前缀和的结果我们该通过什么方式保存起来呢？

# 题目明确要求不允许使用额外空间的，直接原地修改数组
# 不限制空间复杂度时，最好额外开辟空间计算，避免数据污染
# 计算时如果每次只需要获取前一次的累计结果，可以通过数组的方式存储每次获取数组末尾元素的值
# 如果每次计算需要获取前几次或更多次的结果进行对比时，推荐哈希表的方式，这样可以压缩时间复杂度

#! 方法一 自己写的 超时
# class Solution:
#     def subarraySum(self, nums: list[int], k: int) -> int:
#         prefix_sum=[0 for _ in range(len(nums)+1)]
#         cnt=0
#         for i in range(1,len(nums)+1):
#             prefix_sum[i]=prefix_sum[i-1]+nums[i-1]
#         for lenx in range(1,len(nums)+1):
#             for start in range(len(nums)-lenx+1):
#                 if prefix_sum[start+lenx]-prefix_sum[start]==k:
#                     cnt+=1
                    
#         return cnt
# #! 方法2 标答 背下来
class Solution:
    def subarraySum(self, nums, k):
        ans = pre_sum = 0
        pre_dict = {0: 1}
#         但在这里要注意刚才说到的前缀和边界问题。
# 我们在计算这种场景时，需要考虑如果以数组nums[0]为开头的连续子数组就满足题意呢？
# 此时候我们的哈希表还是空的，没办法计算前缀和！所以遇到这类题目，都需要在哈希表中默认插入一个{0:1}的键值对，
# 用于解决从数组开头的连续子数组满足题意的特殊场景。

        for i in nums:
            #! 注意顺序 顺序不能写错
            pre_sum += i
            ans += pre_dict.get(pre_sum - k, 0)
            #!将当前累加和减去整数K的结果，在哈希表中查找是否存在
            #!如果存在该key值，证明以数组某一点为起点到当前位置满足题意，ret加等于将该key值对应的value
            pre_dict[pre_sum] = pre_dict.get(pre_sum, 0) + 1#! 统计每个前缀和出现的次数
        return ans