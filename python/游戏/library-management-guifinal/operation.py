from account import AccountBase
from database import Database
from book import Book
from account import Account, User

import os
import pandas as pd
import exceptions


def login(account_base: AccountBase, username, password):
    """
    登录账户，通过username和password登录account_base
    返回Account，失败返回None
    """
    for account in account_base.UserAccountList:
        if username == account.username and password == account.password:
            return account
    return None


def load_accountbase(path, key=None):
    """
    载入accountbase,key为秘钥（加密），暂时没有加密功能
    返回Accountbase对象，如果不存在则返回InvalidOperation异常
    """
    if path not in os.listdir(os.getcwd()):
        raise exceptions.InvalidOperationException
    account_df = pd.read_excel(path)
    ab = AccountBase()
    ab.loadFromDataFrame(account_df)
    return ab


def load_database(path, key=None):
    """
    载入database,key为秘钥（加密），暂时没有加密功能
    返回Database对象，如果不存在则返回InvalidOperation异常
    """
    if path not in os.listdir(os.getcwd()):
        raise exceptions.InvalidOperationException
    book_df = pd.read_excel(path, sheet_name='Book')
    record_df = pd.read_excel(path, sheet_name='Record')
    db = Database()
    db.loadFromDataFrame(book_df, record_df)
    return db


def save_database(database: Database, path, key=None):
    bookFrame = database.BookDataFrame()
    recordFrame = database.RecordDataFrame()
    with pd.ExcelWriter(path) as writer:
        bookFrame.to_excel(writer, sheet_name="Book", index=False)
        recordFrame.to_excel(writer, sheet_name="Record", index=False)


def save_accountbase(accountbase: AccountBase, path, key=None):
    accountFrame = accountbase.AccountDataFrame()
    with pd.ExcelWriter(path) as writer:
        accountFrame.to_excel(writer)


if __name__ == "__main__":
    ml = Book('123', 'ML', 'Mr.ZZH', 1, 3)
    krp = Book('456', 'KRP', 'Mr. Zhao', 2, 2)
    a = Account('a', 123, 1)
    b = Account('b', 456, 2)
    c = User('c', 789, 3)
    ab = AccountBase()
    ab.appendUser(a)
    ab.appendUser(b)
    ab.appendUser(c)
    db = Database()
    db.add_book(ml)
    db.add_book(krp)
    db.lend(a, ml)
    db.ret(a, ml)
    db.lost(a, ml)
    db.purchase(a, ml)
    db.lend(a, ml)
    db.lend(b, krp)
    db.lend(a, krp)
    db.ret(b, krp)
    db.ret(a, krp)
    save_database(db, r'testdb.xlsx')
    save_accountbase(ab, r'testab.xlsx')
    db2: Database = load_database(r'testdb.xlsx')
    ab2: AccountBase = load_accountbase(r'testab.xlsx')
    print(db2.BookDataFrame())
    print(db2.RecordDataFrame())
    print(ab2.AccountDataFrame())
