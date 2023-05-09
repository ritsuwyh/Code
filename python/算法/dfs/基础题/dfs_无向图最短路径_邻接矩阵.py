
#! 分析问题的时候要注意是有向图还是无向图

# chosen=dict.fromkeys(range(1,5),False)#经过分析 实际上每个点只能用一次 因为如果重复使用就会造成绕圈的情况 必不可能是最短的
# condition_dic={(0, 1): 10 ,(1, 2): 50, (0, 3) :30, (3, 2): 20, (3, 4): 60, (2, 4): 10, (0, 4): 100 }
# min_lenth=9999#!注意全局变量在声明的时候不可以初始化

# lst=[0]
# min_lst=[]
# def dfs(now_number=0,lenth=0):#默认起始为0 长度为0
#     if now_number==4:
#         global min_lenth
#         if lenth<min_lenth:
#             #!global min_lenth 必须在第一次使用min_lenth 之前就声明global
#             min_lenth=lenth
#             global min_lst
#             min_lst=lst.copy()#!用一个min_lst 每次都更新
#         print(lst)#! 打印所有可行的路径

#         return
#     for i in range(1,5):
#         if (now_number,i) not in condition_dic.keys() or chosen[i]:
#             continue
#         chosen[i]=True
#         lenth+=condition_dic[(now_number,i)]
#         temp=now_number
#         now_number=i
        
#         lst.append(i)
        
#         dfs(now_number,lenth)#!dfs 之后必须把所有这步做的操作都还原!!!!!!
#         now_number=temp
#         lenth-=condition_dic[(now_number,i)]
        
#         chosen[i]=False
        
#         lst.pop()
#     return
# def main():
#     dfs()
#     print(min_lenth)
#     print(min_lst)
# main()

# Ritsu 21:28:15
# 先一步到头 递

# Ritsu 21:28:36
# 然后 归 的时候把之前 递 没进行的操作倒过来进行

#todo 尝试用邻接矩阵来存储图 然后用dfs 之前的都是用邻接表dfs的
#condition_dic={(0, 1): 10 ,(1, 2): 50, (0, 3) :30, (3, 2): 20, (3, 4): 60, (2, 4): 10, (0, 4): 100 }

minx=9999
def dfs(u,lenth):
    if u==4:
        global minx#! 必须在这里声明！！！！
        if lenth<minx:
            
            minx=lenth
        return 
    for v in range(5):
        #if vis[u][v] or matrix[u][v]==0:
        if visx[v] or matrix[u][v]==0:
            continue
        visx[v]=True
        #vis[u][v]=True
        lenth+=matrix[u][v]
        dfs(v,lenth)
        lenth-=matrix[u][v]
        
        #vis[u][v]=False
        visx[v]=False
#! 生成图 (用邻接矩阵):
#vis=[[False for j in range(5)] for i in range(5)]
visx=[False for _ in range(5)]#! 注意状态数组的形式！！！ 不一定是二维数组
#!只需要记录 点 是否被走过 而不需要记录 边 是否被走过 因为最短路径走过的点 不可能重复！！！
matrix=[[0 for j in range(5)] for i in range(5)]
for _ in range(7):
    u,v,weight=eval(input())
    matrix[u][v]=weight
    matrix[v][u]=weight#! 别忘了是无向图
visx[0]=True#! 将初始落点改为已走过
dfs(0,0)
print(minx)
#! 测试样例
# 0,1,10
# 1,2,50
# 0,3,30
# 3,2,20
# 3,4,60
# 2,4,10
# 0,4,100
