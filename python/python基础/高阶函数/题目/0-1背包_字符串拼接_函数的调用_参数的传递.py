
#! 仔细思考你每次传入的参数值

#! 见oj题目说明

#! 其实这个 subset_search 就是一个 求子集 加一个每次求出子集的时候条件判断一下 

def subset_search(item_list, condition, current_result=[], current_index=0):
    '''This function searches all subsets of item_list and check whether there is one or more subset satisfies the condition.'''
    if current_index == len(item_list):
        return condition(current_result)

    # case1: include the current item
    result1 = subset_search(item_list, condition, current_result, current_index + 1)

    # case2: does not include the current item
    new_result = current_result.copy()
    new_result.append(item_list[current_index])

    result2 = subset_search(item_list, condition, new_result, current_index + 1)

    return result1 or result2
#! 其实这个就是一个全排列 加上一个条件判断
def permutation_search(item_list, condition, current_result=[]):
    
    '''This function searches all permutation of item_list and check whether there is one or more permutation satisfies the condition.'''
    if len(item_list) == 0:
        return condition(current_result)

    result = False
    for item in item_list:
        remaining_items = item_list.copy()
        new_result = current_result.copy()
        new_result.append(item)
        remaining_items.remove(item)
        result = permutation_search(remaining_items, condition, new_result) or result
    return result

def zero_one_bag(item_list, target):#! 注意到condition调用的时候只传入了一个参数 而他条件判断必须要target 所以要将 target作为默认参数传进去
#! 实际上这个方法就是暴力 枚举所有的子集
        # 在此处填写代码
        def my_condition(item_list,targetx=target):
            sumx=0
            for i in item_list:
                sumx+=i
                
            #! 下面也可以写成 return sumx==targetx
            
            if sumx==targetx:
                return True
            else:
                return False
            
        return subset_search(item_list,my_condition)
        
        
def string_composion(item_list, target):#! 求子集 把每一个子集全排列 如果有符合条件的return True
    #! 自己写 不能用in函数 尝试用dfs和切片
        # 在此处填写代码
        def my_condition(item_list,targetx=target):
            
            def tiaojian(item_listx=item_list,targety=targetx):#! 这里的item_listx=item_list应该可以不用设置默认参数
                if ''.join(item_listx)==targety:
                    return True
                else:
                    return False
            #! 第二步再写下面这句话 然后补充条件函数    
            if permutation_search(item_list,tiaojian):
                return True
            else:
                return False
        #! 思考顺序应该是先写下面这句话 然后补充条件函数
        return subset_search(item_list,my_condition)#! 如果有一个子集 满足他的全排列的join是目标字符串 return True 
              
while True:
    exec(input())


    
# 样例输入：
# item_list = [1, 2, 3, 4, 5]
# target = 10
# print(zero_one_bag(item_list, 10))
# item_list = ['ab', 'abc', 'grth', 'th', 'd']
# target = 'grthabcd'
# print(string_composion(item_list, target))
# exit()
# 样例输出：
# True
# True
myDict = {'name': 'John', 'country': 'Norway'}
mySeparator = 'TEST'
x = mySeparator.join(myDict)
print(x)

#!   ''.join()  
