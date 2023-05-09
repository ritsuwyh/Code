
#! 回溯dfs
#! 注意到n皇后问题每一行只能有一个皇后 所以我选择一行一行放 
ans_lst=[]#! 用来记录符合规则的棋盘
temp=[]#! 与ans_lst 配合使用  这类题都是需要类似的操作
#! 记录答案的变量全在全局变量里

changed_index=[]#! 记录每一步改变的位置 需要记录每一步的而不能仅仅记录当前步的 所以存在一个数组里
#! 不能无差别还原 只能还原一步!!! 所以我们需要记录上一步都改变了哪些位置
cnt=0
def func1(x,y,n):
    #! 因为是一层一层放的 所以不用管左上和右上的对角线
    temp_index=[]
    global vis
    
    for i in range(x,n):
        for j in range(n):
            if i==x or j==y or j-i==y-x or j+i==x+y :#! j-i==y-x 是沿着x,y主对角线上的元素 i+j==x+y 是沿着副对角线上的元素 同时也看看五子棋算法 判负 取棋形
                if vis[i][j]!=True:
                    temp_index.append((i,j))
    changed_index.append(temp_index.copy())

def func2(step,b):#!b 是True或者False
    global vis
    for pos in changed_index[step]:
        vis[pos[0]][pos[1]]=b
         
def dfs(step,n):
    if step==n:#! 注意这里应该是n而不是n-1 一定要注意递归终点
        ans_lst.append(temp.copy())
        global cnt
        cnt+=1
        return 
    
    
    global board
    for i in range(n):
        if vis[step][i]:
            continue
        
        
        board[step][i]='Q'
        #vis[step][i]=True#!此步没必要 在func2中已经实现了
        
        temp.append(board[step].copy())#! 必须用.copy
        
        func1(step,i,n)#! 统计这一步需要改变的位置
        
        func2(step,True)#! 进行改变
        
        dfs(step+1,n)
        #! 不能无差别还原 只能还原一步!!! 所以我们需要记录上一步都改变了哪些位置
        
        func2(step,False)#! 还原
        
        temp.pop()
        changed_index.pop()#! 这一步别忘了
        board[step][i]='.'
    return 

def main():
    n=eval(input())

    global board
    board=[['.'for j in range(n)] for i in range(n)]
    global vis
    vis=[[False for j in range(n)] for i in range(n)]
    
     
    dfs(0,n)
    
    #! 输出答案
    for x in ans_lst:
        for y in x:
            print(y)
        print()
        print()
    print(cnt)
main()