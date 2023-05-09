

#! https://blog.csdn.net/z_feng12489/article/details/105638210

#! leetcode背包总结
#*https://leetcode-cn.com/problems/last-stone-weight-ii/solution/yi-pian-wen-zhang-chi-tou-bei-bao-wen-ti-5lfv/
#! 值得注意的是 如果题目说 能装满就输出 不能装满输出特定值 这就要在初始化上下功夫了

#!基础版本
#!二维表dp[][]，dp[i][j]表示考虑前i个物品装入容量为j的背包中获得的最大价值。可以把每个dp[i][j]都看成一个背包状态。
#! 二维表的第i行表示取第i个物体背包可能的所有状态 其对应的值代表在该状态下(在前i个物体的范围内 使用了j容量)最大价值

# 我们看到的求解最优解的背包问题中，事实和桑有两种不太相同的问法。

# 要求”背包恰好装满“ 时的最优解
# 不要求背包一定要被装满时的最优解
# 我们上面所讨论的就是第2种， 不要求背包一定要被装满时的最优解。

# 一种区别这两种问法的实现方法是在初始化的时候有所不不同。

# 如果是第一种问法，要求恰好装满背包，那么在初始化时除了 d p [ 0 ] dp[0]dp[0] 为0, 其他d p [ 1... W ] 均 设 为 − ∞ dp[1...W]均设为 -\inftydp[1...W]均设为−∞ ，这样就可以保证最终得到 d p [ W ] dp[W]dp[W] 是一种恰好装满背包的最优解

# 如果并没有要求必须把背包装满，而是只希望价格尽量大，初始化时应该将d p [ 0... W ] dp[0...W]dp[0...W] 全部设为0。

# 这是为什么呢？可以这样理解：初始化的d p dpdp 数组事实上就是在没有任何物品可以放入背包时的合法状态。如果要求背包恰好装满，那么此时只有容量为0的背包可以在什么也不装的状态下被 “恰好装满” ，此时背包价值为0。其他容量的背包均没有合法的解，属于未定义的状态，所以都应该被赋值为 − ∞ -\infty−∞ 。当前的合法解，一定是从之前的合法状态推得的

# 如果背包并非必须被装满，那么任何容量的背包都有一个合法解 “什么也不装”，这个解的价值为0,所以初始化时状态的值也就全部为0了


#! 二维可以输出路径 而一维度不能
n,v=eval(input())

#! 行数为物体的数量+1  列数为背包的限重+1
dp=[[0 for __ in range(v+1)]for _ in range(n+1)]#!为了使索引和和序号对上 行数和列数都多声明了1  dp[0]无人用 正好用作初始化(dp边界)  注意双层for循环都是从1开始循环的


#todo 如果想要记录结果 那么就需要一个和dp数组一样大小的标记数组来记录都选了谁
vis=[[False for __ in range(v+1)]for _ in range(n+1)]
#! 如果还有其他的限制条件 声明一个大小和dp数组一样的数组来进行维护即可

# values=[0 for _ in range(n+1)]#! 为了脚标统一 能用上下面循环的i和j
# weights=[0 for _ in range(v+1)]

# for i in range(1,n+1):
#     value=eval(input())
#     values[i]=value
    
# for i in range(1,n+1):
#     weight=eval(input())
#     weights[i]=weight
#! 输入数据的不同的两种方式
values=[0]+list(map(int,input().split()))#! 前面的0是为了统一脚标
weights=[0]+list(map(int,input().split()))  


#! 核心代码
for i in range(1,n+1):#! 记得要从索引1开始
    for j in range(1,v+1):
        if weights[i]>j: #! 放不下
            dp[i][j]=dp[i-1][j]
        else:
            dp[i][j]=max(dp[i-1][j],dp[i-1][j-weights[i]]+values[i])#! 有两种选择 第一种是这个物体不要 第二个选择是选这个物体 其最大价值就是 选这个物体之后能余下的装的最大价值 加上这个物体的价值
            if dp[i-1][j-weights[i]]+values[i]>dp[i-1][j]:#! 说明在某一路经里面选择了这个物体
                
                vis[i][j]=True
      
                
