
#! 这种方法情况太多 太复杂了

#! 没有必要插入后从头到尾合并一次 可以只考虑排序后newInterval的位置
# class Solution:
#     def insert(self, intervals: list[list[int]], newInterval: list[int]) -> list[list[int]]:
#         intervals.append(newInterval)
#         intervals.sort(key=lambda x: (x[0],x[1]))
#         idx=intervals.index(newInterval)
#         if idx==0:
#             if newInterval[-1]>=intervals[-1][0]:
#                 return [[0,max(intervals[-1][-1],newInterval[-1])]]
            
#             temp=0
#             for i in range(idx+1,len(intervals)):
#                 # for i in range(2,1): 不会报错 只是什么也不输出
#                 # print(i)
#                 if intervals[i][0]>newInterval[-1]:
#                     temp=i
#                     break
#             ans_lst=[0,max(intervals[temp-1][-1],newInterval[-1])]+intervals[temp:]
#             return ans_lst
#         else:
#             if ...:
#             pass
#! x,y=[1,2] 合法 
#! for x,y in [[1,2],[2,3]]   合法
#! 见题解 插入区间 区间没有重叠的充要条件  正难则反 怎么求交集 怎么求并集
#! 遍历原lst 和newinterval没有交集的直接加入新lst 有重叠的话就先求并集 求到没有重叠的时候停止 再把其加入到lst中

#!!!那么我们应当在什么时候将区间 SS 加入答案呢？由于我们需要保证答案也是按照左端点排序的，
# todo因此当我们遇到 第一个 满足 li >right 
#!的区间时，说明以后遍历到的区间不会与 SS 重叠，并且它们左端点一定会大于 SS 的左端点。此时我们就可以将 SS 加入答案。
#!特别地，如果不存在这样的区间，我们需要在遍历结束后，将 SS 加入答案。
#! 那么

#* 遍历谁 很重要 哪个情况少就遍历谁
#! 栈的思想
class Solution:
    def insert(self, intervals: list[list[int]], newInterval: list[int]) -> list[list[int]]:
        left, right = newInterval
        placed = False
        ans = list()
        for li, ri in intervals:#* 学会这种用法 
            #! 对于原来lst中的某一个区间 他与要插入的区间只有三种关系 相交的情况复杂 就正难则反
            if li > right:
                # 在插入区间的右侧且无交集
                #! 用一个bool类型的变量 来防止之后重复添加s
                if not placed:
                    ans.append([left, right])
                    placed = True
                ans.append([li, ri])
            elif ri < left:
                # 在插入区间的左侧且无交集
                ans.append([li, ri])
            else:
                # 与插入区间有交集，计算它们的并集
                left = min(left, li)
                right = max(right, ri)
        
        if not placed:#! 注意特判！！！
            ans.append([left, right])
        return ans


