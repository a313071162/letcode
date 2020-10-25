# -*- encoding: utf-8 -*-


"""
@File    : letcode_51_N皇后.py
@Time    : 2020/9/3 下午2:49
@Author  : dididididi
@Email   : 
@Software: PyCharm
"""


class Solution(object):
    def solveNQueens(self, n):
        """
        :type n: int
        :rtype: List[List[str]]
        """
        res = []
        s = "." * n
        if n == 1:
            return [["Q"]]
        elif n < 4:
            return []

        def backtrack(i, tmp, col, z_diagonal, f_diagonal):
            if i == n:
                res.append(tmp)
                return
            for j in range(n):
                if j not in col and i + j not in z_diagonal and i - j not in f_diagonal:
                    backtrack(i + 1, tmp + [s[:j] + "Q" + s[j + 1:]], col | {j}, z_diagonal | {i + j}, f_diagonal | {i - j})

        backtrack(0, [], set(), set(), set())
        return res


if __name__ == '__main__':
    sol = Solution()
    print(sol.solveNQueens(4))