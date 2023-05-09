
#! 求解连通块问题  取消递归终止条件 求出一个点能到达的所有位置 
#! dfs求最短路径必须回溯 但是单纯问能否到达某个点 不需要回溯
#! 求连通块大小也不必回溯 见"连通块问题" 
#! 上述问题bfs全都可以解决


def  maze_input(n,m):
    global maze
    maze=[]
    for i in range(n):
        row=input()
        maze.append(row)

#! 以后将def move 改为 [(),(),()....] 这样写起来更简洁
move=[(-1,0),(0,1),(1,0),(0,-1)]#! 上 右 下 左


def dfs(x,y,n,m):
    for i in range(4):
        temp_x=x+move[i][0]
        temp_y=y+move[i][1]
        if temp_x<0 or temp_x>n-1 or temp_y<0 or temp_y>m-1:
            continue
        if bool_lst[temp_x][temp_y] or maze[temp_x][temp_y]!='#':
            continue
        bool_lst[temp_x][temp_y]=True
        global temp#! 别忘了声明全局变量
        temp+=1
        dfs(temp_x,temp_y,n,m)
    return 


def main():
    n,m=eval(input())
    maze_input(n,m)
    global bool_lst
    bool_lst=[[False for j in range(m)] for i in range(n)]
    
    cnt=0 #!记录连通块的数量
    maxx=0 #!用于更新最大连通块的大小
    for i in range(n):
        for j in range(m):
            if not bool_lst[i][j] and maze[i][j]!='.':
                cnt+=1
                bool_lst[i][j]=True#! 别忘了标记已经走过了
                global temp
                temp=1#! 这里是1 !!!!!!!!!!!!!!!!!!!!!!!
                dfs(i,j,n,m)
                if temp>maxx:
                    maxx=temp
    print(cnt,maxx)   #! cnt是连通块的数量 maxx是最大连通块的大小
main()
        
