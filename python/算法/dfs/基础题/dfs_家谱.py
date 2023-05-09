
#! 模型类似求子树的大小 只不过不用算子树的根节点  家谱必然是一个有向树
def dfs(u,fa):
    for i in Gx[u]:
        if i!=fa:
            lst[u]+=dfs(i,u)
    lst[u]+=1#! 本道题虽然不算根节点但是这一步必须要写 在最后减去1即可
    return lst[u]#! 注意模板 以及return写到哪里
def main():
    n=eval(input())
    #!则边数为n-1
    global Gx
    Gx=[[]for i in range(n)]
    for i in range(n-1):
        u,v=eval(input())
        Gx[u-1].append(v-1)
        
    global lst
    lst=[0 for i in range(n)]#!注意初始化
    
    dfs(0,0)
    
    for i in range(n):
        print(i+1,lst[i]-1)#! 这里为了统一脚标和编号所以i+1 后面要减1 因为不能算根节点
    
    
main()