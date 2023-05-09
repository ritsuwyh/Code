

from teacher import*
from student import*
from subject import*

t1=Teacher('Alice')
t2=Teacher('Bob')

sub1=Subject('神经网络')
sub2=Subject('计算视觉')
sub3=Subject('机器学习')

sub1.set_teacher(t1)
sub2.set_teacher(t2)
sub3.set_teacher(t2)

Teacher.print_info()
stu1=Student('Tom',211300044)
stu2=Student('lan',211300045)
stu3=Student('Andrew',211300046)

# stu1.choose_subject('神经网络','机器学习')
# stu2.choose_subject('神经网络')
# stu3.choose_subject('计算视觉')

stu1.choose_subject(sub1,sub3)
stu2.choose_subject(sub1)
stu3.choose_subject(sub2)

Student.print_info()

Subject.print_info()

