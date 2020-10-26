# -*- encoding: utf-8 -*-


"""
@File    : letcode_1365_有多少小于当前数字的数字.py
@Time    : 2020/10/26 上午10:24
@Author  : dididididi
@Email   : 
@Software: PyCharm
"""

import collections
class Solutions(object):
    def smallerNumbersThanCurrent(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        vals = collections.Counter(nums)
        res = []
        for x in nums:
            cur = 0
            for key, val in vals.items():
                if x > key:
                    cur += val
            res.append(cur)
        return res

class Solution(object):
    """
    这个解题是真的牛逼，先排序，然后直接根据序号查找，完全避开了hash表
    """
    def smallerNumbersThanCurrent(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        new = sorted(nums)
        l = []
        for num in nums:
            l.append(new.index(num))
        return l




if __name__ == '__main__':
    sol = Solution()
    print(sol.smallerNumbersThanCurrent([8,1,2,2,3]))