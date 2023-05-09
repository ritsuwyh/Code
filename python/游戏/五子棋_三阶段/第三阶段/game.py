# -*- coding: utf-8 -*-

#! 加入了异常处理机制
#! 可以自定义棋盘大小 自定义n子棋

import numpy as np


class Board(object):
    """游 戏 板"""

    def __init__(self, **kwargs):
        #!关键字参数的使用方式
        #!arg可变参数允许你传入0个或任意个参数，这些可变参数在函数调用时自动组装为一个tuple
        #!而关键字参数允许你传入0个或任意个含参数名的参数，这些关键字参数在函数内部自动组装为一个dict。
        #.get是字典专用方法 dic.get(key,default)
        self.width = int(kwargs.get('width', 8))
        self.height = int(kwargs.get('height', 8))
        
        #! 与前两个阶段不同 棋盘的存储方式改变为字典 board states stored as a dict,
        # key: move as location on the board,
        # value: player as pieces type
        #! self.states 用来存储已经下过的点
        self.states = {}
        # need how many pieces in a row to win
        self.n_in_row = int(kwargs.get('n_in_row', 5))
        self.players = [1, 2]  # player1 and player2 
        

    def init_board(self, start_player=0):#默认player1先下
        
        # 如果棋盘大小不合法
        if self.width < self.n_in_row or self.height < self.n_in_row:
            raise Exception('board width and height can not be '
                            'less than {}'.format(self.n_in_row))
            
        self.current_player = self.players[start_player]  # start player
        # keep available moves in a list
        self.availables = list(range(self.width * self.height))
        self.states = {}
        self.last_move = -1
        
        
        
    # def move_to_location(self, move):
        
    #     """
    #     3*3 board's moves like:
    #     6 7 8
    #     3 4 5
    #     0 1 2
    #     and move 5's location is (1,2)
    #     """
    #     #行数 列数
    #     h = move // self.width
    #     w = move % self.width
    #     return [h, w]

    def location_to_move(self, location):
        #! 将我们输入的坐标 转为字典所对应的key值
        if len(location) != 2:
            return -1
        h = location[0]
        w = location[1]
        move = h * self.width + w
        if move not in range(self.width * self.height):
            return -1
        return move

    def current_state(self):
        """从当前玩家的角度返回棋盘状态.
        state shape: 4*width*height
        """

        square_state = np.zeros((4, self.width, self.height))#! 三维矩阵
        if self.states:#如果已经有落子了
# dic={'a':1,'b':2}
# print(np.array(list(dic.items())))
# # [['a' '1']]
# #  [['b' '2']]
# print(np.array(list(zip(*dic.items()))))
# # [['a' 'b']
# #  ['1' '2']]
            moves, players = np.array(list(zip(*self.states.items())))
            #! 上述式子等号右侧是一个只有两行的二维矩阵 第一行存的是走在哪里 第二行存的是谁走的
            #! moves就是二维矩阵的第一行 players就是二维矩阵的第二行 (moves players 都是向量)
            move_curr = moves[players == self.current_player]#! 当前选手已经走的步
            move_oppo = moves[players != self.current_player]#! 对方选手已经走的步
            
            #? squre_state的目的？？
            square_state[0][move_curr // self.width,
                            move_curr % self.height] = 1.0
            square_state[1][move_oppo // self.width,
                            move_oppo % self.height] = 1.0
            # 说明上次移动的位置
            square_state[2][self.last_move // self.width,
                            self.last_move % self.height] = 1.0
        if len(self.states) % 2 == 0:
            square_state[3][:, :] = 1.0  # 说明下一个要下的颜色
            
        return square_state[:, ::-1, :]

    def do_move(self, move):
        #!模拟棋盘落子
        self.states[move] = self.current_player
        self.availables.remove(move)
        
        #! 更改出棋方
        self.current_player = (
            self.players[0] if self.current_player == self.players[1]
            else self.players[1]
        )
        #!更新last_move值
        self.last_move = move


    def __has_a_winner(self):
        #! 判断输赢
        width = self.width
        height = self.height
        states = self.states
        n = self.n_in_row
        #! 找到已经落过子的点
        moved = list(set(range(width * height)) - set(self.availables))
        
        if len(moved) < self.n_in_row *2-1:
            return False, -1

        for m in moved:
            h = m // width
            w = m % width
            player = states[m]

            if (w in range(width - n + 1) and
                    len(set(states.get(i, -1) for i in range(m, m + n))) == 1):
                return True, player

            if (h in range(height - n + 1) and
                    len(set(states.get(i, -1) for i in range(m, m + n * width, width))) == 1):
                return True, player

            if (w in range(width - n + 1) and h in range(height - n + 1) and
                    len(set(states.get(i, -1) for i in range(m, m + n * (width + 1), width + 1))) == 1):
                return True, player

            if (w in range(n - 1, width) and h in range(height - n + 1) and
                    len(set(states.get(i, -1) for i in range(m, m + n * (width - 1), width - 1))) == 1):
                return True, player

        return False, -1


    #! 因为游戏结束的方式不只一种 可能存在棋盘下满的情况 其实如果不考虑这个特殊情况 game_end函数就是has_a_winner函数
    def game_end(self):
        """检查游戏是否结束"""
        win, winner = self.__has_a_winner()
        if win:
            #! 如果有胜者 游戏结束 返回获胜者
            return True, winner
        
        elif not len(self.availables):
            #! 如果棋盘满了 游戏结束 没有获胜者
            return True, -1
        
        #! 没有胜者 游戏继续
        return False, -1



    def get_current_player(self):
        return self.current_player




