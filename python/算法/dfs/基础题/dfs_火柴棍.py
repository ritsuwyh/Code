lst=[]
def sumx(a,b,c):
    return a*100+b*10+c
def dfs(step=0):
    if step==9:
        x1=sumx(lst[0],lst[1],lst[2])
        x2=sumx(lst[3],lst[4],lst[5])
        x3=sumx(lst[6],lst[7],lst[8])
        if x1+x2==x3:
            print("{}+{}={}".format(x1,x2,x3))
            return
        
    for i in range(1,10):
        if chosen[i]:
            continue
        chosen[i]=True
        lst.append(i)
        dfs(step+1)
        chosen[i]=False
        lst.pop()
        
def main():
    global chosen
    chosen=dict.fromkeys(range(10),False)
    dfs()
main()