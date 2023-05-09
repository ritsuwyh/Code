from card import Card
from random import shuffle

class Poke:
    def __init__(self):
        """
        构造方法
        在Poke类被实例化时就生成一副有序扑克牌
        """
        colors = ["♥", "♠", "♣", "♦"]
        values = [i for i in range(1, 14)]

        # 装牌列表
        self.poke = []

        # 生产牌
        for color in colors:
            for value in values:
                # 生产card
                c = Card()
                # 赋值花色
                c.color = color
                # 赋值点数
                c.value = value
                # 拼接
                self.poke.append(c)
    
    def __show(self):
        """显示所有的扑克牌"""
        index = 0
        for card in self.poke:
            if index % 13 == 0:
                print("")
            print(card, end='')
            index += 1

    def shuffle(self):
        """洗牌"""
        shuffle(self.poke)

    def deal_poke(self, playerNum):
        """发牌"""
        players = dict()
        for i in range(0, playerNum):
            cards = self.poke[i * 5:i * 5 + 5]
            players['player' + str(i + 1)] = cards
        return players

