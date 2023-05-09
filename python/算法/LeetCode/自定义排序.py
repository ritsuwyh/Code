class Solution:
    def frequencySort(self, nums: list[int]) -> list[int]:
        from collections import Counter
        cnt=dict(Counter(nums))
        nums.sort(key=lambda x:(cnt[x],-x))#! 双关键字排序 为什么是-x? 因为要当频率相同的时候按数值降序排列
        return nums
        

solution=Solution()
print(solution.frequencySort([1,1,1,1,12,2,2,4]))