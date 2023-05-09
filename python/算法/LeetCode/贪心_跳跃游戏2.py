
#! 典型的贪心 https://leetcode-cn.com/problems/jump-game-ii/solution/45-by-ikaruga/

#!贪心算法 寻找每一步能跳到的最远的距离 注意我们这里每一次的起跳点是上一步跳到的最近距离到上一步跳到的最远距离
class Solution:
    def jump(self, nums: list[int]) -> int:
        
        
        target=len(nums)-1#索引
        if target==0:
            return 0
        r=0
        step=0
        l_range=range(step,r+1)

        while r<target:
            step+=1
            for i in l_range:
                r=max(r,i+nums[i])
                if r>=target:
                    return step
            
            l_range=range(step,r+1)
            
            
        return step