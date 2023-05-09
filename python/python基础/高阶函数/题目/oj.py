
#! 以后·直接复制粘贴他的输出 检查的时候用文档对比


# #提示：可以定义基类并继承，从而更简洁地完成以上要求。
# #（港币和人民币的汇率为1:0.8）。
# #注：所有打印的数字均保留小数点后两位，需要print的格式推荐从介绍/样例输出中直接复制，以防符号格式不吻合。
class HKD_Personal_Account():
    def __init__(self, cash=0, loan=0, account=None):
        
        self.cash=cash
        self.loan=loan
        self.account=account
  
    def withdraw(self, money): #取
        temp=self.cash-money
        if temp<0:
            print('余额不足，操作失败')
          
        #todo'（账户名）账户余额：（账户余额）HK$；账户贷款：（账户贷款）HK$'   
        else:
            self.cash=temp
        print(self)    
        #print('%s账户余额：%.2fHK$；账户贷款：%.2fHK$'%(self.account,self.cash,self.loan))
    def deposit(self, money): #存
        self.cash+=money
        print(self)
        #print('%s账户余额：%.2fHK$；账户贷款：%.2fHK$'%(self.account,self.cash,self.loan))
        
    
    def transfer_out(self, other, money):#!other 是我们的自定义对象
        temp=self.cash-money
        if temp<0:
            print('余额不足，操作失败')
            print(self)
            #print('%s账户余额：%.2fHK$；账户贷款：%.2fHK$'%(self.account,self.cash,self.loan))
        else:
            self.cash=temp
            #!!!!! isinstance
            if type(other)==HKD_Personal_Account:
              
                other.cash+=money

            else:
                other.cash+=money*0.8
                other.sales+=money*0.8
            print('转账成功')
            #print('%s账户余额：%.2fHK$；账户贷款：%.2fHK$'%(self.account,self.cash,self.loan))
            print(self)
            print(other)

    def repay_the_loan(self, money):
        temp=self.cash-money
        if temp<0:
            print('余额不足，操作失败')
        else:
            self.cash-=money
            self.loan+=money
            print('%s还款成功'%self.account)
        print(self)    
        #print('%s账户余额：%.2fHK$；账户贷款：%.2fHK$'%(self.account,self.cash,self.loan))    
    def __str__(self):
        #'（账户名）账户余额：（账户余额）HK$；账户贷款：（账户贷款）HK$'
        xxx='%s账户余额：%.2fHK$；账户贷款：%.2fHK$'%(self.account,self.cash,self.loan)
        return xxx
    #允许通过print(HKD_Personal_Account对象)，打印出'（账户名）账户余额：（账户余额）HK$；账户贷款：（账户贷款）HK$'。
class RMB_Company_Account(HKD_Personal_Account):
    def __init__(self, cash=0, loan=0, account=None ,sales=0):
        super().__init__(cash,loan,account)
        self.sales=sales
    
    def withdraw(self, money): 
        super().withdraw(money)

    
    def deposit(self, money): 
        super().deposit(money)

    
    def transfer_out(self, other, money):
        temp=self.cash-money
        if temp<0:
            print('余额不足，操作失败')
            print(self)
            #print('%s账户余额：%.2fHK$；账户贷款：%.2fHK$'%(self.account,self.cash,self.loan))
        else:
            self.cash=temp
            #!!!!! isinstance 以后用type函数
            if type(other)==HKD_Personal_Account:
                
                other.cash+=money/0.8
                
            else:
                other.cash+=money
                other.sales+=money
            print('转账成功')
            #print('%s账户余额：%.2fHK$；账户贷款：%.2fHK$'%(self.account,self.cash,self.loan))
            print(self)
            print(other)        


    def repay_the_loan(self, money):
        
        super().repay_the_loan(money)
    def __str__(self):
        xxx='%s账户余额：%.2f￥；账户贷款：%.2f￥；营业额为：%.2f￥'%(self.account,self.cash,self.loan,self.sales)
        return xxx
    

# NJU = RMB_Company_Account(cash=500, loan=-300, account='NJU', sales=0)

# SEU = RMB_Company_Account(cash=500, loan=-300, account='SEU', sales=0)

# AI = HKD_Personal_Account(cash=30, loan=-20, account='AI')

# CS = HKD_Personal_Account(cash=10, loan=-10, account='CS')

# print('0')

# print(AI)

# print('1')

# print(NJU)

# print('2')

# AI.deposit(20)

# print('3')

# AI.withdraw(10)

# print('4')

# AI.withdraw(100)

# print('5')

# NJU.deposit(20)

# print('6')

# NJU.withdraw(100)

# print('7')

# NJU.withdraw(1000)

# print('8')

# AI.transfer_out(NJU, 20)

# print('9')

# AI.transfer_out(NJU, 200)

# print('10')

# NJU.transfer_out(AI, 50)

# print('11')

# NJU.transfer_out(AI, 5000)

# print('12')

# AI.transfer_out(CS, 10)

# print('13')

# NJU.transfer_out(SEU, 100)

# print('14')

# NJU.transfer_out(SEU, 1000)

# print('15')

# AI.repay_the_loan(20)

# print('16')

# AI.repay_the_loan(200)

# print('17')

# NJU.repay_the_loan(100)

# print('18')

