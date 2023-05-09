
#3<4<5<6<7<8<9<10<J<Q<K<A 这12种牌码，每种牌码的牌最多4张，手牌数量区间为[1,8]。

from collections import Counter
#!Counter用法!
#!https://wjrsbu.smartapps.cn/zhihu/article?id=355601478&isShared=1&_swebfr=1&_swebFromHost=baiduboxapp
#我们都知道在字典中查找不存在的键，程序会抛出 KyeError的异常，但是由于 Counter 用于统计计数，因此 Counter 不同于字典，**如果在 Counter 中查找一个不存在的元素，不会产生异常，而是会返回 0，这其实很好理解，Counter 计数将不存在元素的 count 值设置为 0 
# x=Counter('11122225')
# y=Counter('140')
#print(x+y)#!其实和下面的意思一样 但是+返回了一个新的counter 与dict中的update方法区分

# x.update(y)#!  return None 直接修改x
#print(x)

#print(x-y)#! 与下面有不同 -:keeping only positive counts
# x.subtract(y) #! return None 直接修改x 这个允许values是负数
# print(x)


class Poker:
    def __init__(self, cards: str):
        
        self.lst=cards.split()
        self.counter=Counter(self.lst)
        self.special=None   #!最长的顺子  
        self.sub_special=[]  #! 所有子顺子
        pass

    def check_count(self, count: int) -> bool:
        """
        检查手牌中是否有单张、对子、三连、炸弹
        count 为 1 时，检查单张
        count 为 2 时，检查对子
        count 为 3 时，检查三连
        count 为 4 时，检查炸弹
        有，返回True；否则，返回False
        """
        if count==1:
            if self.lst:
                return True
        elif count==2:
            for i in self.counter.values():
                if i>=2:
                    return True
            
        elif count==3:
            for i in self.counter.values():
                if i>=3:
                    return True
        elif count==4:
            for i in self.counter.values():
                if i==4:
                    return True
        
        
        return False
        
    
    def check_straight(self) -> bool:
        """
        检查手牌中是否有顺子
        有，返回True；否则，返回False
        """
        #! 自定义按value值排序
        lstx=list(set(self.lst))
        dicx={'3':1,'4':2,'5':3,'6':4,'7':5,'8':6,'9':7,'10':8,'J':9,'Q':10,'K':11,'A':12}
        lstx=sorted(lstx,key=lambda y : dicx[y])

        cnt=1
        for i in range(1,len(lstx)):
            if dicx[lstx[i]]-dicx[lstx[i-1]]==1:
                cnt+=1
            else:
                if cnt>=5:#! 必然是最长的
                    self.special=lstx[i-cnt:i]
                    self.find_sub_special()
                    return True
                cnt=1
        if cnt>=5:
            self.special=lstx[i+1-cnt:i+1]#! 注意起始点
            self.find_sub_special()
            return True
         
        return False
        

#! 背下来 找到长度合法的所有连续子列 不要以长度为讨论对象 要以谁为开头为讨论对象
    def find_sub_special(self):

        for p1 in range(len(self.special)):
            for p2 in range(len(self.special)-1,-1,-1):
                if p2-p1+1>=5:
                    self.sub_special.append(self.special[p1:p2+1])
                else:
                   
                    break
    
    
    def cal_all_ways(self) -> int:

        # dicx={}
        # for x in self.lst:
        #     dicx[x]=dicx.get(x,0)+1
        
        ans_dic={0:1,1:1,2:2,3:3,4:5}
        
        def func_prod(co):
            sumx=1
            for i in co.values():
                sumx*=ans_dic[i]
            return sumx
        
        if self.check_straight():
            ans=0
            ans+=func_prod(self.counter)
            
            for xx in self.sub_special:
                temp_count=Counter(xx)
                ans+=func_prod((self.counter-temp_count))
                
            return ans
        else:
            return func_prod(self.counter)
# poker=Poker('3 4 5 6 7')
# print(poker.check_straight())
# print(poker.cal_all_ways())
# print(poker.special)
while True:
    exec(input())
    
    
    
    
