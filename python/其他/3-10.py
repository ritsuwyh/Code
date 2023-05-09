s=input()
lst=list(s)
new_lst=[i for i in lst if i.isupper() and i!='A'and i!='E' and i!='I' and i!='O' and i!='U']
print(len(new_lst))