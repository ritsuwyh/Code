x=input()
y=input()
x=x.strip()
lst=[i for i in x if i!=y.upper() and i!=y.lower()]
new_x=''.join(lst)
print(new_x)
#输入样例 7!jdk*!ASyu   
#!