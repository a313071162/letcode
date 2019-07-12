#!/usr/bin/env python
#!/usr/bin/python
# -*- coding: UTF-8 -*-


"""
@File：letcode_6_Z字形变换.py
@Data：2019/7/11
@param：
@return：
"""

# 按行访问
class Solution:
    """
    按行访问，原理很简单，需要一行一行的判断且未超范围
    """
    def convert(self, s: str, numRows: int) -> str:
        s_len = len(s)
        # 判断小于长度则可直接返回
        if s_len <= numRows or numRows <= 1:
            return s

        distance = numRows * 2 - 2
        nums = ""
        for i in range(numRows):
            j = 0
            while i + j < s_len:
                nums = nums + s[i + j]
                if i != 0 and i != numRows - 1 and j + distance - i < s_len:
                    nums = nums + s[j + distance - i]
                j = j + distance
        return nums



