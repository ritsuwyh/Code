
from game import Board
class Human(object):
    """
    human player
    """

    def __init__(self):
        self.player = None

    def set_player_ind(self, p):
        self.player = p

    def get_action(self, board: Board):

        try:
            location = input("Your move: ")
            if isinstance(location, str):
                location = [int(n, 10) for n in location.split(",")]
            move = board.location_to_move(location)
        except Exception as e:
            move = -1

        if move == -1 or move not in board.availables:
            print("invalid move")
            #! 如果玩家输入位置不合法 那么就重新调用这个函数 直至输入位置合法
            move = self.get_action(board)

        return move

    def __str__(self):
        return "Human {}".format(self.player)
