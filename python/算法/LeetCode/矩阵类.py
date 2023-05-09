
class Matrix:
    def __init__(self, value):
        self.mat=value

# 在此处填写代码

    def matprint(self):
        #! 直接for 循环打印里面的数
        #! 这里有两种输出方式
        #print(str(self.mat).replace("], ","\n").replace("[","").replace("]","").replace(",",""))#?  不是应该把逗号改为空格???
        for i in range(len(self.mat)):
            for j in range(len(self.mat[0])):
                if j==len(self.mat[0])-1:
                    print(self.mat[i][j],end='')
                else:
                    print(self.mat[i][j],end=' ')
            print()

# 在此处填写代码
#! 先要判断数据类型  而且注意矩阵加法需要同型 矩阵乘法需要第一个矩阵列数等于第二个矩阵的行数
    def add_(self, num_or_mat): #! 用type 函数来判断数据类型
        if type(num_or_mat)==int:
            for i in range(len(self.mat)):
                for j in range(len(self.mat[i])):
                    self.mat[i][j]+=num_or_mat
        elif type(num_or_mat)==Matrix:#! 可以判定是否和自定义类型相等
            if len(self.mat)==len(num_or_mat.mat) and len(self.mat[0])==len(num_or_mat.mat[0]):
                for i in range(len(self.mat)):
                    for j in range(len(self.mat[i])):
                        self.mat[i][j]+=num_or_mat.mat[i][j]

# 在此处填写代码
#! 详情见矩阵转置
    def transpose_(self):
        #self.mat=[[self.mat[i][j] for i in range(len(self.mat))] for j in range(len(self.mat[0]))]
        self.mat=list(zip(*self.mat))
        
        for i in range(len(self.mat)):
            self.mat[i]=list(self.mat[i])
# 在此处填写代码

#todo 矩阵乘法 背下来
    def matmul_(self, other_mat):#! 注意传入参数的类型 Matrix 还是 二维list
        if len(self.mat[0])==len(other_mat.mat): #! 第一个矩阵的列数等于第二个矩阵的行数
            tmp=[[0 for i in range(len(other_mat.mat[0]))] for j in range(len(self.mat))]
            for i in range(len(tmp)):
                for j in range(len(tmp[i])):
                    for k in range(len(self.mat[0])):
                        tmp[i][j]+=self.mat[i][k]*other_mat.mat[k][j]
            self.mat=tmp

# 在此处填写代码

while True:
    exec(input())