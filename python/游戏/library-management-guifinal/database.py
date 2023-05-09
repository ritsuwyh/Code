from book import Book
from account import Account

import pandas as pd
from datetime import datetime
import pandas as pd
import exceptions
from book import Book
import time


class Record:  # 一次记录的实体

    # Record Types enum
    BookLend = 'lend'
    BookReturn = 'return'
    BookPurchase = 'purchase'
    BookLost = 'lost'

    def __init__(self, types=None, book: Book = None, account=None, time: datetime = None, ):
        self.types = types  # The record's type is self.type
        self.book = book  # The book involving this record is self.book
        self.account = account  # user
        self.time = time  # The record happens in self.time

    def set(self, types=None, book=None, account=None, time: datetime = None, ):
        if types is not None:
            self.types = type
        if book is not None:
            self.book = book
        if account is not None:
            self.account = account
        if time is not None:
            self.time = time

    def toList(self):
        '''将 record 对象转成 list'''
        return [self.types, self.book, self.account, self.time]

    def toDataFrame(self):
        '''将 record 对象转成 DataFrame'''
        bookFrame = self.book.toDataFrame();
        accountFrame = self.account.toDataFrame();
        otherFrame = pd.DataFrame([[self.types, self.time]], columns=['Type', 'Time'])
        return pd.concat([bookFrame, accountFrame, otherFrame], axis=1)  # 列拼接


