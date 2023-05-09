
#!使用dic判断是否出现了循环

class Solution:
    def isHappy(self, n: int) -> bool:
        dic={}
        def func(n,dic):
            if n==1:
                return True
            elif dic.get(n,0)!=0:
                return False#! 出现重复分数字说明出现了循环
            else:
                dic[n]=1
                temp=0
                for i in range(len(str(n))):
                    temp+=int(str(n)[i])**2
                return func(temp,dic)
        return func(n,dic)