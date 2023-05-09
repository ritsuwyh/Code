
class Vehicle:  # 交通工具
    def run(self):
        print(f"{self.__class__.__name__} running")


class FlyableMixin:
    def fly(self):
        '''
        复杂的飞行相关代码        
        '''
        print(f"{self.__class__.__name__} flying")

# 在此处填写代码，补充完成各个类
# CivilAircraft, Helicopter, Car
class CivilAircraft(Vehicle,FlyableMixin):
    def run(self):
        super().run()
        super().fly()
        
class Helicopter(Vehicle,FlyableMixin):#! 别忘了打Vehicle
    def run(self):
        super().fly()
        
class Car(Vehicle):
    def run(self):
        super().run()    
#测试用代码，请不要改动
while True:
    exec(input())


# 样例输入：
CivilAircraft().run()
Car().run()
print(hasattr(CivilAircraft, "fly"))
print(Vehicle in CivilAircraft.__bases__)
exit()

# 样例输出：
# CivilAircraft running
# CivilAircraft flying
# Car running
# True
# True