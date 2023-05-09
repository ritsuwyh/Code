
class Solution:
    def combinationSum3(self, k: int, n: int) -> list[list[int]]:
        #! 我们注意到 需要设置一个起点 如果数字1已经被使用过了 那么之后的组合不能再出现数字1
        
        ans=[]
        def dfs(start,temp:list,n,k):
            

            
            if sum(temp)==n and len(temp)==k:
                ans.append(temp.copy())
                return
            if len(temp)>=k:
                return 
                        
            for i in range(start,10):
                temp.append(i)
                dfs(i+1,temp,n,k)
                temp.pop()#! 别忘了回溯
        dfs(1,[],n,k)     
        return ans