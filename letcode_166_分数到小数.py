# -*- encoding: utf-8 -*-


"""
@File    : letcode_166_分数到小数.py.py
@Time    : 2020/8/26 下午1:10
@Author  : dididididi
@Email   : 
@Software: PyCharm
"""


class Solution(object):
    def fractionToDecimal(self, numerator, denominator):
        """
        :type numerator: int
        :type denominator: int
        :rtype: str
        """
        res = ""
        if denominator == 0:
            return None
        if numerator % denominator == 0:
            res += (str(numerator // denominator))
        else:
            # 此处有一个位与的操作，之前不是很理解，其就是指同号为正，异号为负
            res += "-" if (numerator < 0) ^ (denominator < 0) else ""
            # 将所以符合都变为正
            numerator = abs(numerator)
            denominator = abs(denominator)
            # 判断整数部分
            res += str(numerator // denominator) + '.'
            numerator = numerator % denominator
            i = 0
            r = []
            r_used = []
            pos = -1
            # 此处一定要记住在进行除法时，如果该数再次出现，一定会进入循环
            while numerator != 0 and numerator not in r_used:
                r_used.append(numerator)
                numerator *= 10
                r.append(numerator // denominator)
                numerator = numerator % denominator
                i = i + 1

            r = ''.join([str(x) for x in r])
            if numerator in r_used:
                for i in range(len(r_used)):
                    if numerator == r_used[i]:
                        pos = i
                        break

            if pos == -1:
                res += r
            else:
                res = res + r[:pos] + '(' + r[pos:] + ')'

        return res


if __name__ == '__main__':
    sol = Solution()
    print(sol.fractionToDecimal(7, 12))
