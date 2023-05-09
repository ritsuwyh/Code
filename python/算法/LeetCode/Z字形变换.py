
class Solution:
    def convert(self, s: str, numRows: int) -> str:
        #! 利用模的思想 和有效的数独我自己的想法 
        #! 利用索引的特点存到相应的list中去
        #! 此题一个循环分成两段 一个循环为 numRows*2-2
        if numRows==1:
            return s
        ans=[[] for _ in range(numRows)]
        loop=numRows*2-2
        for i in range(len(s)):
            check=i%loop
            
            if check//numRows==0:  
                ans[check].append(s[i])
            else:
                ans[-(check-numRows)-2].append(s[i])
            
        ans_str=''
        for col in ans:
             ans_str+=''.join(col)
             
        return ans_str