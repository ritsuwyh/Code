
#! 在定义函数的时候可以声明类型 类似于leetcode
#! 统计单词数量 模板 看笔记 还有笔记上求list嵌套层数的题 递归 (用栈似乎也可以?) 求某一层的所有元素

#! n行 用map作用于每一行 求每一行的dic 然后用reduce实现所有n行字典的合并


#todo 学习 collections.Counter 
def map_func(line:str)->dict:
    #!.upper()的用法
    # txt = 'Hello my friends'
    # x = txt.upper()
    # print(x)
    dic={}
    #! 这个去掉标点符号根据题干 看加不加
    # for i in line:
    #     if not i.isalnum():
    #         line=line.replace(i,' ')
    line=line.lower()
    lst=line.split()
    for word in lst:
        dic[word]=dic.get(word,0)+1
    return dic

def reduce_func(count_dict1:dict, count_dict2:dict)->dict:
    for i in count_dict1.keys():
        if i in count_dict2.keys():
            count_dict1[i]+=count_dict2[i]
    count_dict2.update(count_dict1)#! 注意顺序
    #! 别忘了写返回值
    return count_dict2


from functools import reduce

n = int(input())

input_lines = []

for _ in range(n):

    input_lines.append(input())

# Map

map_out = map(map_func, input_lines)#!map_out 里面的每一个元素都是dict

# Reduce
#! reduce 的返回值依据 传入reduce的函数而定
reduce_out = reduce(reduce_func, map_out)

assert isinstance(reduce_out, dict)

while True:

    exec(input())
#print(reduce_out)






#! 分别运行一下一下程序 看看结果

# map_out=list(map(map_func,[[1],[2],[3]])) 
# print(map_out)
# map_out=map(map_func,[[1],[2],[3]])
# print(map_out)
