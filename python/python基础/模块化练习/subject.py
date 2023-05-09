
from teacher import*

class Subject:
    subject_list=[]
    def __init__(self,subject) -> None:
        self.subject=subject
        self.student=[]
        Subject.subject_list.append(self)
        #! 可以把teacher改为一个list 如果一科有多个人教的话
    def set_teacher(self,teacher:Teacher):
        self.teacher=teacher.name
        teacher.add_subject(self.subject)
    @classmethod
    def print_info(cls):
        for i in cls.subject_list:
            print(i.subject,i.teacher,i.student)
        