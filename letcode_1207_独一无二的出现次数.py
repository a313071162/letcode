# -*- encoding: utf-8 -*-


"""
@File    : letcode_1207_独一无二的出现次数.py
@Time    : 2020/10/28 上午8:42
@Author  : dididididi
@Email   : 
@Software: PyCharm
"""

import collections
class Solutions(object):
    def uniqueOccurrences(self, arr):
        """
        :type arr: List[int]
        :rtype: bool
        """
        vals = collections.Counter(arr)
        res = []
        for key in vals:
            if vals[key] not in res:
                res.append(vals[key])
            else:
                return False
        return True

class Solution(object):
    """
    大佬解题
    """
    def uniqueOccurrences(self, arr):
        """
        :type arr: List[int]
        :rtype: bool
        """
        vals = collections.Counter(arr)
        return len(vals) == len(set(vals.values()))


if __name__ == '__main__':
    sol = Solution()
    print(sol.uniqueOccurrences([1,2,2,1,1,3,4]))