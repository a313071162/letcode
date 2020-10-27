# -*- encoding: utf-8 -*-


"""
@File    : 剑指Offer_58-II_左旋转字符串.py
@Time    : 2020/10/27 下午10:13
@Author  : dididididi
@Email   : 
@Software: PyCharm
"""

class Solution(object):
    def reverseLeftWords(self, s, n):
        """
        :type s: str
        :type n: int
        :rtype: str
        """
        return s[n:] + s[:n]

if __name__ == '__main__':
    sol = Solution()
    print(    sol.reverseLeftWords('abcdefg', 2))