import random
 
class game2048(object):
  def __init__(self):
    self.score=0
    self.number=[[0,0,0,0],[0,0,0,0],[0,0,0,0],[0,0,0,0]]
    self.move=0
    seed=random.randint(0,15)
    line=int(seed/4)
    row=seed%4
    self.number[line][row]=2   
   
  def is_gameover(self):
    numbersum=0
    for i in range(4):
      for j in range(4):
        if (self.number[i][j]!=0):
          numbersum+=1
    if(numbersum!=16): return False
    for i in range(4):
      for j in range(3):
        if(self.number[i][j+1]==self.number[i][j]): return False
    for i in range(3):
      for j in range(4):
        if(self.number[i+1][j]==self.number[i][j]): return False
    print("游戏结束")
    print("您的得分为："+str(self.score))
    self.__init__()
    return True
   
  def rannumber(self):
    rannumber=random.randint(1,10)   
    if(rannumber<=8): rannumber=2
    else: rannumber=4
    done=0
    count=0
    for i in range(4):
      for j in range(4):
        if(self.number[i][j]==0):#! 统计有没有0
          count+=1
    while(done==0 and count!=0):#! 如果有0 
      ranplace=random.randint(0,15)
      line=int(ranplace/4)
      row=ranplace%4
      if(self.number[line][row]==0):
        done=1
        self.number[line][row]=rannumber      
     
  def show(self):
    print(self.number[0])
    print(self.number[1])
    print(self.number[2])
    print(self.number[3])
     
  def print_score(self):
    print("得分："+str(self.score))
     
  def upmove(self):
    for i in range(1,4):
      for j in range(4):
        temp=i
        while(temp>=1 and self.number[temp-1][j]==0):
          box=self.number[temp-1][j]
          self.number[temp-1][j]=self.number[temp][j]
          self.number[temp][j]=box
          if(self.number[temp][j]!=0):self.move=1
          temp-=1
   
  def up(self):
    self.upmove()
    for i in range(1,4):
      for j in range(4):
        if(self.number[i-1][j]==self.number[i][j]):
          if(self.number[i-1][j]!=2048):
            self.score+=self.number[i][j]
            self.number[i][j]=0
            self.number[i-1][j]=2*self.number[i-1][j]         
    self.upmove()      
    if(self.move!=0):self.rannumber()
    self.move=0
    self.show()
    self.is_gameover()
    self.print_score()
   
  def downmove(self):
     for i in range(2,-1,-1):
       for j in range(4):
        temp=i
        while(temp<=2 and self.number[temp+1][j]==0 ):
          box=self.number[temp+1][j]
          self.number[temp+1][j]=self.number[temp][j]
          self.number[temp][j]=box
          if(self.number[temp+1][j]!=0):self.move=1
          temp+=1
       
  def down(self):
    self.downmove()
    for i in range(2,-1,-1):
      for j in range(4):
        if(self.number[i+1][j]==self.number[i][j]):
          if(self.number[i+1][j]!=2048):
            self.score+=self.number[i][j]
            self.number[i][j]=0
            self.number[i+1][j]=2*self.number[i+1][j] 
    self.downmove()
    if(self.move!=0):self.rannumber()
    self.move=0
    self.show()
    self.is_gameover()
    self.print_score()
   
  def leftmove(self):
    for i in range(4):
      for j in range(1,4):    
        temp=j
        while(temp>=1 and self.number[i][temp-1]==0 ):
          box=self.number[i][temp-1]
          self.number[i][temp-1]=self.number[i][temp]
          self.number[i][temp]=box
          if(self.number[i][temp-1]!=0):self.move=1
          temp-=1
   
  def left(self):
    self.leftmove()
    for i in range(4):
      for j in range(0,3):
        if(self.number[i][j+1]==self.number[i][j]):
          if(self.number[i][j+1]!=2048):
            self.score+=self.number[i][j]
            self.number[i][j+1]=0
            self.number[i][j]=2*self.number[i][j] 
    self.leftmove()
    if(self.move!=0):self.rannumber()
    self.move=0
    self.show()
    self.is_gameover()
    self.print_score()
   
  def rightmove(self):
    for i in range(4):
      for j in range(2,-1,-1):    
        temp=j
        while(temp<=2 and self.number[i][temp+1]==0 ):
          box=self.number[i][temp+1]
          self.number[i][temp+1]=self.number[i][temp]
          self.number[i][temp]=box
          self.move=1
          temp+=1
   
  def right(self):
    self.rightmove()
    for i in range(4):
      for j in range(2,-1,-1):
        if(self.number[i][j+1]==self.number[i][j]):
          if(self.number[i][j+1]!=2048):
            self.score+=self.number[i][j]
            self.number[i][j]=0
            self.number[i][j+1]=2*self.number[i][j+1] 
    self.rightmove()
    if(self.move!=0):self.rannumber()
    self.move=0
    self.show()
    self.is_gameover()
    self.print_score()
   
  def nextstep(self,step):
    if(step=='w'): self.up()
    elif(step=='s'): self.down()
    elif(step=='a'): self.left()  
    elif(step=='d'): self.right()
    else: pass
        
if __name__ == '__main__':
  game=game2048()
  game.show()
  while(True):
    step=input()
    if(step=='b'):break
    game.nextstep(step)