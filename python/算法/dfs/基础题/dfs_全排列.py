#生成1-n的全排列
ans_lst=[]

def dfs(n,step=0):
    
    if step==n:
        print(ans_lst)
        return
    for i in range(1,n+1):
        if used[i]:
            continue
        else:
            used[i]=True
            ans_lst.append(i)
            dfs(n,step+1)
            used[i]=False
            ans_lst.pop()
    return 
def main():
    n=eval(input())
    #! global 全局变量不一定要在开头声明
    global used
    used=dict.fromkeys(range(1,n+1),False)
    dfs(n)
    
main()