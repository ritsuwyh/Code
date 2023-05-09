import pygame
import win32api, win32con
import pygame.locals
import pandas as pd


def center_rect(size, center_x = 400, center_y = 300):
    return (center_x - size[0]/2, center_y - size[1]/2, size[0], size[1])

def MessageBox(title, message):
    win32api.MessageBox(0, message, title, win32con.MB_OK)
    

class text_box():
    now_active_obj = None
    appear_time_cnt = 800
    def __init__(self, surface, size, pos, col_list) -> None:
        self.surface = surface
        
        self.ABfont=pygame.font.SysFont('Consolas', size[0])
        self.text_size = self.ABfont.size('a')
        self.max_num = size[1]
        
        self.size = (self.text_size[0] * self.max_num + 20, self.text_size[1]+14)
        self.pos = pos
        self.state = 'normal'
        self.active = False
        self.col_list = col_list
        
        self.cursor_rect = [pos[0]+13,pos[1]+6,3,self.size[1]-12]
        self.time_cnt = 0
        self.text = ""
        self.text_rect = (pos[0]+10, pos[1]+6, self.size[0], self.size[1])
        self.is_code = False
        
        self.isable = True
        self.press = 0
        
    def update(self, mouseflag, down_key):
        if text_box.now_active_obj == self:
            self.state = 'pressed'
            self.active = True
        else:
            self.state = 'normal'
            self.active = False
        
        if self.active:
            self.time_cnt += 1
            if self.time_cnt >= 2 * text_box.appear_time_cnt:
                self.time_cnt = 0
            for i in down_key:
                if i.key == pygame.K_BACKSPACE:
                    self.text = self.text[:-1]
                elif 32 <= i.key <= 126:
                    self.text += chr(i.key)
        
        self.cursor_rect[0] = self.pos[0]+ 13 + min(self.max_num, len(self.text)) * self.text_size[0]
        
        self.lasts=self.state
        x, y = pygame.mouse.get_pos()
        if self.pos[0]<x<self.pos[0]+self.size[0] and self.pos[1]<y<self.pos[1]+self.size[1]:
            if self.isable == True:
                if mouseflag == 1 or mouseflag == 3:
                    self.state = 'pressed'
                    self.press = mouseflag
                    text_box.now_active_obj = self
                    self.time_cnt = 0
                else:
                    self.state = 'active'
    
    def draw(self):
        pygame.draw.rect(self.surface, self.col_list[self.state+'_fr'], (self.pos[0],self.pos[1],self.size[0],self.size[1]))
        pygame.draw.rect(self.surface, self.col_list['pressed'], (self.pos[0]+2,self.pos[1]+2,self.size[0]-4,self.size[1]-4))
        #the cursor
        if self.time_cnt < text_box.appear_time_cnt and self.active:
            pygame.draw.rect(self.surface, self.col_list["cursor"], self.cursor_rect)
        
        if self.is_code:
            ptext = self.ABfont.render('*' * len(self.text[-self.max_num:]), 1, self.col_list["t_pressed"])
        else:
            ptext = self.ABfont.render(self.text[-self.max_num:], 1, self.col_list["t_pressed"])
        self.surface.blit(ptext, self.text_rect)


class button:
    def __init__(self, surface, col_list, size, pos, text = "", r = 5) -> None:
        self.surface = surface
        self.size = size
        self.pos = pos
        self.state = 'normal'
        self.col_list = col_list
        self.r = r
        self.ABfont=pygame.font.SysFont('Arial Black', 18)
        self.text = text
        
        self.isable = True
        self.press = 0
        pass
    
    def update(self, mouseflag, key_down):
        self.lasts=self.state
        x, y = pygame.mouse.get_pos()
        if self.pos[0]<x<self.pos[0]+self.size[0] and self.pos[1]<y<self.pos[1]+self.size[1]:
            if self.isable == True:
                if mouseflag == 1 or mouseflag == 3:
                    self.state = 'pressed'
                    self.press = mouseflag
                else:
                    self.state = 'active'
        else:
            if self.isable == True:
                self.state ='normal'
    
    def draw(self):
        pygame.draw.rect(self.surface, self.col_list[self.state+'_fr'], (self.pos[0],self.pos[1],self.size[0],self.size[1]), border_radius=self.r)
        pygame.draw.rect(self.surface, self.col_list[self.state], (self.pos[0]+1,self.pos[1]+1,self.size[0]-2,self.size[1]-2), border_radius=self.r)
        ptext = self.ABfont.render(self.text, 1, self.col_list['t_'+self.state])
        self.surface.blit(ptext, center_rect(self.ABfont.size(self.text), self.pos[0] + self.size[0]/2, self.pos[1] + self.size[1]/2))
        
    def ispress(self, isleft):
        temp = 3
        if isleft:
            temp = 1
        if (self.state == 'normal' or self.state == 'active') and self.press == temp:
            self.press = 0
            return True
        return False
    
