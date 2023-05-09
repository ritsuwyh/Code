

def func(x):
    print(x,type(x))
    
if __name__=='__main__':#! 如果你不写这句话 那么只要你调用了test.py 他就会执行print(10) 写了这句话就不会执行了 只有执行test.py文件的时候才会执行print(10)
    print(10)