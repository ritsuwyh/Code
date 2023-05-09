import sys
import pygame
#使用pygame之前必须初始化
from settings import Settings#!导入settings.py里面的Settings类
from ship import Ship
import game_functions as gf

pygame.init()

#!导入设置
ai_settings=Settings()

#!设置窗口
#设置主屏窗口 ；设置全屏格式：flags=pygame.FULLSCREEN
screen = pygame.display.set_mode((ai_settings.screen_width,ai_settings.screen_height))
#设置窗口标题
pygame.display.set_caption('alien invasion')

#!设置飞船(操作主体)
ship=Ship(screen)


#! 进行操作 game_functions
while True:
    # # 循环获取事件，监听事件
    # for event in pygame.event.get():
    #     # 判断用户是否点了关闭按钮
    #     if event.type == pygame.QUIT:
    #         #卸载所有模块
    #         pygame.quit()
    #         #终止程序
    #         sys.exit()
    #每次循环的时候都重新绘制屏幕
    gf.check_events(ship)
    #! 将上面注释的部分写成一个函数 写到game_functions.py 当中
    
    ship.update()
    
    # screen.fill(ai_settings.bg_color)
    # ship.blitme()#! 调用方法 绘制飞船
    # pygame.display.flip() #更新屏幕内容
    gf.update_screen(ai_settings,screen,ship)
    #! 将上面注释的内容写成一个函数 携带导game_functions.py 当中
    
    
