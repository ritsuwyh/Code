

# #* 题目1
# n,m,k,s=eval(input())
# #! 建模 经验——总价值(目标值) 忍耐度——背包的容量 怪的种类——物体的种类 最多杀怪的数量——其他需要维护的限制条件
# #todo 先用1维的 dp数组的列数是容量 二维里面行数是物品的种类
# dp=[0 for _ in range(m+1)]
# # dp=[0]+[-99999 for _ in range(m)]
# sumx=[0 for _ in range(m+1)]
# v=[0]
# w=[0]
# for i in range(k):
#     a,b=eval(input())
#     v.append(a)
#     w.append(b)

# for i in range(1,k+1):
#     for j in range(1,m+1):
#         if j<w[i] or sumx[j-w[i]]+1>s:
#             continue
        
        
#         if dp[j]<dp[j-w[i]]+v[i]:
#             sumx[j]=sumx[j-w[i]]+1
#         dp[j]=max(dp[j],dp[j-w[i]]+v[i])
#         #!这里顺序非常重要 必须最后更新值
#         # if dp[j]<dp[j-w[i]]+v[i]:
#         #     sumx[j]=sumx[j-w[i]]+1#! 这样写是错误的!!
            
# flag=False
# for i in range(1,m+1):
#     if dp[i]>=n:
#         print(m-i)
#         flag=True
#         break
# if not flag:
#     print(-1)
# # print(dp[m-1])

# #*题目2
#todo 更换问法 求消耗x点忍耐度(1<=x<=m) 最多得到的经验值 我上面注释掉的两行就是解法 
#! 注意 如果输出的是非法值说明根本不可能消耗完x点耐久度 最后只需要特判即可 if dp[x]<0 print('...')

#! 分钱问题 体积为target_money 种类为面值的个数 求方案数量 我们可以把每个数

dp = [0 for _ in range(200)]#! 把数组开大一点
dp[0] = 1
for itm in [1, 2, 5]:
    for i in range(101):
        if dp[i]:
            dp[i + itm] += dp[i]
    
print(dp[100])


#! 完全背包问题 对于某次选择 选或者不选
#! 思考怎么初始化 
# 为了方便初始化，我们一般让 f[0][x] 代表不考虑任何物品的情况。

# 因此我们有显而易见的初始化条件：f[0][0] = 1，其余 f[0][x] = 0。

# 代表当没有任何硬币的时候，存在凑成总和为 0 的方案数量为 1；凑成其他总和的方案不存在。

#定义 f[i][j] 为考虑前 i 件物品，凑成总和为 j 的方案数量。

# lst=eval(input())
# lst=[0]+lst
# num=eval(input())
# dp=[0 for _ in range(num+1)]
# dp[0]=1
# for i in range(1,len(lst)):
#     for j in range(1,num+1):
#         if j<lst[i]:
#             continue
#         dp[j]+=dp[j-lst[i]]#! 理解这里  我们一层一层的看 第一次循环的时候只用第一种货币来组成这些数
#! 到第二次循环 我们用两个数字来组成这些数 对于每个数而言 其组成方案为 只用第一个数的方案数 加上 含第二个数的方案数
#!dp[j-lst[i]] 即表示数字j使用了第二个数字的方案数(由于dp从前往后 当我们计算到 dp[j]的时候dp[j-lst[i]]已经计算好了 dp[j-lst[i]]即为数字j-lst[i]使用前两个数字的所有方案数)
#! 第三次循环 我们用三个数字来表示 对于每个数而言 其组成方案为 只用前两个数的方案数 加上 含第三个数的方案数 .... 以此类推得出结果
# print(dp[num])
