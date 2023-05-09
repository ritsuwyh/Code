
#! 归并两个有序数组 
# class Solution:
#     def findMedianSortedArrays(self, nums1: list[int], nums2: list[int]) -> float:
        
        
#         nums=nums1+nums2
#         nums.sort()
#         if len(nums)%2==0:
#             return (nums[len(nums)//2-1]+nums[len(nums)//2])/2
#         else:
#             return nums[len(nums)//2]
        
#! 也可以手动实现一下归并 前提是有两个有序数组
class Solution:
    def findMedianSortedArrays(self, nums1: list[int], nums2: list[int]) -> float:
        nums=[]
        p1,p2=0,0
        while p1<len(nums1) and p2<len(nums2):
            if nums1[p1]<=nums2[p2]:
                nums.append(nums1[p1])
                p1+=1
            else:
                nums.append(nums2[p2])
                p2+=1
        while p1<len(nums1):
            nums.append(nums1[p1])
            p1+=1
        while p2<len(nums2):
            nums.append(nums2[p2])
            p2+=1
            
        if len(nums)%2==0:
            return (nums[len(nums)//2-1]+nums[len(nums)//2])/2
        else:
            return nums[len(nums)//2]