class Database:  # 一个Database是由很多次record组成

    # Sort Sequence （排序顺序）
    BlankSeq = 'blank'  # 空顺序，不按照任何顺序进行排序，直接使用原顺序
    BookNameSeq = 'name'  # 书名顺序，按照字典序进行排序，其次按照时间顺序
    TypeSeq = 'type'  # 事件类型顺序，按照事件名的字典序进行排序，其次按照时间顺序

    def __init__(self):
        self.record_length = 0
        self.record_list: list[Record] = []
        self.book_list: list[Book] = []

    def insert(self, record_to_append: Record = None, append_index=None):
        """
        在record_list的append_index处插入一个元素
        :param append_index:
        :param record_to_append:
        :return: 如果成功则返回值为0，否则抛出异常
        """

        if append_index is None:
            append_index = self.record_length

        if append_index < 0 or append_index > self.record_length:
            raise exceptions.IndexException

        self.record_list.insert(append_index, record_to_append)
        self.record_length += 1

    def remove(self, dict):
        for i in self.record_list:
            flag = 1
            for j in dict.keys():
                if dict[j] != i.toDataFrame().iloc[:].to_dict()[j][0]:
                    flag = 0
            if flag == 1:
                self.record_list.remove(i)
                self.record_length -= 1
        #del self.record_list[remove_index]

    def find_book(self, isbn=None, name=None, author=None):
        '''
        优先根据 ISBN 查找，其次是书名，最后是作者
        返回 Book 对象
        '''
        if isbn != None:
            for book in self.book_list:
                if book.isbn == isbn:
                    return book
        elif name != None:
            for book in self.book_list:
                if book.name == name:
                    return book
        elif author != None:
            for book in self.book_list:
                if book.author == author:
                    return book
        else:
            return None

    def add_book(self, book: Book):
        '''添加一本新书'''
        for i in self.book_list:
            if i.isbn == book.isbn:
                print("失败，重复添加书籍")
                return -1
        self.book_list.append(book)
        return 0

    def purchase(self, account: Account, book: Book):
        '''
        购买了某本书，将它加入库存
        注意 book 必须是 book_list 中的一个对象
        方便起见，每次只能购买一本书
        '''
        book.inventory += 1
        book.number += 1
        self.record_list.append(Record(Record.BookPurchase, book.copy(), account, datetime.now()))
        self.record_length += 1

    def lost(self, account: Account, book: Book):
        '''
        书籍丢失
        '''
        if book.inventory < 1 or book.number < 1:
            return -1
        book.inventory -= 1
        book.number -= 1
        self.record_list.append(Record(Record.BookLost, book.copy(), account, datetime.now()))
        self.record_length += 1

    def lend(self, account: Account, book: Book):
        '''
        借书操作，返回 -1 表示失败，成功返回0
        '''
        if book.inventory <= 0:
            # raise exceptions.InvalidObjectException
            print('库存不足，借书失败')
            return -1
        book.inventory -= 1
        self.record_list.append(Record(Record.BookLend, book.copy(), account, datetime.now()))
        self.record_length += 1
        return 0

    def ret(self, account: Account, book: Book):
        '''
        还书操作，同样要求 book 是 book_list 中的一个对象
        返回-1则表示失败，成功返回0
        '''
        if book not in self.book_list:
            # raise exceptions.InvalidObjectException
            return -1
        book.inventory += 1
        self.insert(Record(Record.BookReturn, book.copy(), account, datetime.now()))
        return 0

    def BookDataFrame(self):
        """
        将self.booklist导出为dataFrame
        """
        return pd.concat([book.toDataFrame() for book in self.book_list]).reset_index(drop=True)

    def RecordDataFrame(self):
        """
        将self.recordlist导出为dataFrame
        """
        return pd.concat([rec.toDataFrame() for rec in self.record_list]).reset_index(drop=True)
    
    def filter_by_isbn(self, isbn):
        """
        提出所有和 book 相关的记录，按照 Dataframe 返回
        :param isbn:搜索的 Book 编号
        :return:一份包含给定条件所有记录的Dataframe
        """
        if type(isbn) != str:
            # raise exceptions.InvalidObjectException
            print("类型错误")
            return -1
        rdf = self.RecordDataFrame()
        return rdf.loc[rdf['ISBN'] == isbn, :]

    def filter_by_time(self, start_time: datetime, end_time: datetime):
        """
        提出所有位于[start_time,end_time]之间的记录，按照Dataframe返回
        :param start_time:起始时间
        :param end_time:结束时间
        :return:一份包含给定条件所有记录的Dataframe
        """
        if start_time > end_time:
            raise exceptions.TimeSequenceException
        rdf = self.RecordDataFrame()
        return rdf.loc[(rdf['Time'] >= start_time) & (rdf['Time'] <= end_time), :]

    def filter_by_uid(self, uid):
        """
        提出所有关于 uid 指定的用户的记录，按照Dataframe返回
        :param uid: 用户编号 
        :return:一份包含给定条件所有记录的Dataframe
        """
        rdf = self.RecordDataFrame()
        return rdf.loc[rdf['Uid'] == uid, :]

    def sortedDataFrame(self, sequence='blank', reverse=False):
        """
        按照sequence进行排序，不修改该Account，而是返回一个排序好的Dataframe
        :param sequence:排序顺序，可能取值为BlankSeq,BookNameSeq,TypeSeq(见 database 类开头)
        :param reverse: 如果reverse=True则返回倒序
        :return:Dataframe。
        """
        rdf = self.RecordDataFrame()
        if sequence == 'blank':
            if reverse:
                return rdf.sort_index(ascending=False)
            else:
                return rdf
        elif sequence == 'name':
            orderCol = ['Name', 'Time']
        elif sequence == 'type':
            orderCol = ['Type', 'Time']
        else:
            print("非法参数")
            return -1
        return rdf.sort_values(orderCol, ascending=not reverse)

    def loadFromDataFrame(self, bookdf: pd.DataFrame, recorddf: pd.DataFrame):
        '''从 DataFrame 恢复数据库对象'''
        self.book_list = []
        for index, row in bookdf.iterrows():
            self.book_list.append(Book(row['ISBN'], row['Name'], row['Author'], row['Inventory'], row['Number']))

        self.record_list = []
        for index, row in recorddf.iterrows():
            book = Book(row['ISBN'], row['Name'], row['Author'], row['Inventory'], row['Number'])
            account = Account(row['Username'], None, row['Uid'])
            self.record_list.append(Record(row['Type'], book, account, row['Time']))
        self.record_length = len(self.record_list)


if __name__ == "__main__":
    ml = Book('123', 'ML', 'Mr.ZZH', 1, 3)
    krp = Book('456', 'KRP', 'Mr. Zhao', 2, 2)
    a = Account('a', 123, 1)
    b = Account('b', 456, 2)
    db = Database()
    db.add_book(ml)
    db.add_book(krp)
    db.lend(a, ml)
    db.ret(a, ml)
    db.lost(a, ml)
    time.sleep(1)
    start = datetime.now()
    db.purchase(a, ml)
    db.lend(a, ml)
    db.lend(b, krp)
    db.lend(a, krp)
    end = datetime.now()
    time.sleep(1)
    db.ret(b, krp)
    db.ret(a, krp)
    print(db.BookDataFrame())
    print(db.RecordDataFrame())
    print(db.filter_by_isbn('123'))
    print(db.filter_by_time(start, end))
    print(db.filter_by_uid(2))
    print("####### sort test")
    print("blank")
    print(db.sortedDataFrame('blank'))
    print(db.sortedDataFrame(reverse=True))
    print('name')
    print(db.sortedDataFrame('name'))
    print('type')
    print(db.sortedDataFrame('type', reverse=True))
