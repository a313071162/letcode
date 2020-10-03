# -*- encoding: utf-8 -*-


"""
@File    : letcode_868_二进制间距.py
@Time    : 2020/10/2 上午9:50
@Author  : dididididi
@Email   : 
@Software: PyCharm
"""


class Solution(object):
    """
    思路挺简单的，最开始以为有简便方法就一直没下手
    """
    def binaryGap(self, n):
        """
        :type n: int
        :rtype: int
        """
        A = [i for i in range(32) if (n >> i) & 1]
        print(A)

        maxs = 0
        count = 0
        flag = False
        # 二进制形式
        bins = bin(n)[2:]
        for i in bins:
            if i == '0' and flag:
                count = count + 1
            else:
                maxs = max(count, maxs)
                flag = True
                count = 1
        return maxs



if __name__ == '__main__':
    sol = Solution()
    print(sol.binaryGap(22))