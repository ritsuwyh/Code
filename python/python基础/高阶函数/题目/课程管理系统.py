
#! 以学科为主体 以学生为主体 
class SubjectSystem:#! 写一些学科共有的方法

    
    def __init__(self,pos='any_pos',time='any_time',people_chosen=0) -> None:
        self.pos=pos
        self.time=time
        self.people_chosen=people_chosen
        self.people_in_class=[]
        
    def pos_set(self,pos:str):
        self.pos=pos
        #for
    
    def time_set(self,time:str):
        self.time=time
    
    def __str__(self):#! 用于打印课程基本信息
        return '上课地点为:%s 上课时间为:%s 上课人数为:%d'%(self.pos,self.time,self.people_chosen)
    
    def print_stu_in_class_inf(self):#! 打印上这个课的学生的具体信息
        for x in self.people_in_class:
            print(x.name,x.stu_id)
        
    
class English(SubjectSystem):#! 继承了类属性 sum_people_chosen
    pass
    #! 一些有关英语类的信息 

class Math(SubjectSystem):
    pass

english_class1=English('仙1 201','8:00~9:00')

english_class2=English('仙1 301','8:00~9:00')

English_classes=[english_class1,english_class2]

math_class1=Math('逸B 111','2:00~3:00')

math_class2=Math('逸B 112','2:00~3:00')

Math_classes=[math_class1 , math_class2]

#! 一些初始化信息...

class Student:
    def __init__(self,name:str,stu_id:str) -> None:
        self.name=name
        self.stu_id=stu_id
        self.chosen_class={'English':None,'Math':None}
        
    def chose_subject(self,subject,sub_cla:SubjectSystem):
        self.chosen_class[subject]=sub_cla
        sub_cla.people_chosen+=1
        sub_cla.people_in_class.append(self)#! 直接把Student对象放入
        
    def print_chosen_subject_inf(self,subject:str):
        if self.chosen_class[subject]!=None:
            print(self.chosen_class[subject])
        else:
            print("未选修这门课")
        
    def __str__(self):#! 只能返回str类型!!
        temp_lst=[]
        temp_lst.append(self.name)
        temp_lst.append(self.stu_id)
        for i,j in self.chosen_class.items():
            if j!=None:
                lst=[]
                lst.append(i)
                lst.append(j.pos)
                lst.append(j.time)
                lst.append(j.people_chosen)
                temp_lst.append(lst.copy())
        return str(temp_lst)
    


stu1=Student('bob','211300044')
stu1.chose_subject('English',english_class1)
english_class1.print_stu_in_class_inf()

stu1.print_chosen_subject_inf('Math')
print(stu1)
print(english_class1)        

    