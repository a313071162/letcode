# -*- encoding: utf-8 -*-


"""
@File    : letcode_1002_查找常用字符.py
@Time    : 2020/10/14 上午8:55
@Author  : dididididi
@Email   : 
@Software: PyCharm
"""

import collections
from functools import reduce
class Solution(object):
    """
    看了下相关标签，hash表，昨天想买会员，太贵，10快还能承受
    题目的翻译真的很渣，说真心话很渣，完全曲解了题的意思
    """
    def commonChars(self, A):
        """
        :type A: List[str]
        :rtype: List[str]
        """
        res = []
        vals = {}
        i = 0
        for val in A:
            if i == 0:
                vals = collections.Counter(val)
                i += 1
            else:
                vals &= collections.Counter(val)
        for key in vals:
            for j in range(vals[key]):
                res.append(key)
        return res

        # return list(reduce(lambda x, y: x & y, map(collections.Counter, A)).elements())


if __name__ == '__main__':
    sol = Solution()
    print(sol.commonChars(["bella","label","roller"]))