temp=v       
for i in range(n,0,-1):#! 一件物品一件物品找
    #! 倒着遍历(原因? 贪心)寻找最后一个点是怎么来的
    if temp<=0:
        break
    if vis[i][temp]:
        print('%d'%i,end=' ')
        temp-=weights[i]
    else:
        temp-=1
        
        
print(dp[n][v])#! 最后一个元素即为最大价值 贪心 当然是限重越大价值越可能大


#todo 空间优化 滚动数组 数据量很大 无法定义这么大的二维数组
# 不难发现，每一行是从上一行算出来的，只与上一行有关系，与更前面的行没有关系。
# 那么用新的一行覆盖原来的就好了(就是一行数组进行滚动)，空间复杂度从O(NV)减少为O(V)。
#* 核心代码
#! 把二维dp改为一维dp
# for i in range(1,n+1):
#     for j in range(v,weights[i]-1,-1):

#         #!根据range的范围 等价于 进行过了下面两步骤
#         # if j<weights[i]: 
#         #     break

#         dp[j]=max(dp[j],dp[j-weights[i]]+values[i])
#! 理解为什么要倒序
#!1.f[i][j]的值只与上一行的值f[i-1][]有关 
#! 2.更新f[i][j]时，要用到上一行的旧值，而一维dp 在你操作之前里面存的就是上一行的值 
# 注意j应该逆序循环，即从后面往前面覆盖，不然会多次考虑每件物品（恰恰是完全背包的解）
# ，但我们不能重复选择已经选择的物品。不过，滚动数组覆盖掉了中间转移状态，无法倒推输出方案
# ，如果用path[][]记录就没有优化的意义了。





#todo完全背包问题 c++  #! 循环起点变了 实际上是模板的简化 就不用if判断一下了

#! 最原始的代码:


N, V = map(int, input().split())  # 物品数， 背包容量
#! 这里是先进行的初始化 然后再输入操作的 要掌握这种初始化的操作

v = [0] * (N + 1)
w = [0] * (N + 1)

for i in range(1, N + 1):
    v[i], w[i] = map(int, input().split())


f = [[0 for i in range(V+1)] for i in range(N+1)]  # 初始化全0

