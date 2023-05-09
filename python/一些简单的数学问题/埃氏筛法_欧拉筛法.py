
#! 复习使用generator 生成fib数

#!难理解的就是generator函数和普通函数的执行流程不一样。普通函数是顺序执行，
# !遇到return语句或者最后一行函数语句就返回。而变成generator的函数，在每次调用next()的时候执行，
# !遇到yield语句返回，再次执行时从上次返回的yield语句处继续执行

#!可以先构造一个从3开始的奇数序列：对于无限序列常常使用生成器  基本都是yeild第一个数
def _odd_iter():
    n = 1
    while True:
        n = n + 2
        yield n
#! 定义一个筛选函数 
def _not_divisible(n):
    return lambda x: x % n > 0
#!最后，定义一个生成器，不断返回下一个素数：
def primes():
    yield 2
    it = _odd_iter() # 初始序列
    while True:
        n = next(it) # 返回序列的第一个数
        yield n
        it = filter(_not_divisible(n), it) # 构造新序列

#!注意到filter()函数返回的是一个Iterator，也就是一个惰性序列，所以要强迫filter()完成计算结果，需要用list()函数获得所有结果并返回list。
# 打印1000以内的素数:
for n in primes():
    #!由于primes()也是一个无限序列，所以调用时需要设置一个退出循环的条件：
    if n < 1000:
        print(n)
    else:
        break
    
    


#! 埃氏筛法
# isPrime = [True for _ in range(101)]
#
# for i in range(2, len(isPrime)):
#     if isPrime[i]:
#         j = 2
#         while j * i <= 100:
#             isPrime[i * j] = False
#             j += 1
#
#
# result = []
#
# # print(isPrime)
# for num in range(2, len(isPrime)):
#     if isPrime[num]:
#         result.append(num)
#
# print(result)
# print(len(result))



#!s=''#!生成一个空字符串


#! 欧拉筛法
# #! 求小于等于n的所有素数
# N = int(input("请输入一个大于等于2的整数:"))
# result = []
# isPrime = [True for _ in range(N+1)]#! 注意索引和数字的区别
# for i in range(2, N+1):
#     if isPrime[i]:
#         result.append(i)
#     for x in result:#! 用结果列表里面的数 筛
#         if x * i > N:#! 越界 不用再筛选
#             break
#         isPrime[x * i] = False
#         if i % x == 0:#! 筛过了不用再筛了
#             break

# print(result)

#todo质数数列的中位数

n=eval(input())
ans=[]
is_prime=[True for _ in range(n+1)]
for i in range(2,n+1):
    if is_prime[i]:
           ans.append(i)
    for x in ans:
        if i*x>n:
            break
        is_prime[i*x]=False
        
        if i%x==0:
            break
print(ans)

if len(ans)%2==0: #! 区分索引和长度
    x1=ans[len(ans)//2-1]
    x2=ans[len(ans)//2]
    print((x1+x2)/2)
else:
    print(ans[len(ans)//2])    