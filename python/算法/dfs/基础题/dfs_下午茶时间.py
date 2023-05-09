#8:05 
#! 分析模型 只要是连通块就可以相互认识 一个连通块是一个朋友圈
#! 本题的特殊点 要把这些牛分成几个连通块 要知道哪几头是一个朋友圈的

friend_lst=[]
temp=[]
def dfs(u):
    for i in Gx[u]:
        if vis[i]:
            continue
        vis[i]=True
        temp.append(i)
        dfs(i)
    return 

def main():
    n,m,q=eval(input())
    
    global Gx
    Gx=[[]for i in range(n)]
    
    for i in range(m):
        u,v=eval(input())
        Gx[u-1].append(v-1)
        Gx[v-1].append(u-1)
    
    global vis
    vis=[False for i in range(n)]
    
    
    # for i in range(n):
    #     for j in Gx[i]:
    #! 要明白 研究的对象是奶牛(点) 所以上面注释掉的是错的
    for j in range(n):
        if not vis[j]:
            vis[j]=True
            global temp
            temp.append(j)
            dfs(j)
            friend_lst.append(temp.copy())
            temp=[]#! 目的是把temp清空
    
    for i in range(q):
        flag=False#! 注意变量初始化的位置
        a,b=eval(input())
        for t in friend_lst:
            
            if a-1 in t and b-1 in t:#! 这里找错误找了好长时间
                #! 注意要将编号统一到索引！！！！！！
                flag=True
                break
        if flag:
            print('Yes')
        else:
            print('No')
main()