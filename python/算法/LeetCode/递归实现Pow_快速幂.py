

class Solution:
    
    #! 注意讨论指数 0 负 要特判
    def myPow(self, x: float, n: int) -> float:
        def Pow(x,n):
            if n==0:
                return 1.0
            elif n<0:
                n*=-1
                temp=n//2
                y=Pow(x,temp)#! 这种能先算出来的就先算出来防止之后重复计算!!!
                #! 熟悉三目操作
                return 1/(y*y) if temp*2==n else 1/(x*y*y)
            else:
                temp=n//2
                y=Pow(x,temp)
                return y*y if temp*2==n else x*y*y
        ans=Pow(x,n)
        return ans