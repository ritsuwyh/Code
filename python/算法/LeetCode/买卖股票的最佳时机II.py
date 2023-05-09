
class Solution:
    def maxProfit(self, prices: list[int]) -> int:
        #! 由于最多持有一股 所以只要第二天比前一天价格高就卖出
        #! 画一个价格曲线图更直观 即求所有的上坡之差
        ans=0
        #! 注意到第一天不能卖 所以从第二天开始循环
        for i in range(1,len(prices)):
            if prices[i]>prices[i-1]:
                ans+=prices[i]-prices[i-1]
        return ans
        