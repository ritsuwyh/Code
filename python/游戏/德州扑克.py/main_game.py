from function2 import Play

if __name__ == '__main__':
    print('欢迎进入德州扑克游戏！')
    flag = True
    while flag:
        number = int(input('请输入玩家人数(2-9)：'))
        if number < 2 or number > 10:
            print('玩家人数有误，请重新输入：')
            continue
        play = Play(number)
        print('扑克牌已为您分发完成')
        while True:
            choice = int(input('''请输入您的选择：
1、查看所有玩家            2、查看指定玩家的手牌
3、查看所有玩家的手牌       4、查看指定玩家的手牌类型
5、查看所有玩家的手牌类型   6、重新开始游戏    7、退出游戏

'''))
            if choice == 1:
                play.showPlayers()
            elif choice == 2:
                player = input('请输入您要查看的玩家：')
                try:
                    play.showPlayerCard(player)
                except:
                    print('没有该玩家！')
            elif choice == 3:
                play.showAllPlayersCard()
            elif choice == 4:
                player = input('请输入您要查看的玩家：')
                try:
                    play.showPlayerCardsType(player)
                except:
                    print('没有该玩家！')
            elif choice == 5:
                play.showAllPlayersCardsType()
            elif choice == 6:
                break
            elif choice == 7:
                flag = False
                break
            else:
                print('您输入的数字有误！')
    print('欢迎您下次再来')

