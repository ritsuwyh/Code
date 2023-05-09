import pygame
import sys

#todo 需要改进的 获胜之后还下棋 获胜之后问是否重新开始 开始按钮 提示谁出棋 选择模式 写一些语言

#! 物理棋盘 数学建模矩阵
#todo 1黑 0空 2白 -1黑 1白
dic={'1':'黑方','0':'Empty','2':'白方'}#! 用特征值！！！！！！！！！
#! 用字符0 1 2 为了简化int转为str
black=[0,0,0]
white=[255,255,255]

game_active=True #! 游戏状态 目的是防止有一方获胜之后可以继续下棋


#! 黑棋的评估值要大一点 因为黑色先手  对称的也要写
#.活4（有两个位置可以形成连5） 冲4（有一个位置可以形成连5）活3（走一步可以形成活4）.眠3（走一步可以形成冲4）活2（走一步可以形成活3）：形状自行脑补
#眠2（走一步可以形成眠3）
#活1（走一步可以形成活2）

# #! 这个参数特别重要！！！
# 规则一：己方棋型权重为正，对方棋型权重为负，且相同棋型时，对方权重的绝对值要大于己方(可以设置为2倍或者3倍关系)。这是因为要考虑到进攻和防守，现在是己方(ai白子)下，例如：如果己方走了一步棋形成了活2，而对方已经有一个活2，那么显然是对方占优一些，因为下一步是对方走，对方是可以形成更高等级的活3的，所以己方活2就没有对方活2等级高。

# 规则2：等级：连5>活4>冲4=活3>眠3=活2>眠2=活1，相邻等级的权重设置为相差20倍（也可以30，40倍）。这是因为会重复计算等级比较低的棋型，为了不影响总体判断，比如一开始放一个子，活1的权重会计算16次，我设置为20倍，那么活2的权重刚好比16倍活1还要大一些。

# 规则3：对方连5、对方活4、对方冲4、对方活3的绝对值要设置大一点，这一点非常重要！！如果此时对方已经连五，说明己方已经输了。如果此时对方有活4和冲4，那么如果己方没有连5的话，己方必须要去阻止对方的活4和冲4。像这样可以分析出其他棋型权重。

#! 评估函数!!!!
# dicx={'11111':10000000,'22222':1000000,\
#     '011110':100000,'022220':50000,'0110110':100000,'0220220':50000,'0101110':100000,'0111010':100000,'0202220':50000,'0222020':50000,\
#     '11110':100000,'01111':100000,'22220':400,'02222':400,'11101':100000,'10111':100000,'22202':400,'20222':400,'11011':100000,'22022':400,\
#     '011100':8000,'022200':400,'001110':8000,'002220':400,'011010':8000,'022020':400,'010110':8000,'020220':400,\
#     '11100':50,'22200':20,'00111':50,'00222':20,'11010':50,'22020':20,'01011':50,'02022':20,'10011':50,'20022':20,'11001':50,'22002':20,'10101':50,'20202':20,\
#     '001100':50,'002200':20,'010100':50,'020200':20,'001010':50,'002020':20,'011000':50,'022000':20,'000110':50,'000220':20,'010010':50,'020020':20,\
#     '11000':3,'22000':1,'00011':3,'00022':1,'10100':3,'20200':1,'00101':3,'00202':1,'01100':3,'02200':1,'00110':3,'00220':1,'10010':3,'20020':1,'01001':3,'02002':1,'10001':3,'20002':1,\
#     '00100':3,'00200':1}
dicx={'11111':10000000,'22222':100000000,\
    '011110':500000,'022220':1000000\
    #! 下面这一行其实就是强势的活3
    ,'0110110':50000,'0220220':80000,'0101110':50000,'0111010':50000,'0202220':80000,'0222020':80000,\
    '11110':4000,'01111':4000,'22220':80000,'02222':80000,'11101':4000,'10111':4000,'22202':80000,'20222':80000,'11011':4000,'22022':80000,\
    '011100':50000,'022200':100000,'001110':50000,'002220':100000,'011010':50000,'022020':100000,'010110':50000,'020220':100000,\
    '11100':20,'22200':50,'00111':20,'00222':50,'11010':20,'22020':50,'01011':20,'02022':50,'10011':20,'20022':50,'11001':20,'22002':50,'10101':20,'20202':50,\
    '001100':20,'002200':50,'010100':20,'020200':50,'001010':20,'002020':50,'011000':20,'022000':50,'000110':20,'000220':50,'010010':20,'020020':50,\
    '11000':1,'22000':3,'00011':1,'00022':3,'10100':1,'20200':3,'00101':1,'00202':3,'01100':1,'02200':3,'00110':1,'00220':3,'10010':1,'20020':3,'01001':1,'02002':3,'10001':1,'20002':3,\
    '00100':1,'00200':3}#! 白方权重更大 进攻
