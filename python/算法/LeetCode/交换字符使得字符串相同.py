
#! 最优化问题使用贪心算法和动态规划
class Solution:
    def minimumSwap(self, s1: str, s2: str) -> int:
        #! 注意已经配对的位置就不用动了
        #! 经过筛选之后 两个字符串完全相反
        #! 那么问题实际上转化为了 如何使 xx与yy经过最少的次数 xy与yx经过最少的次数
        #! xx与yy 1次 xy与yx 2次  贪心 我们让字符串中x与x配对 y与y配对 剩下的x与y配对 如果剩下的x与y的个数不一样那么-1
        from collections import Counter
        s=[]
        for i in range(len(s1)):
            if s1[i]!=s2[i]:
                s.append(s1[i])
        cnt=dict(Counter(s))
        print(cnt)
        if cnt.get('x',0)%2!=cnt.get('y',0)%2:
            return -1
        else:
            return cnt.get('x',0)//2+cnt.get('y',0)//2+2*(cnt.get('x',0)%2)
        
solution=Solution()
print(solution.minimumSwap('xx','yy'))
        
            
        