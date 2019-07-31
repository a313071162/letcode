#!/usr/bin/env python
#!/usr/bin/python
# -*- coding: UTF-8 -*-


"""
@File：letcode_29_两数相除.py
@Data：2019/7/31
@param：
@return：
"""


import math
# 偷懒方法
class Solution:
    """
    给定两个整数，被除数 dividend 和除数 divisor。将两数相除，要求不使用乘法、除法和 mod 运算符。
    返回被除数 dividend 除以除数 divisor 得到的商。

    此处说明为不能使用乘除和mod
    """
    def divide(self, dividend: int, divisor: int) -> int:
        if dividend // divisor < 0:
            value = math.ceil(dividend / divisor)
            if value < - 2 ** 31:
                return - 2 ** 31
            else:
                return value
        else:
            value = dividend // divisor
            if value > 2 ** 31 - 1:
                return 2 ** 31 - 1
            else:
                return value

# 按照题意的方法，移位运算
class Solutions:
    def divide(self, dividend: int, divisor: int) -> int:
        symbol = True if (dividend < 0 and divisor > 0) or (dividend > 0 and divisor < 0) else False
        dividend = abs(dividend)
        divisor = abs(divisor)
        res = 0
        if divisor == 1:
            res = dividend
        else:
            while dividend >= divisor:
                cur = 1
                this_val = divisor
                while dividend >= (this_val << 1):
                    this_val = this_val << 1
                    cur = cur << 1
                dividend = dividend - this_val
                res = res + cur
        if res > 2 ** 31 - 1:
            return - 2 ** 31 if symbol else 2 ** 31 - 1
        return -res if symbol else res

