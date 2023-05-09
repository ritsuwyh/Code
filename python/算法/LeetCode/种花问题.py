class Solution:#! 贪心算法
    def canPlaceFlowers(self, flowerbed: list[int], n: int) -> bool:
        count=0
        flowerbed=[0]+flowerbed+[0]#! 头和尾都加上0 减少边界条件的特判
        for i in range(1,len(flowerbed)-1):
            if flowerbed[i]==0 and flowerbed[i-1]==0 and flowerbed[i+1]==0:
                flowerbed[i]=1
                count=count+1
            if count>=n:
                return True
        return False
