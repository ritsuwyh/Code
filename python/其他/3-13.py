s=input()
lst1=[chr(i) for i in range(ord('A'),ord('Z')+1)]
lst2=[chr(j) for j in range(ord('Z'),ord('A')-1,-1)]
dic=dict(zip(lst1,lst2))
s_list=list(s)
for i in range(len(s_list)):
    if s_list[i] in dic.keys():
        s_list[i]=dic[s_list[i]]
new_s=''.join(s_list)
print(new_s)