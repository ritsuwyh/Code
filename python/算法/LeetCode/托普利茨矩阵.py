
#我们没有必要像对角线遍历那样取出来所有的 而是只需要看相邻两项是否相同即可
#!法一
class Solution:
    def isToeplitzMatrix(self, matrix: list[list[int]]) -> bool:
        for i in range(len(matrix) - 1):
            if matrix[i][:-1] != matrix[i + 1][1:]:
                return False
        return True
    
#!法2 
class Solution:
    def isToeplitzMatrix(self,matrix):
        for i in range(len(matrix)-1):
            for j in range(len(matrix[0])-1):
                if matrix[i][j]!=matrix[i+1][j+1]:
                    return False
        return True


