#!/usr/bin/env python
#!/usr/bin/python
# -*- coding: UTF-8 -*-


"""
@File：letcode_1016_子串能表示从1到N数字的二进制串.py
@Data：2019/7/8
@param：
@return：
"""

class Solution:
	#	子串能表示从 1 到 N 数字的二进制串
    def queryString(self, S: str, N: int) -> bool:
        for i in range(1, N + 1):
            s = ""
            while i > 0:
                j = str(i % 2)
                s = s + j
                i = int(i / 2)
            # 字符串反转
            s = list(s)
            s.reverse()
            s = "".join(s)
            if not S.__contains__(s):
                return False
        return True