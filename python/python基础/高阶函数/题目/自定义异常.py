
# 在此处填写代码
# your code here
class OverLengthException(Exception):
    
    pass

class BelowLengthException(Exception):
    pass

class UpperCaseException(Exception):
    pass

def name_test(name, max_length, min_length):
    
    x=name.lower() #! 判断是否有大写字母 
    
    if len(name)>max_length:
        raise OverLengthException('你输入名字长度为%d，最大长度为%d'%(len(name),max_length))
    
    elif len(name)<min_length:
        raise BelowLengthException('你输入名字长度为%d，最小长度为%d'%(len(name),min_length))
    elif x!=name:
        raise UpperCaseException('你的输入包含大写的字母')
    
    
def input_name(test_func):
    # 捕获并处理异常
    name=input()
    try:
        test_func(name)
        print(name)
    except OverLengthException as OE:
        print(OE)
    except BelowLengthException as BE:
        print(BE)
    except UpperCaseException as UE:
        print(UE)
      
        

from functools import partial
test_func = partial(name_test, max_length=6, min_length=4)#! partial 偏函数
#! 这里test_func 是一个新的函数 

exec(input())