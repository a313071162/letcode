# -*- encoding: utf-8 -*-


"""
@File    : letcode_37_解数独.py
@Time    : 2020/9/15 下午2:43
@Author  : dididididi
@Email   : 
@Software: PyCharm
"""


class Solution(object):
    """
    看到这道数独题，心里已经觉得其是使用回溯法来实现
    看到难度，害怕呀
    首先我们要了解数独游戏是横竖不能出现相同元素，且相同方格也不能有相同元素
    但是还是不知道从何处下手，这题直接去看解题思路去了，因为不想花太多时间
    设计的很巧妙，自己完全不会，但读懂了其思路
    """
    def solveSudoku(self, board):
        """
        :type board: List[List[str]]
        :rtype: None Do not return anything, modify board in-place instead.
        """
        # 行列是否完全为True
        row = [[False] * 9 for _ in range(9)]
        col = [[False] * 9 for _ in range(9)]
        # 模拟第几个块
        block = [[[False] * 9 for _ in range(3)] for _ in range(3)]
        valid = False

        space = []
        for i in range(9):
            for j in range(9):
                if board[i][j] == '.':
                    space.append((i, j))
                else:
                    digit = int(board[i][j]) - 1
                    row[i][digit] = col[j][digit] = block[i // 3][j // 3][digit] = True
        def dfs(pos):
            nonlocal valid
            if pos == len(space):
                valid = True
                return

            i, j = space[pos]
            for digit in range(9):
                if row[i][digit] == col[j][digit] == block[i // 3][j // 3][digit] == False:
                    row[i][digit] = col[j][digit] = block[i // 3][j // 3][digit] = True
                    board[i][j] = str(digit + 1)
                    dfs(pos + 1)
                    row[i][digit] = col[j][digit] = block[i // 3][j // 3][digit] = False

                if valid:
                    return
        dfs(0)

        for i in board:
            print(i)



if __name__ == '__main__':
    sol = Solution()
    # print(sol.solveSudoku([["5","3",".",".","7",".",".",".","."],["6",".",".","1","9","5",".",".","."],[".","9","8",".",".",".",".","6","."],["8",".",".",".","6",".",".",".","3"],["4",".",".","8",".","3",".",".","1"],["7",".",".",".","2",".",".",".","6"],[".","6",".",".",".",".","2","8","."],[".",".",".","4","1","9",".",".","5"],[".",".",".",".","8",".",".","7","9"]]))
    sol.solveSudoku([[".","4","6","9",".","3",".",".","."],
                     [".",".","3",".","5",".",".","6","."],
                     ["9",".",".",".",".","2",".",".","3"],
                     [".",".","5",".",".","6",".",".","."],
                     ["8",".",".",".",".",".",".","1","."],
                     [".","1",".","7","8",".","2",".","."],
                     [".",".",".",".",".",".",".","5","."],
                     [".","8","1","3",".",".",".",".","7"],
                     [".",".",".","8",".",".","1",".","4"]])