
#! 使用二分查找的前提条件是已经排好序的数组 
# #! 二分查找 可以用in代替
# def binary_search(new_lst,left,right,target):
    
#     if left==right:
#         if new_lst[left]==target:
#             return True
#         else:
#             return False
        
#     middle=(left+right)//2
#     if new_lst[middle]==target:
#         return True
#     elif target>new_lst[middle]:
#         return binary_search(new_lst,middle+1,right,target)
#     else:
#         return binary_search(new_lst,left,middle-1,target)
#todo 向一个已经排好序的数组中插入一个数字找到插入之后该数字在新数组的索引
def binary_search_index(new_lst,left,right,target):
    #! 特判1
    if target>new_lst[-1]:
        return len(new_lst)
    #! 特判2
    if target<new_lst[0]:
        return 0
    #! 递归终止条件
    if right-left==1:
        return left+1
        
    middle=(left+right)//2

    if target>new_lst[middle]:
        return binary_search_index(new_lst,middle,right,target)#!这里比二分查找改成了middle
    else:
        return binary_search_index(new_lst,left,middle,target)
    
    
lst=list(map(int,input().split()))
target=eval(input())
new_lst=sorted(lst)
print(binary_search_index(new_lst,0,len(new_lst)-1,target))