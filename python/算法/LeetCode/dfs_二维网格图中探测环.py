
class Solution:
    def containsCycle(self, grid: list[list[str]]) -> bool:
        #!我们可以用一个direction变量来记录上一次走的方向,这样我们可以避免在这一步中走回头路 即在本步中不能走direction的相反方向
        
        moves=[(-1,0),(0,1),(1,0),(0,-1)]#!↑ → ↓ ←
        #! 这种周期的我们可以用取模的思想 
        #! 可以发现 (index+2)%4即为反方向的索引
        
        m=len(grid)
        n=len(grid[0])
        flag=False
        vis=[ [-1 for j in range(n)] for i in range(m)]
        
        #! 由于我们不能用相同的标记值 所以不能用True False 不妨用grid里面的字母来做标记
        
        def dfs(s,direction,x,y):
            for i in range(len(moves)):
                
                if direction!=-1 and i==(direction+2)%4:
                    continue
                                
                xx=x+moves[i][0]
                yy=y+moves[i][1]
                
                if xx<0 or xx>m-1 or yy<0 or yy>n-1:
                    continue
                
                #! 递归终点
                if vis[xx][yy]==s: #! 走到了之前走过的点
                    nonlocal flag
                    flag=True
                    return
                
                # if grid[xx][yy]!=s:
                #     continue
                
                if grid[xx][yy]==s:
                    vis[xx][yy]=s
                    dfs(s,i,xx,yy)
                 
            return 
        
        
        for i in range(m):
            for j in range(n):
                if  vis[i][j]==-1:#! 如果这个点没有被访问过 (-1代表非法值)
                    vis[i][j]=grid[i][j]
                    dfs(grid[i][j],-1,i,j)
                    #! 只要有一个环 就可以return
                    if flag==True:
                        return flag
        
        return flag