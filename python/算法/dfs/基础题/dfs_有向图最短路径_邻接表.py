

#! 有向权边用邻接表储存 需要用class
class Road(object):
    def __init__(self,v,weight):
        self.v=v
        self.weight=weight
        #self.vis=False#? 邻接矩阵的状态数组 改为class里面的vis属性?
        
#! 外面的不用声明全局变量 在函数内部只有 赋值 需要声明全局变量 .append()不属于赋值
temp=[1]   #! 用于更新 

min_road=[]  #! 存最短的路径

ans_road=[]  #! 存所有可能的路径(不重复走)

min_lenth=9999 

def dfs(u,lenth):
   
    if u==4:
        ans_road.append(temp.copy())
        global min_lenth
        
        if lenth<min_lenth:
            min_lenth=lenth
            global min_road #!
            min_road=temp.copy()#! 必须写.copy()
        return 
    
    for i in lst[u]:
        if visx[i.v]:
            continue
        visx[i.v]=True    #!可在循环过程中对lst的class属性进行更改
        lenth+=i.weight
        temp.append(i.v +1)#! 加 1 是为了统一脚标
        dfs(i.v,lenth)  #! 这里不能传入i 而应该传入i.v 
        temp.pop()
        lenth-=i.weight
        visx[i.v]=False
    return

def main():    
    n,m=eval(input())
    global lst
    lst=[ [] for i in range(n)]
    for _ in range(m):
        u,v,weight=eval(input())
        road=Road(v-1,weight)#! 这里为了统一脚标 所以减1 还有一种方法就是把lst开大一个 lst[0]不用
        lst[u-1].append(road)
    global visx
    visx=[False for i in range(n)]
    visx[0]=True
    dfs(0,0)
    
    #! 小的注意点 是否需要改变落点的vis值
    print(ans_road)
    print(min_road)
    print(min_lenth)
    
main()
#! 测试样例
# 5,8
# 1,2,2
# 1,5,10
# 2,3,3
# 2,5,7
# 3,1,4
# 3,4,4
# 4,5,5
# 5,3,3