def cal_sum(n):
    up=2
    down=1
    sum=0
    for i in range(n):
        sum+=up/down
        up,down=up+down,up #类似于fib
    return sum
def main():
    n=eval(input())
    print("%.2f"%cal_sum(n))
main()