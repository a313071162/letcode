# -*- encoding: utf-8 -*-


"""
@File    : letcode_121_买卖股票的最佳时机.py
@Time    : 2020/10/19 下午3:19
@Author  : dididididi
@Email   : 
@Software: PyCharm
"""


class Solutions(object):
    """
    需要通过动态规划来解决
    """
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        # 设置一个备忘录
        lens = len(prices)
        if lens == 0:
            return 0
        # arr = [0] * lens
        maxs = 0
        # 本来以为是动态规划，结果超出时间我就知道是暴力了
        for i in range(lens - 1):
            for j in range(i + 1, lens):
                # if prices[i] < prices[j]:
                maxs = max(maxs, prices[j] - prices[i])
        return maxs


class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        if not prices:
            return 0
        maxs = 0
        mins = prices[0]
        for i in range(len(prices)):
            mins = min(prices[i], mins)
            maxs = max(prices[i] - mins, maxs)
        return maxs




if __name__ == '__main__':
    sol = Solution()
    print(sol.maxProfit([7,1,5,3,6,4]))