import pandas as pd
import copy


class Book:
    '''
    图书管理系统中书籍的抽象
    '''

    def __init__(self, isbn, name, author, inventory, number):
        '''
        isbn : 编号
        name : 书名
        author : 作者
        inventory : 库存数量
        number : 总数量(包括借出的书)
        '''
        self.isbn = str(isbn)
        self.name = str(name)
        self.author = str(author)
        self.inventory = int(inventory)
        self.number = int(number)

    def set(self, isbn=None, name=None, author=None, inventory=None, number=None):
        if isbn is not None:
            self.isbn = isbn
        if name is not None:
            self.name = name
        if author is not None:
            self.author = author
        if inventory is not None:
            self.inventory = inventory
        if number is not None:
            self.number = number

    def toList(self):
        '''
        将书籍转换成 List 的形式
        '''
        return [self.isbn, self.name, self.author, self.inventory, self.number]

    def toDataFrame(self):
        '''
        将书籍转换成 DataFrame 的形式
        '''
        return pd.DataFrame([self.toList()], columns=['ISBN', 'Name', 'Author', 'Inventory', 'Number'])
    
    def copy(self):
        return copy.copy(self)


if __name__ == '__main__':
    a = Book('123', 'ML', 'Mr.ZZH', 1, 3)
    a.set(name='西瓜书')
    print(a.toList())
    print(a.toDataFrame())
