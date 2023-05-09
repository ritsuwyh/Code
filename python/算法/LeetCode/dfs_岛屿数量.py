

# #! 注意是字符串'0' 还是数字0 注意怎么算连通

# #todo 连通块数量

# class Solution:
#     def numIslands(self, grid: list[list[str]]) -> int:
        
#         move=[(-1,0),(0,1),(1,0),(0,-1)]
#         m=len(grid)
#         n=len(grid[0])
#         def dfs(x,y):
#             for i in move:
#                 temp_x=x+i[0]
#                 temp_y=y+i[1]
#                 #! 先判断脚标合法性
#                 if temp_x<0 or temp_x>m-1 or temp_y<0 or temp_y>n-1:
#                     continue
#                 if vis[temp_x][temp_y] or grid[temp_x][temp_y]=='0':
#                     continue
#                 vis[temp_x][temp_y]=True
#                 dfs(temp_x,temp_y)
#             return

#         vis=[[False for j in range(n)] for i in range(m)]
#         cnt=0
#         for i in range(m):
#             for j in range(n):
#                 if vis[i][j] or grid[i][j]=='0':#! 条件别忘写了
#                     continue
#                 cnt+=1
#                 vis[i][j]=True#! 这句话别忘写了
#                 dfs(i,j) 
                
#         return cnt
    


#todo 连通块的周长 使用dfs我们可以求出每一个岛屿的周长

# class Solution:
#     def islandPerimeter(self, grid: list[list[int]]) -> int:
#         #! 这条边被算为边长当且仅当在这个方向的下一个方块是水或者出界 
        
#         moves=[(-1,0),(0,1),(1,0),(0,-1)]
#         m=len(grid)
#         n=len(grid[0])
#         def cal(x,y):#! 计算这个点贡献了多少边
            
#             cnt=0
#             for move in moves:
#                 xx=x+move[0]
#                 yy=y+move[1]
#                 if xx<0 or xx>m-1 or yy<0 or yy>n-1 or grid[xx][yy]==0:
#                     cnt+=1
#             return cnt
        
#         sumx=0
        
#         def dfs(x,y):
#             for move in moves:
#                 xx=x+move[0]
#                 yy=y+move[1]
#                 if xx<0 or xx>m-1 or yy<0 or yy>n-1:
#                     continue
#                 if vis[xx][yy] or grid[xx][yy]==0:
#                     continue
#                 vis[xx][yy]=True
#                 nonlocal sumx#! 别忘了写
#                 sumx+=cal(xx,yy)
#                 dfs(xx,yy)
                
#             return 

        
#         vis=[[False for j in range(n)] for i in range(m)]
        
#         ans_lst=[]#! 存储每块连通块的周长
#         for i in range(m):
#             for j in range(n):
#                 if vis[i][j] or grid[i][j]==0:
#                     continue
#                 vis[i][j]=True
#                 sumx+=cal(i,j)
#                 dfs(i,j)
#                 ans_lst.append(sumx)
#                 sumx=0
        
#         return ans_lst

#todo 连通块的最大面积


class Solution:
    def maxAreaOfIsland(self, grid: list[list[int]]) -> int:

        move=[(-1,0),(0,1),(1,0),(0,-1)]
        m=len(grid)#行数
        n=len(grid[0])#列数
        
        max_size=0
        temp=1#! 注意这里要初始化为1
        def dfs(x,y):
            for i in move:
                temp_x=x+i[0]
                temp_y=y+i[1]
                #! 先判断脚标合法性
                if temp_x<0 or temp_x>m-1 or temp_y<0 or temp_y>n-1:
                    continue
                if vis[temp_x][temp_y] or grid[temp_x][temp_y]==0:
                    continue
                vis[temp_x][temp_y]=True
                nonlocal temp
                temp+=1
                dfs(temp_x,temp_y)
            return

        vis=[[False for j in range(n)] for i in range(m)]

        for i in range(m):
            for j in range(n):
                if vis[i][j] or grid[i][j]==0:#! 条件别忘写了
                    continue

                vis[i][j]=True#! 这句话别忘写了
                dfs(i,j)
                if temp>max_size:
                    max_size=temp
                temp=1#! 要初始化为1
                
        return max_size
    
    
solution=Solution()
print(solution.maxAreaOfIsland([[0,0,1,0,0,0,0,1,0,0,0,0,0],
                                [0,0,0,0,0,0,0,1,1,1,0,0,0],
                                [0,1,1,0,1,0,0,0,0,0,0,0,0],
                                [0,1,0,0,1,1,0,0,1,0,1,0,0],
                                [0,1,0,0,1,1,0,0,1,1,1,0,0],
                                [0,0,0,0,0,0,0,0,0,0,1,0,0],
                                [0,0,0,0,0,0,0,1,1,1,0,0,0],
                                [0,0,0,0,0,0,0,1,1,0,0,0,0]]))
    