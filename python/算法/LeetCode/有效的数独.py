
#! 请见 dfs_解数独 有更简单的方法

#! 考察如何取二维数组的 行.列 最大值 统计 行 列 某数字出现的次数 将9*9的矩阵分割成9个3*3的小矩阵
matrix=[]
for i in range(9):
    row=input().split()#! 有'.' 无法使用函数int
    matrix.append(row)
trans_matrix=list(zip(*matrix))

flag=True
#! 取矩阵的列向量可以先求转置再求行向量
for i in matrix:
    for num in range(1,10):
        num=str(num)#! 记得变成字符串
        if i.count(num)!=0 and i.count(num)!=1:
            flag=False
for i in trans_matrix:
    for num in range(1,10):
        num=str(num)
        if i.count(num)!=0 and i.count(num)!=1:
            flag=False
#! 第一个思路 矩阵分割
divided_matrix=[[[],[],[]],[[],[],[]],[[],[],[]]]#!必须要用三维数组


#! 第二个思路 block[i // 3][j // 3][digit] = True 前两个维度确定是哪个3*3矩阵  line[i][digit]  row[i][digit] 也是同理 
#todo 妙啊

for i in range(9):
    for j in range(9):
        divided_matrix[i//3][j//3].append(matrix[i][j])
        
for q in divided_matrix:
    for w in q:
        for num in range(1,10):
            num=str(num)
            if w.count(num)!=0 and w.count(num)!=1:
                flag=False
if flag:
    print(True)
else:
    print(False)
    
# matrix=[[1,2,3],[4,5,6],[7,8,9]]
# print(matrix.count(1)) #! 输出为0
# 5 3 . . 7 . . . .
# 6 . . 1 9 5 . . .
# . 9 8 . . . . 6 .
# 8 . . . 6 . . . 3
# 4 . . 8 . 3 . . 1
# 7 . . . 2 . . . 6
# . 6 . . . . 2 8 .
# . . . 4 1 9 . . 5
# . . . . 8 . . 7 9


