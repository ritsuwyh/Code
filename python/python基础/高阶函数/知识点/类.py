
#todo 1.类属性
# 利用类成员进行类级别的操作，如：
# – 对对象进行计数
#! 在init函数里面 每次调用一次init 类属性就加一
# class My_class():
#     cnt=0
#     def __init__(self,name):
#         self.name=name
#         My_class.cnt+=1

    
        
# class Product:
#     discount=0#! 这是一个类成员 可以通过 Product.discount=.. 来访问和修改
#     def __init__(self,price) -> None:
#         self.price=price
#     def calc_price(self):
#         return self.price*(1-Product.discount)



# test1=Product(0)
# test2=Product(0)
# print(test1.discount)
# print(test2.discount)
# test1.discount=100
# print(test1.discount)
# Product.discount=200
# print(test1.discount)
# print(test2.discount)
# print('----------------------------')

#!出现上述的原因是: 依次 查找绑定关系
# – 在对象的实例成员列表中查找<name>的绑定关系
# – 在对象的类成员列表中查找<name>的绑定关系


# 在此处填写代码

# while True:

#     exec(input())

# ------------------------------

# 输入样例：

# product1 = Product(100)

# product2 = Product(200)

# Product.discount = 0.1

# print(product1.calc_price())

# print(product2.calc_price())

# exit()

# 输出样例：

# 90.0

# 180.0


#* 区分 __xxx  _xxx __xxx__




#todo 2.继承 继承已有的类扩充其功能 子类可以调用父类的方法 子类也可以对父类的方法进行重写
#开闭原则：可以通过继承引入新的类，保持或者更新原有的功能（open对对象进行使用的代码（高层代码）可以保持不变（closed
class Y:
    def __init__(self,amount:int)->None:
        self.amount=amount
        
    def Y_func(self,amount):
        pass
class X(Y):
    #! 父类方法的扩展
    def Y_func_plus(self,amount):
        self.Y_func(amount+1)#! 调用从父类继承而来的方法
        #!Y.Y_func(self,amount+1) 这样写也可以 但别忘了传入一个self参数
        #! super().Y_func(amount+1) 这样也可以
    #! 有时为了避免方法调用错误 名称混淆 可以直接重写父类的方法
    def Y_func(self,amount):
        super().Y_func(amount+1)
    #! 值得注意的是 如果__init__函数发生重写，子类应负责全部数据的初始化
    def __init__(self, amount: int,name) -> None:
        super().__init__(amount) #! 用父类的__init__方法进行初始化 实际上就是插件帮你省略了几步
        self.name=name
        
        
y=Y(100)
x=X(50,'bob')
print(x.amount)

#todo 类方法 @classmethod def func(cls,...):



#todo 可以继承多个类
# 按照 NewAccount, CheckingAccount, SavingsAccount,
# Account, object这一顺序在类中寻找属性名的绑定
# class NewAccount(CheckingAccount, SavingsAccount):
#     pass