
# #! 无向图邻接表的输入 及求连通块的数量
# def dfs(u,G):
#     for i in G[u]:
#         if not vis[i]:
#             vis[i]=True
#             dfs(i,G)

# def main():
#     n,m=eval(input())#! n个点 m条边
#     G=[[]for _ in range(n+1)] #!这是一个动态二维数组
#     #! 注意这里为了统一脚标和第几个 G[0]不用 用n+1
#     for i in range(m):
#         u,v=eval(input())
#         G[u].append(v)
#         G[v].append(u)
    
#     global vis#! 别忘了声明全局变量    
#     vis=[False for i in range(n+1)]#! 这里也要是n+1
    
#     cnt=0
    
#     for i in range(1,n+1):#! 注意这里不要遍历0
#         if not vis[i]:
#          #!   !是 python中的 not
#             cnt+=1
#             vis[i]=True
#             dfs(i,G)    
           
#     print(cnt)
# main()

def dfs(u):
    for i in Gx[u]:
        if vis[i]:
            continue
        vis[i]=True
        dfs(i)



def main():
    n,m=eval(input())
    global Gx
    Gx=[[] for i in range(n)]
    for i in range(m):
        u,v=eval(input())
        Gx[u-1].append(v-1)
        Gx[v-1].append(u-1)
    global vis
    vis=[False for i in range(n)]
    cnt=0
    for i in range(n):
        for j in range(len(Gx[i])):
            if not vis[j]:
                vis[j]=True
                cnt+=1
                dfs(j)
    print(cnt)
main()

#! 上面注释掉的是把脚标统一到编号 所以数组开大一个 而下面的是把编号统一到索引



