from turtle import goto
import pygame
import sys

from settings import*
from game_functions import*
from board import Board
from button import Button
#todo 需要改进的 获胜之后问是否重新开始 开始按钮 提示谁出棋 选择模式 写一些语言

 #! 游戏状态 目的是防止有一方获胜之后可以继续下棋

def main():
    #! 初始化
    while True:
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
                     
        AI_first=True
        times=1
        color='1'#! 默认黑方先手
        break_flag=False
        print('人机先手：1, 玩家先手：2')
        number=eval(input())
        # global game_active
        
        if number==1:
        
        #! 游戏主循环
            while True:
                for event in pygame.event.get():
                    if event.type==pygame.QUIT:
                        pygame.quit()
                        sys.exit()
                    elif event.type==pygame.MOUSEBUTTONDOWN and game_active and AI_first==False:
                        x_board,y_board=pygame.mouse.get_pos()
                        x=round((x_board-40)/40)
                        y=round((y_board-40)/40)
                        if draw_chess(x,y,color,board,screen):
                            #print(has_neighbor(x,y,board))
                            if is_win(board,x,y,color):
                                win_output(color,screen)
                                pygame.display.flip()
                                game_active=False
                            AI_first=True
                    elif game_active and AI_first:
                        if times==1:
                            x,y=7,7
                            draw_chess(x,y,color,board,screen)
                            times+=1
                            pygame.display.flip()
                            color='2'
                            AI_first=False
                        else:
                            color='1'
                                
                            # #! 每次绘制图形之后都要进行下面这句
                            # pygame.display.flip()
                                
                                
                            #! 下面是AI的操作
                            #todo 求x,y
                            x,y=find_pos(board,dicx2)
                            draw_chess(x,y,color,board,screen)
                                
                            if is_win(board,x,y,color):
                                win_output(color,screen)
                                game_active=False
                            pygame.display.flip()
                            color='2'
                            AI_first=False
                                        
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
                        break_flag=True
                        break
                if break_flag:
                    break
                        
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
                                x,y=find_pos(board,dicx1)
                                draw_chess(x,y,color,board,screen)
                            
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
                        break_flag=True
                        break   
                if break_flag:
                    break     
main()
