
class Solution:
    def summaryRanges(self, nums):
        ans_lst=[]
        #vis=[False for _ in range(len(nums))]
        nums.sort()#! 遇事不决先排序
        
        # for i in range(len(nums)):
        #     if vis[i]:
        #         continue
        #     else:
        #         vis[i]=True
        #         temp1=nums[i]
        #         temp2=None#! 以后 初始值 设为None
        #         while i+1<len(nums) and nums[i+1]-nums[i]==1:#! 这种的必须要先判断脚标合法性
        #             temp2=nums[i+1]
        #             vis[i+1]=True
        #             i+=1
        #         if temp2==None:
        #             ans_lst.append(str(temp1))
        #         else:
        #             ans_lst.append("%d->%d"%(temp1,temp2))
        
        #? 我们要根据实际情况 确定使用i-1(后一个数与前一个数相比) 还是 i+1(前一个数与后一个数相比) 来遍历
        i=0
        while i<len(nums):
            l=nums[i]
            r=None
            while  i+1<len(nums) and nums[i+1]-nums[i]==1:#! 我说过什么？？？ 索引判断要放到前面！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！
                r=nums[i+1]
                i+=1
            if r==None:
                ans_lst.append(str(l))
                
            else:
                ans_lst.append("%d->%d" %(l,r))
            i+=1
        return ans_lst
        
        
        #return ans_lst
solution=Solution()
lst=solution.summaryRanges([0,2,3,4,6,8,9,11])
print(lst)