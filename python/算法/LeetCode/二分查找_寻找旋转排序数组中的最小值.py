
#todo I
class Solution:
    def findMin(self, nums: list[int]) -> int:
        #return min(nums)
        #! 题干要求二分查找 时间复杂度为 O(log n) 
        l=0
        r=len(nums)-1
        #! 我们的目的属实找的两段有序的交接点
        #todo 二分查找有没有等号十分重要
        #! 先特判一下特殊情况 旋转完还是原来的数组
        if nums[0]<=nums[-1]:#! 注意这里有等号 因为要考虑只有一个元素的情况
            return nums[0]
        
        
        while l<=r:
            mid=(l+r)//2

            if nums[mid-1]>=nums[mid]:
                return nums[mid]
            if nums[mid]>=nums[0]:#说明左面有序 以nums[0]为标杆 而不是以nums[l]为标杆
                #! 而且需要带等号 要考虑自己和自己比较的特殊情况
                l=mid+1
            else:
                r=mid-1
#todo II
#! 有重复数字!
class Solution:
    def findMin(self, nums: list[int]) -> int:
        n=len(nums)
        left=0
        right=n-1
        # 这里控制条件没取等号，取等号大多是为了在while中直return mid，不取等号就跳出while返回l的值。
        while left<right:#! 无法在循环内部得到返回值 所以要用< 在循环外才return
            mid=left+(right-left)//2
            if nums[mid]>nums[right]:
                # 中间数字大于右边数字，比如[3,4,5,1,2]，则左侧是有序上升的，最小值在右侧
                left=mid+1
            elif nums[mid]<nums[right]:
                # 中间数字小于等于右边数字，比如[6,7,1,2,3,4,5]，则右侧是有序上升的，最小值在左侧
                right=mid
            else:
                # 中间数字等于右边数字，比如[2,3,1,1,1]或者[4,1,2,3,3,3,3]
                # 则重复数字可能为最小值，也可能最小值在重复值的左侧
                # 所以将right左移一位
                right-=1
        return nums[left] 
    

        
        