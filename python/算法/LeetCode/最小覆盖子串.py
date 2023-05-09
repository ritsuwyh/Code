#todo 76                
#!https://wenku.baidu.com/view/5f737608ee630b1c59eef8c75fbfc77da26997ef.html
#todo counter的用法


class Solution:
    def minWindow(self, s: str, t: str) -> str:
        from collections import defaultdict
        need=defaultdict(int) #!所有key所对应的value全都都初始化为0
        for c in t:
            need[c]+=1#! need[c]>0 说明需要  ==0说明恰好 <0说明多余了
            #*这个need是关键
        needCnt=len(t)#! 用来判断 s 是否已经覆盖了 t 
        
        i=0#! 实际上是一个左指针 表示从哪里开始选的
        res=(0,float('inf'))#! 注意这里 float('inf')代表正无穷 float('-inf')代表负无穷
        
        for j,c in enumerate(s):# j是索引 c是元素
            if need[c]>0:
                needCnt-=1#! 选了我们需要的字符 所以 还要选择的字符数量减1
            need[c]-=1#! 这一步的意思是选了这个字符
            if needCnt==0:       #步骤一：滑动窗口包含了所有T元素
                while True:      #步骤二：增加i，排除多余元素
                    c=s[i] 
                    if need[c]==0:#! 说明c必然不能再排除了
                        break
                    need[c]+=1#! 这一步的意思是排除这个字符
                    i+=1
                if j-i<res[1]-res[0]:   #记录结果
                    res=(i,j)
                    
                need[s[i]]+=1  #步骤三：i增加一个位置，寻找新的满足条件滑动窗口
                needCnt+=1
                i+=1
        return '' if res[1]>len(s) else s[res[0]:res[1]+1]    #如果res始终没被更新过，代表无满足条件的结果