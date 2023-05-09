
class Solution:
    #顺序不同的序列被视作不同的组合。
    #! 那就相当于排列问题了 不是组合问题 而且本题每个数字的使用次数不限 所以不需要vis数组
    #! 实际上就是组合总和1 超时的方法的不去重版本
    def combinationSum4(self, nums: list[int], target: int) -> int:
        cnt=0
        #! 其实我们只需要求cnt 不需要求具体结果是多少 如果想求 可以传入参数temp记录结果
        def dfs(nums,target,sumx):
            #if sum(temp)==target:#! 为了防止重复调用sum
            if sumx==target:
                nonlocal cnt#! 别忘了写nonlocal
                cnt+=1
                return
            
            if sumx>target:
                return 
            for i in nums:
                temp=sumx+i
                dfs(nums,target,temp)
                temp-=i
                
            
        
        dfs(nums,target,0)
        return cnt
    
solution=Solution()
print(solution.combinationSum4([1,2,3],4))


#! 尝试使用 组合背包(不是完全背包因为他有序 外层循环dp) 组合问题
class Solution:

    def combinationSum4(self, nums: list[int], target: int) -> int:
        dp=[0 for _ in range(target+1)]
        dp[0]=1
        nums=[0]+nums
        for i in range(1,len(dp)):
            for j in range(1,len(nums)):
                if i<nums[j]:
                    continue
                
                dp[i]+=dp[i-nums[j]]
                
        return dp[target]