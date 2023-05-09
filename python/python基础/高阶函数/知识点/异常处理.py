
#! 自定义异常 可以自定存储相关错误信息等

class My_Error(Exception):
    def __init__(self,x,y, *args: object) -> None:
        super().__init__(*args)
        self.x=x
        self.y=y
        
def func(x,y):
    #! 我们需要明确指出什么情况下raise什么错误 这样在后面对错误进行处理的时候才能对症下药
    #! 注意监测异常的顺序就是你写判断语句的顺序
    if type(x)==str or type(y)==str:
        raise TypeError('xxxx')
    elif y!=0:
        return x/y
    else:
        raise My_Error(x,y,'abcd')#! 后面的字符串是对错误的描述
    
  
try:
    func('a',0)
except My_Error as temp:#* 这里相当于 temp=My_Error(x,y,'abcd')
    print(temp,temp.x,temp.y)#! print(temp) 会输出对错误的描述
except TypeError as te:
    print(te,'type_error')
    
    
# x,y=eval(input())
# try:
#     print(x/y)
# except Exception as s:#! 把错误赋给一个变量s
#     print('Wrong')
#     print(s)#! 把系统定义点的错误名称打印出来
#     #! 如果写下面这句话 程序就会报出错误
    #raise s
    
    
    
#! 上下文管理器
# with <expr> as <name>:
#   <suite>
    