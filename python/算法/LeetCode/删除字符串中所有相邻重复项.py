
#! flag变量的妙用
s=input()
flag=True
while flag:
    for i in range(len(s)-1):
        if s[i]==s[i+1]:
            s=s[:i]+s[i+2:]
            break
#! 注意这里 s[i+2:]即使不存在也可以  s[:0] 也可以 都会返回[]
# lst=[1,2]
# print(lst[3:])

# lst=[[1,2,3],[4,5,6]]
# for i,j,k in lst:
#     print(i,j,k)
#! 看my_eval 里面的for循环注意事项
        if i==len(s)-2:#! 能到这里说明已经没有相邻两个一样的了
            flag=False
print(s)
#todo 这道题也可以用栈的思想 与栈顶元素相同就不入栈 这个更好!!!!!!!!!!!
