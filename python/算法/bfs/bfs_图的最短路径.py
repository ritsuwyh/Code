
#! bfs 和 dfs 根据问题不同选择 求最短路径边权相同的情况下使用bfs更好 因为找到最小的就直接return了
#! 但是dfs求最短路径需要遍历所有可能的情况 但是对于不同的边权值dfs求最短路径更好
#! bfs记录最短路径 用class 用头节点的路径扩展
#! 这道题 无权边 可用bfs
class Point(object):
    def __init__(self,pos,step):
        self.pos=pos
        self.step=step

def main():
    #! 输入点数和边数
    n,m=eval(input())
    
    
    #! 输入起始点和终点
    target_x,target_y=eval(input())
    #! 注意统一脚标
    target_x-=1
    target_y-=1
    
    #! 生成邻接矩阵
    matrix=[[0 for j in range(n)] for i in range(n)] #!邻接矩阵是n*n的 而不是*n*m的！！！！
    
    for i in range(m):#!向矩阵输入边  所以for 边数  
        u,v=eval(input())
        #! 无向图
        matrix[u-1][v-1]=1
        matrix[v-1][u-1]=1
    
    #! 状态数组 用"点"的
    vis=[False for i in range(n)]
    
    #! 初始化栈 以及头元素
    vis[target_x]=True
    lst=[]
    p=Point(target_x,0)
    lst.append(p)
    head=0  #! 只是充当一个指针的作用
    
    #! 退出标志
    flag=False
    
    
    #!主要程序
    while head<len(lst):
        for i in range(len(matrix[lst[head].pos])):#! 这里遍历脚标而不是遍历元素 是因为 需要用matrix[target_x][i]==0   题外话:len(lst[row])可以求该行的长度 遍历的时候必须用range(len()) 
            #if vis[matrix[target_x][i]] or matrix[target_x][i]==0:#!这样写是不对的 因为邻接矩阵只存有没有边 
            if vis[i] or matrix[lst[head].pos][i]==0:
                continue
            #vis[matrix[target_x][i]]=True#! 错误的写法
            vis[i]=True
            #p=Point(matrix[target_x][i],lst[head].step+1)#!错误的写法
            p=Point(i,lst[head].step+1)
            lst.append(p)
            
            #! 判断最新扩展的入栈的点是否到达目的地
            if lst[-1].pos==target_y:
                flag=True
                break
        if flag:
            break
        #! 继续向后扩展
        head+=1
        
        
    #! 输出结果
    print(lst[-1].step)   
    
main()


#! 测试样例
# 5,7
# 1,5
# 1,2
# 1,3
# 2,3
# 2,4
# 3,4
# 3,5
# 4,5
