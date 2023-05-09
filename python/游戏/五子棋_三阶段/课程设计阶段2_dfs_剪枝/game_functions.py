
import pygame
import sys


from settings import*
from board import Board


#! 博弈树节点
class Node():
    def __init__(self,posx,posy,score) -> None:
        self.posx=posx
        self.posy=posy
        self.score=score
        self.children=[]
        self.father=None
        self.alpha=None
        self.beta=None
        


def is_win(board,x,y,color):
    #todo 四个方向 暴力枚举 只需要枚举落点的四个方向即可 模板
    #! 横向
    cnt=1#! 先把自身算上 防止之后重复算自己
    i=1
    while i<5 and x-i>=0:#*左边
        if board.matrix[x-i][y]==color:
            cnt+=1
            i+=1
        else:
            break
    i=1
    while i<5 and x+i<15:#*右边
        if board.matrix[x+i][y]==color:
            cnt+=1
            i+=1
        else:
            break
    if cnt>=5:
        return True
    
    #! 纵向
    cnt=1
    j=1
    while j<5 and y-j>=0:#*上边
        if board.matrix[x][y-j]==color:
            cnt+=1
            j+=1
        else:
            break
    j=1
    while j<5 and y+j<15:#*下边
        if board.matrix[x][y+j]==color:
            cnt+=1
            j+=1
        else:
            break
    if cnt>=5:
        return True
    
    #! 主对角线
    cnt=1
    z=1
    while z<5 and x-z>=0 and y-z>=0:#* 左上
        if board.matrix[x-z][y-z]==color:
            cnt+=1
            z+=1
        else:
            break
    z=1
    while z<5 and x+z<15 and y+z<15:#* 右下
        if board.matrix[x+z][y+z]==color:
            cnt+=1
            z+=1
        else:
            break
    if cnt>=5:
        return True
    
    #! 副对角线
    cnt=1
    k=1
    while k<5 and x-k>=0 and y+k<15:#* 右上
        if board.matrix[x-k][y+k]==color:
            cnt+=1
            k+=1
        else:
            break
    k=1
    while k<5 and x+k<15 and y-k>=0:#* 左下
        if board.matrix[x+k][y-k]==color:
            cnt+=1
            k+=1
        else:
            break
    if cnt>=5:
        return True
    
    return False
        


def has_neighbor(x,y,board):#! 为了减少搜索代价 在旁边有棋子的地方下 
    #! 没办法 只能特判 一个个写
    if x==0 and y==0:
        if board.matrix[x+1][y]!='0' or board.matrix[x+1][y+1]!='0' or board.matrix[x][y+1]!='0':
            return True
        else:
            return False
    if x==0 and y==14:
        if board.matrix[x+1][y]!='0' or board.matrix[x+1][y-1]!='0' or board.matrix[x][y-1]!='0':
            return True
        else:
            return False
    if x==14 and y==0:
        if board.matrix[x-1][y]!='0' or board.matrix[x-1][y+1]!='0' or board.matrix[x][y+1]!='0':
            return True
        else:
            return False
    if x==14 and y==14:
        if board.matrix[x-1][y]!='0' or board.matrix[x-1][y-1]!='0' or board.matrix[x][y-1]!='0':
            return True
        else:
            return False
    if x==0:#! 第一行
        if board.matrix[x+1][y]!='0' or board.matrix[x][y+1]!='0' or board.matrix[x][y-1]!='0'  or board.matrix[x+1][y-1]!='0' or board.matrix[x+1][y+1]!='0':
            return True
        else:
            return False
        
    if x==14:#! 最后一行
        if board.matrix[x-1][y]!='0'  or board.matrix[x][y+1]!='0' or board.matrix[x][y-1]!='0' or board.matrix[x-1][y-1]!='0' or board.matrix[x-1][y+1]!='0':
            return True
        else:
            return False
        
    if y==0:#! 第一列
        if board.matrix[x-1][y]!='0' or board.matrix[x+1][y]!='0' or board.matrix[x][y+1]!='0'  or board.matrix[x-1][y+1]!='0' or board.matrix[x+1][y+1]!='0':
            return True
        else:
            return False
    
    if y==14:#! 最后一列
        if board.matrix[x-1][y]!='0' or board.matrix[x+1][y]!='0'  or board.matrix[x][y-1]!='0' or board.matrix[x-1][y-1]!='0' or board.matrix[x+1][y-1]!='0' :
            return True
        else:
            return False
    
    
    if board.matrix[x-1][y]!='0' or board.matrix[x+1][y]!='0' or board.matrix[x][y+1]!='0' or board.matrix[x][y-1]!='0' or board.matrix[x-1][y-1]!='0' or board.matrix[x-1][y+1]!='0' or board.matrix[x+1][y-1]!='0' or board.matrix[x+1][y+1]!='0':
        return True
    return False