# NJU.repay_the_loan(1000)

# exit()








# class MultiSet():   # 或者 class MultiSet():
#     def __init__(self, elements = None):
#         self.contents = elements
#         self.book = {}
#         for k in self.contents:
#             self.book.setdefault(k,0)
#             self.book[k]+=1
    
#     def __str__(self):
#         return "{"+str(list(sorted(self.contents)))[1:-1]+"}"
    
#     def __len__(self):
#         if not self.contents:
#             return 0
#         return len(self.contents)
    
#     def __contains__(self,element):
#         return element in self.contents

#     def add(self, element):
#         if not self.contents:
#             self.contents = []
#         self.contents.append(element)
#         self.book.setdefault(element,0)
#         self.book[element] += 1
    
#     def remove(self, element):
#         self.contents.remove(element)
#         self.book[element]-=1
    
#     def count(self, element):
#         self.book.setdefault(element,0)
#         return self.book[element]
    
#     def union(self, other_multi_set):
#         outcome = MultiSet([])
#         for k in self.book:
#             outcome.book.setdefault(k,0)
#             outcome.book[k] += self.book[k]
#         for k in other_multi_set.book:
#             outcome.book.setdefault(k,0)
#             if other_multi_set.book[k] > outcome.book[k]:
#                 outcome.book[k] = other_multi_set.book[k]
#         for k,v in outcome.book.items():
#             for i in range(v):
#                 outcome.contents.append(k)
#         return outcome
        


#!9.30
class MultiSet():   # 或者 class MultiSet():
    def __init__(self, elements = None):
        if elements==None:
            self.content=[]
            
        self.content=elements

    
    def __str__(self):
        temp=sorted(self.content)
        return '{'+str(temp)[1:len(str(temp))-1]+'}'#! 

    
    def __len__(self):
        return len(self.content)


    def add(self, element):
        self.content.append(element)

    def __contains__(self,element):
        if element in self.content:
            return True
        else:
            return False
    
    def remove(self, element):
        self.content.remove(element)
        
    
    def count(self, element):
        return self.content.count(element)
    

    def union(self, other_multi_set):
        #编写代码
        new_lst=[]
        lst=list(set(self.content+other_multi_set.content))
        for i in lst:
            x=max(self.content.count(i),other_multi_set.content.count(i))
            new_lst+=x*[i]
        return MultiSet(new_lst)   


ms1 = MultiSet([3,1,2])
ms2 = MultiSet([5,2,3,2])
print(1 in ms1)
print(4 in ms1)
print(ms1)
print(ms2)
print(len(ms1), len(ms2))
ms1.add(3)
print(ms1)
ms1.remove(1)
print(1 in ms1)
print(ms1)
print(ms1.count(3))
ms3 = ms1.union(ms2)
print(ms3)
exit()    

while True:
    exec(input())







# class HKD_Personal_Account():
#     def __init__(self, cash=0, loan=0, account=None):
#         self.cash = cash
#         self.loan = loan
#         self.account = account
#         self.kind = "港币"
    
#     def withdraw(self, money): 
#         if self.cash < money:
#             print('余额不足，操作失败')
#         else:
#             self.cash -= money
#         print(self)
    
#     def deposit(self, money): 
#         self.cash += money
#         print(self)
#     def transfer_out(self, other, money):
#         if self.cash < money:
#             print('余额不足，操作失败')
#             print(self)
#         else:
#             print('转账成功')
#             self.cash -= money
#             print(self)
#             if other.kind == "港币":
#                 other.cash += money
#             else:
#                 other.cash += 0.8*money
#                 other.sales += 0.8*money
#             print(other)
            

#     def repay_the_loan(self, money):
#         if self.cash < money:
#             print('余额不足，操作失败')
#             print(self)
#         else:
#             self.cash -= money
#             self.loan += money
#             print(f'{self.account}还款成功')
#             print(self)
#     def __str__(self):
#         return f'{self.account}账户余额：{self.cash:.2f}HK$；账户贷款：{self.loan:.2f}HK$'
# class RMB_Company_Account():
#     def __init__(self, cash=0, loan=0, account=None ,sales=0):
#         self.cash = cash
#         self.loan = loan
#         self.account = account
#         self.sales = sales
#         self.kind = "人民币"
    
#     def withdraw(self, money): 
#         if self.cash < money:
#             print('余额不足，操作失败')
#         else:
#             self.cash -= money
#         print(self)
    
#     def deposit(self, money): 
#         self.cash += money
#         print(self)
    
#     def transfer_out(self, other, money):
#         if self.cash < money:
#             print('余额不足，操作失败')
#             print(self)
#         else:
#             print('转账成功')
#             self.cash -= money
#             print(self)
#             if other.kind == "港币":
#                 other.cash += 1.25*money
#             else:
#                 other.cash += money
#                 other.sales += money
#             print(other)

#     def repay_the_loan(self, money):
#         if self.cash < money:
#             print('余额不足，操作失败')
#             print(self)
#         else:
#             self.cash -= money
#             self.loan += money
#             print(f'{self.account}还款成功')
#             print(self)
#     def __str__(self):
#         return f'{self.account}账户余额：{self.cash:.2f}￥；账户贷款：{self.loan:.2f}￥；营业额为：{self.sales:.2f}￥'
# while True:
#     exec(input())