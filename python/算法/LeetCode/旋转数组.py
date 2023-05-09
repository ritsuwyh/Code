
class Solution:
    def rotate(self, nums: list[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        #! 像这种周期性的问题 我们使用模的思想
#! 函数里的整个列表不能重新赋值，但是列表里的内容可以被修改。
# 除了数字和字符串不可以被修改其他都可以被修改
        # if k%len(nums)==0:
        #     return 
        # left_lst=nums[-(k%len(nums)):]
        # right_lst=nums[:len(nums)-k%len(nums)]
        # nums=left_lst+right_lst
        #! 上面的写法在函数中是错的 函数里面只能一个个元素修改
        k=k%len(nums)
        temp_lst=nums.copy()
        for i in range(len(nums)):
            nums[i]=temp_lst[-k+i]
            
    
#! 下面是方法2 空间复杂度小
        # def reverse(left,right):
        #     while left<right:
        #         nums[left],nums[right]=nums[right],nums[left]
        #         left+=1
        #         right-=1
        # n=len(nums)
        # # 向右移动的位置k可能会大于n，因此对n取余
        # k=k%n
        # if k==0 or n<2:
        #     return 
        # # 以此为例：nums = [1,2,3,4,5,6,7], k = 3
        # # 先整个数组反转：[7,6,5,4,3,2,1]
        # reverse(0,n-1)
        # # 前k个反转：[5,6,7,4,3,2,1]
        # reverse(0,k-1)
        # # 后n-k个反转：[5,6,7,1,2,3,4]
        # reverse(k,n-1)

