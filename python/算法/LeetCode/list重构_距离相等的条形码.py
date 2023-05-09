

#!请你重新排列这些条形码，使其中任意两个相邻的条形码不能相等。 你可以返回任何满足该要求的答案，此题保证存在答案。
#! 我是垃圾 下面写的是错的 因为 1112222 必须把1插到2里面 
# class Solution:
#     def rearrangeBarcodes(self, barcodes: list[int]) -> list[int]:
#         stack=[]
#         vis=[False for i in range(len(barcodes))]
#         for i,x in enumerate(barcodes):
#             if vis[i]:
#                 continue
#             else:
#                 if len(stack)==0:
#                     stack.append(x)
#                 elif x==stack[-1]:
#                     temp=i
#                     while barcodes[temp]==stack[-1] or vis[temp]:
#                         temp+=1
#                     vis[temp]=True
#                     stack.append(barcodes[temp])
#                     stack.append(x)
#                 else:
#                     stack.append(x)
#         return stack
#! 我们需要进行排序  
#! 这不就是高中的排列组合思想吗？？？  同种元素不相邻问题 
#!求出哪个数字出现的次数最多 然后把其隔位填入lst 中间空的位置再用别的元素来填充
#todo 背下来 注意到本题已经明确说明了一定有解
class Solution:
    def rearrangeBarcodes(self, barcodes: list[int]) -> list[int]:
        #! 下面这句话非常重要
        #! 按出现的次数进行排序 而且还要注意当次数相同时 按数字大小进行比较!!!!!!!!!!!!!!!!!!!!!
        lstx=barcodes.copy()
        barcodes.sort(key=lambda x: (lstx.count(x),x),reverse=True)
# barcodes=[1,2,1]
# barcodes.sort(key=lambda x: barcodes.count(x),reverse=True)#! 这样写是不会改变barcodes 的顺序的 python的限制 
#! 我们需要用一个 lstx=barcodes.copy()    barcodes.sort(key=lambda x: lstx.count(x),reverse=True) 这样才可以
# print(barcodes)
        j = 0    
        n=len(barcodes)
        ans=[0 for _ in range(n)]
        for i in range(0, n, 2):#! 放奇数位 
            ans[i] = barcodes[j]
            j += 1
        for i in range(1, n, 2):#! 放偶数位
            ans[i] = barcodes[j]
            j += 1
        return ans

solution=Solution()
print(solution.rearrangeBarcodes([7,7,7,8,5,7,5,5,5,8]))

#! 如果程序运行超时那么久长时使用dictionary
