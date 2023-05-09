

# 「秘密技巧」可以使老板在窗口大小 X 的时间内不生气。我们使用「秘密技巧」的原则是：寻找一个时间长度为 X 的窗口，能留住更多的原本因为老板生气而被赶走顾客。
# 使用「秘密技巧」能得到的最终的顾客数 = 所有不生气时间内的顾客总数 + 在窗口 X 内使用「秘密技巧」本应生气却没生气的顾客数量。
# 因此，可以把题目分为以下两部分求解：
#! 学会问题的分解
# 所有不生气时间内的顾客总数
# 在窗口 X 内因为生气而被赶走的顾客数：使用大小为 X 的滑动窗口
#! 其实也可以求出在区间内的所有人数 加上不在区间内的不生气的顾客数 在不在区间内可以用一个vis数组来标记(在更新最大人数的时候同步更新一下区间的起始点)
#! 使用一个移动区间
class Solution:
    def maxSatisfied(self, customers: list[int], grumpy: list[int], minutes: int) -> int:
        #! 特判一下如果技能范围特别广
        if minutes>=len(customers):
            return sum(customers)
        
        sum1=0
        for i in range(len(customers)):
            if grumpy[i]==0:
                sum1+=customers[i]
        
        sum2=-999#! 注意temp和sum2 两个变量不同的初始化位置
        for i in range(len(customers)-minutes+1):
            temp=0
            for j in range(i,i+minutes):
                #todo 滚动创空极其容易发生的严重的问题 索引！
        #* for i in range(len(customers)-minutes): 在这个表达式里面 i最大能取len-minutes-1
        #*     temp=0
        #*     for j in range(i,i+minutes): 在这个表达式里面j最大能取到 i+minutes-1= len-2 这显然是错误的 我们需要的是j能够取到 len-1



                if grumpy[j]==1:
                    temp+=customers[j]
            if temp>sum2:
                sum2=temp
                
        return sum1+sum2
solution=Solution()
print(solution.maxSatisfied([1,0,1,2,1,1,7,5],[0,1,0,1,0,1,0,1],3))