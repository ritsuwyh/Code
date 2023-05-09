from collections import deque
lst=list(map(int,input().split()))

# dq=deque(lst)  #! pop popleft 都会返回被删除的元素值
#! 是错误的 deque 不支持切片 print(dq[1:])
# print(dq.popleft())

#! 不是本道题 
#! 找到所有得分的可能性

# score=float('-inf')
# q=1
# def dfs(temp_dq,q,temp_score):
#     if len(temp_dq)==0:
#         print(temp_score)
#         return   
    
#     #! 要么回溯 
#     #!要么在传参的时候改 不对原来的数据进行修改
    
#     for i in [0,-1]:
#         x=temp_dq.copy()
#         temp_number=x.pop(i)
#         dfs(x,q*(-1),temp_score+temp_number*q)
        
# dfs(lst.copy(),q,0)
# print(lst)
# print(score)


#! 博弈树 层数为1
# from collections import deque
# lst=list(map(int,input().split()))
# dq=deque(lst)
# # dq.popleft()
# # print(dq)
# score=0

# flag=True

# while len(dq)>=3:
#     if flag:
#         temp1=dq.copy()
#         temp2=dq.copy()
#         temp1.popleft()
#         threat1=max(temp1[0],temp1[-1])
#         temp2.pop()
#         threat2=max(temp2[0],temp2[-1])
#         if threat1<=threat2:
#             score+=dq[0]
#             dq.popleft()
#         else:
#             score+=dq[-1]
#             dq.pop()
#         flag=False
#     else:
#         temp1=dq.copy()
#         temp2=dq.copy()
#         temp1.popleft()
#         threat1=max(temp1[0],temp1[-1])
#         temp2.pop()
#         threat2=max(temp2[0],temp2[-1])
#         if threat1<=threat2:
#             score-=dq[0]
#             dq.popleft()
#         else:
#             score-=dq[-1]
#             dq.pop()        
#         flag=True
    
#     pass
    
    
# if len(dq)<=2:
#     if flag:
        
#         print(score+max(dq)-min(dq))
#     else:
#         print(score+min(dq)-max(dq))
        
        

#! 递归
#!从简单到复杂 思考能不能把大问题分解
# lst=list(map(int,input().split()))


 
# def func(lstx):
#     if len(lstx)==1:
#         return lstx[0]
#     if len(lstx)==2:
#         return max(lstx)-min(lstx)
#     elif len(lstx)>2:
#         return max(lstx[0]-func(lstx[1:].copy()),lstx[-1]-func(lstx[:len(lstx)-1].copy()))
        
# print(func(lst))