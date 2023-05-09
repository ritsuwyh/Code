n=eval(input())
x=ord('A') #学会这样的用法

for i in range(n):
    for j in range(n-i):
        print(chr(x),end=' ')
        x+=1
    print()
