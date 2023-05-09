
#! 了解其背后的思想 工厂模式 可变参数的应用 
from abc import abstractmethod, ABC

# 工厂模式
class Employee(ABC):
    """员工抽象基类，无需修改"""

    def __init__(self, name, age, gender):
        self.name = name
        self.age = age
        self.gender = gender

    @abstractmethod
    def work(self, *args):
        
        pass

    def __str__(self):
        return f"{self.__class__.__name__}: {self.name}, {self.age} years old {self.gender}"


class Engineer(Employee):
    """继承抽象基类"""
    # 填写代码，重写抽象方法: work(), 完成args求和
    #! 可变参数是可以进行遍历的 ！！！
    def work(self,*args):
        # sumx=0
        # for i in args:
        #     sumx+=i
        # return sumx
        #! 也可以这样写
        return sum(args)
    
class Accountant(Employee):
    """继承抽象基类"""
    # 填写代码，重写抽象方法: work(), 完成求args最大值
    def work(self,*args):
        
        return max(args)
class Admin(Employee):
    """继承抽象基类"""
    # 填写代码，重写抽象方法: work(), 完成求args最小值
    def work(self,*args):
        return min(args)
class EmployeeFactory:
    """定义员工工厂类"""

    @classmethod
    def create(cls, sub_class_name, *args):
        """生成员工实例的工厂方法"""
        # 填写代码
        # 当sub_class_name == 'engineer'时 返回Engineer对象
        if sub_class_name=='engineer':
            p=Engineer(*args)
            return p
        # 当sub_class_name == 'accountant'时 返回Accountant对象
        if sub_class_name=='accountant':
            p=Accountant(*args)
            return p
        # 当sub_class_name == 'admin'时 返回Admin对象
        if sub_class_name=='admin':
            p=Admin(*args)
            return p
        pass

# engineer = EmployeeFactory.create('engineer', '张三', 30, '男')

# print(engineer)

# print(isinstance(engineer, Employee))

# print(isinstance(engineer, Engineer))

# print(engineer.work(1, 2, 3))

# exit()       
while True:
    exec(input())




#! cls
# class Person(object):
#     def __init__(self, name, age):
#         self.name = name
#         self.age = age
#         print('self:', self)

#     # 定义一个build方法，返回一个person实例对象，这个方法等价于Person()。
#     @classmethod
#     def build(cls):
#         # cls()等于Person()
#         p = cls("Tom", 18)
#         print('cls:', cls)
#         return p


# if __name__ == '__main__':
#     person = Person.build()
#     print(person, person.name, person.age)