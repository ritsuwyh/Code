#输出前n个fib数
def main():
    n=eval(input())
    i=1
    a,b=0,1
    while i<=n:
        print(b)
        a,b=b,a+b
        i+=1
main()