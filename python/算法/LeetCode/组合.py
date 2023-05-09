
# class Solution:
#     def combine(self, n: int, k: int) -> list[list[int]]:
#         from itertools import combinations
#         lst=list(range(1,n+1))
#         x=list(map(list,list(combinations(lst,k))))
#         return x
    
# solution=Solution()
# print(solution.combine(4,2))

class Solution:
    def combine(self, n: int, k: int) -> list[list[int]]:
        ans=[]
        def func(start,temp_lst):
            if len(temp_lst)==k:
                ans.append(temp_lst.copy())
                return #! 别忘了写return
            
            for i in range(start,n+1):
                temp_lst.append(i)
                
                func(i+1,temp_lst)
                temp_lst.pop()
                
                
        func(1,[])
        return ans
