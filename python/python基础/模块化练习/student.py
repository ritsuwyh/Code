
from subject import*

class Student:
    student_list=[]
    def __init__(self,name,id) -> None:
        self.name=name
        self.id=id
        self.subject=[]
        Student.student_list.append(self)
    def choose_subject(self,*subject:Subject):
        for i in subject:
            self.subject.append(i.subject)
            i.student.append((self.name,self.id))
        
    @classmethod
    def print_info(cls):
        for student in cls.student_list:
            print(student.name,student.subject)
            
