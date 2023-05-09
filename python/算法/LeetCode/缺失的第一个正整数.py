
#! 不要再循环之中一次次用count 或者in 可以用哈希表dict一遍循环来统计每个出现的次数
class Solution:
    def firstMissingPositive(self, nums: list[int]) -> int:
        #nums=list(map(int,input().split()))
        dic={}
        for num in nums:
            dic[num]=dic.get(num,0)+1
        cnt=1
        while dic.get(cnt,-1)!=-1:
            cnt+=1
        return (cnt)