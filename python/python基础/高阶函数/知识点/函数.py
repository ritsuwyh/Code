

# mutable
# https://zhuanlan.zhihu.com/p/384032060#:~:text=%E6%9C%AC%E6%96%87%E4%BB%8B%E7%BB%8D%E4%BA%86Pyt,%E4%BB%85%E9%99%90%E5%85%B3%E9%94%AE%E5%AD%97%E5%8F%82%E6%95%B0%E3%80%82
# 函数的参数

def func1(x1,x2=1,*x3,**x4):
    print(x1)
    print(x2)
    print(x3)
    print(x4)
    
func1(1,4,2,2,2,4,a=1,b=2,c=3)


#! 函数如何运行的  global frame local frame 函数中形参和变量的作用域
#! 嵌套函数的执行顺序
def func2(x):
    x+=1
    def qaq():
        #print('内层',x)
        nonlocal x
        x+=1
        print('改变后的',x)
    qaq()
    return x
x=2
print(func2(x))
print(x)

#如果要在嵌套函数里面更改外层函数的变量要使用nonlocal,而且在内层函数nonlocal x 之前不能使用x (可以尝试一下把那行取消注释)

# assert
assert 1==2,'wrong'