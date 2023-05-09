

class Solution:
    def canArrange(self, arr: list[int], k: int) -> bool:
        #! 关键点:如果两个数的和可以被k整除 那么这两个数模k的余数的和一定能够被k整除(实际因为和不可能大于2*k 所以就是取模之后的余数和为k 或者为0)
        #! 还要注意题干有负数 注意python中负数取模的机制 好好思考一下负数的情况
        #* 一个数模k之后的范围是 [0,k-1] 我们可以用dict存储  每个数模k之后的值 所对应的次数 如果余数和为k的每组数 次数都相同 那return True
        #! 由于dict不能访问不存在的key对应的value 所以要初始化
        dic=dict.fromkeys(range(k), 0)
        for num in arr:
            dic[num%k]=dic.get(num%k,0)+1
        for i in range(k):
            if i==0:#!  余数为0的情况要特判
                if dic[0]%2!=0:
                    return False
            else:
                if dic[i]!=dic[k-i]:
                    return False
        return True
            