# -*- encoding: utf-8 -*-


"""
@File    : letcode_463_岛屿的周长.py
@Time    : 2020/10/30 上午8:43
@Author  : dididididi
@Email   : 
@Software: PyCharm
"""


class Solution(object):
    def islandPerimeter(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        w = len(grid)
        h = len(grid[0])
        # cor = [(0, 0), (0, h - 1), (w - 1, 0), (w - 1, h - 1)]
        res = 0
        if not w or not h:
            return 0

        def check(i, j):
            temp = 0
            if i == 0 or grid[i - 1][j] == 0:
                temp += 1
            if j == w - 1 or grid[i][j + 1] == 0:
                temp += 1
            if i == h - 1 or grid[i + 1][j] == 0:
                temp += 1
            if j == 0 or grid[i][j - 1] == 0:
                temp += 1
            return temp

        for i in range(w):
            for j in range(h):
                if grid[i][j] == 1:
                    res += check(i, j)

        return res


if __name__ == '__main__':
    sol = Solution()
    sol.islandPerimeter([[0,1,0,0],[1,1,1,0],[0,1,0,0],[1,1,0,0]])