import pygame
import sys

#! 物理棋盘 数学建模矩阵
#todo -1黑 0空 1白
dic={-1:'黑方',0:'Empty',1:'白方'}#! 用特征值！！！！！！！！！
black=[0,0,0]
white=[255,255,255]

class Board(object):
 
    def __init__(self):
        self.matrix=[[0 for j in range(15)] for i in range(15)]
        
        
    def reset_matrix(self):
        self.matrix=[[0 for j in range(15)] for i in range(15)]
    
    
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
    elif board.matrix[x][y]!=0:
        print('illegal')
        return False
    else:
        pos=[(x+1)*40,(y+1)*40]
        color_to_print=black if color==-1 else white  #!整理笔记 学会使用特征值！！！！ 学会使用三目运算符
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



def main():
    pygame.init()
    board=Board()
    set_background()
    board.draw_board(screen)
    pygame.display.flip()#刷新窗口
    
    color=(-1)#! 默认黑方先手
    
    #play_button=Button(screen,'Start')
    
    game_active=True #! 游戏状态 目的是防止有一方获胜之后可以继续下棋
    
    #! 游戏主循环
    while True:
        for event in pygame.event.get():
            if event.type==pygame.QUIT:
                pygame.quit()
                sys.exit()
            elif event.type==pygame.MOUSEBUTTONDOWN and game_active:
                x_board,y_board=pygame.mouse.get_pos()
                x=round((x_board-40)/40)
                y=round((y_board-40)/40)
                if draw_chess(x,y,color,board):
                    
                    if is_win(board,x,y,color):
                        f = pygame.font.Font('C:/Windows/Fonts/Arial.ttf',50)
                        text = f.render('{}获胜'.format(dic[color]),True,(255,0,0))#! 最后一个参数是背景颜色 不填则为透明
                        textRect =text.get_rect()
                        textRect.center = (320,320)
                        screen.blit(text,textRect)
                        pygame.display.flip()
                        game_active=False
                        # pygame.quit()
                        # sys.exit()
                        
                
                    color*=-1      #! 黑白棋出招顺序的实现
                    print('出棋方:{}'.format(dic[color]))
                    #! 每次绘制图形之后都要进行下面这句
                    pygame.display.flip()
                    
main()
