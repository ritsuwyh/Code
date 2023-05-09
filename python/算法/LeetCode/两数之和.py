
#todo 1.数组中的k-diff数对 2.缺失的第一个正整数
#! 使用dict更快!


# nums=list(map(int,input().split()))
# target=eval(input())
# #! 这道题的注意点就是在于一个数不能重复使用
# #! 已知只有一个解
# for x in nums:
#     if 2*x==target:
#         if nums.count(x)==2:
#             ans=[]
#             ans.append(nums.index(x))
#             ans.append(nums.rindex(x))
#             break#! 别忘了加break
#     else:
#         if target-x in nums:
#             ans=[]
#             ans.append(nums.index(x))
#             ans.append(nums.index(target-x))
#             break
        
# print(ans)        

# fruits = [4, 55, 64, 32, 16, 32]
# x = fruits.index(32)
# print(x)
class Solution:
    def twoSum(self, nums: list[int], target: int) -> list[int]:
        
#! 这道题的注意点就是在于一个数不能重复使用
#! 已知只有一个解
        for x in nums:
            if 2*x==target:
                if nums.count(x)==2:
                    ans=[]
                    ans.append(nums.index(x))
                    ans.append(nums.index(x,ans[0]+1,))#! 或者直接用rindex
                    break#! 别忘了加break
                else:
                    continue
            else:
                if target-x in nums:
                    ans=[]
                    ans.append(nums.index(x))
                    ans.append(nums.index(target-x))
                    break
        return ans
    
solution=Solution()
print(solution.twoSum([4,4],8)) 