def dfs(root:Node,step,target_step,board:Board):#! vscode 文件向右拆分 可以同时看两个
    print('loading')
    pygame.display.update()
    
    
    if step%2==1:
        color='1'
        score=float('-inf')#! 别忘了是从下往上赋值
        func=min
        
    else:
        color='2'
        score=float('inf')
        func=max
        
    if step==target_step+1:
        board_score=0
        for i in range(15):
            for j in range(15):
                if board.matrix[i][j]=='1' or( board.matrix[i][j]=='0' and has_neighbor(i,j,board)):
                    board_score-=cal_score(i,j,'1',board,sum_dict_black)
                elif board.matrix[i][j]=='2' or (board.matrix[i][j]=='0' and has_neighbor(i,j,board)):
                    board_score+=cal_score(i,j,'2',board,sum_dict_white)
        root.score=board_score#!board_score 分数越大 对白AI越有利 越小对黑人类越有利
        
        return 
                    
                 
    else:
        if step%2==1:#!根位于min层
            if root.alpha<=root.beta:
            # print('******************************************')
                return
        else:
            if root.alpha>=root.beta:
                # print('******************************************')
                return        
        for i in range(15):
            for j in range(15):
                if step%2==1:#!根位于min层
                    if root.alpha<=root.beta:
            # print('******************************************')
                        return
                else:
                    if root.alpha>=root.beta:
                # print('******************************************')
                        return        
                if board.matrix[i][j]=='0' and has_neighbor(i,j,board):
                    
                    temp=Node(i,j,score)
                    temp.father=root
                    
                    
                    temp.alpha=root.beta
                    temp.beta=root.alpha
                    
                    #root.children.append(temp)
                    board.matrix[i][j]=color#!模拟下棋
                    dfs(temp,step+1,target_step,board)
                    board.matrix[i][j]='0'#!还原
                  
                    root.score=func(temp.score,root.score)
                    
                    
                    
                    root.alpha=root.score
                    if root.father:#! father存在
                    
                    #! 需要一个判断限制条件
                        if (step-1)%2==1:#! 上一层是奇数层 即min层 我的层数是从0开始的
                            # if root.father.alpha<root.alpha:
                            #     root.father.alpha=root.alpha
                            root.father.alpha=min(root.father.alpha,root.alpha)
                            
                        else:
                            root.father.alpha=max(root.father.alpha,root.alpha)
                            
                    
                    if step==0:#! 只有这里才更新坐标
                       
                        if root.score==temp.score:
                            root.posx=temp.posx
                            root.posy=temp.posy
                    
                    del temp
                    
                    
        
    

