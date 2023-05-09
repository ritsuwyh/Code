import pygame


dic={'1':'黑方','0':'Empty','2':'白方'}#! 用特征值！！！！！！！！！
#! 用字符0 1 2 为了简化int转为str
black=[0,0,0]
white=[255,255,255]

def set_background():
    pygame.display.set_caption('五子棋') # 改标题
    # pygame.display.set_mode()表示建立个窗口，左上角为坐标原点，往右为x正向，往下为y轴正向
    # global screen#! 注意使用全局变量
    screen = pygame.display.set_mode((640,640))
    # 给窗口填充颜色，颜色用三原色数字列表表示
    screen.fill([125,95,24])
    return screen
def draw_chess(x,y,color,board,screen):
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


def win_output(color,screen):
    f = pygame.font.Font('C:/Windows/Fonts/simhei.ttf',50)
    text = f.render('{}获胜'.format(dic[color]),True,(255,0,0))#! 最后一个参数是背景颜色 不填则为透明
    textRect =text.get_rect()
    textRect.center = (320,250)
    screen.blit(text,textRect)
    pygame.display.flip()
