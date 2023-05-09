
#! 强制类型转换 约分 模拟我们分数加法的过程 先通分再加 再约分
def gcd(a,b):#! 传入的顺序无所谓
    if b==0:
        return a
    return gcd(b,a%b)

#todo 类型转换函数
def fraction(num):
    if isinstance(num,int):
        
        return Fraction(num,1)
    
    elif isinstance(num,float):
#! 方法: 获取float的整数部分和小数部分 
# a=input()
# x,y=a.split (’.’)
# print(‘整数{}小数{}’.format(x,int(y)//1))
        num=str(num)
        a,b=num.split('.')
        xx=int(a+b)
        lenx=len(b)
        
        aa=Fraction(xx,pow(10,lenx))
        aa.simplify()
        return aa
    else:#! 本身是分数类就不用动
        return num
    
    
class Fraction:
    #todo 约分
    def simplify(self):
        x=gcd(self.up,self.down)
        self.up=self.up//x
        self.down=self.down//x
    
    
    def __init__(self,up:int,down:int):
        self.up=up
        self.down=down
        self.simplify()


    #todo 加减乘除重写
    
    def __add__(self,other:any):
        yy=fraction(other)
        lcm=self.down*yy.down//gcd(self.down,yy.down)
        temp1=lcm//self.down
        temp2=lcm//yy.down
        
        ff=Fraction(temp1*self.up+temp2*yy.up,lcm)
        ff.simplify()
        return ff
    
    def __sub__(self,other:any):
        yy=fraction(other)
        lcm=self.down*yy.down//gcd(self.down,yy.down)
        temp1=lcm//self.down
        temp2=lcm//yy.down
        
        ff=Fraction(temp1*self.up-temp2*yy.up,lcm)
        ff.simplify()
        return ff
        
    def __mul__(self,other:any):
        yy=fraction(other)
        ff=Fraction(self.up*yy.up,self.down*yy.down)
        ff.simplify()
        return ff
    
    def __truediv__(self,other:any):
        yy=fraction(other)
        ff=Fraction(self.up*yy.down,self.down*yy.up)
        ff.simplify()
        return ff
    
    def __str__(self):
        return '%d/%d'%(self.up,self.down)
    
    
f1=Fraction(1,2)
f2=Fraction(2,5)
f3=fraction(1.8)
f4=fraction(Fraction(1,10))
print(f1+f2,f1-f2,f1*f2,f1/f2)
print(f3)
print(f3+f4)
print(f1+1.25)
    
