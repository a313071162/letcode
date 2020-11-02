# -*- encoding: utf-8 -*-


"""
@File    : letcode_349_两个数组的交集.py
@Time    : 2020/11/2 上午8:42
@Author  : dididididi
@Email   : 
@Software: PyCharm
"""

class Solutions(object):
    def intersection(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: List[int]
        """
        return set(nums1) & set(nums2)

class Solution(object):
    def intersection(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: List[int]
        """
        nums1.sort()
        nums2.sort()
        len1, len2 = len(nums1), len(nums2)
        res = []
        i1 = i2 = 0
        while i1 < len1 and i2 < len2:
            n1 = nums1[i1]
            n2 = nums2[i2]
            if n1 == n2:
                if not res or n1 != res[-1]:
                    res.append(n1)
                i1 += 1
                i2 += 1
            elif n1 < n2:
                i1 += 1
            elif n1 > n2:
                i2 += 1
        return res


if __name__ == '__main__':
    sol = Solution()
    sol.intersection([4,9,5], [9,4,9,8,4])