class Game(object):
    """游戏 server"""

    def __init__(self, board, **kwargs):
        self.board = board

    def graphic(self, board, player1, player2):
        """绘制棋盘并显示游戏信息"""
        width = board.width
        height = board.height

        print("Player", player1, "with X".rjust(3))
        print("Player", player2, "with O".rjust(3))
        print()
        for x in range(width):
            print("{0:8}".format(x), end='')
        print('\r\n')
        for i in range(height - 1, -1, -1):
            print("{0:4d}".format(i), end='')
            for j in range(width):
                loc = i * width + j
                p = board.states.get(loc, -1)
                if p == player1:
                    print('X'.center(8), end='')
                elif p == player2:
                    print('O'.center(8), end='')
                else:
                    print('_'.center(8), end='')
            print('\r\n\r\n')
            
            
            
            
    def start_play(self, player1, player2, start_player=0, is_shown=1):
        
        """在两个玩家之间开始游戏"""
        #! start_player=0 代表前者先手 =1代表后者先手
        if start_player not in (0, 1):
            raise Exception('start_player should be either 0 (player1 first) '
                            'or 1 (player2 first)')
        
        self.board.init_board(start_player)
        #! 下面四行建立了双射 p1等价于player1 p2等价于player2
        p1, p2 = self.board.players
        player1.set_player_ind(p1)
        player2.set_player_ind(p2)
        players = {p1: player1, p2: player2}
        
        if is_shown:
            self.graphic(self.board, player1.player, player2.player)
        while True:
            current_player = self.board.get_current_player()
            player_in_turn = players[current_player]
            move = player_in_turn.get_action(self.board)
            self.board.do_move(move)
            if is_shown:
                self.graphic(self.board, player1.player, player2.player)
            end, winner = self.board.game_end()
            if end:
                if is_shown:
                    if winner != -1:
                        print("Game end. Winner is", players[winner])
                    else:
                        print("Game end. Tie")
                return winner


#! 尚未使用

    def start_self_play(self, player, is_shown=0, temp=1e-3):
        self.board.init_board()
        p1, p2 = self.board.players
        states, mcts_probs, current_players = [], [], []
        while True:
            move, move_probs = player.get_action(self.board,
                                                 temp=temp,
                                                 return_prob=1)
            # 存储数据
            states.append(self.board.current_state())
            mcts_probs.append(move_probs)
            current_players.append(self.board.current_player)
            # 执行移动
            self.board.do_move(move)
            if is_shown:
                self.graphic(self.board, p1, p2)
            end, winner = self.board.game_end()
            if end:
                # 从每个状态的当前玩家的角度来看赢家
                winners_z = np.zeros(len(current_players))
                if winner != -1:
                    winners_z[np.array(current_players) == winner] = 1.0
                    winners_z[np.array(current_players) != winner] = -1.0
                # 重置MCTS根节点
                player.reset_player()
                if is_shown:
                    if winner != -1:
                        print("Game end. Winner is player:", winner)
                    else:
                        print("Game end. Tie")
                return winner, zip(states, mcts_probs, winners_z)
