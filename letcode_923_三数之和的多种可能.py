#!/usr/bin/env python
#!/usr/bin/python
# -*- coding: UTF-8 -*-


"""
@File：letcode_923_三数之和的多种可能.py
@Data：2019/7/8
@param：
@return：
"""
import collections
class Solution:
    def threeSumMulti(self, A: list, target: int) -> int:
	#	三数之和的多种可能
        """
                :type A: List[int]
                :type target: int
                :rtype: int
                """
        c = collections.Counter(A)
        result = 0
        for i, x in c.items():
            for j, y in c.items():
                k = target - i - j
                print(i, x, j, y, k)
                if k not in c:
                    continue
                # 此处根据题得出i <= j <= k
                if i == j == k:
                    result += x * (x - 1) * (x - 2) // 6
                elif i == j != k:
                    result += x * (x - 1) // 2 * c[k]
                elif i < j and j < k:
                    result += x * y * c[k]

        return result % (10 ** 9 + 7)