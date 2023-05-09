import pygame

#! 物理棋盘 数学建模矩阵
black=[0,0,0]
white=[255,255,255]
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
        