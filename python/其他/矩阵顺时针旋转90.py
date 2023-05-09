
# m,n=eval(input())
# matrix=[[None for j in range(n)] for i in range(m)]
# print(matrix)#声明一个空矩阵
m,n=eval(input())
matrix=[]
for i in range(m):
    row=list(map(int,input().split()))
    matrix.append(row)
new_matrix=[[matrix[-j-1][i] for j in range(m)] for i in range(n)]
print(new_matrix)