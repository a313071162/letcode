#!/usr/bin/env python
#!/usr/bin/python
# -*- coding: UTF-8 -*-


"""
@File：letcode_28_实现strStr().py
@Data：2019/7/31
@param：
@return：
"""


class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        if not needle:
            return 0
        h_len = len(haystack)
        n_len = len(needle)
        if h_len < n_len or needle not in haystack:
            return -1
        # find则可直接找出子串所在的第一个元素所在的index
        # 可直接使用find即可得到值
        return haystack.find(needle)

