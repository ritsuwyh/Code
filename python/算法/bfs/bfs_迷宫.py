from collections import deque


#! 这道题使用的是popleft
class Point(object):
    def __init__(self,x,y,step,road):
        self.x=x
        self.y=y
        self.step=step
        
        #! 这里为了记录最短的路径所以定义了一个road
        self.road=road
        
        
#! 下面的函数可以简化
def move(point,i):
    if i==0:
        return (point.x-1,point.y)
    elif i==1:
        return (point.x,point.y+1)
    elif i==2:
        return (point.x+1,point.y)
    else:
        return (point.x,point.y-1)


def maze_input(n,m):
    print("请输入一个迷宫('.' 代表空地):")
    global maze
    maze=[]
    for i in range(n):#! 用字符串数组作为二维数组
        row=input()
        maze.append(row)
        
def main():
    n,m=eval(input("请输入迷宫的行数和列数:"))
    
    maze_input(n,m)
    #! 状态数组 vis
    bool_lst=[[False for j in range(m)] for i in range(n)]
    
    q=deque([])
    x1,y1=eval(input("请输入王子的坐标索引:"))
    bool_lst[x1][y1]=True#! 别忘了把初始点设为已走过的点
    p1=Point(x1,y1,0,[(0,0)])
    q.append(p1)
    
    x2,y2=eval(input("请输入公主的坐标索引:"))
    
    f=False#! 记录是否到达最终位置
    
    #! 特判一下王子和公主一开始就在一个点
    if x1==x2 and y1==y2:
        print('最短的步数为:')
        print(q[-1].step)
        print('最短的路径为:')
        print(q[-1].road)
        exit()
        
        
    while len(q)!=0:
        for i in range(4):
            x=move(q[0],i)[0]
            y=move(q[0],i)[1]
            #!合法性判断
            if x<0 or x>n-1 or y<0 or y>m-1:
                continue
            if maze[x][y]!='.' or bool_lst[x][y]:
                continue
            
            #!road=q[0].road.append((x,y)) 这样写是错误的 因为append返回值是None
            road=q[0].road.copy()
            road.append((x,y))
            #!记录路径 用父亲的路径继续扩充
            
            
            p=Point(x,y,q[0].step+1,road)
            q.append(p)
            bool_lst[x][y]=True
            
            #! 如果到达了最终的位置 直接两个flag(模板) 退出双层循环 因为现在q队列最后一个点就是最短的
            #! 边权相同 谁先到谁最短!
            if q[-1].x==x2 and q[-1].y==y2:
                f=True
                break
        if f:
            break
        q.popleft()#! 父点已经完成了拓展 无用了 所以直接去掉 使父点一直是q[0]
        #! 注意 这里可以不用popleft 可以用head++ 把父节点向后移动 
    if f:
        print('最短的步数为:')
        print(q[-1].step)
        print('最短的路径为:')
        print(q[-1].road)
    else:
        print('无法到达')
main()