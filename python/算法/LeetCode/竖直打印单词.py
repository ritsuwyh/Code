

#! 字符串函数的应用 以及转置
class Solution:
    def printVertically(self, s: str) -> list[str]:
        lst=s.split()
        max_len=0
        #* max_len=max([len(row) for row in lst])
        for i in lst:
            if len(i)>max_len:
                max_len=len(i)
                
        for i in range(len(lst)):
            lst[i]=lst[i].ljust(max_len)
        lst=list(zip(*lst))
        for i in range(len(lst)):
            lst[i]=''.join(list(lst[i]))#! 必须先将tuple转为list
            lst[i]=lst[i].rstrip()
        return lst
            
    
# txt = 'banana'
# x = txt.rjust(20, 'O') #! OOOOOOOOOOOOOObanana

# print(x)
# txt = '50'
# x = txt.zfill(10)#! 默认右对齐 0000000050
# print(x)

