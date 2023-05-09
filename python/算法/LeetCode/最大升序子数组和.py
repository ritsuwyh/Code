

#! 模板背下来!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
class Solution:
    def maxAscendingSum(self, nums: list[int]) -> int:
        #! 注意 大小为1的子数组也视为升序子数组
        #! 能特判就先特判
        if len(nums)==1:
            return nums[0]
        
        x=1
        maxx=nums[0]
        temp=nums[0]
        #! x是一个指针
        while x<=len(nums)-1:#! 一定是往前 而不是往后 注意索引的问题
            if nums[x-1]<nums[x]:
                temp+=nums[x]
                #! 边界要特判!
            else:

                if temp>maxx:
                    maxx=temp
                temp=nums[x]#! 以这个数为起点
            x+=1
        
        #!别忘了最后还要更新一次
        maxx=max(temp,maxx)
        return maxx