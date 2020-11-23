# -*- encoding: utf-8 -*-


"""
@File    : 剑指Offer_67_把字符串转换成整数.py
@Time    : 2020/11/9 下午11:27
@Author  : dididididi
@Email   : 
@Software: PyCharm
"""

class Solution(object):
    def strToInt(self, str):
        """
        :type str: str
        :rtype: int
        """
        if str == "":
            return 0
        flag = True
        res = ""
        def judge(res):
            if res[0] == '+':
                if int(res[1:]) >= 2 ** 31 - 1:
                    return 2 ** 31 - 1
                else:
                    return int(res)
            elif res[0] == '-':
                if int(res[1:]) >= 2 ** 31:
                    return -2 ** 31
                else:
                    return -int(res[1:])
            else:
                if int(res) >= 2 ** 31 - 1:
                    return 2 ** 31 - 1
                else:
                    return int(res)
        for val in str:
            if flag:
                if val == ' ':
                    continue
                else:
                    if val == '+' or val == '-' or 48 <= ord(val) <= 57:
                        res += val
                        flag = False
                    else:
                        return 0
            else:
                if 48 <= ord(val) <= 57:
                    res += val
                else:
                    return judge(res)
        return judge(res)


if __name__ == '__main__':
    sol = Solution()
    print(sol.strToInt('42'))