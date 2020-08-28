# -*- encoding: utf-8 -*-


"""
@File    : letcode_657_机器人能否返回原点.py
@Time    : 2020/8/28 下午1:29
@Author  : dididididi
@Email   : 
@Software: PyCharm
"""
import collections

class Solution(object):
    def judgeCircle(self, moves):
        """
        :type moves: str
        :rtype: bool
        """
        x = y = 0
        for move in moves:
            if move == 'U':
                y -= 1
            elif move == 'D':
                y += 1
            elif move == 'L':
                x -= 1
            elif move == 'R':
                x += 1
        # python的优先级有些怪，是先x 与 y 进行比较，再 y 与 0 进行比较
        return x == y == 0

class Solutions(object):
    def judgeCircle(self, moves):
        """
        :type moves: str
        :rtype: bool
        """
        c = collections.Counter(moves)
        return c["U"] == c["D"] and c["L"] == c["R"]


if __name__ == '__main__':
    sol = Solutions()
    print(sol.judgeCircle("UDLRRRLL"))