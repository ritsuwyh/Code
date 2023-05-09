


class Teacher:
    teacher_list=[]
    
    # @classmethod
    # def print_teacher_list(cls):#!cls 就是类本身
    #     print(cls.teacher_list)
        
    def __init__(self,name):
        
        self.name=name
        self.subject=[]
        Teacher.teacher_list.append(self)
    def add_subject(self,subject):
        self.subject.append(subject)
        
    @classmethod
    def print_info(cls):
        for teacher in cls.teacher_list:
            print(teacher.name,teacher.subject)
            
# teacher1=Teacher('bob')
# teacher2=Teacher('aa')
# Teacher.print_info()