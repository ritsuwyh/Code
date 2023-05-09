from datetime import datetime
import pandas as pd
from exceptions import IndexException
from book import Book


class Account:
    def __init__(self, username, password, uid):
        self.username = str(username)
        self.password = str(password)
        self.uid = str(uid)
        self.permission = 0

    def toList(self):
        '''将 Account 对象转成 list(万万不可泄漏密码)'''
        return [self.uid, self.username, self.permission]

    def toListFull(self):
        '''将 Account 对象转成 list(万万不可泄漏密码)'''
        return [self.uid, self.username, self.password, self.permission]

    def toDataFrame(self):
        '''将 record 对象转成 DataFrame(万万不可泄漏密码)'''
        return pd.DataFrame([self.toList()], columns=['Uid', 'Username', 'Permission'])

    def toDataFrameWithKey(self):
        return pd.DataFrame([self.toListFull()], columns=['Uid', 'Username', 'Password', 'Permission'])



class User(Account):

    def __init__(self, username, password, uid):
        super().__init__(username, password, uid)
        self.permission = 0


CurrentAccount = None

class AccountBase:
    def __init__(self):
        self.UserAccountList = []
        self.UserAccountNum = 0
        self.MaxUid = 0

    def appendUser(self, user: User):
        for u in self.UserAccountList:
            if u.uid == user.uid:
                return -1
        self.UserAccountList.append(user)
        self.UserAccountNum += 1
    
    def removeUser(self, uid):
        for u in self.UserAccountList:
            if u.uid == uid:
                self.UserAccountList.remove(u)
    
    def loadFromDataFrame(self, accountdf: pd.DataFrame):
        for index, row in accountdf.iterrows():
            self.UserAccountList.append(User(row["Username"], row["Password"], row["Uid"]))
            self.UserAccountNum += 1
        
        for u1 in self.UserAccountList:
            self.MaxUid = max(self.MaxUid, int(u1.uid))
            for u2 in self.UserAccountList:
                if u1 != u2 and u1.uid == u2.uid:
                    return -1

    def AccountDataFrame(self):
        bookDf = [ele.toDataFrameWithKey() for ele in self.UserAccountList]
        if bookDf!= []:
            return pd.concat(bookDf)
        return pd.DataFrame()
