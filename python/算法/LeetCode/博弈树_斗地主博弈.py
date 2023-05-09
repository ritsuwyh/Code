from collections import Counter


class Node():
    def __init__(self,boolx) -> None:
        self.boolx=boolx


class Poker:
    def __init__(self, cards: str):
        
        lst=cards.split()
        
        self.counter=Counter(lst)
        
        self.special=None   #!最长的顺子  
        
        self.sub_special=[]  #! 所有顺子
        
        self.all_ways=[]#! 存储当前他可以出的所有牌型
           
    
    def __check_straight(self) -> bool:
        """
        检查手牌中是否有顺子
        有，返回True；否则，返回False
        """
        #! 自定义按value值排序
        
        lstx=list(self.counter.keys())
        dicx={'3':1,'4':2,'5':3,'6':4,'7':5,'8':6,'9':7,'10':8,'J':9,'Q':10,'K':11,'A':12}
        lstx=sorted(lstx,key=lambda y : dicx[y])

        cnt=1
        for i in range(1,len(lstx)):
            if dicx[lstx[i]]-dicx[lstx[i-1]]==1:
                cnt+=1
            else:
                if cnt>=5:#! 必然是最长的
                    self.special=lstx[i-cnt:i]
                    self.__find_sub_special()
                    return True
                cnt=1
        if cnt>=5:
            self.special=lstx[i+1-cnt:i+1]#! 注意起始点
            self.__find_sub_special()
            return True
         
        return False
        

#! 背下来 找到长度合法的所有连续子列 不要以长度为讨论对象 要以谁为开头为讨论对象
    def __find_sub_special(self):

        for p1 in range(len(self.special)):
            for p2 in range(len(self.special)-1,-1,-1):
                if p2-p1+1>=5:
                    self.sub_special.append(self.special[p1:p2+1])
                else:
                   
                    break
    
    
    def find_all_ways(self) -> list:#! 找到当前他所有可以出的牌型
        
        self.all_ways=[]#! 别忘了初始化
        if self.__check_straight():
            self.all_ways+=self.sub_special
        
        for x,y in self.counter.items():
            if y==4:
                self.all_ways+=[[x],[x,x],[x,x,x],[x,x,x,x]]
            elif y==3:
                self.all_ways+=[[x],[x,x],[x,x,x]]
            elif y==2:
                self.all_ways+=[[x],[x,x]]
            else:
                self.all_ways+=[[x]]
                
    def out_cards(self,q:list):#! 出牌
        
        self.counter-=Counter(q)
        
    def in_cards(self,p:list):#! 收牌
        self.counter+=Counter(p)

        
        
def is_bigger(poker1: str, poker2: str) -> bool:#! 判断poker2 是否能大过poker1 这里规定poker1和2都是合法牌型     且已经顺子排好序(之前的函数里面已经实现)

    dicx={'3':1,'4':2,'5':3,'6':4,'7':5,'8':6,'9':7,'10':8,'J':9,'Q':10,'K':11,'A':12}
    lst1=poker1.split()
    lst2=poker2.split()
    
    if len(lst1)!=len(lst2):
        if len(lst2)==4:
            return True
        else:
            return False
    
    else:
        if dicx[lst1[0]]>=dicx[lst2[0]]:
            return False
        else:
            return True


#! 博弈树  从叶子节点往上赋值 分为不同的层 and和or层   
#todo 要掌握从叶子节点向上传递值的方法
def func(root:Node,p1: Poker,p2: Poker, last_cards:list , step:int ) -> bool:
    #! 用了特征值 step*-1 代表攻守交换  这种就适合博弈类  也可以（step+1）%2 来表示 如果是多人博弈 那就用 （step+1）%n
    '''
    
    step==1 代表A层  or层
    step==-1 代表B层  and层
    这里规定 p1就是攻击方 p2就是防守方 
    当step=1时 是玩家1进攻 
     step=-1时 是玩家2进攻
    
    '''
    
    p1.find_all_ways()
    p2.find_all_ways()
    
    flag=False#! 别忘了初始化
    if_cut=False
    
    #! 递归终点往往最后考虑 
    
    #! 叶子节点的bool值 玩家1获胜了叶子节点就是True 否则False 
    if len(p1.all_ways)==0  :#! 这种情况就是对方管不上 进攻方直接把牌全出了
        
        if step==1:
            root.boolx=  (True)
        else:
            root.boolx=  (False)
        
        return #! 别忘了写return
    
    #! p1 是进攻方 p2是防守方 那肯定就是原来的进攻方把牌走光了 但是防守方能管上 然后调换了攻守顺序 显然这时原来的进攻方已经获胜了 但是step已经乘-1了
    if len(p2.all_ways)==0:
        if step==1:#! 说明原来的进攻方是玩家2 玩家2赢了所以返回False
            root.boolx= False
        else:
            root.boolx= True
        return 
    
    
    
    #! 博弈过程
    for x in p1.all_ways:
        
        if last_cards==None:#! 上一次对手没出牌 两种可能 第一种是 本来就是先手 第二种是 我出了牌但是对面管不上
             
            p1.out_cards(x)
            
        else: #! 如果对手出牌了 那我出的时候就不能随便出了 要比他大
            if is_bigger(' '.join(last_cards),' '.join(x)):
                
                p1.out_cards(x)
                
            else:
                continue


        #! 判断对手能不能管上
        for y in p2.all_ways:
            if is_bigger(' '.join(x),' '.join(y)):
                flag=True
                break
            
        if flag:#! 如果能管上 那么就管 即交换攻守方 上一次出的牌就是x
            if step==1: #!or层
                temp=Node(True)#! 这个初始化有讲究 少画几层就理解了 看看他是怎么向上传递的 

                func(temp,p2,p1,x,step*(-1))
                
                root.boolx=root.boolx or temp.boolx
                
                if root.boolx==True:#!剪枝 这里不能直接return 因为要回溯之后再return
                    if_cut=True
                    
            else: #! and层
                temp=Node(False)

                func(temp,p2,p1,x,step*(-1))
                
                root.boolx=root.boolx and temp.boolx

                if root.boolx==False:#!剪枝
                    if_cut=True
            
            #! 回溯
            p1.in_cards(x)
            
            if if_cut:
                #! 注意如果不写return 那么就在这个函数的最后return 但是如果return 写在循环里面，那就会提前终止循环
                return 
            
            
        else:#! 如果对手没有牌能管上 那就继续出牌 攻守方不变 上一次出的牌为None
            func(root,p1,p2,None,step) 
            p1.in_cards(x)
            
         
          
def is_winner(p1:str,p2:str):
    p1=Poker(p1)
    p2=Poker(p2)
    node=Node(False)

    func(node,p1,p2,None,1)
    return node.boolx
    
    
print(is_winner('3 3 7 7','5 5 6 6'))


#list转字符串 '...'.join()

# print((x.counter))#! 如果len(counter)==0 那么说明他空了

# xx=Counter([1,2,3,4,4,5])
# for i,j in xx.items():
#     print(i,j)

# x=[[1,2,3],[1,2,4]]
# y=[[1,2,3],[7,8,9]]
# z=[1]
# print(x+y)
# print(z+y)

#print(type(' '.join(['1','2','3'])))

# for x in []:
#     print(1)#! 什么也不输出 根本不进行循环
    
#print(None or True) #输出True