

#!block[i // 3][j // 3][digit] = True 前两个维度确定是哪个3*3矩阵  line[i][digit]  row[i][digit] 也是同理 第几行/列 哪个数 是否用过
#! 这样就不用再写check函数了 还用到了矩阵降维升维操作 见笔记

class Solution:
    def solveSudoku(self, board: list[list[str]]) -> None:#! 审题 注意元素类型
        
        def dfs(pos: int):
            nonlocal valid
            if pos == len(spaces):
                valid = True
                return
            
            i, j = spaces[pos]
            for digit in range(9):
                if line[i][digit] == column[j][digit] == block[i // 3][j // 3][digit] == False:
                    
                    line[i][digit] = column[j][digit] = block[i // 3][j // 3][digit] = True
                    board[i][j] = str(digit + 1)
                    dfs(pos + 1)
                    line[i][digit] = column[j][digit] = block[i // 3][j // 3][digit] = False
                    
                if valid:
                    return
            
        line = [[False] * 9 for _ in range(9)]
        column = [[False] * 9 for _ in range(9)]
        block = [[[False] * 9 for _a in range(3)] for _b in range(3)]
        valid = False
        spaces = list()

        for i in range(9):
            for j in range(9):
                if board[i][j] == ".":#! . 代表空地 这一步是记录我们能走哪个位置 这样也方便我们在dfs中遍历 只需要遍历一个方向就可以了
                    spaces.append((i, j))
                else:
                    digit = int(board[i][j]) - 1
                    line[i][digit] = column[j][digit] = block[i // 3][j // 3][digit] = True

        dfs(0)

        