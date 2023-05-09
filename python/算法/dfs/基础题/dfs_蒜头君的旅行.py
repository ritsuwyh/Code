
ans_lst=[0]
class Point(object):
    def __init__(self,pos,weight):
        self.pos=pos
        self.weight=weight


def dfs(u):
    i=lst[u][0] #!注意i是一个class类
    if vis[i.pos]:
        # global min_step
        # if step<min_step:
        #     min_step=step

        return#! return别忘了写 而且要注意写的位置
    vis[i.pos]=True
    ans_lst.append(i.pos)
    dfs(i.pos)
    # ans_temp.pop()
    # vis[i.pos]=False
    return    
  
def main():
    n,m=eval(input())
    global lst
    lst=[[]for i in range(n)]
    global vis
    vis=[False for _ in range(n)]
    
    vis[0]=True
    
    for i in range(m):
        u,v,weight=eval(input())
        #! 无向图
        p1=Point(v-1,weight)
        lst[u-1].append(p1)
        p2=Point(u-1,weight)
        lst[v-1].append(p2)
        
    for i in range(n):
        lst[i].sort(key=lambda x:(x.weight,x.pos))
          
    dfs(0)
#! 一定要注意是类还是 数
    for i in ans_lst:
        print(i+1,end=" ")#! 根据题干 注意题目要的是脚标还是编号 此题一开始把编号统一成脚标 要还原成编号！！
        

main()
'''
4,4
3,4,4
4,2,5
2,1,7
4,1,5
'''