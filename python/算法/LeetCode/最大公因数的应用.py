class Solution:
    def simplifiedFractions(self, n: int) -> list[str]:
        if n==1:
            return []
        
        ans=[]
        
        def gcd(a,b):#! 传入的顺序无所谓
            if b==0:
                return a
            return gcd(b,a%b)
        for i in range(1,n):
            for j in range(i+1,n+1):#! 这样遍历 如果出现可以约分的 那么约分之后的结果一定已经存过了
                if gcd(i,j)==1:
                    ans.append('%d/%d'%(i,j))
        return ans  