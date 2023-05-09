#灵活运用索引 #遍历谁要想清楚
#思路 如果matrix[i][j]既是该行最大 又是该列最小 则为鞍点

n=eval(input())
#生成矩阵
matrix=[]
for i in range(n):
    row=list(map(int,input().split()))
    matrix.append(row)

#求出每一行的最大值 每一列的最小值
row_max=[x[0] for x in matrix]# 先假定每一行的第一个元素是该行的最大值
#上面这行也可以写成: [matrix[i][0] for i in range(n)]
line_min=[matrix[0][i] for i in range(n)]# 先假定每一列的第一个是该列的最小值
for i in range(n):
    for j in range(n):
        if matrix[i][j]>=row_max[i]:
            row_max[i]=matrix[i][j]
        if matrix[i][j]<=line_min[j]:
            line_min[j]=matrix[i][j]
#遍历matrix中的所有元素
flag=False
for i in range(n):
    for j in range(n):
        if matrix[i][j]==row_max[i] and matrix[i][j]==line_min[j]:
            flag=True
            print(i,j)
            break
    if flag:
        break
if not flag:
    print("None")       
        
        
    
    