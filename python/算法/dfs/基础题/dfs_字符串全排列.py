# lst=[]
# ans_lst=[]
# def dfs(s,step):
#     if step==len(s):
#         ans_lst.append(''.join(lst.copy()))
#         return
#     for i in range(len(s)):
#         if not vis[i]:
#             vis[i]=True
#             lst.append(s[i])
#             dfs(s,step+1)
#             lst.pop()
#             vis[i]=False
#     return 

# s=list(input())
# new_s=[]
# for i in s:
#     if i not in new_s:
#         new_s.append(i)
# vis=[False for _ in range(len(new_s))]
# dfs(new_s,0)
# ans_lst.sort()
# print(ans_lst)

lst=[]
ans_lst=[]
#! 可以进行优化 
def dfs(s,step):
    if step==len(s):
        ans_lst.append(''.join(lst.copy()))
        return
    for i in range(len(s)):
        if not vis[i]:
            vis[i]=True
            lst.append(s[i])
            dfs(s,step+1)
            lst.pop()
            vis[i]=False
    return 

s=list(input())
vis=[False for _ in range(len(s))]
dfs(s,0)

ans_lst.sort()
ans_lstx=[]
for i in ans_lst:
    if i not in ans_lstx:
        ans_lstx.append(i)
print(ans_lstx)
