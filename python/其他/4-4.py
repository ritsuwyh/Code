def prime(x):
    for i in range(2,x):
        if x%i==0:
            return False
    return True
def main():
    x=eval(input())
    
    lst=[ (a,b) for a in range(2,x) for b in range(a,x) if prime(a) and prime(b) and a+b==x]
    #上面这一行可以化简为: lst=[(a,x-a) for a in range (2,x) if prime(a) and prime (x-a) and a<=b]
    print(lst)
main()