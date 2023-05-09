
#! 超时
class Solution:
    def combinationSum2(self, candidates: list[int], target: int) -> list[list[int]]:
        vis=[False for _ in range(len(candidates))]
        ans=[]
        # ans=set([])
        dic={}

        if sum(candidates)<target:
            return []
        
        def dfs(candidates,target,vis,lst:list,sumx):
            if sumx==target:
                lstx=sorted(lst)#! 注意这里不能用list.sort 这样会改变原list的顺序 从而使回溯出现问题
                # ans.add(lst.copy())
                if lstx not in ans:
                    
                    ans.append(lstx.copy())
                return
            if sumx>target:
                return 
            
            for i in range(len(candidates)):
                if vis[i]:
                    continue
                else:
                    vis[i]=True
                    sumx+=candidates[i]
                    lst.append(candidates[i])
                    dfs(candidates,target,vis,lst,sumx)
                    sumx-=candidates[i]
                    lst.pop()
                    vis[i]=False
                    
            return
        
        dfs(candidates,target,vis,[],0)
        return ans
    
solution=Solution()
print(solution.combinationSum2([10,1,2,7,6,1,5],8))
print(solution.combinationSum2([1,1,1,1,1],6))#! 只要处理过数字1 那么之后如果再次遇到就不用处理了



from typing import List

#! 排序剪枝版本
class Solution:

    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        def dfs(begin, path, residue):
            if residue == 0:
                res.append(path[:])#! 必须用copy或者[:]
                return

            for index in range(begin, size):
                if candidates[index] > residue:
                    break

                if index > begin and candidates[index - 1] == candidates[index]:#! 关键
                    #! 有点像三数之和 上面第一个判断条件属于是index-1存不存在 合法性判断在前!
                    continue

                path.append(candidates[index])
                dfs(index + 1, path, residue - candidates[index])#! 与组合总和1区分 这里是index+1
                path.pop()

        size = len(candidates)
        if size == 0:
            return []

        candidates.sort()
        res = []
        dfs(0, [], target)
        return res