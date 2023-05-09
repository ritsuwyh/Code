
#! 用lst初始化链表
# class Node:
#     def __init__(self,item) -> None:
#         self.item=item
#         self.next=None
#         #! 可以添加一些自定义的属性
# def head_creat_linklist(lst): #! 使用一个list来初始化链表
#     #! 头插法链表存储顺序是lst的倒序
#     head=Node(lst[0])
#     for element in lst[1:]:
#         node=Node(element)
#         node.next=head
#         head=node
#     return head

# def tail_create_linklist(lst):
#     head=tail=Node(lst[0])
#     for element in lst[1:]:
#         node=Node(element)
#         tail.next=node
#         tail=node
#     return head

# def print_linklist(lk:Node):
#     while lk:
#         print(lk.item,end=' ')
#         lk=lk.next
#     print()#!纯纯是为了换行

# #todo 按元素值 按下标 
# def insert_linklist()
    
# lk1=head_creat_linklist([1,2,2,3,4,4])
# print_linklist(lk1)

# lk2=tail_create_linklist([1,2,2,3,4,4])
# print_linklist(lk2)



# 按元素值查找:
#      按顺序查找，复杂度是一样的。
#      按二分查找，链表没法查找.
# 按下标查找:
#      列表是O( 1 )
#      链表是O(n)
# 在某元素后插入:
#      列表是O(n)
#      链表是O( 1 )
# 删除某元素:
#      列表是O(n)
#      链表是O( 1 )


''' 为文档字符串 用作提示作用'''
class Node(object):
    """节点"""
    def __init__(self, elem):
        self.elem = elem
        self.next = None


class SingleLinkList(object):
    """单链表"""
    def __init__(self, content=None):
        def tail_create_linklist(lst):
            if lst==None or lst==[]:
                return None
            head=tail=Node(lst[0])
            for element in lst[1:]:
                node=Node(element)
                tail.next=node
                tail=node
            return head
        self.__head=tail_create_linklist(content)


    def is_empty(self):#! 只需要判断头结点是否为空即可
        """链表是否为空"""
        return self.__head == None

    def length(self):
        """链表长度"""
        # cur游标，用来移动遍历节点
        cur = self.__head#! 替罪羊cur
        # count记录数量
        count = 0
        while cur != None:
            count += 1
            cur = cur.next
        return count

    def travel(self):
        """遍历整个链表"""
        cur = self.__head
        while cur != None:
            print(cur.elem, end=" ")
            cur = cur.next
        print("")

    def add(self, item):
        """链表头部添加元素，头插法"""
        node = Node(item)
        node.next = self.__head
        self.__head = node

    def append(self, item):
        """链表尾部添加元素, 尾插法"""
        node = Node(item)
        if self.is_empty():
            self.__head = node
        else:
            cur = self.__head
            while cur.next != None:
                cur = cur.next
            cur.next = node

    def insert(self, pos, item):
        """指定位置添加元素
        :param  pos 从0开始
        """
        if pos <= 0:
            self.add(item)
        elif pos > (self.length()-1):
            self.append(item)
        else:
            pre = self.__head
            count = 0
            while count < (pos-1):
                count += 1
                pre = pre.next
                #! while a<x: 退出循环的时候a的大小就是x
            # 当循环退出后，pre指向pos-1位置
            node = Node(item)
            node.next = pre.next
            pre.next = node

    def remove(self, item):
        """删除节点"""
        cur = self.__head
        pre = None
        #! 用pre来记录上一个节点
        while cur != None:
            if cur.elem == item:
                # 先判断此结点是否是头节点
                # 头节点
                if cur == self.__head:
                    self.__head = cur.next
                else:
                    pre.next = cur.next
                break
            else:
                pre = cur
                cur = cur.next

    def search(self, item):
        """查找节点是否存在"""
        cur = self.__head
        while cur != None:
            if cur.elem == item:
                return True
            else:
                cur = cur.next
        return False
    
lk1=SingleLinkList()
print(lk1.length())

#todo 双链表

class Node:
    def __init__(self,item) -> None:
        self.item=item
        self.next=None
        self.prior=None
class Doublelinklist:
    
    pass
