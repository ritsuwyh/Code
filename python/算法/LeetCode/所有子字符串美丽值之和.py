
#!子串，计算机术语，串中任意个连续的字符组成的子序列称为该串的子串
#! 注意必须是连续的!
# class Solution:
#     def substr(self, s: str) -> int:
#         ans=[]
#         #! 问题1 求出所有子串
#         for i in range(len(s)):    
#             for j in range(i,len(s)):
#                 ans.append(s[i:j+1])
#         return ans
    
class Solution:
    def beautySum(self, s: str) -> int:
        from collections import Counter
        ans=0
        for i in range(len(s)):

            for j in range(i+2,len(s)):
                
                cnt=Counter(s[i:j+1])
                
                maxx=max(cnt.values())
                minn=min(cnt.values())
                ans+=maxx-minn
        return ans