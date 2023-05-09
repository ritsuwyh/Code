
class BiTreeNode:#!  二叉树节点
    def __init__(self,data) -> None:
        self.data=data
        self.lchild=None
        self.rchild=None

#! 前序遍历

def pre_order(root:BiTreeNode):#! 本质上是dfs
    
    if root:#* 其实就是如果root不为空
        
        print(root.data,end=' ')
        #! 属于人为规定顺序 先左后右
        pre_order(root.lchild)
        pre_order(root.rchild)
    
    
#! 中序遍历  

def in_order(root: BiTreeNode):
    '''先递归左子树 然后访问自己 然后递归右子树'''
    if root:
        in_order(root.lchild)
        print(root.data,end=' ')
        in_order(root.rchild)   


#! 后序遍历

   
def post_order(root: BiTreeNode):
    '''先递归左 然后递归右 最后打印自己'''
    if root:
        post_order(root.lchild)
        post_order(root.rchild)
        print(root.data,end=' ')

   
   
#! 前三种实际上是dfs     
#! 层次遍历 实际上是bfs 也可以用于多叉树的遍历
def level_order(root: BiTreeNode):
    lst=[]
    lst.append(root)
    head=0
    while head<len(lst):
        #! 如果有孩子 那么进队
        if lst[head].lchild!=None:
            lst.append(lst[head].lchild)
        if lst[head].rchild!=None:            
            lst.append(lst[head].rchild)
        head+=1 
    for node in lst:
        print(node.data,end=' ')   

   
#! 递归的思想
def func(pre_lst,in_lst):
    if pre_lst==[]:
        return []
    x=pre_lst.pop(0)
    
    in_lst1=in_lst[:in_lst.index(x)]
    in_lst2=in_lst[in_lst.index(x)+1:]
    pre_lst1=pre_lst[:len(in_lst1)]
    pre_lst2=pre_lst[-len(in_lst2):]
    #! 左子树 右子树 根节点
    return func(pre_lst1,in_lst1)+func(pre_lst2,in_lst2)+[x]



#! 手动输入一个树

a=BiTreeNode('A')
b=BiTreeNode('B')
c=BiTreeNode('C')
d=BiTreeNode('D')
e=BiTreeNode('E')
f=BiTreeNode('F')
g=BiTreeNode('G')

e.lchild=a
e.rchild=g
a.rchild=c
c.lchild=b
c.rchild=d
g.rchild=f



#! 看视频 了解怎么直接写出遍历结果 中序就垂直投影就好了
# 后序，从左往右，孩子节点都遍历完了才遍历父节点
pre_order(e)
print()
in_order(e)
print()
post_order(e)
print()
level_order(e)
print()

#!知道二叉树的前序和中序遍历 还原二叉树 并给出后序遍历
# 根据前序 E必然是根 然后看中序 E左面的一定是左子树 右边的是右子树 那么我们就知道左右两个字数的大小了
# 之后的确定方法是一样的 看前序A必然是左子树的根 再看中序

#!知道二叉树的后序和中序遍历 还原二叉树 并给出前序遍历
#同理
#! 我自己写了一个函数 求后序遍历
print(func(['E','A','C','B','D','G','F'],['A','B','C','D','E','G','F']))