#!/usr/bin/env python
#!/usr/bin/python
# -*- coding: UTF-8 -*-


"""
@File：letcode_13_罗马数字转整数.py
@Data：2019/7/16
@param：
@return：
"""

"""
总的来说，感觉罗马数字转整数难度更大一些
"""
# 替换两个数字的思路，后面再遍历
class Solution:
    def romanToInt(self, s: str) -> int:
        rows = {
            'M' : 1000, 'D': 500, 'C': 100, 'L': 50, 'X': 10, 'V': 5, 'I':1
        }
        num = 0
        if 'CM' in s:
            num = num + 900
            s = s.replace("CM", "")
        if 'CD' in s:
            num = num + 400
            s = s.replace("CD", "")
        if 'XC' in s:
            num = num + 90
            s = s.replace("XC", "")
        if 'XL' in s:
            num = num + 40
            s = s.replace("XL", "")
        if 'IX' in s:
            num = num + 9
            s = s.replace("IX", "")
        if "IV" in s:
            num = num + 4
            s = s.replace("IV", "")

        for value in s:
            num = num + rows[value]

        return num


# 遍历思路，通过判断大小看是否需要连接字符
class Solutions:
    def romanToInt(self, s: str) -> int:
        rows = {
            'M': 1000, 'D': 500, 'C': 100, 'L': 50, 'X': 10, 'V': 5, 'I': 1
        }
        print(list(enumerate(s)))
        num = 0
        """
        判断前一个元素的值与后一个的关系，如果比后一个小，证明是代表4，9的值。就减掉该值
        如果比后一个大，就加上该值，则表现了4，9数的特性，最后加上最后一个没有遍历的元素
        """
        for i in range(len(s) - 1):
            if rows[s[i]] >= rows[s[i + 1]]:
                num = num + rows[s[i]]
            else:
                num = num - rows[s[i]]
        return num + rows[s[len(s) - 1]]

