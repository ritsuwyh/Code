


matrix=[[1,2,3],[2,3,4]]

new_matrix=list(zip(*matrix))
#! 必须要注意到 用zip矩阵转置 得到的每个元素都是tuple型 需要list进行转换
#! 而且还要特别注意转换格式
# for row in new_matrix:  
#     row=list(row)
#! 上面这样写并不会更改matrix的值
for i in range(len(new_matrix)):
    new_matrix[i]=list(new_matrix[i])
print(str(matrix))

        #! 直接for 循环打印里面的数
#!print(str(self.mat).replace("], ","\n").replace("[","").replace("]","").replace(",",""))#?  不是应该把逗号改为空格???
#! 上面是输出格式1 转换成字符串 注意str(matrix) 之后 他会自动在每一个元素后面加一个空格

#! 还有一种就是单纯的输出元素
for i in range(len(new_matrix)):
    for j in range(len(new_matrix[0])):
        print(new_matrix[i][j],end=' ')
    print()

