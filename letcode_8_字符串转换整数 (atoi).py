#!/usr/bin/env python
#!/usr/bin/python
# -*- coding: UTF-8 -*-


"""
@File：letcode_8_字符串转换整数 (atoi).py
@Data：2019/7/12
@param：
@return：
"""


class Solution:
    """
    这道题做的我真的心累，明明很简单的一个东西，老是提交出错，犯一些小错误
    自己的思路还是不够完善，老是想不全面，下次一定要反复思考再提交
    其次自己的看题真的很有问题，希望多加改进
    """
    def myAtoi(self, str: str) -> int:
        nums = str.strip().split(' ')
        for value in nums:
            if value == '':
                continue
            if value[0] == "-":
                this_str = "-"
                value = value[1:]
            elif value[0] == "+":
                this_str = ""
                value = value[1:]
            else:
                this_str = ""
            for i in value:
                if i.isdigit():
                    this_str = this_str + i
                else:
                    break
            if this_str.replace('-', "").isdigit():
                if int(this_str) >= 2 ** 31:
                    return 2 ** 31 - 1
                elif int(this_str) < - 2 ** 31:
                    return - 2 ** 31
                else:
                    return int(this_str)
            else:
                return 0
        return 0
