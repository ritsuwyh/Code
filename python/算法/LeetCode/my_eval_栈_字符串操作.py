
#! 使用双栈解决表达式问题 栈 先入后出

# 从前往后做，对遍历到的字符做分情况讨论：

# 空格 : 跳过
# ( : 直接加入 ops 中，等待与之匹配的 )
# ) : 使用现有的 nums 和 ops 进行计算，直到遇到左边最近的一个左括号为止，计算结果放到 nums
# 数字 : 从当前位置开始继续往后取，将整一个连续数字整体取出，加入 nums
# + - * / ^ % : 需要将操作放入 ops 中。在放入之前先把栈内可以算的都算掉（只有「栈内运算符」比「当前运算符」优先级高/同等，才进行运算），使用现有的 nums 和 ops 进行计算，直到没有操作或者遇到左括号，计算结果放到 nums
#!只有「栈内运算符」比「当前运算符」优先级高/同等，才进行运算 是什么意思：

# 因为我们是从前往后做的，假设我们当前已经扫描到 2 + 1 了（此时栈内的操作为 + ）。

# 如果后面出现的 + 2 或者 - 1 的话，满足「栈内运算符」比「当前运算符」优先级高/同等，可以将 2 + 1 算掉，把结果放到 nums 中；
# 如果后面出现的是 * 2 或者 / 1 的话，不满足「栈内运算符」比「当前运算符」优先级高/同等，这时候不能计算 2 + 1。
# 一些细节：

# 由于第一个数可能是负数，为了减少边界判断。一个小技巧是先往 nums 添加一个 0
# 为防止 () 内出现的首个字符为运算符，将所有的空格去掉，并将 (- 替换为 (0-，(+ 替换为 (0+（当然也可以不进行这样的预处理，将这个处理逻辑放到循环里去做）
# 从理论上分析，nums 最好存放的是 long，而不是 int。因为可能存在 大数 + 大数 + 大数 + … - 大数 - 大数 的表达式导致中间结果溢出，最终答案不溢出的情况

#todo 关于字符串操作的一些模型
# #! 在某种特定元素之后插入特定元素
# s='012  351  34'
# lst=s.split('1')
# s='1x'.join(lst)
# print(s)

# #! 在特定的相邻元素对之间插入特定元素
# s='2122112112231'
# lst=list(s)
# for i in range(len(lst)):
#     if i+1<len(lst) and lst[i]=='1' and lst[i+1]=='2':#! 其实不用list 用str切片也可以 s[:i]+'x'+s[i:]
#         lst[i]+='x'
# s=''.join(lst)
# print(s)


# #! 删除字符串中的所有某一特定元素
# #!方法一:
# s='012  351  34'
# lst=s.split('1')
# s=''.join(lst)
# print(s)
# #!方法二:
# s='1234 123 04 '
# #lst=s.split()#! 默认以空格分隔 #! 如果想保留空格 那么只能用list函数
# lst=list(s)
# while lst.count('1')!=0:
#     lst.remove('1')#! remove 函数里面是元素
# s=''.join(lst)
# print(s)


#!!! 非常重要的知识点!!!!
#todo 关于for循环的一些易错点
    # s='12345'
    # for i in range(len(s)): 在循环中更改字符串长度 字符串确实会变 但是循环次数不会变
    #   s+='0'
    #   print(s)
    #   print(i)
    
# s='1234'
# for i in s:
#     s=s+'1'
#     print(s)
    
# print(s)

    
    # for i in range(0,2): i在每一次循环都会被初始化 第一次为0 第二次为1 更改i的值只对当次循环生效
    #   i=i+2
    #   print(i)
    
#todo 关于.split()的知识点
#! .split() 知识点 传入字符串 返回list 一定要输出结果试一试

# s='(-1+(-2)*3)*2'
# x=s.split('(')
# print(x)#['', '-1+', '-2)*3)*2']#! 前面有个''

# s='12345'
# x=s.split('(')
# print(x)


#! 不在循环中的replace
# txt = 'one one was a race horse, two two was one too.'
# x = txt.replace('one', 'three',2) #! 不指定2 默认全换
# print(x)
#! 在循环中的replace 特殊！！！
# s='abcadb'
# for i in s[:2]:
#     s=s.replace(i, '1')
#     print(s)
# print(s)

# txt = ',,,,,ssaaww.....abanana'
# x = txt.lstrip(',.asw')
# print(x)

#! .join 的用法特殊



#! 我们需要打一个dict 权值 记录算数符号的优先级顺序


num_lst=[]
ops_lst=[]

