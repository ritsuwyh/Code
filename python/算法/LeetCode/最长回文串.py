
#! 求最长回文串的长度
class Solution:
    def longestPalindrome(self, s: str) -> int:
        #! 使用dict存储每个字母出现的次数 看有多少个相同字母对 别忘了如果有单的最后要加1
        dic={}
        for i in s:
            dic[i]=dic.get(i,0)+1
        flag=False
        sumx=0
        for x in dic.values():
            if x%2==1:
                flag=True
            sumx+=x//2*2
        if flag:
            sumx+=1
        return sumx
    