def cal_score(x,y,color,board: Board, sum_dict):

    
    
    #todo四个方向棋形统计  掌握模型
    chess_look=[]
    
    temp1=[board.matrix[x][y]]
    temp2=[]
    i=1
    while i<5 and x-i>=0:#*左边
        if board.matrix[x-i][y]==color or board.matrix[x-i][y]=='0' :
            temp1.append(board.matrix[x-i][y])
            i+=1
        else:
            break
    i=1
    while i<5 and x+i<15:#*右边
        if board.matrix[x+i][y]==color or board.matrix[x+i][y]=='0' :
            temp2.append(board.matrix[x+i][y])
            i+=1
        else:
            break
    temp=temp1[::-1].copy()+temp2.copy()
    chess_look.append(''.join(temp.copy()))
    
    
    #! 纵向
    temp1=[board.matrix[x][y]]
    temp2=[]
    j=1
    while j<5 and y-j>=0:#*上边
        if board.matrix[x][y-j]==color or board.matrix[x][y-j]=='0':
            temp1.append(board.matrix[x][y-j])
            j+=1
        else:
            break
    j=1
    while j<5 and y+j<15:#*下边
        if board.matrix[x][y+j]==color or board.matrix[x][y+j]=='0':
            temp2.append(board.matrix[x][y+j])
            j+=1
        else:
            break
    temp=temp1[::-1].copy()+temp2.copy()
    chess_look.append(''.join(temp.copy()))
    
    #! 主对角线
    temp1=[board.matrix[x][y]]
    temp2=[]
    z=1
    while z<5 and x-z>=0 and y-z>=0:#* 左上
        if board.matrix[x-z][y-z]==color or board.matrix[x-z][y-z]=='0':
            temp1.append(board.matrix[x-z][y-z])
            z+=1
        else:
            break
    z=1
    while z<5 and x+z<15 and y+z<15:#* 右下
        if board.matrix[x+z][y+z]==color or board.matrix[x+z][y+z]=='0':
            temp2.append(board.matrix[x+z][y+z])
            z+=1
        else:
            break
    temp=temp1[::-1].copy()+temp2.copy()
    chess_look.append(''.join(temp.copy())) #! 别忘了用.join() 将list变成字符串
    
    
    #! 副对角线
    temp1=[board.matrix[x][y]]
    temp2=[]
    k=1
    #todo 整理笔记 先操作还是先加 要特别注意!!! 以及先对脚标进行合法性判断
    while k<5 and x-k>=0 and y+k<15:#* 右上
        if board.matrix[x-k][y+k]==color or board.matrix[x-k][y+k]=='0':
            temp1.append(board.matrix[x-k][y+k])#! 必须之后 k+=1 ！！！！！！ 注意是先操作再更改 还是先更改再操作
            k+=1
#! index out of range?
#! list index out of range 使用list索引之前 必须要注意是否为空 索引的合理性!!!!!
#             错误原因有二：
# 1、超出了list范围：
# 例如 list=（0,1，2），却在编程中使用了list【5】

# 2、list为空，在这种情况下使用list【0】便会报错
        else:
            break
    k=1
    while k<5 and x+k<15 and y-k>=0:#* 左下
        if board.matrix[x+k][y-k]==color or board.matrix[x+k][y-k]=='0':
            temp2.append(board.matrix[x+k][y-k])
            k+=1
        else:
            break
    temp=temp1[::-1].copy()+temp2.copy()
    chess_look.append(''.join(temp.copy()))
    
    
    score=0
    cnt=0
    #*print(chess_look) 测试用

    
    if color=='1':
        lst=lst1
    else:
        lst=lst2
        
    for mm in chess_look:
        for q in range(len(lst)):
            if lst[q] in mm:
                score+=sum_dict[lst[q]]
                break
        for p in range(len(special_lst)):
            if special_lst[p] in mm or para_special_lst[p] in mm:
                cnt+=1
                #! 会重复计算等级比较低的棋形 在设计评估函数的时候需要考虑到这一点
    
    #! 特殊棋型判断
    if cnt>1:
        if color=='1':
            score+=150000
        else:
            score+=150000
    #print(score)
    return score


def check_events(play_button): 

    for event in pygame.event.get(): 
        if event.type==pygame.QUIT:
            pygame.quit()
            sys.exit()
        elif event.type == pygame.MOUSEBUTTONDOWN:
            mouse_x, mouse_y = pygame.mouse.get_pos()
            return check_play_button(play_button, mouse_x, mouse_y) 

def check_play_button(play_button, mouse_x, mouse_y): 
    if play_button.rect.collidepoint(mouse_x, mouse_y): 
        return True
    else:
        return False