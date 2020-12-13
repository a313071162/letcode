# -*- encoding: utf-8 -*-


"""
@File    : letcode_204_计数质数.py
@Time    : 2020/12/3 下午8:09
@Author  : dididididi
@Email   : 
@Software: PyCharm
"""

import math
class Solutions(object):
    """
    超时
    """
    def countPrimes(self, n):
        """
        :type n: int
        :rtype: int
        """
        if n <= 1:
            return 0
        res = 0

        def isZhi(x):
            for i in range(2, int(math.sqrt(x)) + 1):
                if x % i == 0:
                    return False
            return True

        for i in range(2, n):
            if i == 2 or i == 3:
                res += 1
            else:
                if isZhi(i):
                    res += 1
        return res

class Solutionss(object):
    """
    超时
    """
    def countPrimes(self, n):
        """
        :type n: int
        :rtype: int
        """
        if n == 0 or n == 1:
            return 0
        res = 0
        dic = []

        def isZhi(i):
            for j in dic:
                if i % j == 0:
                    return False
            return True

        for i in range(2, n):
            if not dic:
                res += 1
                dic.append(i)
            else:
                if isZhi(i):
                    res += 1
                    dic.append(i)
        return res


class Solution(object):
    """
    这个方法异常的牛逼
    """
    def countPrimes(self, n):
        """
        :type n: int
        :rtype: int
        """
        if n < 3:
            return 0
        prime = [1] * n
        prime[0] = prime[1] = 0
        for i in range(2, int(n ** 0.5) + 1):
            if prime[i] == 1:
                prime[i * i:n:i] = [0] * len(prime[i * i:n:i])
        return sum(prime)


if __name__ == '__main__':
    sol = Solution()
    print(sol.countPrimes(20))