
board_pos=[[],[],[],[],[]]
board_scores=[[],[],[],[],[]]

def dfs(depth,target_depth,board):
    if depth==target_depth:
        board_score=0
        for i in range(15):
            for j in range(15):
                if board.matrix[i][j]=='1':
                    board_score-=cal_score(i,j,'1',board,sum_dict_black)
                elif board.matrix[i][j]=='2':
                    board_score+=cal_score(i,j,'2',board,sum_dict_white)
                else:
                    continue
        # ax,by=board_pos[depth-1][-1]
        
        # board_score-=cal_score(ax,by,'1',board,sum_dict_black)
        board_scores[depth-1].append(board_score)
        return 
    if depth==1:
        for i in range(15):
            for j in range(15):
                if board.matrix[i][j]=='0' and has_neighbor(i,j,board):
                    board.matrix[i][j]='2'
                    board_pos[depth].append((i,j))
                    dfs(depth+1,target_depth,board)
                    
                    
                    for k in range(15):
                        print(board.matrix[k])
                    print()
                    
                    board.matrix[i][j]='0'
        indexx=board_scores[depth].index(max(board_scores[depth]))
        board_scores[depth-1].append(board_scores[depth][indexx])
        board_pos[depth-1].append(board_pos[depth][indexx])  
        board_pos[depth]=[]
        board_scores[depth]=[]
        return 
    if depth==3:#! 白色方出棋
        for i in range(15):
            for j in range(15):
                if board.matrix[i][j]=='0' and has_neighbor(i,j,board):
                    board.matrix[i][j]='2'
                    board_pos[depth].append((i,j))
                    dfs(depth+1,target_depth,board)
                    

                    
                    board.matrix[i][j]='0'
        indexx=board_scores[depth].index(max(board_scores[depth]))
        board_scores[depth-1].append(board_scores[depth][indexx])
        #board_pos[depth-1].append(board_pos[depth][indexx])  
        board_pos[depth]=[]
        board_scores[depth]=[]
    elif depth==2:
        for i in range(15):
            for j in range(15):
                if board.matrix[i][j]=='0' and has_neighbor(i,j,board):
                    board.matrix[i][j]=='1'
                    board_pos[depth].append((i,j))#! 位置与分数索引一致
                    dfs(depth+1,target_depth,board)
                    
                    
                    board.matrix[i][j]='0' #!区分循环内外!!!
                    
        indexx=board_scores[depth].index(min(board_scores[depth]))
        board_scores[depth-1].append(board_scores[depth][indexx])
        #board_pos[depth-1].append(board_pos[depth][indexx])  
        board_pos[depth]=[]
        board_scores[depth]=[]   
                



def cal_score(x,y,color,board,sum_dict):
    
    
    
    #todo四个方向棋形统计  掌握模型
    chess_look=[]
    
    temp1=[color]
    temp2=[]
    i=1
    while i<6 and x-i>=0:#*左边
        if board.matrix[x-i][y]==color or board.matrix[x-i][y]=='0' :
            temp1.append(board.matrix[x-i][y])
            i+=1
        else:
            break
    i=1
    while i<6 and x+i<15:#*右边
        if board.matrix[x+i][y]==color or board.matrix[x+i][y]=='0' :
            temp2.append(board.matrix[x+i][y])
            i+=1
        else:
            break
    temp=temp1[::-1].copy()+temp2.copy()
    chess_look.append(''.join(temp.copy()))
    
    
    #! 纵向
    temp1=[board.matrix[x][y]]
    temp2=[]
    j=1
    while j<6 and y-j>=0:#*上边
        if board.matrix[x][y-j]==color or board.matrix[x][y-j]=='0':
            temp1.append(board.matrix[x][y-j])
            j+=1
        else:
            break
    j=1
    while j<6 and y+j<15:#*下边
        if board.matrix[x][y+j]==color or board.matrix[x][y+j]=='0':
            temp2.append(board.matrix[x][y+j])
            j+=1
        else:
            break
    temp=temp1[::-1].copy()+temp2.copy()
    chess_look.append(''.join(temp.copy()))
    
    #! 主对角线
    temp1=[board.matrix[x][y]]
    temp2=[]
    z=1
    while z<6 and x-z>=0 and y-z>=0:#* 左上
        if board.matrix[x-z][y-z]==color or board.matrix[x-z][y-z]=='0':
            temp1.append(board.matrix[x-z][y-z])
            z+=1
        else:
            break
    z=1
    while z<6 and x+z<15 and y+z<15:#* 右下
        if board.matrix[x+z][y+z]==color or board.matrix[x+z][y+z]=='0':
            temp2.append(board.matrix[x+z][y+z])
            z+=1
        else:
            break
    temp=temp1[::-1].copy()+temp2.copy()
    chess_look.append(''.join(temp.copy())) #! 别忘了用.join() 将list变成字符串
    
    
    #! 副对角线
    temp1=[board.matrix[x][y]]
    temp2=[]
    k=1
    #todo 整理笔记 先操作还是先加 要特别注意!!! 以及先对脚标进行合法性判断
    while k<6 and x-k>=0 and y+k<15:#* 右上
        if board.matrix[x-k][y+k]==color or board.matrix[x-k][y+k]=='0':
            temp1.append(board.matrix[x-k][y+k])#! 必须之后 k+=1 ！！！！！！ 注意是先操作再更改 还是先更改再操作
            k+=1
#! index out of range?
#! list index out of range 使用list索引之前 必须要注意是否为空 索引的合理性!!!!!
#             错误原因有二：
# 1、超出了list范围：
# 例如 list=（0,1，2），却在编程中使用了list【5】

# 2、list为空，在这种情况下使用list【0】便会报错
        else:
            break
    k=1
    while k<6 and x+k<15 and y-k>=0:#* 左下
        if board.matrix[x+k][y-k]==color or board.matrix[x+k][y-k]=='0':
            temp2.append(board.matrix[x+k][y-k])
            k+=1
        else:
            break
    temp=temp1[::-1].copy()+temp2.copy()
    chess_look.append(''.join(temp.copy()))
    
    
    score=0
    cnt=0
    #*print(chess_look) #!测试用
    for mm in chess_look:
        for q in range(len(lst1)):
            if lst1[q] in mm or lst2[q] in mm:
                score+=sum_dict[lst1[q]]
        for p in range(len(special_lst)):
            if special_lst[p] in mm or para_special_lst[p] in mm:
                cnt+=1
                #! 会重复计算等级比较低的棋形 在设计评估函数的时候需要考虑到这一点
    
    #! 特殊棋型判断
    if cnt>1:
        if color=='1':
            score+=150000
        else:
            score+=150000
    return score
