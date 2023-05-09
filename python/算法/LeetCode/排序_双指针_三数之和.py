

#!!!!! 注意 如果排序对题干不影响 那么遇事不决一定先排序 最基本的思想就是三重循环 怎么优化
#! 怎么防止重复遍历 可能排序之后想法会清晰一点?
#*https://leetcode-cn.com/problems/3sum/solution/san-shu-zhi-he-by-leetcode-solution/
class Solution:
    def threeSum(self, nums: list[int]) -> list[list[int]]:
        n = len(nums)
        nums.sort()
        ans = list()
        #! python内置 in 函数 就相当于一层for的时间复杂度了
        # 枚举 a
        for first in range(n):
            
            #! 如果第一个数都大于0 那么必不可能有解
            if nums[first]>0:
                break
            
            # 需要和上一次枚举的数不相同
            
            if first > 0 and nums[first] == nums[first - 1]:#!建议使用往前比较 而不是往后比较
                continue
            # c 对应的指针初始指向数组的最右端
            third = n - 1
            target = -nums[first]
            # 枚举 b
            for second in range(first + 1, n):
                # 需要和上一次枚举的数不相同
                if second > first + 1 and nums[second] == nums[second - 1]:
                    continue
                # 需要保证 b 的指针在 c 的指针的左侧
                while second < third and nums[second] + nums[third] > target:
                    third -= 1
                #! 当 前两个数字确定的时候 第三个数已经确定  由于我们已经排除了第一个和第二个数重复的情况 所以可以放心大胆地遍历第三个数
                #! 从while里面出来 要么是second==third 要么是 <=target
                # 如果指针重合，随着 b 后续的增加
                # 就不会有满足 a+b+c=0 并且 b<c 的 c 了，可以退出循环
                if second == third:
                    break
                if nums[second] + nums[third] == target:
                    ans.append([nums[first], nums[second], nums[third]])
        
        return ans
#!

#!当我们需要枚举数组中的两个元素时，如果我们发现随着第一个元素的递增，第二个元素是递减的，那么就可以使用双指针的方法， 需要在排好序的前提下

#todo 扩展 四数之和

class Solution:
    def fourSum(self, nums: list[int], target: int) -> list[list[int]]:
        quadruplets = list()
        if not nums or len(nums) < 4:
            return quadruplets
        
        nums.sort()
        length = len(nums)
        for i in range(length - 3):
            #! 不重复
            if i > 0 and nums[i] == nums[i - 1]:
                continue
            
            #todo 两个极端情况的特判 减少循环次数
            if nums[i] + nums[i + 1] + nums[i + 2] + nums[i + 3] > target:#! 当前最小的可能组合都比目标大 那么肯定凑不出来目标了
                break
            if nums[i] + nums[length - 3] + nums[length - 2] + nums[length - 1] < target:#! 当前最大的可能组合都比目标小 那么肯定凑不出来目标了
                continue
            
            
            for j in range(i + 1, length - 2):
                #! 不重复
                if j > i + 1 and nums[j] == nums[j - 1]:
                    continue
                
                #todo 两个极端情况的特判 减少循环次数
                if nums[i] + nums[j] + nums[j + 1] + nums[j + 2] > target:
                    break
                if nums[i] + nums[j] + nums[length - 2] + nums[length - 1] < target:
                    continue
                #! 类似于三数之和 三数的时候把第一个确定下来 剩下两个用双指针 这道题 确定前两个 后两个数用双指针
                
                left, right = j + 1, length - 1
                while left < right:
                    total = nums[i] + nums[j] + nums[left] + nums[right]
                    if total == target:
                        quadruplets.append([nums[i], nums[j], nums[left], nums[right]])
                        while left < right and nums[left] == nums[left + 1]:
                            left += 1
                        left += 1
                        while left < right and nums[right] == nums[right - 1]:
                            right -= 1
                        right -= 1
                    elif total < target:
                        left += 1
                    else:
                        right -= 1
        
        return quadruplets
    
        