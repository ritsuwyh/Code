from function1 import Poke

class Play:
    def __init__(self, number=5):
        """
        初始化扑克堆并进行发牌
        :param number: 参与人数
        """
        self.poke = Poke()
        self.poke.shuffle()
        if number < 2 or number > 10:
            print('玩家数错误，无法开始游戏')
        self.players = self.poke.deal_poke(number)

    def showPlayers(self):
        """展示所有玩家"""
        print(self.players.keys())

    def showPlayerCard(self, player):
        """展示指定玩家的牌"""
        cards = self.players[player]
        print(player + '\'s cards: ', end='')
        for card in cards:
            print(card, end='')
        print()

    def showAllPlayersCard(self):
        """展示所有玩家的牌"""
        for player in self.players.keys():
            self.showPlayerCard(player)

    def showPlayerCardsType(self, player):
        """
        展示指定玩家的牌型
        :param player:
        :return:
        """
        # 获取该玩家的手牌
        cards = self.players[player]
        # 将该玩家的手牌的花色和数值分开
        colors = []
        values = []
        for card in cards:
            colors.append(card.color)
            values.append(card.value)
        # 获取该玩家手牌的花色和数值的种类数
        # set()集合不允许重复，通过set()强制转型并取其长度，即可获得种类数
        colorsLen = len(set(colors))
        valuesLen = len(set(values))

        # 获取该玩家手牌中 数值数量最多的牌的数量 与 数值数量最少的牌的数量 之差，最终结果为sameCardNum
        # result，统计每种数值类型的个数的字典
        # 例对于 3, 4, 4, 5, 5 数值数量分别为3：一个，4：两个，5：两个，所以...之差为2-1 = 1，result={3: 1, 4: 2, 5: 2}
        # 例对于 4, 4, 4, 4, 5 数值数量分别4：四个，5：一个，所以...之差为4-1 = 3，result={4: 4, 5: 1}
        result = dict()
        for i in values:
            if i not in result.keys():
                result[i] = 1
            else:
                result[i] += 1
        sameCardNum = max(result.values()) - min(result.values())

        print('玩家' + player + '的牌型是')
        if colorsLen == 1 and [1, 10, 11, 12, 13] == sorted(values):
            print('大同花顺')
        elif colorsLen == 1 and valuesLen == 5 and max(values) - min(values) == 4:
            print('同花顺')
        elif valuesLen == 2 and result[min(result.keys())] - result[max(result.keys())] == 3:
            print('四条')
        elif valuesLen == 2 and sameCardNum == 1:
            print('满堂红')
        elif colorsLen == 1:
            print('同花')
        elif valuesLen == 5 and max(values) - min(values) == 4:
            print('顺子')
        elif valuesLen == 3 and sameCardNum == 2:
            print('三条')
        elif valuesLen == 3 and sameCardNum == 1:
            print('两队')
        elif valuesLen == 4 and sameCardNum == 1:
            print('一对')
        else:
            print('散牌')

    def showAllPlayersCardsType(self):
        """
        展示所有玩家的牌型
        :return:
        """
        for i in self.players.keys():
            self.showPlayerCardsType(i)

