
#! 注意本题 1,3   3,1 是一样的 所以我们要保证符合条件的数对之和要不一样!
class Solution:
    def findPairs(self, nums: list[int], k: int) -> int:
        #! 遇事不决先排序
        
        nums=sorted(list(nums))
        #! 为了防止用in 时间长 我们用dict

        dic={}
        for i in nums:
            dic[i]=dic.get(i,0)+1
        cnt=0
        ans_pair=[]
        for x in nums:
            dic[x]-=1#! 这个数不能再用了 讨论完这个数 这个数就没用了 所以就相当于不存在 
            if dic.get(x+k,0)!=0 and x+x+k not in ans_pair:#! 后面这个条件是为了同一个数字出现多次的情况
                cnt+=1
                ans_pair.append(x+x+k)
            if dic.get(x-k,0)!=0 and x+x-k not in ans_pair:
                cnt+=1
                ans_pair.append(x+x-k)
        return cnt     



        