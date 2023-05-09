
#! 一种分治递归的思想 二分查找 归并排序 以ops为分界线 计算左边表达式 右边表达式 最后合
def diffWaysToCompute(input):
        # 如果只有数字，直接返回
        if input.isdigit():#! 注意在递归函数中 每一层的res都不一样 
            return [int(input)]
        
        
        #! 返回值类型要一致 要么都有返回值 要么就都没有

        res = []
        for i, char in enumerate(input):#! 学习enumerate函数
            if char in ['+', '-', '*']:
                # 1.分解：遇到运算符，计算左右两侧的结果集 注意是集合！！！ 
                # 2.解决：diffWaysToCompute 递归函数求出子问题的解
                left = diffWaysToCompute(input[:i])
                right =diffWaysToCompute(input[i+1:])
                # 3.合并：根据运算符合并子问题的解
                #! 这里怎么合并的十分关键 双层循环组合两个结果集
                for l in left:
                    for r in right:
                        if char == '+':
                            res.append(l + r)
                        elif char == '-':
                            res.append(l - r)
                        else:
                            res.append(l * r)

        return res

print(diffWaysToCompute('1*3+4*5'))
