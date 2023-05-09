
#! 学习差分数组的应用 对差分数组求前缀和可以还原原来的数组
class Solution:
    def corpFlightBookings(self, bookings: list[list[int]], n: int) -> list[int]:
        nums = [0] * (n+1)
        for left, right, inc in bookings:
            nums[left] += inc
            if right < n:
                nums[right+1] -= inc
    
        for i in range(1, n+1):
            nums[i] += nums[i - 1]

#差分数组对应的概念是前缀和数组，对于数组 [1,2,2,4]，其差分数组为 [1,1,0,2]，差分数组的第 i 个数即为原数组的第 i 个元素和第 i-1 个元素的差值，也就是说我们对差分数组求前缀和即可得到原数组。


        return nums[1:]
