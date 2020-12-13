# -*- encoding: utf-8 -*-


"""
@File    : letcode_217_存在重复元素.py
@Time    : 2020/12/13 上午9:13
@Author  : dididididi
@Email   : 
@Software: PyCharm
"""

class Solutions(object):
    """
    python 一行代码解决
    """
    def containsDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        return len(nums) != len(set(nums))


import collections

class Solution(object):
    def containsDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        dic = collections.defaultdict(int)
        for i in nums:
            if not dic[i]:
                dic[i] = 1
            else:
                return True
        return False

if __name__ == '__main__':
    sol = Solution()
    sol.containsDuplicate([1,2,3,1])