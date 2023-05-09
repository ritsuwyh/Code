
#! 求某一点所在连通块的大小


#! 需要多种数据那就用class

def maze_input(n,m):
    global maze
    maze=[]
    for i in range(n):
        row=input().split()
        maze.append(row)
        
move=[(-1,0),(0,1),(1,0),(0,-1)]
def main():
    
    n,m=eval(input("请输入矩阵的行数和列数:"))
    startx,starty=eval(input("请输入起始坐标:"))
    maze_input(n,m)
    vis=[[False for j in range(m)] for i in range(n)]
    
    
    cnt=0
    lst=[]
    lst.append((startx,starty))
    vis[startx][starty]=True
    cnt+=1
    head=0
    
    while head<len(lst):
        for t in move:
            xx=lst[head][0]+t[0]
            yy=lst[head][1]+t[1]
            if xx<0 or xx>n-1 or yy<0 or yy>m-1:
                continue
            
            if vis[xx][yy] or maze[xx][yy]=='0':#! 区分数字0和字符0
                continue
            
            vis[xx][yy]=True
            cnt+=1
            lst.append((xx,yy))
        head+=1
    print(cnt) 
    
main()