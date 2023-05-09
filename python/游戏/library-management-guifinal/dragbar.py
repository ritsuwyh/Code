import pygame
import win32api, win32con
import pygame.locals
import pandas as pd

from gui import button


class dragbar:
    def __init__(self, surface, pos, col_list, size, length):
        """
        初始化一个拖动框，坐标和大小分别是pos和size，可显示和最长显示的值分别为show_len和max_len。
        文本框自带边线
        param:
            surface: the surface which dragbar is on.
            col_list: the color config of the dragbar.
            size: (width, height), the size of the dragbar.
            pos: (x, y), the position of the dragbar.
            length: (show_len, max_len), the length pair
        """
        # fixed
        self.surface = surface
        self.pos = pos
        self.col_list = col_list
        self.size = size
        self.inpos = (pos[0]+2, pos[1]+2)
        self.insize = (size[0]-4, size[1]-4)
        
        self.button = button(surface, col_list, (self.insize[0], max(20, int(self.insize[1]*(length[0]/length[1])))), self.inpos)
        
        self.isdrag = False
        
        
    def update(self, mouseflag):
        self.button.update(mouseflag, None)
        
        if self.button.state == 'pressed':
            self.isdrag = True
        
        if mouseflag == 0:
            self.isdrag = False
        
        if self.isdrag == True:
            x, y = pygame.mouse.get_pos()
            y = min(y, self.inpos[1] + self.insize[1] - self.button.size[1])
            y = max(y, self.inpos[1])
            self.button.pos = (self.button.pos[0], y)
            
    def draw(self):
        pygame.draw.rect(self.surface, self.col_list['background_fr'], (self.pos[0], self.pos[1],self.size[0], self.size[1]), border_radius=5)
        pygame.draw.rect(self.surface, self.col_list['background'], (self.inpos[0], self.inpos[1],self.insize[0], self.insize[1]), border_radius=5)
        self.button.draw()
        
    def get_rate(self):
        return (self.button.pos[1] - self.inpos[1]) / (self.insize[1] - self.button.size[1])


class dragbar2(dragbar):
    def __init__(self, surface, pos, col_list, size, length):
        dragbar.__init__(self, surface, pos, col_list, size, length)
        self.button = button(surface, col_list, (max(20, int(self.insize[0]*(length[0]/length[1]))), self.insize[1]), self.inpos)
    
    def update(self, mouseflag):
        self.button.update(mouseflag, None)
        
        if self.button.state == 'pressed':
            self.isdrag = True
        
        if mouseflag == 0:
            self.isdrag = False
        
        if self.isdrag == True:
            x, y = pygame.mouse.get_pos()
            x = min(x, self.inpos[0] + self.insize[0] - self.button.size[0])
            x = max(x, self.inpos[0])
            self.button.pos = (x, self.button.pos[1])

    def get_rate(self):
        return (self.button.pos[0] - self.inpos[0]) / (self.insize[0] - self.button.size[0])

if __name__ == "__main__":
    pygame.init()
    main_screen = pygame.display.set_mode((1000, 500))
    default_col_list = {"background": (100, 0, 0), "background_fr": (255, 255, 255), \
                        "normal": (205, 223, 175), "normal_fr": (240, 161, 110), \
                        "active": (255, 251, 172), "active_fr": (255, 212, 149), \
                        "pressed": (180, 122, 108), "pressed_fr": (125, 90, 80), \
                        "t_normal": (26, 188, 156), "t_active": (41, 128, 185), "t_pressed": (155, 89, 182), \
                        "cursor": (0, 0, 0)}

    Bar = dragbar(main_screen, (50, 50), default_col_list, (24, 244), (50, 200))
    Bar2 = dragbar2(main_screen, (150, 50), default_col_list, (244, 24), (50, 200))
    # Button

    mouseflag = 0
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
            elif event.type == pygame.MOUSEBUTTONDOWN:
                mouseflag = event.button
            elif event.type == pygame.MOUSEBUTTONUP:
                mouseflag = 0
        
        Bar.update(mouseflag)
        Bar2.update(mouseflag)
        Bar.draw()
        Bar2.draw()
        pygame.display.flip()
        
