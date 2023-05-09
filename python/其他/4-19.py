n=eval(input())


#是否符合输入格式??
'''matrix=[]
for i in range(n):
    row=[]
    for j in range(n):
        x=eval(input())
        row.append(x)
    matrix.append(row)'''

matrix=[]
for i in range(n):
    row=list(map(int,input().split()))
    matrix.append(row)
    
    
sum=0
for i in range(n):
    for j in range(n):
        if i!=n-1 and j!=n-1 and i+j!=n-1:
            sum+=matrix[i][j]
print(sum)