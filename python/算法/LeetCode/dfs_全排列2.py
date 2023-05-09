
#! 第一种方法是先不管重复不重复 最后去一遍重 见dfs_字符串全排列

#! 第二种思路就是在dfs递归终点进行筛选 见dfs_回溯搜索_组合求和 类似于字母异位词的思想--排序之后看是否相等
class Solution:
    def permuteUnique(self, nums: list[int]) -> list[list[int]]:
        #! 先排序 使相同的数字相邻
        nums.sort()
        res=[]
        ans=[]
        n=len(nums)
        visited=[0]*n
        def dfs():
            if len(ans)==n:
                res.append(ans[::])
            for i in range(n):
                #! 下面这句话是关键
#!加上 !vis[i - 1]来去重主要是通过限制一下两个相邻的重复数字的访问顺序

#!举个栗子，对于两个相同的数11，我们将其命名为1a1b, 1a表示第一个1，1b表示第二个1； 
#! 那么，不做去重的话，会有两种重复排列 1a1b, 1b1a， 我们只需要取其中任意一种排列； 
# !为了达到这个目的，限制一下1a, 1b访问顺序即可。 比如我们只取1a1b那个排列的话，只有当visit nums[i-1]之后我们才去visit nums[i]， 
# !也就是如果!visited[i-1]的话则continue
                if visited[i] or i>0 and nums[i]==nums[i-1] and not visited[i-1]:
                    continue
                ans.append(nums[i])
                visited[i]=1
                dfs()
                ans.pop()
                visited[i]=0
        dfs()
        return res