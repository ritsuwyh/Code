

class My_Set:
    def __init__(self,item:list):
        self.item=list(set(item))
        self.start=0
        self.temp=sorted(self.item,reverse=True)
    def __iter__(self):
        return self
    def __next__(self):
        if self.start<len(self.item):
            ans=self.temp[self.start]
            self.start+=1
            return ans
        else:
            self.start=0#! 这里必须写 
            raise StopIteration

setx=My_Set([1,2,3,3,0,4,4,4,5])
for i in setx:
    print(i)
xx=[i for i in setx]
print(xx)
yy=list(map(str,xx))
print(yy)

# class MyRange(object):
#         def __init__(self, end):
#             self.start = 0
#             self.end = end
# #         #! 可迭代对象必须要有 __iter__ 和 __next__ 
# # 什么是迭代器？
# # – 具有__next__()方法的对象
# #  什么是可迭代对象？
# # – 具有__iter__()方法，且返回的是迭代器的对象
#         def __iter__(self):
#             return self
#         def __next__(self):
#             if self.start < self.end:
#                 ret = self.start
#                 self.start += 1
#                 return ret
#             else:
#                 raise StopIteration#! 以抛出异常的形式表示遍历结束