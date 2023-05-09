

#! 用树模拟目录系统
class Node:
    '''dir:目录  file:文件'''
    def __init__(self,name,type='dir') -> None:
        self.name=name
        # self.type=type #* 'dir' or 'file'
        self.children=[]#! 因为可能有很多孩子
        self.parent=None#! 根据实际需求 来看写不写这个
    #! 与__str__方法有区别 这样print以node为元素的list时 会以[node.name...]的形式输出list
    
    def __repr__(self) -> str:
        return self.name
    
class FilesystemTree:
    def __init__(self) -> None:
        self.root=Node('/')
        self.now=self.root
        
    def mkdir(self,name:str):
        '''在当前目录下创建文件或 约定目录的name以'/'结尾 '''
        #! 为了防止意外
        if name[-1]!='/':
            name+='/'
        
        node=Node(name)
        self.now.children.append(node)
        node.parent=self.now
    
    def ls(self) -> list :
        '''展示当前目录下的所有目录'''
        return self.now.children
    
    def cd(self,name):
        '''切换目录 1.切换到当前目录下的另一个目录 2.返回上一级目录 约定name为'.../' '''
        if name=='.../':
            self.now=self.now.parent
            return
        for child in self.now.children:
            if child.name==name:
                self.now=child
                return
            
        raise ValueError('invalid dir')
    def mkfile(self):
        
        pass   
                
    
my_system=FilesystemTree()
my_system.mkdir('WU/')
my_system.mkdir('QQ/')
my_system.mkdir('Wechat/')

print(my_system.ls())
my_system.cd('QQ/')
my_system.mkdir('data/')
print(my_system.ls())
my_system.cd('.../')
print(my_system.ls())