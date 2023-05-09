
#todo 13:30 这道题用dic可以 用一个lst 也可以见家谱(求子树大小的变形)
def dfs(u,fa):
    
    for x in G[u]:
        
        if x!=fa:
            #!dic[u]+=dfs(x,u) 这个写法是错误的 因为dic[u]可能不存在
            dic[u]=dic.get(u,0)+dfs(x,u)
    #!dic[u]+=1 这个写法是错误的 理由同上
    
    dic[u]=dic.get(u,0)+1
    return dic[u]

def main():
    #! 输入树的节点数:
    n=eval(input())
    global G
    G=[[]for _ in range(n+1)]
    #! 则树的边数为n-1:
    for i in range(n-1):
        u,v=eval(input())
        G[u].append(v)
        G[v].append(u)
    global dic
    dic={}
    dfs(1,0)
    for i in range(1,n+1):
        print(i,dic[i])
main()