def cal():
    ops=ops_lst.pop()#! 利用pop返回被删除的元素的性质 
    x1=num_lst.pop()
    x2=num_lst.pop()
    if ops=='+':
        num_lst.append(x2+x1)
    elif ops=='-':
        num_lst.append(x2-x1)#! 注意顺序
    elif ops=='/':
        num_lst.append(x2/x1)
    elif ops=='*':
        num_lst.append(x2*x1)
    elif ops=='%':
        num_lst.append(x2%x1)
    else:
        num_lst.append(x2//x1)   
        
def my_eval(s):
    
    dic={'+':1,'-':1,'*':2,'/':2,'//':2,'%':2}

    #! 预处理 处理1 防止第一个数字是负数
    if s[0]=='-' or s[0]=='+':
        #!s=s+'0' 严重的错误
        s='0'+s#! 注意顺序!!!
        
    #todo 改  防止小括号后面是负数 如果小括号后面是负号 将该小括号后面都加上一个0 模型 在字符串某种特定元素之后加上一个符号
    lst=list(s)
    for i in range(len(lst)):
        if i+1<len(lst) and lst[i]=='(' and lst[i+1]=='-':
            lst[i]+='0'        
    s=''.join(lst)
    
    vis=[False for _ in range(len(s))]
    
    for i in range(len(s)):
        
        if vis[i]:#! 由于for i in range(len(s)) 内部修改i只能在本次循环中更改i的值(与c++不同!!!!) 
            continue

        if s[i]==' ':
            continue
        elif s[i]=='(':
            ops_lst.append('(')
        elif s[i]==')':
            memorize_index=-1
            #while s[memorize_index]!='(':#! 这里出了大问题
            while ops_lst[memorize_index]!='(':    
                cal()
                #memorize_index-=1#! 这里出了大问题 因为你已经把最后一个符号弹出了 所以只能一直判断最后一个符号！！！
            ops_lst.pop()#! 删除左面的小括号
                
            
        elif s[i].isdigit():
            temp_s=s[i]
            vis[i]=True
            digit_index=i
            #! 从字符串中取出数字 模板
            while  digit_index+1<len(s) and not vis[digit_index+1] and s[digit_index+1].isdigit():#! 必须先判判断是否越界 !!!!!!!!!!!!凡是遇到这种什么 lst[i+1] lst[i-1] 都要先判断脚标合法性
                temp_s+=s[digit_index+1]
                digit_index+=1
                
                vis[digit_index]=True
                
            num=int(temp_s)#! 这里也可以用*10+int(s[i+1])的方法(放到循环里)
            #*print(num) 测试用
            num_lst.append(num)
        else:#! 运算符讨论

            if s[i]=='/':
                if s[i+1]=='/':
                    #! 对于//
                    if len(ops_lst)==0 or ops_lst[-1]=='(':
                        ops_lst.append('//')
                    else:
                        if dic[ops_lst[-1]]>=dic['//']:
                            
                            cal()
                            
                            ops_lst.append('//')
                        else:
                            
                            ops_lst.append('//')
                    vis[i+1]=True

                else:
                    #! 对于/
                    if len(ops_lst)==0 or ops_lst[-1]=='(':
                        ops_lst.append('/')
                    else:
                        if dic[ops_lst[-1]]>=dic['/']:
                            
                            cal()
                            
                            ops_lst.append('/')
                        else:
                            
                            ops_lst.append('/')
                            
            else:
                if len(ops_lst)==0 or ops_lst[-1]=='(':
                    ops_lst.append(s[i])
                else:
                    if dic[ops_lst[-1]]>=dic[s[i]]:
                        
                        cal()
                        
                        ops_lst.append(s[i])
                        
                    else:
                        
                        ops_lst.append(s[i])
                        
    while len(ops_lst)!=0:
        cal() 
    return num_lst[-1]           
   
s=input("请输入一个数学计算式:") #! python的list其实就是一个stack
#!vis=[False for _ in range(len(s))] 这句话有问题 因为经过预处理之后 len(s)发生了变化 所以要在预处理之后再声明
print('my_eval',my_eval(s))
print()
print('eval',eval(s))




#! 有关栈的应用 火车站问题
# #include <iostream>
# #include <vector>
# #include <stack>
# using namespace std;
# int main() {
#     int n;
#     cin >> n;
#     vector<int> a(n);
#     //没必要用vector 用普通的数组即可; 
#     for (int i = 0; i < n; i++) {
#         cin >> a[i];//输入的顺序即出栈的顺序 规定输入的数是1到n 且不重复
#     }//入栈顺序为1-n; 程序的目的是判断出栈顺序能否符合输入顺序
#     stack<int> s;
#    // int cur=1;
#     bool f=1;//需要用一个bool类型的变量来存贮是否合法 //是还是不是这样的问题 用bool类型 
#     int index=0;
#        /* while(cur<=n){
#             if(s.empty()||s.top()!=a[index]){
#                 s.push(cur);
#                 cur++;
#             }*/
#             for(int i=1;i<=n;i++){
#             	s.push(i);
#        while(!s.empty()&&s.top()==a[index]){//要弹出就弹干净 所以里面用一个while套while 
#        	s.pop();//无论是pop() 还是在stack中访问top() 还是在queue中访问front() 都要判断是否为空  
#        	index++;
# 	   }
# }
#     //}
#         if(!s.empty()){
#             f=0;
#         }
#     if(f){
#         cout<<"legal"<<endl;
#     }else{
#         cout<<"illegal"<<endl;
#     }
#     return 0;
# }