special_dict={ '011100':8000,'022200':400,'001110':8000,'002220':400,'011010':8000,'022020':400,'010110':8000,'020220':400}
special_lst=list(special_dict.keys())
lst=sorted(list(dicx.keys()),key=lambda x:dicx[x],reverse=True)



class Board(object):
 
    def __init__(self):
        self.matrix=[['0' for j in range(15)] for i in range(15)]
        
        
    def reset_matrix(self):
        self.matrix=[['0' for j in range(15)] for i in range(15)]
    
    
    def draw_board(self,screen):
        #画棋盘
        for h in range(1,16):
            pygame.draw.line(screen,black,[40,h*40],[600,h*40],1)
            pygame.draw.line(screen,black,[h*40,40],[h*40,600],1)
        
        # 给棋盘加一个外框，使美观
        pygame.draw.rect(screen, black, [36, 36, 568, 568], 3)
        # 在棋盘上标出，天元以及另外4个特殊点位
        pygame.draw.circle(screen, black, [320, 320], 7, 0)
        pygame.draw.circle(screen, black, [160, 160], 5, 0)
        pygame.draw.circle(screen, black, [160, 480], 5, 0)
        pygame.draw.circle(screen, black, [480, 160], 5, 0)
        pygame.draw.circle(screen, black, [480, 480], 5, 0)
        
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
        
def draw_chess(x,y,color,board):
    if x<0 or x>14 or y<0 or y>14:
        print('illegal')
        return False
    elif board.matrix[x][y]!='0':
        print('illegal')
        return False
    else:
        pos=[(x+1)*40,(y+1)*40]
        color_to_print=black if color=='1' else white  #!整理笔记 学会使用特征值！！！！ 学会使用三目运算符
        pygame.draw.circle(screen,color_to_print,pos,18,0)#! screen 必须使用全局变量
        board.matrix[x][y]=color
        return True

def set_background():
    pygame.display.set_caption('五子棋') # 改标题
    # pygame.display.set_mode()表示建立个窗口，左上角为坐标原点，往右为x正向，往下为y轴正向
    global screen#! 注意使用全局变量
    screen = pygame.display.set_mode((640,640))
    # 给窗口填充颜色，颜色用三原色数字列表表示
    screen.fill([125,95,24])

def win_output(color):
    f = pygame.font.Font('C:/Windows/Fonts/simhei.ttf',50)
    text = f.render('{}获胜'.format(dic[color]),True,(255,0,0))#! 最后一个参数是背景颜色 不填则为透明
    textRect =text.get_rect()
    textRect.center = (320,320)
    screen.blit(text,textRect)
    pygame.display.flip()
    global game_active
    game_active=False


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

    



