class Solution:
    def countAndSay(self, n: int) -> str:
        from collections import OrderedDict
        #! 尝试使用递归函数 像这种递推关系的 递归函数也可以从前向后推
        def func(step,n,s='1'):
            if step==n:
                return s
            else:
                # dic=OrderedDict()
                # for x in s:
                #     dic[x]=dic.get(x,0)+1
                # temp=''  
                # for i,j in dic.items():
                #     temp=temp+str(j)+i
                temp=''
                cnt=1
                for i in range(1,len(s)):
                    if s[i]==s[i-1]:
                        cnt+=1
                    else:
                        temp=temp+str(cnt)+s[i-1]
                        cnt=1
                #! 别忘了最后还要更新一下
                temp=temp+str(cnt)+s[-1]
                return func(step+1,n,temp)
        
        return func(1,n) 