
#!https://www.testalent.com/#/course/8777
#! 归并排序



#! 这道题让我想到了 合并区间 那个题 实际上那个题求的是并集 这个题我们也可以尝试把A B这两个区间合并起来然后再用类似的思想求交集
#! 但是这个思路是错的因为你要 求两个集合的交集 无法分辨哪个是哪个


#! 尝试用双指针 背下来

class Solution:
    
    def intervalIntersection(self, A: list[list[int]], B: list[list[int]]) -> list[list[int]]:
        ans = []
        i = j = 0

        while i < len(A) and j < len(B):
            # Let's check if A[i] intersects B[j].
            # lo - the startpoint of the intersection
            # hi - the endpoint of the intersection
            lo = max(A[i][0], B[j][0])
            hi = min(A[i][1], B[j][1])
            if lo <= hi:#! 说明相交 妙啊 注意这里带了等号 因为由题干 若交集为常数 写成 [λ,λ]
                ans.append([lo, hi])
                #! 那么如果不相交 谁的右端点小 消谁
            # Remove the interval with the smallest endpoint
            if A[i][1] < B[j][1]:
                i += 1
            else:
                j += 1

        return ans