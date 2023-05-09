import pygame
import sys
import numpy as np
from graphical_interface import*
from game_functions import*
from board import Board
from button import Button
#todo 需要改进的 获胜之后问是否重新开始 开始按钮 提示谁出棋 选择模式 写一些语言

 #! 游戏状态 目的是防止有一方获胜之后可以继续下棋

def main():
    #! 初始化
    pygame.init()
    board=Board()
    screen=set_background()
    board.draw_board(screen)
    pygame.display.flip()#刷新窗口
    color='1'#! 默认黑方先手
    AI_move=True
    game_active=False
    
    play_button=Button(screen,'Play')
    play_button.draw_button()
    pygame.display.flip()
    while not check_events(play_button):
        continue
    game_active=True
    screen.fill([125,95,24])
    board.draw_board(screen)
    pygame.display.flip()#刷新窗口
    pos_cnt_black=1
    pos_cnt_white=1
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
                if x>14 or y>14:
                    print('flip')
                    continue
                
                
                if draw_chess(x,y,color,board,screen,pos_cnt_black):
                    pos_cnt_black+=1
                    pygame.display.flip()
                    
                    #! 用图形指示下一个落子的是谁
                    draw_chess(15,15,'2',board,screen,0)
                    pygame.display.flip()
                    
                    #print(has_neighbor(x,y,board))
                    
                    if is_win(board,x,y,color):
                        win_output(color,screen)
                        AI_move=False
                        game_active=False
                    color='2'
                    if AI_move:
                        
                    
                        #! 每次绘制图形之后都要进行下面这句
                        
                    
                    
                        #! 下面是AI的操作
                        #todo 求x,y
                        
                        
                        #pygame.display.update()
                        
                        rootx=Node(x,y,float('-inf'))
                        rootx.alpha=float('-inf')
                        rootx.beta=float('inf')
                        
                        dfs(rootx,0,2,board)
                        
                        #! 这个得分越大 说明AI白棋赢得可能性越大 越小人类越可能赢
                        #print(rootx.score)
                        pygame.display.flip()
                        #pygame.display.update()
                        draw_chess(15,15,'1',board,screen,0)
                        
                        pygame.display.flip()
                        #pygame.display.update()
                        x,y=rootx.posx,rootx.posy
                        
                        
                        
                        
                        draw_chess(x,y,color,board,screen,pos_cnt_white)#! 画棋子
                        pygame.display.flip()
                        print(np.array(board.matrix).T)
                        #pygame.display.update()
                        #print(1)
                        
                        fclock = pygame.time.Clock()   #* creat a object to track time(控制时间) *
                        fps = 40
                        fclock.tick(fps) 
                        
                        #print(2)
                        
                        pos_cnt_white+=1
                        pygame.display.flip()
                        #pygame.display.update()
                        
                        #print(3)

                        
                        if is_win(board,x,y,color):
                            win_output(color,screen)
                            game_active=False
                        pygame.display.flip()
                        color='1'
            elif game_active==False:
                play_button=Button(screen,'Replay')
                play_button.draw_button()
                pygame.display.flip()
                while not check_events(play_button):
                    continue
                game_active=True
                screen.fill([125,95,24])
                board.draw_board(screen)
                pygame.display.flip()#刷新窗口
                board.reset_matrix()
                pos_cnt_black=1
                pos_cnt_white=1
                AI_move=True
main()
