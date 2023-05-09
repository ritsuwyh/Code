
#! 其实不在原来的数组上面更改 十分简单 只需要去重模型的变形 if ans.count(x)<k: ans.append(x) 这种写法可以进一步改进为使用dict

#* https://leetcode-cn.com/problems/remove-duplicates-from-sorted-array-ii/solution/gong-shui-san-xie-guan-yu-shan-chu-you-x-glnq/
#! 数据有序，相同元素保留 k 位    快慢指针 
class Solution:
    def removeDuplicates(self, nums: list[int]):
        def solve(k):
            u = 0
            for x in nums:
                if u < k or nums[u - k] != x:
                    nums[u] = x
                    u += 1
            #!return nums 这样写是错误的
            return nums[:u] #! 这样才对 因为你后面的元素没有被覆盖 所以要剪掉
        return solve(1)#! 这里的2可以被更改为任意值
solution=Solution()
print(solution.removeDuplicates([1,1,1,1,3,4,4,5,5,6,6,7]))

#! 别忘了 能排序先排序