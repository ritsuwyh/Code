
#! 题干见"马的覆盖点" 求马 三步能到达的所有位置 不能回溯！！！！
#! 注意点 马的移动选项有8种
#!我们不能用之前的vis[x][y]表示这个点访问没访问过了，比如第一步不能走1,2 不代表第二步不能走1,2
#!但是我们可以加一维，变成vis[step][x][y]，记录我们是不是曾经在step步的时候到达了(x, y)这个点，
#!也就是(x, y, step)这个状态是不是被访问过了。
#! 如果有蹩马脚的棋子 要特判!!!!! 实际上马走一步分为两个步骤
#! 此题没有蹩马脚的棋子
#! 此题还可以扩展 问第N步能跳到的位置

move = [(2, 1), (2, -1), (1, 2), (1, -2), (-2, 1), (-2, -1), (-1, 2), (-1, -2)]


def dfs(x, y, n, m, step):
    if step == 4:
        return
    for k in move:
        temp_x = x+k[0]
        temp_y = y+k[1]
        if temp_x < 0 or temp_x > n-1 or temp_y < 0 or temp_y > m-1:
            continue
        if bool_lst[step-1][temp_x][temp_y]:  # ! 这里是step-1
            continue

        bool_lst[step-1][temp_x][temp_y] = True

        board[temp_x][temp_y] = '#'
        # todo 把上面这句话替换为下面这句话 就只会显示第三步会到达的点 而不会显示第一步第二步可能到达的点
        #!if step==3:
        #!   board[temp_x][temp_y]='#'
        dfs(temp_x, temp_y, n, m, step+1)
    return


def main():
    n, m = eval(input("请输入棋盘的行数和列数:"))
    x, y = eval(input("请输入马的索引坐标:"))
    global board
    board = [['.' for j in range(m)] for i in range(n)]
    global bool_lst  # ! 三维的
    bool_lst = [[[False for k in range(m)]for j in range(n)]for i in range(3)]

    dfs(x, y, n, m, 1)
    for i in range(n):
        for j in range(m):
            print(board[i][j], end="")
        print()


main()
# *测试样例
'''

.#....#S#
..#.#.#..
..##.#..#
......##.
...T.....
...#.#...
...#.....
...###...
.........
.##......

'''
