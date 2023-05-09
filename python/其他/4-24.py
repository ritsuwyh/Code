n=eval(input())
for i in range(1,n+1):
    for j in range(1,i+1):
        print("%d*%d=%d"%(j,i,i*j),end="    ")#体会 end= 的用法
    print()
