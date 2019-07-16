#!/usr/bin/env python
#!/usr/bin/python
# -*- coding: UTF-8 -*-


"""
@File：letcode_12_整数转罗马数字.py
@Data：2019/7/15
@param：
@return：
"""

# 低位计算，运行效率较高，但内存消耗过大
class Solution:
    """
    罗马数字包含以下七种字符： I， V， X， L，C，D 和 M。
        字符          数值
        I             1
        V             5
        X             10
        L             50
        C             100
        D             500
        M             1000
    """
    def intToRoman(self, num: int) -> str:
        rows = ['I', 'V', 'X', 'L', 'C', 'D', 'M']
        res = ""
        if num < 0:
            return res
        if num > 3999:
            return "M*"
        j = 0
        while num > 0:
            div = num % 10
            num = num // 10
            if div > 0 and div < 4:
                res = rows[j] * div + res
            elif div == 4:
                res = rows[j] + rows[j + 1] + res
            elif div > 4 and div < 9:
                res = rows[j + 1] + rows[j] * (div % 5) + res
            elif div == 9:
                res = rows[j] + rows[j + 2] + res
            j = j + 2
        return res

# hash解决
class Solutions:
    def intToRoman(self, num: int) -> str:
        res = ""
        if num < 0:
            return res
        elif num > 3999:
            return "M*"
        row = {
            1000: 'M', 900: 'CM', 500: 'D', 400: 'CD', 100: 'C',
            90: 'XC', 50: 'L', 40: 'XL', 10: 'X', 9: 'IX', 5: 'V',
            4: 'IV', 1: 'I'
        }
        j = 0

        for key in row:
            div = num // key
            if div == 0:
                continue
            res = res + row[key] * div
            num = num - key * div
            if num == 0:
                break
        return res

