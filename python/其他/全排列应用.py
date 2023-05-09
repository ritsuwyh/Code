from itertools import permutations
num_lst=list(eval(input()))
if num_lst[-1]>num_lst[-2]:
    num_lst[-1],num_lst[-2]=num_lst[-2],num_lst[-1]
    print(num_lst)
else:
    num_tuple=tuple(num_lst.copy())

    #print(num_tuple)
    num_lst.sort()

    lst=list(permutations(num_lst))
    x=lst.index(num_tuple)
    if x==len(lst)-1:
        print(list(lst[0]))
    else:
        print(list(lst[x+1]))
    #print(lst)


# from itertools import permutations


# num_lst=list(eval(input()))
# num_tuple=tuple(num_lst.copy())
# #print(num_tuple)
# num_lst.sort()
# lst=list(permutations(num_lst))
# x=lst.index(num_tuple)
# if x==len(lst)-1:
#     print(list(lst[0]))
# else:
#     print(list(lst[x+1]))
# #print(lst)

