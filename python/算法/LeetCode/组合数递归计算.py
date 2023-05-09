
#! 利用数学公式进行递归计算 过程完全类似于走台阶
#! Cnk=Cn-1k+Cn-1 k-1 公式使用条件 k>=1 and n>k
def comb(n,k):
    #! 递归终点
    if k==0 or k==n:
        return 1
    return comb(n-1,k)+comb(n-1,k-1)
print(comb(5,2))