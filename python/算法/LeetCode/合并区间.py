
#! 网站 贪心 实现不相交的线段
#! 也可以用第i-1个来扩充第i个
#! 本题使用了栈的思想 把区间放入栈里面 然后扩到不能继续扩展为止 然后再放一个区间
# intervals=list(eval(input()))
# stack=[]
# intervals.sort(key=lambda x: (x[0],x[-1]))
# for i in intervals:
#     if stack==[] or i[0]>stack[-1][-1]:#! 一定先要考虑空的情况 如果栈为空 或者区间左端点大于栈顶需要扩充的区间右端点 那么就入栈
#         stack.append(i)
#     else:
#         if i[-1]<=stack[-1][-1]:
#             continue
#         else:
#             stack[-1][-1]=i[-1]
# print(stack)


lst1=[[3,2,3],[3,1,4]]
lst2=[[4,5,6],[7,8,9]]
lst=lst1+lst2
lst.sort()
print(lst)
