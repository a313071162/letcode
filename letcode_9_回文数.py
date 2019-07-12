#!/usr/bin/env python
#!/usr/bin/python
# -*- coding: UTF-8 -*-


"""
@File：letcode_9_回文数.py
@Data：2019/7/12
@param：
@return：
"""


class Solution:
    """
    这道题比较简单，看看即可
    """
    def isPalindrome(self, x: int) -> bool:
        if str(x) == str(x)[::-1]:
            return True
        else:
            return False

