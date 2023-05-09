

#! 第一个方法是 从给一个字符串进行编码的角度来看 先变成list(有两种方式 具体情况具体分析) 然后去重 然后编码
# class Solution:
#     def wordPattern(self, pattern: str, s: str) -> bool:
#         #! 首先去重 pattern 和 s 都去重 
#         pattern=list(pattern)
#         s=s.split()#! 与s=list(s)区分
#         lst1=[]
#         lst2=[]
#         #* 注意 有一些情况可以直接排除掉 这样可以避免进行边界判断
#         #! 长度不一样 排除
#         if len(pattern)!=len(s):
#             return False
        
#         for x in pattern:
#             if x not in lst1:
#                 lst1.append(x)
                
#         for y in s:
#             if y not in lst2:
#                 lst2.append(y)
#         #! 种类数不一样 排除
#         if len(lst1)!=len(lst2):
#             return False
#         dic=dict(zip(lst1,lst2))
        
#         #! 至此我们已经把每个不同的单词全都编上了号码
#         for i in range(len(pattern)):
#             if dic[pattern[i]]!=s[i]:
#                 return False
        
#         return True
#todo 方法2 遍历
class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:
        s=s.split()
        #! 长度特判
        if len(pattern)!=len(s):
            return False
        
        dic={}
        for i in range(len(s)):
            if s[i] not in dic.keys() :#! 这个单词没被编过 
                #! 如果所用编号已经用于其他的单词身上
                if pattern[i] in dic.values():
                    return False
                else:
                    dic[s[i]]=pattern[i]
            else:
                if dic[s[i]]!=pattern[i]:
                    return False
        return True