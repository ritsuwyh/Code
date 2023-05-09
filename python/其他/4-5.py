def calculate_e(n):
    def jiecheng(x):
        if x==0:
            return 1
        else:
            sum_muti=1
            for i in range(1,x+1):
                sum_muti*=i
            return sum_muti
    sum=0
    for i in range(n+1):
        sum+=1/jiecheng(i)
    return sum
def main():
    n=eval(input())
    print("{:.8f}".format(calculate_e(n)))
main()
        
        
    