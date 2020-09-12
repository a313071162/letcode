# -*- encoding: utf-8 -*-


"""
@File    : letcode_486_预测赢家.py
@Time    : 2020/9/1 上午9:45
@Author  : dididididi
@Email   : 
@Software: PyCharm
"""

import copy

class Solution(object):
    def PredictTheWinner(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        lens = len(nums)
        if lens == 1:
            return True
        dp = nums.copy()

        for i in range(lens - 2, -1, -1):
            for j in range(i + 1, lens):
                print(i, j, dp[j])
                dp[j] = max(nums[i] - dp[j], nums[j] - dp[j - 1])
        return dp[lens - 1] >= 0





if __name__ == '__main__':
    sol = Solution()
    print(sol.PredictTheWinner([1, 6, 5, 2]))