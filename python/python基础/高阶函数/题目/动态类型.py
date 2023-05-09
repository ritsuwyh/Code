
#! isinstance 和 函数返回值问题
# class A:
#     pass
# class B(A):
#     pass
# b=B()
# print(isinstance(b,A))#! 输出结果是True
# print(type(b)==type(A))#! 输出False
#* 记住 以后使用type 别用isinstance

class IntValue:
    def __init__(self,x):
        self.x=x
    def add(self,y):
        return (self.x +y)

class Matrix:
    def __init__(self,x):
        self.x=x
    def add(self,y):
        n=len(self.x)
        m=len(self.x[0])
        
        new_matirx=[[0 for j in range(m)] for i in range(n)]
        for i in range(n):
            for j in range(m):
                new_matirx[i][j]=self.x[i][j]+y[i][j]
        return (new_matirx)

#! 学会使用isinstance
def adder(element_type, value_to_add):#! 注意题干给的不是字符串 所以只能用isinstance函数
    # if element_type=='intvalue':
    #     pass
    # if element_type=='matrix':
    #     pass
    if isinstance(element_type,IntValue):
        return element_type.add(value_to_add)
        
    if isinstance(element_type,Matrix):
        return element_type.add(value_to_add)
         
    pass


while True:
    exec(input())

# 样例输入：
matrix = Matrix([[1,2],[3,4]])
print(adder(matrix, [[3,3],[4,2]]))#! 要注意返回值!! 由于print才输出 所以adder函数应该有返回值
#! 而add函数也应该是有返回值 而不是直接输出
exit()

# 样例输出：
# [[4, 5], [7, 6]]