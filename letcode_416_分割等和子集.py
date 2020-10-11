# -*- encoding: utf-8 -*-


"""
@File    : letcode_416_分割等和子集.py
@Time    : 2020/10/11 上午9:29
@Author  : dididididi
@Email   : 
@Software: PyCharm
"""


class Solution(object):
    """
    碰到头疼的题啦，动态规划，硬伤
    但看了下题解是0-1背包问题，决定尝试一下
    """
    def canPartition(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        target = sum(nums)
        if target % 2 == 1:
            return False
        target = target // 2
        dp = [False] * (target + 1)
        dp[0] = True
        for n in nums:
            for i in range(len(dp) - 1, -1, -1):
                # i可以，那么i+n可以
                if dp[i] and i + n <= target:
                    dp[i + n] = True
        return dp[-1]



if __name__ == '__main__':
    sol = Solution()
    print(sol.canPartition([1, 7, 13, 5]))