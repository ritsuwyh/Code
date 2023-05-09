t=eval(input())
#这道题在生成矩阵的时候就可以求出答案 
#为了记录答案 需要一个list
ans_lst=[]
for i in range(t):
    n=eval(input())
    matrix=[]
    for i in range(n):
        row=list(map(int,input().split()))
        matrix.append(row)
    flag=True
    for i in range(n):
        for j in range(n):
            if i>j and matrix[i][j]!=0:
                flag=False
                ans_lst.append("NO")
                break# 只是退出了内层的循环
        if not flag:
            break
    if flag:
        ans_lst.append("YES")
        
for i in ans_lst:
    print(i)          