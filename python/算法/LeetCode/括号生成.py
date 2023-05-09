

#! 体会使用全局变量 和 传入参数的区别
class Solution:
    def generateParenthesis(self, n: int) -> list[str]:# n是 n 对括号
        ans_lst=[]
        temp=[]
        def dfs(sum_l,sum_r):
            if sum_l==sum_r==n:#! 别忘了之前.copy 的教训
                s=''.join(temp)
                ans_lst.append(s)
            
            if sum_l>n or sum_r>n or sum_l<sum_r:
                return
            #! 其实跟我之前传统的写法相比就是把for循环展开了
            
            #todo 相当于第一次循环
            temp.append('(')
            dfs(sum_l+1,sum_r)
            temp.pop()
            
            #todo 相当于第二次循环
            temp.append(')')
            dfs(sum_l,sum_r+1)
            temp.pop()
            
        dfs(0,0)
        return ans_lst  

#! 思路1 暴力 求全排列 然后找出有效的
#! 思路2 dfs 不需要回溯(即使用vis数组) 每一步有两个决策


    


# class solution:
#     def generateParenthesis(self, n):
#         res = []

#         def dfs(s, left, right):#!这里的s跟我之前temp一样 可以当作参数传进来 也可以在全局变量写 左括号数 右括号数
#             #! dfs终点
#             if left == n == right:
#             # 终止条件是括号数都是n
#                 res.append(s)
#                 return
#             #! 由于之前的决策步有很多 所以使用for循环  但是这个题决策只有两个 就不用for了 直接写出来即可
#             #! 筛选条件也很简单 直接从正面写
#             if right <= left<= n:
#                 # 如果左边的括号数大于右边的括号数且小于n则可以继续递归
#                 # 只要满足上述条件就一定还有分支有解
#                 dfs(s + '(', left+1, right)
#                 dfs(s + ')', left, right + 1)
                
                
#         dfs('', 0, 0)
#         return res