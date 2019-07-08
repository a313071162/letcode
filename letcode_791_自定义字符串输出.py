#!/usr/bin/env python
#!/usr/bin/python
# -*- coding: UTF-8 -*-


"""
@File：letcode_791_自定义字符串输出.py
@Data：2019/7/8
@param：
@return：
"""


class Solution:
    # 自定义字符串输出
    def customSortString(self, S: str, T: str) -> str:
        fir_str = str()
        sec_str = str()
        for i in T:
            if i in S:
                fir_str = fir_str + i
            else:
                sec_str = sec_str + i
        sec_str = "".join(i for i in sorted(sec_str))
        res = str()
        for i in range(len(S)):
            res = res + S[i] * T.count(fir_str[i])


        return res + sec_str