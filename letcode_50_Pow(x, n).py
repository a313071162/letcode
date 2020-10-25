# -*- encoding: utf-8 -*-


"""
@File    : letcode_50_Pow(x, n).py
@Time    : 2020/10/25 上午9:46
@Author  : dididididi
@Email   : 
@Software: PyCharm
"""
class Solutions(object):
    def myPow(self, x, n):
        """
        :type x: float
        :type n: int
        :rtype: float
        """
        return pow(x, n)

class Solutionss(object):
    def myPow(self, x, n):
        """
        :type x: float
        :type n: int
        :rtype: float
        """
        if n == 0:
            return 1
        elif n < 0:
            x = 1 / x
            n = -n
        ans = 1.0
        while n > 0:
            if n & 1:
                ans *= x
            x *= x
            n >>= 1
        return ans

class Solution(object):
    def myPow(self, x, n):
        """
        :type x: float
        :type n: int
        :rtype: float
        """
        def quickMul(N):
            if N == 0:
                return 1
            y = quickMul(N // 2)
            return y * y if N % 2 == 0 else y * y * x
        return quickMul(n) if n >= 0 else 1.0 / quickMul(-n)


if __name__ == '__main__':
    sol = Solution()
    print(sol.myPow(2.00000, 10))