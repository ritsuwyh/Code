from account import User,AccountBase
import os
import window
import operation
from database import Database

MainAccountBase = None  # 账户数据库的初始化
MainDataBase = None
CurrentAccount = None

if __name__=="__main__":
    MainAccountBase = AccountBase()
    if os.path.exists("AccountData.xlsx"):
        MainAccountBase = operation.load_accountbase("AccountData.xlsx")
    MainDataBase = Database()
    if os.path.exists("Data.xlsx"):
        MainDataBase = operation.load_database("Data.xlsx")

    main_window = window.window(MainAccountBase, MainDataBase)
    while True:
        main_window.update()
        main_window.draw()