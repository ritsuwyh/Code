
#todo 递归实现
ans_lst=[]

def func(lst,step,target_step):
    if step==target_step:
        for i in lst:
            if isinstance(i,int):
                ans_lst.append(i)
        return
    for i in lst:
        if isinstance(i,int):
            continue
        if isinstance(i,(list,tuple)):
            func(i,step+1,target_step)
 

func([1,2,[1,2,[1,2,3],5],[1,3,4,(1,3),4] ] ,1  ,3)           
print(ans_lst)

