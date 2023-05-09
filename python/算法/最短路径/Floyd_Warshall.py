
#! 我们需要把 无边 的规定成一个很大的数 
inf=99999
n,m=eval(input())
matrix=[[inf if i!=j else 0 for j in range(n)] for i in range(n)]
#! 要习惯使用三目操作符和列表生成式 且邻接矩阵是n*n的！！
for i in range(m):
    u,v,weight=eval(input())
    #! 有向图
    matrix[u-1][v-1]=weight
#! 下面是错误写法  
# for i in range(n):
#     for j in range(n):
#         for k in range(n):
#             if matrix[i][j]>matrix[i][k]+matrix[k][j]:#! 注意是大于而不是大于等于
                # matrix[i][j]=matrix[i][k]+matrix[k][j]
#todo 要注意k在最外层 核心代码:
for k in range(n):
    for i in range(n):
        for j in range(n):
            if matrix[i][j]>matrix[i][k]+matrix[k][j]:#! 注意是大于而不是大于等于
                matrix[i][j]=matrix[i][k]+matrix[k][j]

print(matrix) #!matrix[i][j]的值就是编号i+1到j+1的最短路径
#! 测试样例
# 4,8
# 1,2,2
# 1,3,6
# 1,4,4
# 2,3,3
# 3,1,7
# 3,4,1
# 4,1,5
# 4,3,12