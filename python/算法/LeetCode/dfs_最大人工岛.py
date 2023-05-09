

#!1.类似LC695-岛屿的最大面积, 首先计算最大岛屿面积；将各个岛屿进行编号，index放入grid中，用哈希表保存{index:size}
#! 其实就是类似于把每一个连通块图上不同的颜色 
#!2.对每个海洋pixel计算周围岛屿的总面积   

class Solution:
    def largestIsland(self, grid: list[list[int]]) -> int:

        
        
        
        m=len(grid)
        n=len(grid[0])
        flag=False
        for row in grid:
            if 0 in row:
                flag=True
                break
        if not flag:
            return m*n
        color=0
        matrix=grid.copy()#todo 我们要在这个matrix矩阵上面进行操作 更改元素的值为编号
        vis=[[False for j in range(n)] for i in range(m)]
        moves=[(-1,0),(0,1),(1,0),(0,-1)]
        size=1
        dic={}
        def dfs(x,y,color):
            for move in moves:
                xx=x+move[0]
                yy=y+move[1]
                if xx<0 or xx>m-1 or yy<0 or yy>n-1:
                    continue
                if vis[xx][yy] or grid[xx][yy]==0:
                    continue
                vis[xx][yy]=True
                
                nonlocal size
                size+=1
                
                matrix[xx][yy]=color
                dfs(xx,yy,color)
                
            return 
        
        for i in range(m):
            for j in range(n):
                if vis[i][j] or grid[i][j]==0:
                    continue
                vis[i][j]=True
                matrix[i][j]=color
                dfs(i,j,color)
                dic[color]=size
                color+=1
                size=1
        max_size=0
        for i in range(m):
            for j in range(n):
                color_set=set([])
                temp_size=0
                for move in moves:
                    ii=i+move[0]
                    jj=j+move[1]
                    if ii<0 or ii>m-1 or jj<0 or jj>n-1:
                        continue
                    if vis[ii][jj]:#! 说明已经被涂上色了
                        color_set.add(matrix[ii][jj])
                for q in color_set:
                    temp_size+=dic[q]
                if temp_size+1>max_size:#! 别忘了加1 !!!!
                    max_size=temp_size+1
        return max_size