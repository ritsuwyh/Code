import functools
class Team(object):
    def __init__(self,name,score,time):
        self.name=name
        self.score=score
        self.time=time
    #def print_name(self):
    #    print(self.name)
def cmp(x,y):
    if x.score>y.score:
        return -1
    elif x.score==y.score and x.time<y.time:
        return -1
    elif x.score==y.score and x.time==y.time and x.name<y.name:
        return -1
    return 0
def main():
    n=eval(input("请输入队伍数量:"))
    l=[]
    for i in range(n):
        name=input("请输入名字:")
        score=int(input("请输入分数:"))
        time=int(input("请输入时间:"))
        x=Team(name,score,time)
        #print(x.name)
        l.append(x)
    l.sort(key=functools.cmp_to_key(cmp))
    for i in l:
        print(i.name) #调用对象的方法 在class内部 用self.xxxx  class外部用 对象名.函数名
main()