#! 无向图邻接表的输入 求最小的dfs序
def dfs(u,G):
    for i in G[u]:
        if not vis[i]:
            vis[i]=True
            print(i,end=" ")
            dfs(i,G)

def main():
    n,m=eval(input())#! n个点 m条边
    G=[[]for _ in range(n+1)] #!这是一个动态二维数组
    #! 注意这里为了统一脚标和第几个 G[0]不用 用n+1
    for i in range(m):
        u,v=eval(input())
        G[u].append(v)
        G[v].append(u)
    
    global vis#! 别忘了声明全局变量    
    vis=[False for i in range(n+1)]#! 这里也要是n+1
    
    for i in range(1,n+1):
        G[i]=sorted(G[i])
    
    for i in range(1,n+1):#! 注意这里不要遍历0
        if not vis[i]:
         #!   ! 是 python中的 not
            print(i,end=" ")
            vis[i]=True
            dfs(i,G)    
    #?   如果已知连通就不用循环了 直接
    #? dfs(1)
    #? 把dfs改为下面的
    #? def dfs(i,G):
    #?     vis[i]=True
    #?     for x in range(G[i]):
    #?         if not vis[x]:
    #?             dfs(x,G)
                
main()
#!  依据字典序人为规定方向
# 回顾之前学习的迷宫问题，如果约定往上走一步是'U'，
# 往下走一步是'D'，往左走一步是'L'，往右走一步是'R'，
# 一个从起点走到终点的方案就可以写成一个字符串，
# 现在希望求解字典序最小的方案，如何去做？ 
# 其实对于当前所在的点，下一步就按照
# 下（'D'），左（'L'），右（'R'），上（'U'）的顺序依次来尝试就可以了，
# 相当于每一步也是选了字典序尽可能小的方案。