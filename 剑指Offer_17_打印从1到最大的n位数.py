# -*- encoding: utf-8 -*-


"""
@File    : 剑指Offer_17_打印从1到最大的n位数.py
@Time    : 2020/10/27 下午7:52
@Author  : dididididi
@Email   : 
@Software: PyCharm
"""

class Solutions(object):
    def printNumbers(self, n):
        """
        :type n: int
        :rtype: List[int]
        """
        res = []
        for i in range(1, pow(10, n)):
            res.append(i)
        return res

class Solution(object):
    def printNumbers(self, n):
        """
        :type n: int
        :rtype: List[int]
        """
        return list(range(1, 10**n))


if __name__ == '__main__':
    sol = Solution()
    print(sol.printNumbers(1))