class textbutton:
    def __init__(self, surface, col_list, size, pos, active_area, text="", r=0) -> None:
        self.surface = surface
        self.size = size
        self.pos = pos
        self.state = 'normal'
        self.col_list = col_list
        self.r = r
        self.ABfont = pygame.font.SysFont('Consolas', 18)
        self.text = text
        self.lasts = "normal"
        self.press = 0
        self.isable = True
        self.active_area = active_area
        pass

    def update(self, mouseflag, key_down):
        if self.isable == False:
            return
        self.lasts = self.state
        x, y = pygame.mouse.get_pos()
        if self.active_area[0] < x < self.active_area[1] and self.active_area[2] < y < self.active_area[3]:
            pass
        else:
            return
        if self.pos[0]<x<self.pos[0]+self.size[0] and self.pos[1]<y<self.pos[1]+self.size[1]:
            if mouseflag == 1 or mouseflag == 3:
                self.state = 'pressed'
                self.press = mouseflag
            else:
                if self.state != "pressed":
                    self.state = 'active'
        else:
            if self.state != "pressed":
                self.state ='normal'

        if self.lasts == "active" and self.state == "pressed":
            self.press = 1

    def draw(self):
        pygame.draw.rect(self.surface, self.col_list[self.state + '_fr'],
                         (self.pos[0], self.pos[1], self.size[0], self.size[1]), border_radius=self.r)
        pygame.draw.rect(self.surface, self.col_list[self.state],
                         (self.pos[0] + 1, self.pos[1] + 1, self.size[0] - 2, self.size[1] - 2), border_radius=self.r)
        ptext = self.ABfont.render(self.text, 1, self.col_list['t_' + self.state])
        self.surface.blit(ptext, center_rect(self.ABfont.size(self.text), self.pos[0] + self.size[0] / 2,
                                             self.pos[1] + self.size[1] / 2))

    def ispress(self):
        if self.press == 1:
            self.press = 0
            return True
        return False

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
        self.inpos = (pos[0] + 2, pos[1] + 2)
        self.insize = (size[0] - 4, size[1] - 4)
        temp = 1
        if length[1] != 0:
            temp = length[0] / length[1]
        self.button = button(surface, col_list,
                             (self.insize[0], max(20, int(self.insize[1] * min(temp, 1)))), self.inpos)

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
        pygame.draw.rect(self.surface, self.col_list['background_fr'],
                         (self.pos[0], self.pos[1], self.size[0], self.size[1]), border_radius=5)
        pygame.draw.rect(self.surface, self.col_list['background'],
                         (self.inpos[0], self.inpos[1], self.insize[0], self.insize[1]), border_radius=5)
        self.button.draw()

    def get_rate(self):
        if self.insize[1] == self.button.size[1]:
            return 0
        return (self.button.pos[1] - self.inpos[1]) / (self.insize[1] - self.button.size[1])


class dragbar2(dragbar):
    def __init__(self, surface, pos, col_list, size, length):
        dragbar.__init__(self, surface, pos, col_list, size, length)
        temp = 1
        if length[1] != 0:
            temp = length[0] / length[1]
        self.button = button(surface, col_list,
                             (max(20, int(self.insize[0] * min(temp, 1))), self.insize[1]), self.inpos)

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
        if self.insize[0] == self.button.size[0]:
            return 0
        return (self.button.pos[0] - self.inpos[0]) / (self.insize[0] - self.button.size[0])


