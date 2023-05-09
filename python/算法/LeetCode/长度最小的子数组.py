
# class Solution:
#     #! 求连续区间的和 想到用前缀和的思想
#     #! 遍历的时候使用了滚动区间的思想
    
#     def minSubArrayLen(self, target: int, nums: list[int]) -> int:
#         prefix_sum=[0 for _ in range(len(nums)+1)]#! 多设置一个
#         #! 计算前缀和
#         for i in range(1,len(nums)+1):
#             prefix_sum[i]=prefix_sum[i-1]+nums[i-1]
        
#         #*prefix_sum[k]就是前k个数的和
#         for arraylen in range(1,len(nums)+1):
#             for i in range(len(nums)-arraylen+1):#! 注意范围
#                 if prefix_sum[i+arraylen]-prefix_sum[i]>=target:
#                     return arraylen
    
#         return 0
    
    
# #todo 解法二双指针  滑动窗口 暴力思路是 以第i个数为起点 然后往后求和直到大于等于target 然后以第i+1个数为起点...
# #! 但是这样会重复计算 比如说第1 2 3 个数的和小于target 而第1 2 3 4个数的和大于target 
# #! 那么第2 3个数的和一定小于target 只需要从 第2 3 4 个数的和开始往后即可
#* 双指针滑动窗口
# 滑动窗口的力所不及
# 在套模板的同时，大家是否考虑过，假设题目同样是求连续的子数组，但是在数组中出现了负数，那这种情况下还可以使用滑动窗口么？

# 答案是不行的，为什么？

# 我们窗口滑动的条件是什么，while窗口内元素超过或者不满足条件时移动，但如果数组存在负数，遇到不满足题意的时候，我们应该移动窗口左边界，还是扩大窗口右边界从而寻找到符合条件的情况呢？

# 当一种场景存在多种可能时，显然就是当前的算法不适配解.只能用前缀和。



class Solution:
    def minSubArrayLen(self, target: int, nums: list[int]) -> int:
        start=end=0
        sumx=nums[start]
        min_lenx=len(nums)+1#! 初始值用于更新
        
        #! 不存在的情况我们可以特判
        if sum(nums)<target:
            return 0 
        #! 能够走下去说明必然有解
        while start<=end<=len(nums)-1:#! 想清楚条件
            
            while sumx<target:
                
                #! 判断end是否越界
                if end>=len(nums)-1:#! 如果这里都达不到target 那么以后必然也达不到
                    return min_lenx
                end+=1
                sumx+=nums[end]
                
            if end-start+1<min_lenx:
                min_lenx=end-start+1
            #! 关键   画个图就明白了
            sumx-=nums[start]
            start+=1
        return min_lenx





