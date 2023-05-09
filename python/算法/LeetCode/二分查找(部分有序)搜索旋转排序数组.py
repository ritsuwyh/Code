

#todo I
# class Solution:
#     def search(self, nums: list[int], target: int) -> int:
#         if target not in nums:
#             return -1
#         else:
#             return nums.index(target)
#! 二分查找  但是这道题中，数组本身不是有序的，进行旋转后只保证了数组的局部是有序的，这还能进行二分查找吗？答案是可以的。
class Solution:
    def search(self, nums: list[int], target: int) -> int:
        if not nums:
            return -1
        l,r=0,len(nums)-1
        # 这里控制条件取等号，取等号大多是为了在while中直return mid，不取等号就跳出while返回l的值。
        while l<=r:
            mid=l+(r-l)//2
            
            # 中间值即为target，直接返回
            if nums[mid]==target:
                return mid
            
            # 左半部分是有序
            if nums[0]<=nums[mid]:
                # target落在左半部分有序区域内
                if nums[0]<=target<nums[mid]:
                    r=mid-1
                else:
                    # target落在右半部分无序区域内
                    l=mid+1
            else: # 右半部分是有序
                # target落在右半部分有序区域内
                if nums[mid]<target<=nums[len(nums)-1]:
                    l=mid+1
                else:
                    # target落在左半部分无序区域内
                    r=mid-1
        return -1

# 可以发现的是，我们将数组从中间分开成左右两部分的时候，一定有一部分的数组是有序的。拿示例来看，我们从 6 这个位置分开以后数组变成了 [4, 5, 6] 和 [7, 0, 1, 2] 两个部分，其中左边 [4, 5, 6] 这个部分的数组是有序的，其他也是如此。
# 这启示我们可以在常规二分查找的时候查看当前 mid 为分割位置分割出来的两个部分 [l, mid] 和 [mid + 1, r] 哪个部分是有序的，并根据有序的那个部分确定我们该如何改变二分查找的上下界

#todo II 有重复数字 1 0 1 1 1
class Solution:
    def search(self, nums: list[int], target: int) -> bool:
        if not nums:
            return False
        l,r=0,len(nums)-1
        while l<=r:
            # 重点在于处理重复数字
            # 左边有重复数字，将左边界右移
            #! 与I相比 只多了下面这两个while
            while l<r and nums[l]==nums[l+1]:
                l+=1
            # 右边有重复数字，将右边界左移
            while l<r and nums[r]==nums[r-1]:
                r-=1
                
            mid=(l+r)//2
            if nums[mid]==target:
                return True
            # 左半部分有序
            if nums[0]<=nums[mid]:
                if nums[0]<=target<nums[mid]:
                    r=mid-1
                else:
                    l=mid+1
            else:# 右半部分有序
                if nums[mid]<target<=nums[len(nums)-1]:
                    l=mid+1
                else:
                    r=mid-1
        return False
