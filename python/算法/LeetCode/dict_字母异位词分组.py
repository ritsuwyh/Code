
# #! 超时
from collections import defaultdict


# class Solution:
#     def groupAnagrams(self, strs):
#         ans_lst=[]
        
#         vis=[False for i in range(len(strs))]
#         for i in range(len(strs)):
        
#             if vis[i]:
#                 continue
#             xx=[]
#             str_lst=sorted(list(strs[i]))
#             for j in range(len(strs)):
#                 temp=sorted(list(strs[j]))
#                 if temp==str_lst:
#                     vis[j]=True
#                     xx.append(strs[j]) 
#             ans_lst.append(xx)                
#         return ans_lst

#! python里面的dict 是一个哈希表 速度比list要快很多 dict的key必须是不可变对象 当超时的时候想想能不能用dict代替list 这种映射关系
class Solution:
    def groupAnagrams(self, strs):
        dic=defaultdict (list) #! 使每个key对应的value值是一个[]  
        for s in strs:
            temp=''.join(sorted(list(s)))#! 注意.join 的用法
            dic[temp].append(s)#! 这一步就避免了二重循环
            
        return list(dic.values())