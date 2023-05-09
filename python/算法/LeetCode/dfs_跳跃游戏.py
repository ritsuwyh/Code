
#! 这道题不可能走回头路 所以不用回溯
def dfs(pos,step):
    if pos==len(nums)-1:
        global min_len
        if step<min_len:
            min_len=step
        return
    for i in range(1,nums[pos]+1):#!连动都不动必然不行 如果num[pos]==0 那么必然走不到终点
        if pos+i<=len(nums):
            
            dfs(pos+i,step+1)
        else:
            break
    return 


def main():
    global nums
    nums=list(map(int,input().split()))
    global min_len
    min_len=len(nums)
    #? nums=list(eval(input()))
    dfs(0,0)
    print(min_len)
main()