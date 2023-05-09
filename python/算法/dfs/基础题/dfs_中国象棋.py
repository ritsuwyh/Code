
#!17:25 本题不限跳的次数
move=[(-2,1),(-1,2),(1,2),(2,1),(2,-1),(1,-2),(-1,-2),(-2,-1)]

flag=False
def dfs(x1,y1,x2,y2):
    if x1==x2 and y1==y2:
        global flag  #! 像这种判断能不能走到的题 都可以使用一个全局变量flag来记录
        flag=True
        return 
    for t in move:
        xx=x1+t[0]
        yy=y1+t[1]
        if xx<0 or xx>9 or yy<0 or yy>8:
            continue
        if bool_lst[xx][yy] or board[xx][yy]=='#':
            continue
        bool_lst[xx][yy]=True
        dfs(xx,yy,x2,y2)
    return 
def main():
    global board
    board=[]
    
    for _ in range(10):
        row=list(input())
        board.append(row)
    
    global bool_lst
    bool_lst=[[False for j in range(9)] for i in range(10)]
    for i in range(10):
        for j in range(9):
            if board[i][j]=='S':
                x1,y1=i,j
            if board[i][j]=='T':
                x2,y2=i,j
    dfs(x1,y1,x2,y2)           
    if flag:
        print('Yes')
    else:
        print('No')
main()