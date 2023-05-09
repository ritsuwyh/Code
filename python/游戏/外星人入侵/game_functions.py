import sys
import pygame
def check_events(ship):
    #响应按键和鼠标事件
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
        elif event.type==pygame.KEYDOWN:
            if event.key==pygame.K_RIGHT:
                #! 这句话是点一次动一次 ship.rect.centerx+=1
                ship.moving_right=True
        elif event.type==pygame.KEYUP:
            if event.key==pygame.K_RIGHT:
                ship.moving_right=False
                
                
def update_screen(ai_settings,screen,ship):
    screen.fill(ai_settings.bg_color)
    ship.blitme()#! 调用方法 绘制飞船
    pygame.display.flip() #更新屏幕内容
