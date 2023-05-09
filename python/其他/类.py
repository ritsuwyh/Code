class Person(object):
    def __init__(self,name,age,gender):
        self.name=name
        self.age=age
        self.gender=gender
    def printinf(self):
        #!复习.format函数
        print("姓名为:{name} 年龄为:{age} 性别为:{gender} ".format(name=self.name,age=self.age,gender=self.gender))
        #print("{} {} {}".format(self.name,self.age,self.gender))

class Student(Person):
    def __init__(self, name, age, gender,college,classes):
        super().__init__(name, age, gender)
        self.college=college
        self.classes=classes
    def learn(self,)
    pass
class Teacher():
    pass
def main():
    
    pass
main()
       