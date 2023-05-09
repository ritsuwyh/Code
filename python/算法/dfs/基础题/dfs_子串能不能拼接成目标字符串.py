

#! 本题目限制了item_lst里面的元素只能使用0或者1次 用过了就不能再用了 如果无限制使用 那么可以不用标记数组
#! 第一个想法 dfs 注意不能用in函数 
flag=False
#! 下面这两个lst是常见的记录答案方式
ans=[]
temp=[]
#? 有一个小缺点 必须dfs完才能得到结果 遇到一个True不会停下来 
def dfs(target,L):#! 用一个L记录已经拼到哪了 关键!!!!!!
    
    
    if L==len(target):#! 注意递归终点
        global flag
        flag=True
        ans.append(temp.copy())
        return
        
    for i in range(len(item_lst)):
        if vis[i]:
            continue
        #! 这里要稍微修改一下 应该注意 L+len(item_lst[i]) 是否越界
        if item_lst[i]!=target[L:L+len(item_lst[i])]:
            continue
        vis[i]=True
        temp.append(item_lst[i])
        
        #! 其实这里可以不用now_str 我们只需要知道已经拼到哪里即可  并不需要记录已经拼成了什么 我们还可以用一个lst来记录是用谁拼成的目标字符串
        dfs(target,L+len(item_lst[i]))
        
        temp.pop()
        vis[i]=False#! 回溯
    return
    
    

#! 其实可以进行一下预处理? 1.把根本不在target里面的直接筛掉
#! 2. 如果筛完之后 总的子串长度都不够target长度 直接False

item_lst=input().split()
vis=[False for _ in range(len(item_lst))]
target=input()
dfs(target,0)
if flag:
    print(True)
    print(ans)
else:
    print(False)
