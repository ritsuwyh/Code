

#! 这种栈之类的数据结构 我们使用的时候必须特判是否为空   对数组进行操作的时候也要注意脚标的范围判断
#! 灵活使用lst-tuple 和 dictionary
#! 背下来
valid=[('(',')'),('[',']'),('{','}')]#! 设定一个匹配规则
dic={'(':1,'[':2,'{':3}#! 设定一个优先级顺序

#! 每一次访问栈顶元素都要判断栈是否为空
def match(s,stack):#! 这里写了一些stack=[]是为了防止重复调用时出现旧数据
    for i in s:
        if i in ['(','[','{']: #! 这句话等价于i=='(' or ...
            
            if len(stack)==0:#! 这句话是在判断是否为空
                stack.append(i)
            else:
                if dic[stack[-1]]>=dic[i]:#! 我们在放左括号的时候要注意顺序
                    stack.append(i)
                else:
                    stack=[]
                    return False
        else: 
            if len(stack)==0:
                stack=[]
                return False
            else:
                if (stack[-1],i) not in valid:
                    stack=[]
                    return False
                else:
                    stack.pop()
                    
    if len(stack)!=0:#! 最后要判断还剩没剩元素
        stack=[]
        return False
    else:
        stack=[]
        return True


s=input()
stack=[]
print(match(s,stack))

