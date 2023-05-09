class Solution:
    def isToeplitzMatrix(self, matrix: list[list[int]]):
        m=len(matrix)
        n=len(matrix[0])
        x0=m-1#! 起点
        cnt=0
        
        ans=[]
        while cnt<=m+n-1:#! 共有行数加列数减1条对角线
            i=x0
            
            j=0
            while i<=m-1:
                if i>=0 and j<=n-1:
                    ans.append(matrix[i][j])
                i+=1
                j+=1
            
            
            
            x0-=1
            cnt+=1
        return (ans)      
        
solution=Solution()
print(solution.isToeplitzMatrix([[1,2,3],[4,5,6],[7,8,9],[1,2,3],[11,12,13]]))