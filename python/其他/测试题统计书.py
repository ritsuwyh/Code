n=eval(input())
dic={}
book_lst=[]
emptyx=True
cnt=0
for i in range(n):
    book,num=input().split(',')
    num=int(num)
    dic[book]=dic.get(book,0)+num
    if book not in book_lst:
        book_lst.append(book)
    if num!=0:
        emptyx=False
        
if emptyx:
    print(None)
else:
    book_lst.sort()
    for i in book_lst:
        if dic[i]!=0:
            print(i+','+str(dic[i]))