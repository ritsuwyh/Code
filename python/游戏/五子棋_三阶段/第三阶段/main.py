
#import pickle
from game import Board, Game
from mcts_pure import MCTSPlayer as MCTS_Pure
from human import Human

def run():
    print('默认设置 8*8棋盘 5子相连为获胜')
    print('是否更改默认设置:(1 代表不更改 , 2代表更改):')
    temp=eval(input())
    if temp==2:
        print('请分别输入棋盘的行数,列数,几个棋子相连为获胜:')
        height,width,n_in_row=eval(input())

    elif temp==1:#! 默认设置
        n_in_row = 5
        width, height = 8, 8
    
    first=0
    print('请选择游戏模式:(1 代表 玩家 VS 玩家 , 2代表 玩家 VS AI , 3代表 AI VS AI)')
    game_Model=eval(input())
    if game_Model==1:
        player1 = Human()
        player2 = Human()
    elif game_Model==2:
        print('玩家先手输入1  AI先手输入2:')
        first=eval(input())
        print('设置难度:请输入AI的 n_playout(数值越大AI越强,默认初始值为2000)')
        set_n_playout=eval(input())
        player1 = Human()
        player2 = MCTS_Pure(c_puct=5, n_playout=set_n_playout)
    else:
        
        print('请分别输入第一个和第二个AI的 n_playout(数值越大AI越强,默认初始值为2000)')
        set1_n_playout,set2_n_playout=eval(input())
        print('第一个AI先手输入1  第二个AI先手输入2:')
        first=eval(input())
        player1= MCTS_Pure(c_puct=5, n_playout=set1_n_playout)
        player2= MCTS_Pure(c_puct=5, n_playout=set2_n_playout)

    
    try:
        print('human player please input your move in the format: 行数,列数')
        board = Board(width=width, height=height, n_in_row=n_in_row)
        game = Game(board)
        #! 注意这里传入对象的顺序代表了谁是玩家1 谁是玩家2 玩家1的棋子是'X' 玩家2的棋子是'O'
        game.start_play(player1, player2, start_player=first-1, is_shown=1)

    except KeyboardInterrupt:
        print('\n\rquit')


if __name__ == '__main__':
    run()
