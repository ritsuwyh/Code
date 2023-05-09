
#! 求连通块数量 !!!!!
move=[(-1,0),(0,1),(1,0),(0,-1)]

def dfs(x,y,n,m):
    for t in move:
        #!  注意！！！ 一定不要直接对原来的坐标进行操作！！！！ 
        xx=x
        yy=y
        #! 下面注释掉的问题要好好反思
        # while xx>=0 and xx<=n-1 and yy>=0 and yy<=m-1:
        #     xx+=t[0]
        #     yy+=t[1]
        #     if matrix[xx][yy]=='1' and not bool_lst[xx][yy]:
        #         bool_lst[xx][yy]=True
        #         dfs(xx,yy,n,m)
        while xx+t[0]>=0 and xx+t[0]<=n-1 and yy+t[1]>=0 and yy+t[1]<=m-1:
            xx+=t[0]
            yy+=t[1]
            if matrix[xx][yy]=='1' and not bool_lst[xx][yy]:
                bool_lst[xx][yy]=True
                dfs(xx,yy,n,m)      
    return
def main():
    cnt=0
    n,m=eval(input())
    global matrix
    matrix=[]
    for i in range(n):
        row=list(input())
        matrix.append(row)
        
        
    global bool_lst
    bool_lst=[[False for j in range(m)] for i in range(n)]
    for i in range(n):
        for j in range(m):
            if matrix[i][j]=='1' and not bool_lst[i][j]:#! 区分 1还是 '1'
                cnt+=1
                bool_lst[i][j]=True#! 别忘了标记已经走过了
                dfs(i,j,n,m)
    print(cnt)
main()