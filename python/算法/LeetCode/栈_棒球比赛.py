
#! 想这种弹出上一次元素的题 我们可以使用栈
class Solution:
    def calPoints(self, ops: list[str]) -> int:
        stk=[]
        for i in range(len(ops)):

            if ops[i]=='C':
                stk.pop()
            elif ops[i]=='D':
                stk.append((stk[-1])*2)
            elif ops[i]=='+':
                stk.append((stk[-1])+(stk[-2]))
            else:#! 最难判断的放到最后面
                stk.append(int(ops[i]))
        return sum(stk)
        
        
solution=Solution()
print(solution.calPoints(["5","-2","4","C","D","9","+","+"]))
# print('-1'.isdigit()) 结果是False
#! isdigit 函数只能辨别正整数,对小数和负数的判断都出现了错误
    