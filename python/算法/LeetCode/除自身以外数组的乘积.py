# 给你一个整数数组 nums，返回 数组 answer ，其中 answer[i] 等于 nums 中除 nums[i] 之外其余各元素的乘积 。

# 题目数据 保证 数组 nums之中任意元素的全部前缀元素和后缀的乘积都在  32 位 整数范围内。

# 请不要使用除法，且在 O(n) 时间复杂度内完成此题。

#! 前缀乘积 后缀乘积的使用(迭代的思想)  一个双重循环变成3个单层循环
class Solution:
    def productExceptSelf(self, nums):
        length = len(nums)
        
        # L 和 R 分别表示左右两侧的乘积列表
        L, R, answer = [0]*length, [0]*length, [0]*length
        
        # L[i] 为索引 i 左侧所有元素的乘积
        # 对于索引为 '0' 的元素，因为左侧没有元素，所以 L[0] = 1
        L[0] = 1#! 累乘初始化为1 累加初始化为0
        
        for i in range(1, length):
            L[i] = nums[i - 1] * L[i - 1]
        
        
        # R[i] 为索引 i 右侧所有元素的乘积
        # 对于索引为 'length-1' 的元素，因为右侧没有元素，所以 R[length-1] = 1
        R[length - 1] = 1
        for i in reversed(range(length - 1)):
            R[i] = nums[i + 1] * R[i + 1]

        # 对于索引 i，除 nums[i] 之外其余各元素的乘积就是左侧所有元素的乘积乘以右侧所有元素的乘积
        for i in range(length):
            answer[i] = L[i] * R[i]
        
        return answer

