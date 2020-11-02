# -*- encoding: utf-8 -*-


"""
@File    : 剑指Offer_53-I_在排序数组中查找数字 I.py
@Time    : 2020/10/27 下午10:15
@Author  : dididididi
@Email   : 
@Software: PyCharm
"""

import collections
class Solutions(object):
    """
    调库
    """
    def search(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        vals = collections.Counter(nums)
        return vals[target]

class Solutionss(object):
    """
    超时
    """
    def search(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        start, end = 0, len(nums) - 1
        res = 0
        while start < end:
            mid = (start + end) // 2
            if nums[mid] == target:
                res += 1
                left = mid - 1
                right = mid + 1
                while nums[left] == target:
                    res += 1
                    left -= 1
                while nums[right] == target:
                    res += 1
                    right += 1
                break
            elif nums[mid] < target:
                start = mid
            elif nums[mid] > target:
                end = mid
        return res


class Solution(object):
    def search(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        print(nums, target)

if __name__ == '__main__':
    sol = Solution()
    print(sol.search([5,7,7,8,8,10], 8))