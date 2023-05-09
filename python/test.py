
# lst=[ i for i in range(10)]
# print(lst)
# dic={k:v for k,v in [(1,2),(3,4)]}
# print(dic)
#
# #print(lst[ [1,2,3] ])
# # # return a==b
#
# a=10
# b=10.89849
# print('%d,%.2f'%(a,b))
#
# # default arguments
# print('Hello {}, your balance is {}.'.format('Adam', 230.2346))
#
# # positional arguments
# print('Hello {0}, your balance is {1}.'.format('Adam', 230.2346))
#
# # keyword arguments
# print('Hello {name}, your balance is {blc}.'.format(name='Adam', blc=230.2346))
#
# # mixed arguments
# print('Hello {0}, your balance is {blc}.'.format('Adam', blc=230.2346))


# # #todo 三目
# # x if ... else y

# # lst=[[1,3],[6,9]]
# # for i,j in lst:
# #     print(i,j)

# #left, right =[0,1]

# #maxx=max(maxx,temp)

# x=1 if 1==2 else 2

# print(x)
# #!if not lst: 表示如果lst为空

# # def rotate(nums: list[int], k: int) -> None:
# #         """
# #         Do not return anything, modify nums in-place instead.
# #         """
# #         #! 像这种周期性的问题 我们使用模的思想
# # # 函数里的整个列表不能重新赋值，但是列表里的内容可以被修改。
# # # 除了数字和字符串不可以被修改其他都可以被修改
# #         if k%len(nums)==0:
# #             return 
# #         left_lst=nums[-(k%len(nums)):]
# #         right_lst=nums[:len(nums)-k%len(nums)]
# #         nums=left_lst+right_lst 

# # nums=[1,2,3,4,5,6,7]
# # k=3
# # rotate(nums,k)
# # print(nums)

# #ans = [0] * n

# # while 还是 for i-1 还是 i+1

# #while matrix:#! 当矩阵不为空

# #! 特殊情况能特判就特判!
# print(199999999<float('-inf'))

# lst=[1,2,3,4]
# lst[1:]=[5,6,7]
# print(lst*2)

# ! 自定义排序
# lst=['3','10','J','K','Q']
# lst.sort()
# print(lst)
# lstx=list(set(lst))
# dicx={'3':1,'4':2,'5':3,'6':4,'7':5,'8':6,'9':7,'10':8,'J':9,'Q':10,'K':11,'A':12}
# lstx=sorted(lstx,key=lambda y:dicx[y])
# print(lstx)


# lst=[1,2,3,4]
# lst.pop(-1)
# print(lst)

# from itertools import combinations
# print(list(combinations(range(3),2)))
# ! 怎么快速将txt文件的数据转换?

# import numpy as np
# square_state = np.zeros((4, 2, 2))
# print(square_state)

# dic={'a':1,'b':2}
# temp=np.array(list(dic.items()))
# x,y=temp
# print(x,y)
# # [['a' '1']]
# #  [['b' '2']]
# print(np.array(list(zip(*dic.items()))))
# # [['a' 'b']
# #  ['1' '2']]


# print(1 in {2:1,62:3}.values())


# ! 进制转换成x进制
# ! 手打过于复杂 也可使用zip函数
# dic=dict(zip(range(0,16),'0123456789ABCDEF'))
# #print(dic)
# #dic={10:'A',11:'B',12:'C',13:'D',14:'E',15:'F'}
# def func(num,x):
#     if num//x==0:
#         return dic[num%x]
#     return func(num//x,x)+dic[num%x]
#
# print(func(10,8))


# def funcx(x,word):
#     print(x)
#     word.append(x)
#     print(word)
#
# word=[]
# funcx(1,word)
# funcx(2,word)


# for else 语句
# for i in range(0, 10, 1):
#     print(i)
#     if i == 9:
#         print("stop at i==9")
#         break;
# else:
#     print("for has finished")


x=1
match  x:   
    case 1|2:
        print("match 1 or 2")
        
    case 1:
        print(1)