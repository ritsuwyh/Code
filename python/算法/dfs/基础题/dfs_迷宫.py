# .空地 *炸弹 别忘了写return 别忘了所有都要逆序复原 在哪层语句要注意
#! 这道题不用position元组 直接用x,y 记录坐标更简单
#! 如果求解一个1迷宫有多少种可行的路径 声明一个全局变量即可搜到终点结果就加1
min_step=9999
lst=[]
min_lst=[]
road_lst=[]
def maze_input(n,m):
    print("请输入一个迷宫('.' 代表空地):")
    global maze
    maze=[]
    for i in range(n):
        row=input()
        maze.append(row)
        
def move(i,position1):
    if i==0:
        return (position1[0]-1,position1[1])
    elif i==1:
        return (position1[0],position1[1]+1)
    elif i==2:
        return (position1[0]+1,position1[1])
    else:
        return (position1[0],position1[1]-1)
    
def dfs(position1,position2,n,m,step=0):
    if position1==position2:
        global min_step
        if step<min_step:
            min_step=step
            global min_lst
            min_lst=lst.copy()#! 一定要用copy！！！！ 否则lst的改变也会造成min_lst改变
        road_lst.append(lst.copy())#!要放在内层的if语句外面！！！    
        #print(lst)  这里不想在调用函数的时候直接输出所有路径 就用一个road_lst来记录
        #这个方法是通用的 以解决上述注释的问题
        return
    for i in range(4):#规定 上 右 下 左
        temp=move(i,position1)
        #pos=position1#记录一下 以便之后复原
        #! 模板 先不要动 而是试探一下 先把下一步不合法的筛掉
        #!先对脚标进行合法性判断: 必须分成两步 先要保证脚标合法！！
        if temp[0]<0 or temp[0]>n-1 or temp[1]<0 or temp[1]>m-1:
            continue
        if maze[temp[0]][temp[1]]!="." or bool_lst[temp[0]][temp[1]]:
            continue
        #! 这里可以简化 根本就不用改position1 直接用temp就可以了
        #position1=temp
        #bool_lst[position1[0]][position1[1]]=True
        bool_lst[temp[0]][temp[1]]=True
        lst.append(temp)
        
        #dfs(position1,position2,n,m,step+1)
        dfs(temp,position2,n,m,step+1)
        
        lst.pop()
       # bool_lst[position1[0]][position1[1]]=False
        bool_lst[temp[0]][temp[1]]=False
       # position1=pos
        #!以倒过来的顺序来还原！！！
    return
    
    
def main():
    #手动输入一个maze
    n,m=eval(input("请输入迷宫的行数和列数:"))
    maze_input(n,m)
    
    #生成一个对应于maze大小的bool二维数组 用于记录一下每个点是否被走过
    global bool_lst
    bool_lst=[[False for j in range(m)] for i in range(n)]
    
    #输入两个人的坐标
    x1,y1=eval(input("请输入王子的坐标索引:"))
    position1=(x1,y1)
    #! 这里不要忘记了将王子的落点改为已走过
    bool_lst[position1[0]][position1[1]]=True
    
    x2,y2=eval(input("请输入公主的坐标索引:"))
    position2=(x2,y2)
    dfs(position1,position2,n,m)
    #调用函数
    if min_step==9999:
        print("无法到达公主的位置")
    else:
        print('所有路径为:')
        for i in road_lst:
            print(i)
        #dfs(position1,position2,n,m)
        print("最短的路径及步数为:")
        print(min_lst,min_step)
    
main()