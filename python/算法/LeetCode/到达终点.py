
# #! 尝试使用dfs
# #! 正向计算 超出递归深度
# class Solution:
#     def reachingPoints(self, sx: int, sy: int, tx: int, ty: int) -> bool:
#         #! 可以将移动方法写成一个函数 因为每次移动的距离不一致 但是由于情况只有两种 就不写了
#         flag=False
#         def dfs(sx,sy,tx,ty):
#             if sx==tx and sy==ty:
#                 nonlocal flag#! 闭包别忘了写nonlocal
#                 flag=True
#                 return
            
#             # x1,y1=sx,sx+sy
#             # if x1>tx or y1>ty:
#                 #return
#             #! 这样直接写return 是不对的 因为我们需要尝试下一种可能性     return
#             # dfs(x1,y1,tx,ty)
#             # x2,y2=sx+sy,sy
#             # if x2>tx or y2>ty:
#             #     return
#             # dfs(x2,y2,tx,ty)
#             for i in range(2):
#                 if i==0:
#                     xx,yy=sx+sy,sy
#                 else:
#                     xx,yy=sx,sx+sy
                
#                 if xx>tx or yy>ty:
#                     continue
#                 dfs(xx,yy,tx,ty)
#             return       
#         dfs(sx,sy,tx,ty)
#         return flag    
# solution=Solution()
# print(solution.reachingPoints(1,1,1,1))


#!看不懂
#! 反向计算
class Solution:
    def reachingPoints(self, sx: int, sy: int, tx: int, ty: int) -> bool:
        while sx < tx != ty > sy:
            if tx > ty:
                tx %= ty
            else:
                ty %= tx
        if tx == sx and ty == sy:
            return True
        elif tx == sx:
            return ty > sy and (ty - sy) % tx == 0
        elif ty == sy:
            return tx > sx and (tx - sx) % ty == 0
        else:
            return False

