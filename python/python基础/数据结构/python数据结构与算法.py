class BinaryTree: 
    #! 由树的递归定义 每一个节点其实都是根节点 这个树的根节点就代表整个树
    def __init__(self, rootObj): 
        self.key = rootObj 
        self.leftChild = None 
        self.rightChild = None
    def insertLeft(self, newNode): 
        if self.leftChild == None: 
            self.leftChild = BinaryTree(newNode) 
        else: #! 类似链表插入
            t = BinaryTree(newNode) 
            t.left = self.leftChild 
            self.leftChild = t 
    def insertRight(self, newNode): 
        if self.rightChild == None: 
            self.rightChild = BinaryTree(newNode) 
        else: 
            t = BinaryTree(newNode) 
            t.right = self.rightChild 
            self.rightChild = t
    def getRightChild(self): 
        return self.rightChild 
    def getLeftChild(self): 
        return self.leftChild 
    def setRootVal(self, obj): 
        self.key = obj 

    def getRootVal(self): 
        return self.key
    
    #! 只能由下向上构建树
    
    #! 见解析树的创建
    
    
    
    
def preorder(tree:BinaryTree):
    if tree:
        print(tree.getRootVal())
        preorder(tree.getLeftChild)
        preorder(tree.getRightChild)
        
        
#! 数据结构 堆       
#!https://www.jianshu.com/p/6b526aa481b1
# 堆就是用数组实现的二叉树，所以它没有使用父指针或者子指针。堆根据“堆属性”来排序，“堆属性”决定了树中节点的位置。

# 堆的常用方法：

# 构建优先队列
# 支持堆排序
# 快速找出一个集合中的最小值（或者最大值）
# 在朋友面前装逼
# 堆属性
# 堆分为两种：最大堆和最小堆，两者的差别在于节点的排序方式。

# 在最大堆中，父节点的值比每一个子节点的值都要大。在最小堆中，父节点的值比每一个子节点的值都要小。这就是所谓的“堆属性”，并且这个属性对堆中的每一个节点都成立。

class Min_BinaryHeap():
    def __init__(self) -> None:
        self.heapList=[0]
        self.currentSize=0#! 记录堆里面有多少个节点
# heapList 中的元素 0 正好能发挥重要作用。我们使用整数除法计算任意节点的父节点。就当前
# 节点而言，父节点的下标就是当前节点的下标除以 2。

    #todo 为了实现插入操作 我们需要一个上移函数
    def __percUp(self, i): #! 向上移动函数 把 第 i个元素上移直到符合堆性质
        while i // 2 > 0: #! 这句话的意思是 如果有父节点
            #! i==0  堆为空 i==1 堆只有一个根节点 
            if self.heapList[i] < self.heapList[i // 2]: 
                tmp = self.heapList[i // 2] 
                self.heapList[i // 2] = self.heapList[i] 
                self.heapList[i] = tmp 
            i = i // 2
            
    def insert(self,k):

        self.heapList.append(k) 
        self.currentSize = self.currentSize + 1 
        self.__percUp(self.currentSize)
    
    #todo 为了实现从二叉堆里删除最小的元素 我们需要下移函数和 找最小孩子的函数


    def minChild(self, i): #! 找到最小孩子是第几个节点
        if i * 2 + 1 > self.currentSize: #! 右孩子超界 返回左孩子
            return i * 2 
        else: 
            if self.heapList[i*2] < self.heapList[i*2+1]: 
                return i * 2 
            else: 
                return i * 2 + 1        
    
    def __percDown(self, i): 
        while (i * 2) <= self.currentSize: #! 在范围内
            mc = self.minChild(i) 
            if self.heapList[i] > self.heapList[mc]: 
                tmp = self.heapList[i] 
                self.heapList[i] = self.heapList[mc] 
                self.heapList[mc] = tmp 
            i = mc 
 
    def delMin(self): #! 删除并返回最小元素
        retval = self.heapList[1] 
        self.heapList[1] = self.heapList[self.currentSize] 
        self.currentSize = self.currentSize - 1     
        self.heapList.pop() 
        self.__percDown(1) 
        return retval
    
    def buildHeap(self, alist): #! 二分
        i = len(alist) // 2
        self.currentSize = len(alist) 
        self.heapList = [0] + alist[:] 
        while (i > 0): 
            self.__percDown(i) 
            i = i - 1