for i in range(1, N + 1):
    for j in range(V + 1):
        f[i][j] = f[i - 1][j]
        for k in range(1, j // v[i] + 1):#! 这重循环限制了这个背包放的最大数量
            f[i][j] = max(f[i][j], f[i - 1][j - k * v[i]] + k * w[i])

print(f[N][V])


#todo 简化操作 省略每个物品取的次数k的等价转换代码


#! 一维
# for (int i = 1; i <= n; i++)
#             for (int j = w[i]; j <= m; j++)
#                 dp[j] = max(dp[j], dp[j - w[i]] + v[i]);

#! 例题:
#!忍耐度->容量，经验值->价值，同时再维护sum[]记录个数，输出达到价值n后的最大剩余容量。
#! 例题 比普通的完全背包问题多了一个s限制条件 只需要在核心代码处增加一个判断 维护sum
#! 耐力值 杀敌数 两个限制条件
# #include<cstdio>
# #include<algorithm>
# #include<cstring>
# using namespace std;
# const int maxn = 102;
# int n, m, k, s;
# int v[maxn], w[maxn], dp[maxn], sum[maxn];
# int main() {
#     while (~scanf("%d%d%d%d", &n, &m, &k, &s)) {
#         for (int i = 1; i <= k; i++)
#             scanf("%d%d", &v[i], &w[i]);
#         memset(dp, 0, sizeof(dp));
#         memset(sum, 0, sizeof(sum));
#         for(int i=1;i<=k;i++)
#             for (int j = w[i]; j <= m; j++) {
    
#todo 下面的几行更加利于理解
#! 实际上完全等价于 for(int j=1;j<=m;j++){
#     if w[i]>j or sum[j-w[i]]+1>s:
#         continue
# }


#                 if (sum[j - w[i]] + 1 > s)continue;#! 用于维护sum 本题多了一个限制条件

#                 if (dp[j] < dp[j - w[i]] + v[i]) {
#                     dp[j] = dp[j - w[i]] + v[i];
#                     sum[j] = sum[j - w[i]] + 1;#! 维护sum
#                 }
#             }
#         int ans = -1;
#         for (int i = 1; i <= m; i++)#! 越往后空间剩余越少 价值越大 从前往后 是为了找到第一个价值够的 用了该点所在的列数的空间就达到了目标价值 即剩余的空间最多
#             if (dp[i] >= n) {
#                 ans = m - i;
#                 break;
#             }
#         printf("%d\n", ans);
#     }
#     return 0;
# }






#todo 多重背包问题
# N 件物品 ， 背包容量 V， 每件使用次数s
# 数组存入物品的体积和价值和使用次数:使用次数s[i],i = 0 , 1 , 2 , . . . , N − 1 , N i=0,1,2,...,N-1,Ni=0,1,2,...,N−1,N。

# 定义状态：f[i][j], 代表前i个物品，存入容量为j的背包里的最大价值。

# 状态转移：f [ i ] [ j ] = max ⁡ ( f [ i − 1 ] [ j − k ∗ v [ i ] ] + k ∗ w [ i ] ) , k = 0 , 1 , . . . , min ⁡ ( s i , j / / v [ i ] )
# k的范围代表，第i个物品取的次数。上限不能超过当前背包的容量,也不能超过题目限制的使用次数。


如果是二维dp 则三重循环 与完全背包的二维dp类似 

#* 一维dp 加三重循环 注意第二层循环是倒序
# N,V = map(int, input().split())

# v = [0] * (N+1)
# w = [0] * (N+1)
# s = [0] * (N+1)

# for i in range(1, N+1):
#     v[i], w[i], s[i] = map(int, input().split())
    
    
# f = [0] *(V+1)

# for i in range(1, N+1):
#     for j in range(V,v[i]-1,-1):
#         for k in range(1, min(s[i], j//v[i])+1):#! 能放的最多数量有两个限制条件 别忘了加1
#             f[j] = max(f[j], f[j-k*v[i]]+k*w[i])
            
# print(f[V])



#todo 组合背包 见leetcode网站 组合背包实际上就是完全背包加上考虑顺序 详情请见组合总和4 与零钱兑换2区分！！！



#todo  分组背包问题
#! 例子详见 掷骰子的n种方法
与01背包区分 分组背包是以组为单位，每组里面有很多元素，但是每组只能选择一个。
# 　分组背包就是把N件商品分成K组，但是每个组里的商品要么一件都不拿要么最多只能拿走一件，问你如何选择才能取得的价值最大。 其实一个骰子就是一个组 因为里面有 "面数" 个商品 

# 　首先这是一个动态规划问题，动态规划问题就要找到递归基，这个的递归基和01背包问题的差不多。

# f[k][v] = max(f[k-1][v], f[k-1][v-cost]+worth)
# 这个k是第K组 v指的是当前背包的容积，这个递归基的意思就是我们在第K组要么一件都不要那样背包容积就不会减少还是原先的V，
# 所以它的最优解肯定就是它前一组也就是K-1组的最优解，表达式就是f[k-1][v]。或者第K组我们取其中一件商品设那件商品体积为cost，价值为worth，
# 这样表达式就是 f[k-1][v-cost]+worth，我们取这两种情况的最优解就行了。


#! 如果套用求方案数的模板
# int numRollsToTarget(int d, int f, int target)
# {
#     vector<vector<int>> dp(d + 1, vector<int>(target + 1, 0));
#     dp[0][0] = 1;
#     for (int i = 1; i <= d; i++)#! 1层循环组数
#         for (int j = 1; j <= target; j++) #!2层循环背包容量
#             for (int k = 1; k <= f ; k++) #!3层循环每组内部的商品
#                 if j<k:
#                     continue
#                 dp[i][j] += dp[i - 1][j - k];
#     return dp[d][target];
# }




#* 小小的总结一下 三重循环的有多重背包 分组背包 
#* 倒序循环的有0-1背包第二层循环  多重背包第二层循环
#* 用二维dp的只有分组背包 其余都是一维dp



#https://leetcode-cn.com/problems/last-stone-weight-ii/solution/yi-pian-wen-zhang-chi-tou-bei-bao-wen-ti-5lfv/