# 以空格分隔数据只能用 input().split()



m,n=eval(input())
matrix=[]
for i in range(m):
    row=[]
    for j in range(n):
        x=eval(input())
        row.append(x)
    matrix.append(row)
for i in matrix:
    print(sum(i))

        