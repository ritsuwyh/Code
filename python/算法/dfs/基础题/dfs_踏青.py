
#todo 6:10 找不到人 说明人在草丛里面 若有n块草丛 则最多只需要n-1次寻找
#! 这道题其实就是统计连通块的个数 四个方向



move=[(-1,0),(0,1),(1,0),(0,-1)]

def dfs(x,y,n,m):
    for t in move:
        xx=x+t[0]
        yy=y+t[1]
        if xx<0 or xx>n-1 or yy<0 or yy>m-1:
            continue
        if bool_lst[xx][yy] or matrix[xx][yy]!='#':
            continue
        bool_lst[xx][yy]=True
        dfs(xx,yy,n,m)
            
    return 
def main():
    cnt=0
    n,m=eval(input())
    global matrix
    matrix=[]
    for _ in range(n):
        row=list(input())
        matrix.append(row)
    
    global bool_lst
    bool_lst=[[False for j in range(m)] for i in range(n)]
    
    for i in range(n):
        for j in range(m):
            if matrix[i][j]!='.' and not bool_lst[i][j]:
                cnt+=1
                bool_lst[i][j]=True#! 别忘了标记已经走过了
                dfs(i,j,n,m)
    print(cnt-1)
    
main()
