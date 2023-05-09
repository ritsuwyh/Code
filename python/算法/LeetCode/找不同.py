
#! 方法1计数
class Solution:
    def findTheDifference(self, s: str, t: str) -> str:
        dic1={x:s.count(x) for x in s}
        dic2={y:t.count(y) for y in t}
        #! 有两种情况 第一种情况是添加旧的元素 第二种添加新的
        for xx in t:
            if xx not in dic1.keys() or dic1[xx]!=dic2[xx]:#! 注意条件的顺序
                return xx
            
#!将所给的字符串转换为字符数组，求字符数组的int和，作差，再转回char，返回（3ms，击败100%）
#!使用ord chr 函数
#! 方法2 ascall码
class Solution:
    def findTheDifference(self, s: str, t: str) -> str:
        sum1=sum(list(map(ord,list(s))))
        sum2=sum(list(map(ord,list(t))))
        return chr(sum2-sum1)
    

#!方法三 妙用奇偶性
# 执行用时：16 ms, 在所有 Python 提交中击败了92.55%的用户

# class Solution(object):
#     def findTheDifference(self, s, t):
#         m=s+t
#         for i in m:
#             if m.count(i)%2==1:
#                 return i
# s和t拼接后遍历，统计其个数，若为奇数则输出