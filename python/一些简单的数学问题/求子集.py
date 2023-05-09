
#! 全排列 组合数(只需要更改递归终点) 类似于下面的思想

# ans_lst=[[]]#! 注意任何集合的子集都有空集 要在ans_lst 里面加 而不是在temp里
# temp=[]  
# def dfs(now_step,target_step):
#     if now_step==target_step:
#         xx=sorted(temp)
#         if xx not in ans_lst:
#             ans_lst.append(xx)
#         return
#     for i in range(len(lst)):
#         if vis[i]:
#             continue
#         vis[i]=True
#         temp.append(lst[i])
#         dfs(now_step+1,target_step)
#         vis[i]=False
#         temp.pop()
#     return 

# lst=list(eval(input()))

# vis=[False for _ in range(len(lst))]
# for targetx in range(len(lst)+1):
#     dfs(0,targetx)#! 分层dfs搜索
# ans_lst.sort()
# print(ans_lst)

#! 下面这个是考虑有序的情况 输出Anm
# ans_lst=[]
# temp=[]
# def dfs(now_step,target_step):
#     if now_step==target_step+1:#! 注意要加1
#         ans_lst.append(temp.copy())
#         return
#     for i in range(len(lst)):
#         if vis[i]:
#             continue
#         vis[i]=True
#         temp.append(lst[i])
#         dfs(now_step+1,target_step)
#         vis[i]=False
#         temp.pop()
#     return 


# # lst=list(eval(input()))
# # lst.sort()
# # vis=[False for _ in range(len(lst))]
# # for targetx in range(len(lst)):
# #     dfs(0,targetx)#! 分层dfs搜索
# # print(ans_lst)


# #! 求子集 !!!
# list_1 = input()
# list_1 = list_1[1:-1].split(",")
# list_1 = [int(x) for x in list_1]

# #! 必须先排序 使集合中的每个集合都是有序的
# list_1.sort()

# def get_sub_set(nums):
#     sub_sets = [[]]
#     for x in nums:#! 用已知数组中的元素以空集为起点一次次进行扩展
#         sub_sets.extend([item + [x] for item in sub_sets])
#     return sub_sets

# answer = get_sub_set(list_1)  [:]#! 浅拷贝
# #! 使大集合有序
# answer.sort()
# print(answer)


#! 求子集 找子集中有没有和为target的 这样可以输出所有的可能方案

# item_lst=list(map(int,input().split()))
# target=eval(input())
# lst=[[]]
# for x in item_lst:
#     lst+=[temp+[x] for temp in lst]#! 这里最好写成temp+[x] 而不是写成[x]+temp
# #*print(lst)
# flag=False
# for xx in lst:
#     if sum(xx)==target:
#         flag=True
#         break
# if flag:
#     print(True)
# else:
#     print(False)


#! 排列的思想解决求子集的问题
lst=eval(input())
lst.sort()
ans_lst=[[]]

def dfs(lst,now,start):
    global ans_lst
    for i in range(start,len(lst)):
        now.append(lst[i])
        ans_lst.append(now.copy())
        
        dfs(lst,now,i+1)
        now.pop()
        
dfs(lst,[],0)
print(ans_lst)

