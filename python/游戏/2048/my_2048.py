

#! 养成写注释的习惯 左 和 右相似 左操作更简单因为是正向思维 写完左再在这个基础上写右   上和下 的操作和左右大体相似 同
#! 学会随机数生成 (比例 在空白处) 学会数字合并 学会数字移动 (必须先合并再移动) 判断矩阵是否有相邻的相同的元素！！！！！背下来 同时看看五子棋获胜条件 八皇后问题
import random

change=False

matrix=[[0 for j in range(4)]for i in range(4)]
score=0

def rannumber():
    global matrix
    rannumber=random.randint(1,10)   
    if(rannumber<=8):
        rannumber=2 #! 生成两种概率不同的数字的方法:
    else: 
        rannumber=4

    count=0
    for i in range(4):
      for j in range(4):
        if matrix[i][j]==0:#! 统计有没有0
          count+=1
          
    if count!=0:#! 如果有0 
        while True:
            ranplace=random.randint(0,15) 
            #! 在空白处生成随机数的方法
            #! 直到随机到矩阵某点不为0 再退出循环
            line=int(ranplace/4)
            row=ranplace%4
            
            if matrix[line][row]==0:
                matrix[line][row]=rannumber 
                break
            
            
def left():
    for i in range(4):
        for j in range(4):
            if matrix[i][j]==0:#! 对0什么都不用操作
                continue
            #todo 合并
            
            temp=1
            while j+temp<=3:#! 脚标合法性 
                if matrix[i][j+temp]!=matrix[i][j] and matrix[i][j+temp]!=0:#! 找到1个非0的不同元素就break
                    break
                elif matrix[i][j+temp]==matrix[i][j]:
                    matrix[i][j+temp]=0
                    matrix[i][j]*=2
                    global score
                    score+=1
                    break 
                temp+=1   
                
    for i in range(4):
        for j in range(4):
            #todo 向前调换 一次内层循环只能调一个数
            if j==0 or matrix[i][j]==0:#! 头元素不用调换 0也不用调换
                continue
            else:#! 模型 背下来
                aa=j#! 不能直接对j进行更改 所以用替罪羊
                while aa-1>=0 and matrix[i][aa-1]==0:#! 脚标合法性
                    matrix[i][aa-1],matrix[i][aa]=matrix[i][aa],matrix[i][aa-1]
                    aa-=1
                    global change
                    change=True
def right():
    for i in range(4):
        for j in range(3,-1,-1):
            if matrix[i][j]==0:#! 对0什么都不用操作
                continue
            #todo 合并
            
            temp=1
            while j-temp>=0:#! 脚标合法性 
                if matrix[i][j-temp]!=matrix[i][j] and matrix[i][j-temp]!=0:#! 找到1个非0的不同元素就break
                    break
                elif matrix[i][j-temp]==matrix[i][j]:
                    matrix[i][j-temp]=0
                    matrix[i][j]*=2
                    global score
                    score+=1
                    break 
                temp+=1 
    for i in range(4):
        for j in range(3,-1,-1):
            #todo 向前调换 一次内层循环只能调一个数
            if j==3 or matrix[i][j]==0:#! 头元素不用调换
                continue
            else:#! 模型 背下来
                aa=j#! 不能直接对j进行更改 所以用替罪羊
                while aa+1<=3 and matrix[i][aa+1]==0  :#! 脚标合法性 注意顺序！！！！ 脚标合法性判断必须放在and的前面!!!!
                    matrix[i][aa+1],matrix[i][aa]=matrix[i][aa],matrix[i][aa+1]
                    aa+=1
                    global change
                    change=True
                    
def up():
    for i in range(4):
        for j in range(4):
            if matrix[i][j]==0:#! 对0什么都不用操作
                continue
            #todo 合并
            
            temp=1
            while i+temp<=3:#! 脚标合法性 
                if matrix[i+temp][j]!=matrix[i][j] and matrix[i+temp][j]!=0:#! 找到1个非0的不同元素就break
                    break
                elif matrix[i+temp][j]==matrix[i][j]:
                    matrix[i+temp][j]=0
                    matrix[i][j]*=2
                    global score
                    score+=1
                    break 
                temp+=1   
    for i in range(4):
        for j in range(4):
            #todo 向前调换 一次内层循环只能调一个数
            if i==0 or matrix[i][j]==0:#! 头元素不用调换
                continue
            else:#! 模型 背下来
                aa=i#! 不能直接对j进行更改 所以用替罪羊
                while aa-1>=0 and matrix[aa-1][j]==0:#! 脚标合法性
                    matrix[aa-1][j],matrix[aa][j]=matrix[aa][j],matrix[aa-1][j]
                    aa-=1
                    global change
                    change=True

def down():
    for i in range(3,-1,-1):
        for j in range(4):
            if matrix[i][j]==0:#! 对0什么都不用操作
                continue
            #todo 合并
            
            temp=1
            while i-temp>=0:#! 脚标合法性 
                if matrix[i-temp][j]!=matrix[i][j] and matrix[i-temp][j]!=0:#! 找到1个非0的不同元素就break
                    break
                elif matrix[i-temp][j]==matrix[i][j]:
                    matrix[i-temp][j]=0
                    matrix[i][j]*=2
                    global score
                    score+=1
                    break 
                temp+=1   
    for i in range(3,-1,-1):
        for j in range(4):
            #todo 向前调换 一次内层循环只能调一个数
            if i==3 or matrix[i][j]==0:#! 头元素不用调换
                continue
            else:#! 模型 背下来
                aa=i#! 不能直接对j进行更改 所以用替罪羊
                while aa+1<=3 and matrix[aa+1][j]==0:#! 脚标合法性
                    matrix[aa+1][j],matrix[aa][j]=matrix[aa][j],matrix[aa+1][j]
                    aa+=1
                    global change
                    change=True
                    
def win():
    for row in matrix:
        if 2048 in row:
            return True
    return False


#! 注意到 下面的是错误的 没有0了 而且没有2048 而且没有相邻的相同的元素
def lose():
    
    for row in matrix:
        if 0 not in row and 2048 not in row:#! 矩阵满了(即没有0了) 但是还没有2048 就输了
            continue
        else:
            return False
        #! 下面判断有没有相邻的相同元素
        #!模型
    for i in range(4):
        for j in range(4):
            if j!=3:
                if matrix[i][j]==matrix[i][j+1]:
                    return False
            if i!=3:
                if matrix[i][j]==matrix[i+1][j]:
                    return False
    return True
                

def main():
    #! 在游戏开始之前先随机生成2个数
    
    rannumber()
    rannumber()
    while True:
        global change#! 每次循环需要更新flag
        change=False
        for i in matrix:
            print(i)
    
    
        if win():
            print("获胜","您的得分为:",score)
        
            break
    
        if lose():
            print("失败","您的得分为:",score)
            break
    
        print('您的得分为:',score)
    
        
        t=score#!记录一下之前的得分
        
        act=input()
        if act=='w':
            up()
        elif act=='a':
            left()
        elif act=='s':
            down()
        elif act=='d':
            right()
        
        
        #! 注意什么情况下生成随机数 1.有数字合并了 2.有数字发生了移动 只需要在移动那步操作里面加上一个bool类型变量即可 注意每次循环的初始化 老生常谈
        #! flag的妙用
        if change or score!=t:
            rannumber()
main()