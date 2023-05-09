
    #*这样不会报错
    #     for i in range(2,1):
    # print(i)
# 这道题主要用到思路是：滑动窗口        #!滑动窗口 双指针

# 什么是滑动窗口？

# 其实就是一个#!队列
# 比如例题中的 abcabcbb，进入这个队列（窗口）为 abc 满足题目要求，当再进入 a，队列变成了 abca，这时候不满足要求。所以，我们要移动这个队列！

# 如何移动？

# 我们只要把第一个重复字母及之前全删了

# 一直维持这样的队列，找出队列出现最长的长度时候，求出解！

# 时间复杂度：O(n)


class Solution:
    def lengthOfLongestSubstring(self,s):
        ans=0
        lst=[]
        for x in s:
            if x not in lst:
                lst.append(x)
            else:
                
                ans=max(len(lst),ans)
                
                lst=lst[lst.index(x)+1:]#! 利用切片操作 把第一个重复字母及之前全删了
                lst.append(x)#!注意写的顺序
        #! 别忘了最后还要更新一下 因为上面的逻辑是只有遇到重复的才会更新
        ans=max(len(lst),ans)
        return ans

        
        
        
        

