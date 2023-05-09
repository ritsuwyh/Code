
#todo 使用bfs找到所有能走的点将其存到一个list中 如果使用popleft 那么就只能在bfs的过程中更新杀敌最大值及其索引坐标
#todo 本题除了下面的方法(求出所有可以到达的点 以及该点的杀敌数 排序可以得到最大值 ) 
#todo 还可以popleft 然后用遍历更新的思想 max=9999 ans_x ans_y 来记录最大杀敌数及其对应的坐标
#todo 如果head++ 那么queue中的所有数据都在 我们可以知道所有可以走到的点 以及每个点的杀敌数

#! 这道题使用的是 head++的模板
class Point(object):
    def __init__(self,x,y,kill_number):
        self.x=x
        self.y=y
        self.kill_number=kill_number
        
def maze_input(n,m):
    print("请输入迷宫('.'代表空地 '#'代表墙壁 'G'代表敌人 索引为(2,2)的点为小人的初始点 必须是空地):")
    global maze
    maze=[]
    for i in range(n):
        row=input()
        maze.append(row)

def target_killed(x,y):
    sumx=0
    memorizex=x
    memorizey=y
    
    while maze[x][y]!='#':
        if maze[x][y]=='G':
            sumx+=1
        y+=1
    x=memorizex
    y=memorizey
    
    while maze[x][y]!='#':
        if maze[x][y]=='G':
            sumx+=1
        y-=1
    x=memorizex
    y=memorizey
    
    while maze[x][y]!='#':
        if maze[x][y]=='G':
            sumx+=1
        x+=1
    x=memorizex
    y=memorizey
    
    while maze[x][y]!='#':
        if maze[x][y]=='G':
            sumx+=1
        x-=1
    x=memorizex
    y=memorizey   
    return sumx        

def move(point,i):
    if i==0:
        return (point.x-1,point.y)
    elif i==1:
        return (point.x,point.y+1)
    elif i==2:
        return (point.x+1,point.y)
    else:
        return (point.x,point.y-1)
    
      
def main():
    n,m=eval(input("请输入迷宫的行和列:"))
    maze_input(n,m)
    
    bool_lst=[[False for j in range(m)] for i in range(n)]
    
    q=[]#* 用来存储可以放的点
    p1=Point(2,2,target_killed(2,2))
    bool_lst[2][2]=True
    q.append(p1)
    
    #*本道题的起始点固定为索引坐标(2,2)
    
    head=0
    
    while head<len(q):#! 这里非常重要!!!!!
        for i in range(4):
            x=move(q[head],i)[0]
            y=move(q[head],i)[1]
            if x<0 or x>n-1 or y<0 or y>m-1:#! 先判断脚标合法性
                continue
            if bool_lst[x][y] or maze[x][y]!='.': #! 别忘了把条件写全了  走没走过+能不能走
                continue
            kill_number=target_killed(x,y)
            p=Point(x,y,kill_number)
            bool_lst[x][y]=True
            q.append(p)
            
            #!不用break了 因为求的不是最短路径
        head+=1    
    
    #! 对一个全是自定义类对象的list 排序
    q.sort(key=lambda x:x.kill_number,reverse=True)
    #!deque 没有.sort 函数
    
    print("最多杀敌数为:{} 放的索引坐标为:({},{})".format(q[0].kill_number,q[0].x,q[0].y))     
    
main()

