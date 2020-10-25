# -*- encoding: utf-8 -*-


"""
@File    : letcode_53_最大子序和.py
@Time    : 2020/10/20 下午9:20
@Author  : dididididi
@Email   : 
@Software: PyCharm
"""

class Solutions(object):
    """
        这道题是一道非常经典的动态规划题
        sum[i] = max(sum[i - 1] + a[i], a[i])
    """
    def maxSubArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        maxs = cur = nums[0]
        for x in nums[1:]:
            cur = max(x, cur + x)
            maxs = max(cur, maxs)
        return maxs

class Solution(object):
    def maxSubArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        for i in range(1, len(nums)):
            nums[i] = nums[i] + max(nums[i - 1], 0)
        return max(nums)




if __name__ == '__main__':
    sol = Solution()
    print(sol.maxSubArray([-2,1,-3,4,-1,2,1,-5,4]))