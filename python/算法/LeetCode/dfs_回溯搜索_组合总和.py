
# #!区分排列和组合问题 见题解里面的树状图

# #!https://leetcode-cn.com/problems/combination-sum/solution/hui-su-suan-fa-jian-zhi-python-dai-ma-java-dai-m-2/
# #!https://leetcode-cn.com/problems/combination-sum/ 相似题目
# temp=[]
# ans_lst=[]
#! 超时
# def dfs(lst,target,sumx):
    
#     if sumx==target:#! 在递归终点对其进行排序 判断排序后的是否在ans_lst中
#         sorted_temp=sorted(temp)
#         if sorted_temp not in ans_lst:
#             ans_lst.append(sorted_temp)
#         return 
#     if sumx>target:
#         return 
    
    

#     for i in lst:
#         sumx+=i
#         temp.append(i)
    
#         dfs(lst,target,sumx)
        
#         temp.pop()
#         sumx-=i#! 回溯搜索

# def main():
#     lst=list(map(int,input().split()))
#     target=eval(input())
#     lst.sort()
#     dfs(lst,target,0)
#     print(ans_lst)
# main()

from typing import List


class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:

        def dfs(candidates, begin, size, path, res, target):
            if target < 0:
                return
            if target == 0:
                res.append(path)
                return

            for index in range(begin, size):#! 他比我多设置了一个起点！！！！！！！
                dfs(candidates, index, size, path + [candidates[index]], res, target - candidates[index])

        size = len(candidates)
        if size == 0:
            return []
        path = []
        res = []#! 存储结果 注意如果传入函数里面的参数是list 那么在函数中进行的操作会对list进行修改
        dfs(candidates, 0, size, path, res, target)
        return res
    
    

#! 进一步优化 排序剪枝
from typing import List


class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:

        def dfs(candidates, begin, size, path, res, target):
            if target == 0:
                res.append(path)
                return

            for index in range(begin, size):
                residue = target - candidates[index]
                if residue < 0:#! 妙
                    break

                dfs(candidates, index, size, path + [candidates[index]], res, residue)

        size = len(candidates)
        if size == 0:
            return []
        candidates.sort()
        path = []
        res = []
        dfs(candidates, 0, size, path, res, target)
        return res
