


#! 双指针 我们很容易得到公式 min(nums[L],nums[R])*(R-L)
#! 别无他法 min(...)我们不知道 但是我们可以让区间长度尽可能大 所以从最大的区间开始找 
#* 有点类似于最长回文子串 外层for区间长度 但是那个题用dp可以记录数据 而这道题如果那么做知识单纯的二重循环
#! 感觉这个移动有点博弈论的味了，每次都移动自己最差的一边，(数值较小的一边)
# 虽然可能变得更差，但是总比不动（或者减小）强，动最差的部分可能找到更好的结果
# ，但是动另一边总会更差或者不变 因为你取的是min() ，兄弟们，这不是题，这是人生，逃离舒适圈！！
# （这解释我觉得无敌了，哈哈哈）
class Solution:
    def maxArea(self, height: list[int]) -> int:
        l, r = 0, len(height) - 1
        ans = 0
        while l < r:
            area = min(height[l], height[r]) * (r - l)
            ans = max(ans, area)
            if height[l] <= height[r]:#! 谁矮动谁 尝试改变短板
                l += 1
            else:
                r -= 1
        return ans
