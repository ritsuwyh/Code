
#! 即计算后元素减前元素的最大差值
#* 超时
# class Solution:
#     def maxProfit(self, prices: list[int]) -> int:
#         temp=0#! 因为不能获取任何利润返回0 所以我们正好初始化为0
#         for i in range(len(prices)-1):#! 注意索引 不能让i+1越界
#             if max(prices[i+1:])-prices[i]>temp:
#                 temp=max(prices[i+1:])-prices[i]
#         return temp
# solution=Solution()
# print(solution.maxProfit([7,1,5,3,6,4]))



#! 我们第i天买入股票 第j天卖出股票  那么第i天的价格必是1到j-1天最便宜的 第j天必然是 i+1到最后一天最贵的
#todo 能够在遍历中做的事情就不要用循环做!!!!! 例如求最大最小值 我们可以边遍历边更新
#! 理解!!!! 背下来 我们考虑哪天卖出 注意到最小值可以在遍历中得到 不需要 min(之前所有的价格) 因为这样实际上多了一重循环
# class Solution:
#     def maxProfit(self, prices: list[int]) -> int:
#         inf = int(1e9)
#         minprice = inf
#         maxprofit = 0
#         for price in prices:
#             maxprofit = max(price - minprice, maxprofit)
#             minprice = min(price, minprice)
#         return maxprofit

#! 自己改写的答案 
#! 实际上第一种超时的方法就是讨论了在第几天买入 但是这样我们需要求出之后的最大值 
#! 而这一种方法是讨论在第几天卖出 我们需要求出在这之前的最小值 而我们通过遍历的过程 可以算出前i-1个数的最小值
class Solution:
    def maxProfit(self, prices: list[int]) -> int:
        min_price=prices[0]
        max_profit=0
        #! 讨论在第几天卖出 第一天不能卖
        for i in range(1,len(prices)):
            profit=prices[i]-min_price
            
            #* 下面这个判断也可以写成 max_profit=max(max_profit,profit)
            #todo 要习惯max min这样的写法 少用if
            if profit>max_profit:
                max_profit=profit
    
            #todo 为了下一次循环做准备
            min_price=min(min_price,prices[i])
            
            
        return max_profit
