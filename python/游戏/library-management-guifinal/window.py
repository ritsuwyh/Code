# 不要修改此文件
import pygame
import gui
import sys
import random
import operation
import account
import book

key_shift = {"1":"!","2":"@","3":"#","4":"$","5":"%","6":"^","7":"&","8":"*","9":"(","0":")",\
             "-":"_","=":"+","[":"{","]":"}","\\":"|",";":":","\'":"\"",",":"<",".":">","/":"?","`":"~"}


class window:
    win_w = 800
    win_h = 600
    back_col = (166,187,141)
    front1_col = (116,187,141)
    front2_col = (116,127,141)
    
    title1_col = (45, 89, 182)
    title2_col = (41, 128, 185)
    title3_col = (41, 128, 185)
    def __init__(self, AccountBase, DataBase) -> None:
        '''
        初始化窗口
        '''
        self.AccountBase = AccountBase
        self.DataBase = DataBase
        self.CurrentAccount = None
        
        self.now_stage = "Login"
        self.helloname = 'yhj137'
        self.mousepos = None                    # 上一次鼠标左键点击的位置
        self.mouseflag = 0
        
        pygame.init()
        self.screen = pygame.display.set_mode((window.win_w, window.win_h))
        pygame.display.set_caption('Lib Management')
        pygame.key.set_repeat(600, 100)
        
        self.ABfontT=pygame.font.SysFont('Arial Black', 25)
        self.ABfont=pygame.font.SysFont('Arial Black', 30)
        self.ABfontm=pygame.font.SysFont('Arial Black', 20)
        self.ABfonts=pygame.font.SysFont('Arial Black', 15)
        
        self.col_list = {"normal":(205, 223, 175),"normal_fr":(240, 161, 110),\
                         "active":(255, 251, 172),"active_fr":(255, 212, 149),\
                         "pressed":(180, 122, 108),"pressed_fr":(125, 90, 80),\
                         "t_normal":(26, 188, 156),"t_active":(41, 128, 185),"t_pressed":(45, 89, 182),\
                         "cursor":(0,0,0), "background": (0, 100, 100), "background_fr": (116,127,141)}
        
        self.col_list_t = {"normal":(205, 223, 175),"normal_fr":(125, 90, 80),\
                         "active":(255, 251, 172),"active_fr":(255, 212, 149),\
                         "pressed":(180, 122, 108),"pressed_fr":(240, 161, 110),\
                         "t_normal":(26, 188, 156),"t_active":(41, 128, 185),"t_pressed":(45, 89, 182),\
                         "cursor":(0,0,0)}
        
        self.login_gui = []
        self.login_gui.append(gui.text_box(self.screen, (30,25), (240,200), self.col_list_t))
        self.login_gui.append(gui.text_box(self.screen, (30,25), (240,280), self.col_list_t))
        self.login_gui[1].is_code = True
        
        button_rect = gui.center_rect((250, 70), center_y=450)
        self.login_gui.append(gui.button(self.screen, self.col_list, button_rect[2:], button_rect[:2], "Login", 20))
        
        self.manage_gui = {}
        self.manage_gui["UserButton"] = gui.button(self.screen, self.col_list, (150, 50), (50, 530), "User", 20)
        self.manage_gui["BookButton"] = gui.button(self.screen, self.col_list, (150, 50), (230, 530), "Book", 20)
        self.manage_gui["RecordButton"] = gui.button(self.screen, self.col_list, (150, 50), (410, 530), "Record", 20)
        self.manage_gui["SaveButton"] = gui.button(self.screen, self.col_list, (150, 50), (590, 530), "Save", 20)
        
        self.user_gui = {}
        self.user_gui["NameTextBox"] = gui.text_box(self.screen, (15,16), (625,100), self.col_list_t)
        self.user_gui["PasswordTextBox"] = gui.text_box(self.screen, (15,16), (625,150), self.col_list_t)
        self.user_gui["PasswordTextBox"].is_code = True
        self.user_gui["AppendButton"] = gui.button(self.screen, self.col_list, (150, 30), (625, 190), "Append", 10)
        self.user_gui["RemoveButton"] = gui.button(self.screen, self.col_list, (150, 30), (625, 233), "Remove", 10)
        self.Display = gui.table_displayer(self.screen, self.col_list, (580, 430), (20, 80))
        
        self.book_gui = {}
        self.book_gui["Page1Button"] = gui.button(self.screen, self.col_list, (25, 25), (725, 488), "1", 10)
        self.book_gui["Page2Button"] = gui.button(self.screen, self.col_list, (25, 25), (755, 488), "2", 10)
        self.book_nowpage = 1
        
        self.book_gui1 = {}
        self.book_gui1["isbnTextBox"] = gui.text_box(self.screen, (15,16), (625,100), self.col_list_t)
        self.book_gui1["BookNameTextBox"] = gui.text_box(self.screen, (15,16), (625,150), self.col_list_t)
        self.book_gui1["AuthorTextBox"] = gui.text_box(self.screen, (15,16), (625,200), self.col_list_t)
        self.book_gui1["InventoryTextBox"] = gui.text_box(self.screen, (15,16), (625,250), self.col_list_t)
        self.book_gui1["AppendButton"] = gui.button(self.screen, self.col_list, (150, 30), (625, 290), "Append", 10)
        self.book_gui1["PurchaseButton"] = gui.button(self.screen, self.col_list, (150, 30), (625, 333), "Purchase", 10)
        self.book_gui1["LendButton"] = gui.button(self.screen, self.col_list, (150, 30), (625, 373), "Lend", 10)
        self.book_gui1["ReturnButton"] = gui.button(self.screen, self.col_list, (150, 30), (625, 413), "Return", 10)
        self.book_gui1["LostButton"] = gui.button(self.screen, self.col_list, (150, 30), (625, 453), "Lost", 10)
        
        self.book_gui2 = {}
        self.book_gui2["isbnTextBox"] = gui.text_box(self.screen, (15,16), (625,100), self.col_list_t)
        self.book_gui2["BookNameTextBox"] = gui.text_box(self.screen, (15,16), (625,150), self.col_list_t)
        self.book_gui2["AuthorTextBox"] = gui.text_box(self.screen, (15,16), (625,200), self.col_list_t)
        self.book_gui2["FindButton"] = gui.button(self.screen, self.col_list, (150, 30), (625, 240), "Find", 10)
        
        self.record_gui = {}
        self.record_gui["isbnTextBox"] = gui.text_box(self.screen, (15,16), (625,100), self.col_list_t)
        self.record_gui["uidTextBox"] = gui.text_box(self.screen, (15,16), (625,150), self.col_list_t)
        self.record_gui["FindButton"] = gui.button(self.screen, self.col_list, (150, 30), (625, 190), "Find", 10)
        self.record_gui["SortButton"] = gui.button(self.screen, self.col_list, (150, 30), (625, 233), "Sort", 10)
        self.record_gui["RemoveButton"] = gui.button(self.screen, self.col_list, (150, 30), (625, 273), "Remove", 10)
        
        
        
    def update_login(self, down_key):
        for b in self.login_gui:
            b.update(self.mouseflag, down_key)
        
        if self.login_gui[2].ispress(True):
            self.CurrentAccount = operation.login(self.AccountBase, self.login_gui[0].text, self.login_gui[1].text)
            if self.CurrentAccount != None:
                self.now_stage = "User"
                self.Display.load_dataframe(self.AccountBase.AccountDataFrame())
                self.helloname = self.CurrentAccount.username
            else:
                gui.MessageBox("Error","Wrong user name or password!")
    
    def update_user(self, down_key):
        for b in self.user_gui.values():
            b.update(self.mouseflag, down_key)
        if self.user_gui["AppendButton"].ispress(True):
            if self.user_gui["NameTextBox"].text != "" and self.user_gui["PasswordTextBox"].text != "":
                self.AccountBase.MaxUid += 1
                self.AccountBase.appendUser(account.User(self.user_gui["NameTextBox"].text, self.user_gui["PasswordTextBox"].text, self.AccountBase.MaxUid))
                self.Display.load_dataframe(self.AccountBase.AccountDataFrame())
        if self.user_gui["RemoveButton"].ispress(True):
            self.AccountBase.removeUser(self.Display.return_row()["Uid"])
            self.Display.load_dataframe(self.AccountBase.AccountDataFrame())
            
                
    def update_book(self, down_key):
        for b in self.book_gui.values():
            b.update(self.mouseflag, down_key)
        
        if self.book_gui["Page1Button"].ispress(True):
            self.book_nowpage = 1
        if self.book_gui["Page2Button"].ispress(True):
            self.book_nowpage = 2
        if self.book_gui1["AppendButton"].ispress(True):
            if self.book_gui1["isbnTextBox"].text != "" and self.book_gui1["BookNameTextBox"].text != "" and \
               self.book_gui1["AuthorTextBox"].text != "" and self.book_gui1["InventoryTextBox"].text != "":
                res = self.DataBase.add_book(book.Book(self.book_gui1["isbnTextBox"].text, self.book_gui1["BookNameTextBox"].text,\
                                                 self.book_gui1["AuthorTextBox"].text, int(self.book_gui1["InventoryTextBox"].text), int(self.book_gui1["InventoryTextBox"].text)))
                if res == -1:
                    gui.MessageBox('Error!',"Add books repeatedly!")
                self.Display.load_dataframe(self.DataBase.BookDataFrame())
        if self.book_gui1["PurchaseButton"].ispress(True):
            if self.Display.return_row() != None:
                for i in self.DataBase.book_list:
                    if i.isbn == self.Display.return_row()["ISBN"]:
                        self.DataBase.purchase(self.CurrentAccount, i)
                self.Display.load_dataframe(self.DataBase.BookDataFrame())
        if self.book_gui1["LendButton"].ispress(True) and self.Display.return_row() != None:
            res = 0
            for i in self.DataBase.book_list:
                if i.isbn == self.Display.return_row()["ISBN"]:
                    res = self.DataBase.lend(self.CurrentAccount, i)
                if res == -1:
                    gui.MessageBox('Error!',"There's no enough book!")
                    break
            self.Display.load_dataframe(self.DataBase.BookDataFrame())
            
        if self.book_gui1["ReturnButton"].ispress(True) and self.Display.return_row() != None:
            res = 0
            for i in self.DataBase.book_list:
                if i.isbn == self.Display.return_row()["ISBN"]:
                    res = self.DataBase.ret(self.CurrentAccount, i)
                if res == -1:
                    gui.MessageBox('Error!',"This book is not in Booklist")
                    break
            self.Display.load_dataframe(self.DataBase.BookDataFrame())
        
        if self.book_gui1["LostButton"].ispress(True) and self.Display.return_row() != None:
            res = 0
            for i in self.DataBase.book_list:
                if i.isbn == self.Display.return_row()["ISBN"]:
                    res=self.DataBase.lost(self.CurrentAccount, i)
                if res == -1:
                    gui.MessageBox('Error!',"Lost book error!")
                    break
            self.Display.load_dataframe(self.DataBase.BookDataFrame())
        
        if self.book_gui2["FindButton"].ispress(True):
            if self.book_gui2["isbnTextBox"].text != "":
                res = self.DataBase.find_book(self.book_gui2["isbnTextBox"].text,None,None)
                if res == None:
                    gui.MessageBox('Error!','No book here!')
                else:
                    self.Display.load_dataframe(res.toDataFrame())
            elif self.book_gui2["BookNameTextBox"].text != "":
                res = self.DataBase.find_book(None,self.book_gui2["BookNameTextBox"].text,None)
                if res == None:
                    gui.MessageBox('Error!','No book here!')
                else:
                    self.Display.load_dataframe(res.toDataFrame())
            elif self.book_gui2["AuthorTextBox"].text != "":
                res = self.DataBase.find_book(None,None,self.book_gui2["AuthorTextBox"].text)
                if res == None:
                    gui.MessageBox('Error!','No book here!')
                else:
                    self.Display.load_dataframe(res.toDataFrame())
        
        if self.book_nowpage == 1:
            for b in self.book_gui1.values():
                b.update(self.mouseflag, down_key)
        elif self.book_nowpage == 2:
            for b in self.book_gui2.values():
                b.update(self.mouseflag, down_key)
    
    def update_record(self, down_key):
        for b in self.record_gui.values():
            b.update(self.mouseflag, down_key)
        if self.record_gui["FindButton"].ispress(True):
            if self.record_gui["isbnTextBox"].text != "":
                res = self.DataBase.filter_by_isbn(self.record_gui["isbnTextBox"].text)
                if type(res) == int:
                    gui.MessageBox('Error!','Find Error!')
                else:
                    self.Display.load_dataframe(res)
            elif self.record_gui["uidTextBox"].text != "":
                res = self.DataBase.filter_by_uid(self.record_gui["uidTextBox"].text)
                if type(res) == int:
                    gui.MessageBox('Error!','No book here!')
                else:
                    self.Display.load_dataframe(res)
        if self.record_gui["SortButton"].ispress(True):
            self.Display.load_dataframe(self.DataBase.sortedDataFrame('type'))
        if self.record_gui["RemoveButton"].ispress(True) and self.Display.return_row() != None:
            self.DataBase.remove(self.Display.return_row())
            self.Display.load_dataframe(self.DataBase.RecordDataFrame())
            
    def update(self):
        '''
        update the game.
        '''
        down_key = []
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == pygame.MOUSEBUTTONDOWN:
                self.mouseflag = event.button
            elif event.type == pygame.MOUSEBUTTONUP:
                self.mouseflag = 0
            
            if event.type == pygame.KEYDOWN:
                flag = 1
                if 32 <= event.key <= 126 and pygame.key.get_mods() & pygame.KMOD_CAPS:
                    flag *= -1
                if 32 <= event.key <= 126 and pygame.key.get_mods() & pygame.KMOD_SHIFT:
                    flag *= -1
                    if chr(event.key) in key_shift.keys():
                        event.key = ord(key_shift[chr(event.key)])
                
                if ord('a') <= event.key <= ord('z') and flag == -1:
                    event.key -= 32
                down_key.append(event)
        
        if self.now_stage == "Login":     
            self.update_login(down_key)
        elif self.now_stage == "User":
            self.update_user(down_key)
        elif self.now_stage == "Book":
            self.update_book(down_key)
        elif self.now_stage == "Record":
            self.update_record(down_key)
        
        if self.now_stage != "Login":
            self.Display.update(self.mouseflag, down_key)
            for b in self.manage_gui.values():
                b.update(self.mouseflag, down_key)
            if self.manage_gui["UserButton"].ispress(True):
                self.now_stage = "User"
                self.Display.load_dataframe(self.AccountBase.AccountDataFrame())
            if self.manage_gui["BookButton"].ispress(True):
                self.now_stage = "Book"
                self.Display.load_dataframe(self.DataBase.BookDataFrame())
            if self.manage_gui["RecordButton"].ispress(True):
                self.now_stage = "Record"
                self.Display.load_dataframe(self.DataBase.RecordDataFrame())
            if self.manage_gui["SaveButton"].ispress(True):
                operation.save_accountbase(self.AccountBase, "AccountData.xlsx")
                operation.save_database(self.DataBase, "Data.xlsx")
                gui.MessageBox('save','Save Successfully!')
                
                
            
        
        
    def draw_login(self):
        pygame.draw.rect(self.screen, window.back_col,(0,0,window.win_w,window.win_h))
        pygame.draw.rect(self.screen, window.front2_col,(60,80,680,450), border_radius=20)
        pygame.draw.rect(self.screen, window.front1_col,(60+3,80+3,680-6,450-6), border_radius=20)
        
        for b in self.login_gui:
            b.draw()
        
        ptext = self.ABfont.render("Login Your Account", 1, window.title2_col)
        utext = self.ABfontm.render("User Name", 1, window.title3_col)
        ctext = self.ABfontm.render("Password", 1, window.title3_col)
        
        self.screen.blit(ptext, gui.center_rect(self.ABfont.size("Login Your Account"),center_y=130))
        self.screen.blit(utext, (90,204,100,100))
        self.screen.blit(ctext, (100,284,100,100))
    
    def draw_User(self):
        pygame.draw.rect(self.screen, window.front2_col,(610,70,180,450), border_radius=10)
        pygame.draw.rect(self.screen, window.front1_col,(610+3,70+3,180-6,450-6), border_radius=10)
        
        nametext = self.ABfonts.render("Username", 1, window.title3_col)
        passwordtext = self.ABfonts.render("Password", 1, window.title3_col)
        
        self.screen.blit(nametext, (625,80,100,100))
        self.screen.blit(passwordtext, (625,130,100,100))
        
        pygame.draw.rect(self.screen, window.front2_col,(620,225,160,3))
        
        for b in self.user_gui.values():
            b.draw()
        
    def draw_Book(self):
        pygame.draw.rect(self.screen, window.front2_col,(610,70,180,450), border_radius=10)
        pygame.draw.rect(self.screen, window.front1_col,(610+3,70+3,180-6,450-6), border_radius=10)
        
        if self.book_nowpage == 1:
            isbntext = self.ABfonts.render("ISBN", 1, window.title3_col)
            booknametext = self.ABfonts.render("BookName", 1, window.title3_col)
            authortext = self.ABfonts.render("Author", 1, window.title3_col)
            inventorytext = self.ABfonts.render("Inventory", 1, window.title3_col)
            
            self.screen.blit(isbntext, (625,80,100,100))
            self.screen.blit(booknametext, (625,130,100,100))
            self.screen.blit(authortext, (625,180,100,100))
            self.screen.blit(inventorytext, (625,230,100,100))
            
            pygame.draw.rect(self.screen, window.front2_col,(620,325,160,3))
            
            for b in self.book_gui1.values():
                b.draw()    
        elif self.book_nowpage == 2:
            isbntext = self.ABfonts.render("ISBN", 1, window.title3_col)
            booknametext = self.ABfonts.render("BookName", 1, window.title3_col)
            authortext = self.ABfonts.render("Author", 1, window.title3_col)
            
            self.screen.blit(isbntext, (625,80,100,100))
            self.screen.blit(booknametext, (625,130,100,100))
            self.screen.blit(authortext, (625,180,100,100))
            
            for b in self.book_gui2.values():
                b.draw()
        
        for b in self.book_gui.values():
            b.draw() 
        
    def draw_record(self):
        pygame.draw.rect(self.screen, window.front2_col,(610,70,180,450), border_radius=10)
        pygame.draw.rect(self.screen, window.front1_col,(610+3,70+3,180-6,450-6), border_radius=10)
        
        nametext = self.ABfonts.render("ISBN", 1, window.title3_col)
        passwordtext = self.ABfonts.render("uid", 1, window.title3_col)
        
        self.screen.blit(nametext, (625,80,100,100))
        self.screen.blit(passwordtext, (625,130,100,100))
        
        pygame.draw.rect(self.screen, window.front2_col,(620,225,160,3))
        
        for b in self.record_gui.values():
            b.draw()
    
    def draw(self):
        '''
        draw the game.
        '''
        pygame.draw.rect(self.screen, window.back_col,(0,0,window.win_w,window.win_h))
        
        if self.now_stage != "Login":
            self.Display.draw()
            
        if self.now_stage == "Login":
            self.draw_login()
        elif self.now_stage == "User":
            self.draw_User()
        elif self.now_stage == "Book":
            self.draw_Book()
        elif self.now_stage == "Record":
            self.draw_record()
        
        if self.now_stage != "Login":
            for b in self.manage_gui.values():
                b.draw()
            weltext = self.ABfontm.render("Hi, "+self.helloname, 1, window.title2_col)
            viewtext = self.ABfontm.render(self.now_stage, 1, window.title2_col)
            pygame.draw.rect(self.screen, window.front2_col,(10,10,180,50), border_radius=5)
            pygame.draw.rect(self.screen, window.front1_col,(10+3,10+3,180-6,50-6), border_radius=5)
            pygame.draw.rect(self.screen, window.front2_col,(610,10,180,50), border_radius=5)
            pygame.draw.rect(self.screen, window.front1_col,(610+3,10+3,180-6,50-6), border_radius=5)
            self.screen.blit(weltext, gui.center_rect(self.ABfontm.size("Hi, "+self.helloname), 100, 35))
            self.screen.blit(viewtext, gui.center_rect(self.ABfontm.size(self.now_stage), 700, 35))
        
        pygame.draw.rect(self.screen, window.front2_col,(200,10,400,50), border_radius=5)
        pygame.draw.rect(self.screen, window.front1_col,(200+3,10+3,400-6,50-6), border_radius=5)
        ptext = self.ABfontT.render("Library Management", 1, window.title1_col)
        self.screen.blit(ptext, gui.center_rect(self.ABfontT.size("Library Management"),center_y=35))
        
        pygame.display.flip()