# 这题如果没有留意到限制条件"所有花园 最多 有 3 条路径可以进入或离开", "四种花", 很容易想复杂了.
# 比如使用回溯法, 找到一个可行解.
# 最多三个邻近点, 但是有四种花可以选择, 那么, 对于当前需要考虑的花园来说, #!任意选择一种与相邻花园不同的花, 即可, 不可能在后面会出现矛盾v 因此, 不需要使用回溯法, 简单根据花园编号进行循环即可, 时间复杂度为O(n).
# 我甚至不知道这归类为什么算法, 勉强算是贪心法(说是勉强的原因: 贪心法往往每个决策阶段只有一种决策, 但是这个是每个决策阶段可能有多种决策, 任选其中一个即可)吧.
#! 利用集合进行操作 

class Solution:
    def gardenNoAdj(self, n: int, paths: list[list[int]]) -> list[int]:
        G = [[]for _ in range(n+1)]#! 为了编号和索引对应
        for u, v in paths:
            G[u].append(v)
            G[v].append(u)
            
        ans = [0] * (n+1) #!我们需要一个数组对应顶点来记录相应的颜色
        for u in range(1, n + 1):
            #! 秒啊 涂色问题用集合的操作 背下来
            colors = set(range(1, 5)) - set(ans[v] for v in G[u])#! 所有颜色(1,2,3,4)里面排除掉与其相邻的颜色!!!!
            
            ans[u] = colors.pop()
            
        return ans
# colors.pop()表示随机弹出一个可行的花种, 平时很少用到这个method, 但是非常适合这道题.


# #todo 集合的操作   https://www.cnblogs.com/lei0213/p/5748756.html
# 1. 交集 &
# 2. 并集 |
# 3. 差集 -
# 4. 判断x是否是y的子集 x.issubset(y) 
