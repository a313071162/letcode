#!/usr/bin/env python
#!/usr/bin/python
# -*- coding: UTF-8 -*-


"""
@File：letcode_7_整数反转.py
@Data：2019/7/12
@param：
@return：
"""


# python 作弊写法
class Solution:
    def reverse(self, x: int) -> int:
        # 我是采用分片来进行反转的
        if x < 0:
            x = int("-" + str(x)[1:][::-1])
        else:
            x = int(str(x)[::-1])

        if x > 2 ** 31 or x < - 2 ** 31:
            return 0
        else:
            return x
