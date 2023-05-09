


class Student(object):
    def __init__(self,name,chinese,math,english,science):
        self.name=name
        self.chinese=chinese
        self.math=math
        self.english=english
        self.science=science

    
def main():
    n=eval(input("请输入学生人数:"))
    stu_lst=[]
    for i in range(n):
        lst=input().split()
        stu=Student(lst[0],int(lst[1]),int(lst[2]),int(lst[3]),int(lst[4]))
        sumscore=int(lst[1])+int(lst[2])+int(lst[3])+int(lst[4])
        stu.sumscore=sumscore
        stu_lst.append(stu)
    stu_lst.sort(key=lambda stu:stu.chinese,reverse=True)
    for i in stu_lst[0:4]:
        print(i.name,end=" ")
    stu_lst.sort(key=lambda stu:stu.sumscore,reverse=True)
    for i in stu_lst[0:4]:
        print(i.name,end=" ")
main()