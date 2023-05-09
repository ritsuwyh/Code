# lst=input().split()
# chosen=[]
# dic={}
# x=223700001
# for i in lst:
#     if i not in chosen:
#         chosen.append(i)
#         dic[i]=x
#         x+=1
# ans_lst=[]
# for i in lst:
#     ans_lst.append(dic[i])
# print(list(map(str,ans_lst)))


#!上面的程序超时了
#!目的 建立一个  名字-学号  的字典  注意如果已经有学号了就不用再给他学号了
lst=input().split()

dic={}
#print(dic)
x=223700001
for i in lst:
    if dic.get(i,0)==0: #if i not in dic.keys()
        dic[i]=x
        x+=1
ans_lst=[]
for i in lst:
    ans_lst.append(str(dic[i]))
print(ans_lst)