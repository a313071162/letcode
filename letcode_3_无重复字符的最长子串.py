#!/usr/bin/env python
#!/usr/bin/python
# -*- coding: UTF-8 -*-


"""
@File：letcode_3_无重复字符的最长子串.py
@Data：2019/7/10
@param：
@return：
"""


class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        """
        无重复字符的最长子串
        :param s:
        :return:
        """
        maxs = 1
        s_len = len(s)
        if s_len <= 1:
            return s_len
        t = s[0]
        for i in range(1, s_len):
            if s[i] not in t:
                t = t + s[i]
                maxs = maxs if maxs > len(t) else len(t)
            else:
                t = t[t.index(s[i]) + 1:]
                t = t + s[i]
        return maxs

