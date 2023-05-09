x,y=map(int,input().split())
temp=0
if x>y:
    print("Invalid")
else:
    print("fahr celsius")
    for i in range(x,y+1,2):
        temp=5*(i-32)/9
        print("{:d}{:>6.1f}".format(i,temp))

