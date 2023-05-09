def shuixianhuashu(x,n):
    sum=0
    memorize_x=x #注意因为以后x的值发生了变化 所以要记录一下之前x的值
    while x>0:
        temp=x%10
        sum+=pow(temp,n)
        x=x//10
    if sum==memorize_x:
        return True
    else:
        return False
    #下面是错误示例
    '''def shuixianhuashu(x,n):
        sum=0
    while x>0:
        temp=x%10
        sum+=pow(temp,n)
        x=x//10
    if sum==x:
        return True
    else:
        return False'''
def main():
    n=eval(input())
    lst=[x for x in range(pow(10,n-1),pow(10,n)) if shuixianhuashu(x,n)]
    #print(lst)
    for i in lst:
        print(i)
main()