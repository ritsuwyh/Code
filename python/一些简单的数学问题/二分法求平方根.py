
# #! 二分法求平方根 注意 要以1为分界点讨论 tuple 是上界和下界
# def improve(update, accurate, guess):

#     while not accurate(guess):

#         guess = update(guess)

#     return "%.9f"%((guess[0]+guess[1])/2)



# def appr_equal(x, y, epsilon = 1e-10):

#     return abs(x - y) < epsilon



# def sqrt_update(guess):

#     mid = average(guess)

#     if mid * mid > n :

#         return guess[0], mid

#     else :

#         return mid, guess[1]


# def average(tup):#! 求中间值

#     return (tup[0] + tup[1]) / 2



# def sqrt_accurate(guess):

#     mid = average(guess)

#     return appr_equal(mid * mid, n)


# n=eval(input())#! 求n的平方根

# if n>=1:
#     print(improve(sqrt_update, sqrt_accurate, (1, n))) #! 这里的1是下界 n是上界
# else:
#     print(improve(sqrt_update, sqrt_accurate, (n, 1))) 
    
    
#! 递归函数如果要是有 返回值 那么都要return返回值
def search_sqrt(l,r,target):
    mid=(l+r)/2
    x=abs(mid*mid-target)
    #! 递归终点
    if x<=1e-10:
        return mid
    
    if mid*mid>target:
        r=mid
        return search_sqrt(l,r,target)#! 必须写return
    else:
        l=mid
        return search_sqrt(l,r,target)
    
print(search_sqrt(0,2,0.0625))