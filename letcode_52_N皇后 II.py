# -*- encoding: utf-8 -*-


"""
@File    : letcode_52_N皇后 II.py
@Time    : 2020/10/17 下午2:39
@Author  : dididididi
@Email   : 
@Software: PyCharm
"""


class Solution(object):
    def totalNQueens(self, n):
        """
        :type n: int
        :rtype: int
        """
        if n == 1:
            return 1
        elif n < 4:
            return 0
        nums = 0
        s = "." * n

        def backtrack(i, tmp, col, z_diagonal, f_diagonal):
            nonlocal nums
            if i == n:
                nums += 1
                return ""
            for j in range(n):
                if j not in col and i + j not in z_diagonal and i - j not in f_diagonal:
                    print(col | {j}, z_diagonal | {i + j}, f_diagonal | {i - j})
                    backtrack(i + 1, tmp + [s[:j] + "Q" + s[j + 1:]], col | {j}, z_diagonal | {i + j},
                              f_diagonal | {i - j})

        backtrack(0, [], set(), set(), set())
        return nums


if __name__ == '__main__':
    sol = Solution()
    sol.totalNQueens(4)