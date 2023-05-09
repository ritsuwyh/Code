
# #! 这道题和八皇后问题联系起来看 如何取对角的元素
# n=eval(input())
# matrix=[]
# for i in range(n):
#     row=list(map(int,input().split()))
#     matrix.append(row)
# #! 不定二维数组 第二维度长度不定 我们需要确定最大的长度

# #* 要习惯使用 max() 写法1
# max_len=-1#! 找一个必然能更新的值
# for row in matrix:
#     max_len=max(max_len,len(row))
# #* 写法2
# # max_len=-1
# # for i in matrix:
# #     if len(i)>max_len:
# #         max_len=len(i)
# #* 写法3 
# #max_len=max([len(row) for row in matrix])

# #! 主对角线方向 i-j 副对角线方向i+j
# lst=[[]for _ in range(n+max_len-1)]#! 注意开的大小 注意到副对角线的条数为 
# for i in range(max_len):
#     for j in range(max_len):
#         if i <n and j<len(matrix[i]):#! 在原有矩阵内
#             lst[i+j].append(matrix[i][j])
# ans_lst=[]     
# for i in lst: #! 这里的i 是某个副对角线 (从右上到左下的顺序)
#     ans_lst+=i[::-1]#! 注意顺序 
# print(ans_lst)

#! 对角线遍历1
class Solution:
    def findDiagonalOrder(self, mat: list[list[int]]) -> list[int]:
        m=len(mat)
        n=len(mat[0])
        max_len=max(m,n)
        # ans=[ [] for _ in range(m+n-1) ] 
        # for i in range(max_len):
        #     for j in range(max_len):
        #         if i>=m or j>=n:
        #             continue
        #         ans[i+j].append(mat[i][j])

            
        # ansx=[]
        # for i in range(len(ans)):
        #     if i%2==0:
        #         #! 与II的区别
        #         ansx+=ans[i][::-1]
        #     else:
        #         ansx+=ans[i]
        # return ansx
        
        #todo 实现全沿着右上方向的副对角遍历
        
        # ans=[]      
        # cnt=0
        # while cnt<m+n-1:
        #     i=cnt
        #     j=0
        #     while i>=0:
        #         if i<m and j<n:
        #             ans.append(mat[i][j])
        #         j+=1
        #         i-=1
        #     cnt+=1
        # return ans
        #todo 按题干的意思
        ans=[]      
        cnt=0
        while cnt<m+n-1:
            if cnt%2==0:
                i=cnt
                j=0
                while i>=0:
                    if i<m and j<n:
                        ans.append(mat[i][j])
                    j+=1
                    i-=1
            else:
                j=cnt
                i=0
                while j>=0:
                    if i<m and j<n:
                        ans.append(mat[i][j])
                    j-=1
                    i+=1
            cnt+=1
        return ans
        
    
solution=Solution()
print(solution.findDiagonalOrder([[0,1],[1,2],[6,3],[12,14]]))
            


#!主对角线遍历

