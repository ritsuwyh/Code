

# #! 超时
# class Solution:
#     #*给你一个长度为 n 的整数数组 nums ，请你判断在 最多 改变 1 个元素的情况下，该数组能否变成一个非递减数列。
#     #! 即等价于是否存在一个数 删之后是非递减的
#     def checkPossibility(self, nums: list[int]) -> bool:
#         temp=nums.copy()
#         for i in range(len(temp)):
#             nums.pop(i)#! 注意remove只是删去 第一个 值为value的元素 
            
#             if sorted(nums)==nums:
#                 return True
#             nums=temp.copy()
#         return False
# solution=Solution()
# print(solution.checkPossibility([2,3,3,2,4]))

#! 标答
# class Solution(object):
#     def checkPossibility(self, nums):
#         N = len(nums)
#         count = 0
#         for i in range(1, N):
#             if nums[i] < nums[i - 1]:
#                 count += 1
#                 if i == 1 or nums[i] >= nums[i - 2]:
#                     nums[i - 1] = nums[i]
#                 else:
#                     nums[i] = nums[i - 1]
#         return count <= 1

class Solution(object):
    def checkPossibility(self, nums):
        cnt=0#! cnt为改的次数
        for i in range(1,len(nums)-1):
            #! 我们知道 如果有下降 那么必然这两个数要改一个(可以用反证法理解)
            #! 显然有一个必要条件是cnt<=1 但是不是充要条件 思考 4 5 6 1 2 3 这种情况
            #! 那么我们进一步简化问题 如何对付这样的情况?
            if nums[i-1]>nums[i]:
                cnt+=1
                if cnt>=2:
                    return False
                
                #todo 出现降序 有两种情况的降序 第一种是正常降序 第二种是特殊情况
                #todo  必然要对这两个数里面的一个进行更改 每种情况的元素更改方式也有两种
                
                if  nums[i-1]>nums[i+1]:#!特殊情况降序
                    
                    if i==1:
                        #! 在这种特殊情况下 我们只能更改前面的数
                        #? 因为 更改后面的数必死 更改前面的数还有一线生机
                        nums[i-1]=nums[i]

                    else:
                        nums[i-1]=nums[i]
                #? 现在还存在一个问题 我们改后的这个数 不能打破原来的非递减顺序
                        if nums[i-1]<nums[i-2]:
                            return False
                    
                else:#! 非特殊情况降序
                    nums[i-1]=nums[i]
                    
            #! 边界特判
            if i==len(nums)-2:
                if nums[-1]<nums[-2]:
                    cnt+=1
                if cnt>=2:
                    return False        
        return True

               
                
                
