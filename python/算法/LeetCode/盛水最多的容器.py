class Solution:
    def maxArea(self, height: list[int]) -> int:
        l=0
        r=len(height)-1
        ans=min(height[l],height[r])*(r-l)
        while l<r:
            if height[l]<height[r]:
                l+=1
            else:
                r-=1
            ans=max(min(height[l],height[r])*(r-l),ans)
        return ans