#'+'.join(lst) 这个lst里的元素必须是str类型
def my_division(x):#返回一个序列 
    l=[]
    for i in range(1,x):
        if x%i==0:
            l.append(i)
    return l

def my_num(x):
    division_lst=my_division(x)
    if sum(division_lst)==x:
        return True
    else:
        return False

def main():
    m,n=list(map(int,input().split()))
    lst=[i for i in range(m,n+1) if my_num(i)]
    if len(lst)==0:
        print("None")
    else:
        for x in lst:
            new_list=list(map(str,my_division(x)))
            s='+'.join(new_list)
            print(str(x)+"="+s)
main()