def find_pos(board):
    max_score=-1000
    posx,posy=0,0
    for i in range(0,15):
        for j in range(0,15):
            if has_neighbor(i,j,board) and board.matrix[i][j]=='0':
                score=cal_score(i,j,'1',board)+cal_score(i,j,'2',board)#! 可攻可守
                
                #!score=cal_score(i,j,'1',board)#! 只守
                #!score=cal_score(i,j,'2',board)#! 只攻
                #*print(score) 测试用
                if score>max_score:
                    max_score=score
                    posx=i
                    posy=j
    return posx,posy



def cal_score(x,y,color,board):
    board.matrix[x][y]=color#! 先放上棋子
    
    
    #todo四个方向棋形统计  掌握模型
    chess_look=[]
    
    temp1=[color]
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
    for mm in chess_look:
        for kk in lst:#! 注意我们需要按等级排序 从分高到分低检索棋形
            if kk in mm:
                score+=dicx[kk]
        for zz in special_lst:
            if zz in mm:
                cnt+=1
                #! 会重复计算等级比较低的棋形 在设计评估函数的时候需要考虑到这一点
    board.matrix[x][y]='0'#! 拿走棋子 恢复原样
    #! 特殊棋型判断
    if cnt>1:
        if color=='1':
            score+=150000
        else:
            score+=100000
    return score

def main():
    pygame.init()
    board=Board()
    set_background()
    board.draw_board(screen)
    pygame.display.flip()#刷新窗口
    xx=True
    times=1
    color='1'#! 默认黑方先手
    
    print('人机先手：1, 玩家先手：2')
    number=eval(input())
    global game_active
    if number==1:
        
    #! 游戏主循环
        while True:
            for event in pygame.event.get():
                if event.type==pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                    
                elif event.type==pygame.MOUSEBUTTONDOWN and game_active and xx==False:
                    x_board,y_board=pygame.mouse.get_pos()
                    x=round((x_board-40)/40)
                    y=round((y_board-40)/40)
                    if draw_chess(x,y,color,board):
                        #print(has_neighbor(x,y,board))
                        if is_win(board,x,y,color):
                            win_output(color)
                        color='1'
                        print('出棋方:{}'.format(dic[color]))
                        #! 每次绘制图形之后都要进行下面这句
                        pygame.display.flip()
                        xx=True
                        
                elif xx==True:  
                        #! 下面是AI的操作
                        #todo 求x,y
                        if times==1:
                            x,y=7,7
                            draw_chess(x,y,color,board)
                            times+=1
                            pygame.display.flip()
                            color='2'
                            xx=False                        
                        else:
                            x,y=find_pos(board)
                            draw_chess(x,y,color,board)
                        
                            if is_win(board,x,y,color):
                                win_output(color)
                            pygame.display.flip()
                            color='2'
                            xx=False
    else:
        while True:
            for event in pygame.event.get():
                if event.type==pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                elif event.type==pygame.MOUSEBUTTONDOWN and game_active:
                    x_board,y_board=pygame.mouse.get_pos()
                    x=round((x_board-40)/40)
                    y=round((y_board-40)/40)
                    if draw_chess(x,y,color,board,screen):
                        #print(has_neighbor(x,y,board))
                        if is_win(board,x,y,color):
                            win_output(color,screen)
                            AI_move=False
                            game_active=False
                        if AI_move:
                            color='2'
                        
                            #! 每次绘制图形之后都要进行下面这句
                            pygame.display.flip()
                        
                        
                            #! 下面是AI的操作
                            #todo 求x,y
                            x,y=find_pos(board)
                            draw_chess(x,y,color,board,screen)
                        
                            if is_win(board,x,y,color):
                                win_output(color,screen)
                                game_active=False
                            pygame.display.flip()
                            color='1'
                elif game_active==False:
                    # play_button=Button(screen,'Replay')
                    # play_button.draw_button()
                    pygame.display.flip()
                    # while not check_events(play_button):
                    #     continue
                    game_active=True
                    screen.fill([125,95,24])
                    board.draw_board(screen)
                    pygame.display.flip()#刷新窗口
                    board.reset_matrix()        
                    
main()
