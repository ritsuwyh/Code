
class Solution:
    
    def letterCombinations(self, digits: str) -> list[str]:
        dic=dict(zip([str(i) for i in range(2,10)],['abc','def','ghi','jkl','mno','pqrs','tuv','wxyz']))#! 注意这里必须用字符串类型的数字
        ans=[]
        if not digits:
            return []
        def dfs(step,digits,temp:str):#! temp存储已经拼好的字符串
            if step==len(digits):#! 实际上这个step参数可以省略 直接用temp的长度就知道step是多少了
                ans.append(temp)
                return 
            
            for x in dic[digits[step]]:
                temp+=x
                dfs(step+1,digits,temp)
                temp=temp[:len(temp)-1]#! 回溯
        dfs(0,digits,'')
        return ans       