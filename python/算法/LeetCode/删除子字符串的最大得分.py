
# #! 最优问题先尝试贪心算法   这种擦除问题比如括号匹配之类的 使用栈



# class Solution:
#     def maximumGain(self, s: str, x: int, y: int) -> int:
#         '''ab x分  ba y分'''
#         if x>=y:
    
#             priority_substr='ab'
#             priority_score=x
#             other='ba'
#             other_score=y
            
#         else:
#             priority_substr='ba'
#             priority_score=y
#             other='ab'
#             other_score=x      
              
#         score=0
#         stk=[]
#         for i in range(len(s)):
#             stk.append(s[i])
#             if len(stk)>=2 and stk[-2]+stk[-1]==priority_substr:
#                 stk=stk[:len(stk)-2]
#                 score+=priority_score
                
#         temp=''.join(stk)
#         stk2=[]
#         for i in range(len(temp)):
#             stk2.append(temp[i])
#             if len(stk2)>=2 and stk2[-2]+stk2[-1]==other:
#                 stk2=stk2[:len(stk2)-2]
#                 score+=other_score    
#         return score           
                
class Solution:
    def maximumGain(self, s: str, x: int, y: int) -> int:
        #! 除了a,b 剩余的字符权当做分隔符号
        #! 注意这种遇到特殊情况才计算的退出循环后要判断一下
        #! 注意边界 因为我们遇到分隔符才计算低分的情况 如果根本没有分隔符呢  所以我们在最后面人为加上一个分隔符 
        s=s+'#'
        score=0
        cnt_a=0
        cnt_b=0
        if x>=y:
            for i in range(len(s)):
                if s[i]=='b':
                    if cnt_a>=1:
                        cnt_a-=1
                        score+=x
                    else:
                        cnt_b+=1
                elif s[i]=='a':
                    cnt_a+=1
                else:#!遇到了分隔符
                    score+=min(cnt_a,cnt_b)*y
                    cnt_a=cnt_b=0#! 别忘了归0
        
        else:
            for i in range(len(s)):
                if s[i]=='a':
                    if cnt_b>=1:
                        cnt_b-=1
                        score+=y
                    else:
                        cnt_a+=1
                elif s[i]=='b':
                    cnt_b+=1
                else:#!遇到了分隔符
                    score+=min(cnt_a,cnt_b)*x
                    cnt_a=cnt_b=0
        return score
        