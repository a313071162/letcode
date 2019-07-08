#!/usr/bin/env python
#!/usr/bin/python
# -*- coding: UTF-8 -*-


"""
@File：letcode_744_寻找比目标字母大的最小字母.py
@Data：2019/7/8
@param：
@return：
"""

class Solution:
	#	寻找比目标字母大的最小字母
    def nextGreatestLetter(self, letters: list, target: str) -> str:
        for item in letters:
            if item > target:
                return item
        return letters[0]