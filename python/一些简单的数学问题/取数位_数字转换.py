
#! 进制转换 递归 转换他 我只需要转换前 n-1位再合并上最后一位
# def toStr(n,base):
#     """进制转换,base是进制参数"""
#     convertString = "0123456789ABCDEF"#! 有的时候也可以用字符串来打表
#     if n < base:
#         return convertString[n]
#     else:
#         return toStr(n//base,base) + convertString[n%base]
 
# result = toStr(123,16)
# print(result)

#!ord chr
    
# #! 十进制转换到n进制 模n取余法  只有16进制需要打一个字典
# dic=dict(zip(range(16),['0','1','2','3','4','5','6','7','8','9','A','B','C','D','E','F']))
# def func(n,base):
#     s=''#! 直接用str不用list 省的之后.join 
#     if n==0:#! 别忘了特判0
#         return dic[0]
#     while n>0:#! 有点类似于取位数
#         x=n%base
#         s=s+dic[x]
#         n//=base
#     return s[::-1]#! 别忘了倒着
# n,base=eval(input())      
# print(func(n,base))


#! 取带基的位数
    # def divide(x):
    #     nums=[]
    #     base=1
    #     while x>0:
    #         temp=x%10
    #         x//=10
    #         nums.append(temp*base)
    #         base*=10
    #     return nums[::-1]


#! 罗马数字转换 
#! 先不考虑特殊情况 思考怎么做 抽象太过复杂那就if暴力判断
# !特殊情况只需要特判 写一个特判函数 必须要循环特判！！！
# def special_check():
#     while True:#! 特殊情况可能会连着!!!!
#         global number
#         if number == 4:
#             print("IV")
#             number -= 4
#             break
#         elif number == 9:
#             number -= 9
#             print("IX")
#             break
#         elif number >= 40 and number <= 49:
#             print("XL",end='')
#             number -= 40
#         elif number >= 90 and number <= 99:
#             print("XC",end='')
#             number -= 90
#         elif number >= 400 and number <= 499:
#             print("CD",end='')
#             number -= 400
#         elif number >= 900 and number <= 999:
#             print("CM",end='')
#             number -= 900
#         else:
#             break
# number = input()
# number = int(number)
#todo 下面的可以用for循环简化 写一个lst=[1000,500,100,50,5,1] for i in lst:

# m = number//1000
# number %= 1000
# print("M"*m,end='')
# special_check()
# d = number//500
# number %= 500
# print("D"*d,end='')
# special_check()
# c = number//100
# number %= 100
# print("C"*c,end='')
# special_check()
# l = number//50
# number%= 50
# print("L"*l,end='')
# special_check()
# x = number//10
# number %= 10
# print("X"*x,end='')
# special_check()
# v = number//5 
# number %= 5
# print("V"*v,end='')
# special_check()