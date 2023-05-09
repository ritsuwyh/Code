import pygame
from settings import*
from board import Board

def set_background():
    pygame.display.set_caption('五子棋') # 改标题
    # pygame.display.set_mode()表示建立个窗口，左上角为坐标原点，往右为x正向，往下为y轴正向
    # global screen#! 注意使用全局变量
    screen = pygame.display.set_mode((800,640))#! 窗口大小
    # 给窗口填充颜色，颜色用三原色数字列表表示
    screen.fill([125,95,24])
    return screen
def draw_chess(x,y,color,board:Board,screen:pygame.Surface,pos_cnt:int):
    
    if x==15 and y==15:
        pos=[(x+2)*40,50]
        color_to_print=black if color=='1' else white
        pygame.draw.circle(screen,color_to_print,pos,25,0)#! screen 必须使用全局变量
        return
    if x<0 or x>14 or y<0 or y>14:
        print('illegal')
        return False
    elif board.matrix[x][y]!='0':
        print('illegal')
        return False
    else:
        
        pos=[(x+1)*40,(y+1)*40]
        color_to_print=black if color=='1' else white  #!整理笔记 学会使用特征值！！！！ 学会使用三目运算符
        if color=='1':
            my_RGB=[255,0,0]
        else:
            my_RGB=[0,0,255]
            
        
        
         
        pygame.draw.circle(screen,color_to_print,pos,18,0)#! screen 必须使用全局变量
        pygame.display.update()
        
        
        f = pygame.font.SysFont('宋体',30,True)
        
        surface1 = f.render("%s"%str(pos_cnt), True,my_RGB)
        screen.blit(surface1,pos)
        board.matrix[x][y]=color
        fclock = pygame.time.Clock()   #* creat a object to track time(控制时间) *
        fps = 40
        fclock.tick(fps)  #* 控制每次屏幕刷新的时间间隔，每次屏幕刷新后都引用此方法 （This method should be called once per frame. It will compute how many milliseconds have passed since the previous call.）*
        pygame.display.update()
        return True


def win_output(color,screen):
    f = pygame.font.Font('C:/Windows/Fonts/simhei.ttf',50)
    text = f.render('{}获胜'.format(dic[color]),True,(255,0,0))#! 最后一个参数是背景颜色 不填则为透明
    textRect =text.get_rect()
    textRect.center = (320,250)
    screen.blit(text,textRect)
    pygame.display.flip()