class table_displayer:
    def __init__(self, surface, col_list, size, pos):
        self.surface = surface
        self.pos = pos
        self.bias_pos = [0, 0]
        self.col_list = col_list
        self.size = size
        self.state = 'normal'
        self.df = None
        self.last = 0
        self.dataframe_row = 0
        self.dataframe_col = 0
        self.showsize = (size[0] - 35, size[1] - 35)
        self.totalsize = [0, 0]
        self.table = []
        self.headtable = []
        self.font = pygame.font.SysFont('Consolas', 18)
        self.rowdragbar = dragbar2(surface, (pos[0], pos[1] + size[1] - 30), col_list, (size[0] - 30, 30), (200, 500))
        self.coldragbar = dragbar(surface, (pos[0] + size[0] - 30, pos[1]), col_list, (30, size[1] - 30), (200, 500))

    def load_dataframe(self, df: pd.DataFrame):
        self.df = df
        self.dataframe_row = df.shape[0]
        self.dataframe_col = df.shape[1]
        self.table = [[None for j in range(self.dataframe_col)] for i in range(self.dataframe_row)]
        self.headtable = [None for j in range(self.dataframe_col)]
        self.totalsize = [self.dataframe_col * 160, self.dataframe_row * 25 + 25]
        self.rowdragbar = dragbar2(self.surface, (self.pos[0], self.pos[1] + self.size[1] - 30), self.col_list,
                                   (self.size[0] - 30, 30), (self.showsize[0], self.totalsize[0]))
        self.coldragbar = dragbar(self.surface, (self.pos[0] + self.size[0] - 30, self.pos[1]), self.col_list,
                                  (30, self.size[1] - 30), (self.showsize[1], self.totalsize[1]))
        for i in range(self.dataframe_row):
            for j in range(self.dataframe_col):
                temp_str=str(df.iloc[i,j])
                if len(temp_str)>12:
                    temp_str=temp_str[:9]+"..."
                
                self.table[i][j] = textbutton(self.surface, self.col_list, (160, 25), (self.pos[0], self.pos[1]), (self.pos[0],self.pos[0]+self.showsize[0],self.pos[1],self.pos[1]+self.showsize[1]),
                                              text=temp_str)
        for j in range(self.dataframe_col):
            self.headtable[j] = textbutton(self.surface, self.col_list, (160, 25), (self.pos[0], self.pos[1]), (self.pos[0],self.pos[0]+self.showsize[0],self.pos[1],self.pos[1]+self.showsize[1]),
                                           text=df.columns[j])
            self.headtable[j].isable = False

    def update(self, mouseflag, key_down):
        self.last = mouseflag
        row_rate = self.rowdragbar.get_rate()
        col_rate = self.coldragbar.get_rate()
        self.bias_pos[0] = row_rate * (self.showsize[0] - self.totalsize[0])
        self.bias_pos[1] = col_rate * (self.showsize[1] - self.totalsize[1])

        self.rowdragbar.update(mouseflag)
        self.coldragbar.update(mouseflag)
        for i in range(self.dataframe_row):
            for j in range(self.dataframe_col):
                self.table[i][j].pos = (
                    self.pos[0] + self.bias_pos[0] + 160 * j, self.pos[1] + self.bias_pos[1] + 25 * (i + 1))
                self.table[i][j].update(mouseflag, None)
        for j in range(self.dataframe_col):
            self.headtable[j].pos = (self.pos[0] + self.bias_pos[0] + 160 * j, self.pos[1])
            self.headtable[j].update(mouseflag, None)

        for i in range(self.dataframe_row):
            for j in range(self.dataframe_col):
                if self.table[i][j].state == "active":
                    for o in range(self.dataframe_col):
                        self.table[i][o].state = "active"
                    break
        for i in range(self.dataframe_row):
            for j in range(self.dataframe_col):
                if self.table[i][j].ispress():
                    for i2 in range(self.dataframe_row):
                        for j2 in range(self.dataframe_col):
                            self.table[i2][j2].state = "normal"
                    for o in range(self.dataframe_col):
                        self.table[i][o].state = "pressed"


        pass

    def draw(self):
        pygame.draw.rect(self.surface, (116,187,141), (self.pos[0], self.pos[1], self.size[0], self.size[1]))
        for i in range(self.dataframe_row):
            for j in range(self.dataframe_col):
                self.table[i][j].draw()

        for j in range(self.dataframe_col):
            self.headtable[j].draw()

        pygame.draw.rect(self.surface, (166,187,141), (0, 0, self.pos[0] + self.size[0] - 30, self.pos[1]))
        pygame.draw.rect(self.surface, (166,187,141), (0, 0, self.pos[0], self.pos[1] + self.size[1] - 30))
        pygame.draw.rect(self.surface, (166,187,141), (self.pos[0] + self.size[0] - 35, 0, 1999, 999))
        pygame.draw.rect(self.surface, (166,187,141), (0, self.pos[1] + self.size[1] - 35, 1999, 999))
        self.rowdragbar.draw()
        self.coldragbar.draw()

        pass
        
    def return_row(self):
        for i in range(self.dataframe_row):
            if self.table[i][0].state=="pressed":
                return self.df.iloc[i,:].to_dict()
        return None
    