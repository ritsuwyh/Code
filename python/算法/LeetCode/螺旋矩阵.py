
matrix=[[1,2],[4,5],[7,8]]

matrixa=list(zip(*matrix))#! 求矩阵转置的好方法 *matrix 是把matrix里面的元素(list类型)变成可变参数传进去
#! 等价于zip([1,2,3],[4,5,6],[7,8,9]) 然后1 4 7, 2 5 8, 3 6 9 成了三对tuple 
print(matrixa)

matrix1=matrix[::-1]#! 第i行变成倒数第i行
print(matrix1)

matrix2=[row[::-1] for row in matrix ] #! 第i列变成倒数第i列
print(matrix2)

matrix3=list(zip(*matrix))[::-1]#! 逆时针旋转 90
print(matrix3)

matrix4=list(zip(*matrix))#! 顺时针旋转 90
matrix4=[row[::-1] for row in matrix4]
print(matrix4)
#! 矩阵螺旋输出
def spiralOrder(matrix):
        res = []
        while matrix:#! 当矩阵不为空
            # 削头（第一层）
            res += matrix.pop(0)#! 注意pop的返回值
            # 将剩下的逆时针转九十度，等待下次被削
            matrix = list(zip(*matrix))[::-1]
        return res