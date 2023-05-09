

#todo 自定义dict类  学会调用父类的方法
class SymmetryDict(dict):
    def __init__(self, items):
        data={}
        
        for x,y in items.items():
            data[x]=y
            data[y]=x
        super().__init__(data) #! 用父类的__init__ 方法
    
    def __setitem__(self, key, value):
        # self[key]=value
        # self[value]=key
        #! 上面这样写是错误的 必须同时改
        
        #self[key],self[value]=value,key
        #! 这样写也是错的
        #! 我们需要讨论key是否存在 分情况讨论 
        if key in self:
            #! 更改
            pre_value=self[key]
            # print(pre_value)
            super().__setitem__(key,value)
            super().__delitem__(pre_value)#! 别忘了把原来的删了
            #! 注意无法通过value值推出key值 
            super().__setitem__(value,key)
        else:#! 设置
            super().__setitem__(key,value)
            super().__setitem__(value,key)
    #     pass
        
    def __delitem__(self, key):
        value=self[key]
        if key!=value:
            
            super().__delitem__(key)
        #! 要特别注意如果k==v 那么就不能删两遍 因为第二遍找不到k了
            super().__delitem__(value)
        else:
            super().__delitem__(key)
        pass

while True:
    exec(input())
# ###########################
# 样例输入：
# d = SymmetryDict({0:0, 'dog':1})
# print(d)

# del d[0]
# print(d)
# d[0]='python'
# print(d['python'])

# d[1]=1
# print(d)
# exit()

#! 运行一下 注意调用顺序 以及在什么情况下会调用
# class Tag:
#     def __init__(self):
#         self.change={'python':'This is python',
#                      'php':'PHP is a good language'}
 
#     def __getitem__(self, item):
#         print('调用getitem')
#         return self.change[item]
 
#     def __setitem__(self, key, value):
#         print('调用setitem')
#         self.change[key]=value
 
#     def __delitem__(self, key):
#         print('调用delitem')
#         del self.change[key]
 
# a=Tag()
# print(a['php'])
# a['php']='xxx'
# del a['php']
# print(a.change)

# # coding:utf-8
# '''
#     desc：尝试定义一种新的数据类型
#           等差数列
#     author：pythontab.com
# '''
# class ArithemeticSequence(object):
#     def __init__(self,start=0,step=1):
#         print 'Call function __init__'
#         self.start=start
#         self.step=step
#         self.myData={}
#     # 定义获取值的方法
#     def __getitem__(self,key):
#         print 'Call function __getitem__'
#         try:
#             return self.myData[key]
#         except KeyError:
#            return self.start+key*self.step
#     # 定义赋值方法
#     def __setitem__(self,key,value):
#         print 'Call function __setitem__'
#         self.myData[key]=value
#     # 定义获取长度的方法
#     def __len__(self):
#         print 'Call function __len__'
#         # 这里为了可以看出__len__的作用， 我们故意把length增加1
#         return len(self.myData) + 1
#     # 定义删除元素的方法
#     def __delitem__(self, key):
#         print 'Call function __delitem__'
#         del self.myData[key]
     
# s=ArithemeticSequence(1,2)
# print s[3]  # 这里应该执行self.start+key*self.step，因为没有3这个key
# s[3] = 100  # 进行赋值
# print s[3]  # 前面进行了赋值，那么直接输出赋的值100
# print len(s) # 我们故意多加了1，应该返回2
# del s[3] # 删除3这个key
#!这些魔术方法的原理就是：当我们对类的属性item进行下标的操作时，首先会被__getitem__()、__setitem__()、__delitem__()拦截，从而进行我们在方法中设定的操作，如赋值，修改内容，删除内容等等。