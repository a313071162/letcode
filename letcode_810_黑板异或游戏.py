# -*- encoding: utf-8 -*-


"""
@File    : letcode_810_黑板异或游戏.py
@Time    : 2020/9/25 上午10:45
@Author  : dididididi
@Email   : 
@Software: PyCharm
"""

import functools
import operator
class Solution(object):
    def xorGame(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        print(functools.reduce(operator.xor, nums))


if __name__ == '__main__':
    sol = Solution()
    print(sol.xorGame([1, 2, 4]))