
#!注意1要特判 
#!所以我们发现，如果 n 是合数，我们一定可以找到它的一个不超过根号n的因数，所以试除实际上只需要进行到根号n
#!如果不break，那我们也可以求 n的除了1 和 本身 以外的全部因子
# !或者求因子个数，需要同时存下符合条件时的 i 和 n / i ，需要特别注意 i * i==n 的时候，这时候只存一个，统计数量也只加 1个 
# !而且别忘了加上1和他本身这两个因子。
from cmath import sqrt

def is_prime(x):
    if x==1:
        return False
    else:
        #!不用sqrt函数了 以后负数开根再用 x的根号2就是 x**0.5
        temp=int(sqrt(x).real)+1 #! sqrt函数返回complex .real返回float 需要用int进一步类型转换 
        for i in range(2,temp):
            if x%i==0:
                return False
        return True
print(is_prime(2))