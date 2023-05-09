

#!下一个全排列的另一个版本————上一个全排列
# class Solution:
#     def prevPermOpt1(self, arr: list[int]) -> list[int]:
#         if sorted(arr)==arr:
#             return arr
#         else:
#             for i in range(len(arr)-1,0,-1):
#                 if arr[i]>=arr[i-1]:
#                     continue
#                 else:
#                     minx=99999
#                     pos=-1
#                     #! 下面这个循环是为了找一个比目标小且尽可能大的数
#                     for k in range(i,len(arr)):
#                         if arr[i-1]>arr[k] and arr[i-1]-arr[k]<minx:#! 两个都不能带等号！！！！思考原因
#                             minx=arr[i-1]-arr[k]
#                             pos=k
# ! 遍历完成之后才能得到结论所以要在循环外面写 别写错位置   
#                     arr[i-1],arr[pos]=arr[pos],arr[i-1]
#                     arr[i:]=sorted(arr[i:],reverse=True)
#                     break#! 别忘了写break
#             return arr
# solution=Solution()
# print(solution.prevPermOpt1([1,9,4,6,7]))


#! leetcode上面这个只允许一次交换 要审题!!!!! 
# 给你一个正整数的数组 A（其中的元素不一定完全不同），请你返回可在 一次交换（交换两数字 A[i] 和 A[j] 的位置）后得到的、按字典序排列小于 A 的最大可能排列。

# 如果无法这么操作，就请返回原数组。


class Solution:
    def prevPermOpt1(self, arr: list[int]) -> list[int]:
        if sorted(arr)==arr:
            return arr
        else:
            for i in range(len(arr)-1,0,-1):
                if arr[i]>=arr[i-1]:
                    continue
                else:
                    minx=99999
                    pos=-1
                    #! 下面这个循环是为了找一个比目标小且尽可能大的数
                    
                    for k in range(i,len(arr)):
                        if arr[i-1]>arr[k] and arr[i-1]-arr[k]<minx:#! 两个都不能带等号！！！！思考原因
                            minx=arr[i-1]-arr[k]
                            pos=k
                    #! 注意写在哪里 循环内还是外 别忘了写break
                    arr[i-1],arr[pos]=arr[pos],arr[i-1]
                    break   
        return arr                
                        
                    
                    
solution=Solution()
print(solution.prevPermOpt1([1,9,4,6,7]))