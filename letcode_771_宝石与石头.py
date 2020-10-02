# -*- encoding: utf-8 -*-


"""
@File    : letcode_771_宝石与石头.py
@Time    : 2020/10/2 上午9:42
@Author  : dididididi
@Email   : 
@Software: PyCharm
"""
import collections
class Solution(object):
    """
    这道题非常简单，当之无愧的简单题
    """
    def numJewelsInStones(self, J, S):
        """
        :type J: str
        :type S: str
        :rtype: int
        """
        vals = collections.Counter(S)
        sums = 0
        for index in J:
            sums = sums + vals[index]
        return sums

if __name__ == '__main__':
    sol = Solution()
    print(sol.numJewelsInStones('aA', 'aAAbbbb'))