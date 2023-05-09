def func(num):
    lst=[]
    if num==0:
        return [0] #! 别忘了特判
    while num>0:
        temp=num%10
        lst.append(temp)
        num//=10
        lst.reverse()#! 返回值为none 这样就是从高位到低位了 
    return lst