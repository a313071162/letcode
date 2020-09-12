# -*- encoding: utf-8 -*-


"""
@File    : 剑指Offer_20_表示数值的字符串.py
@Time    : 2020/9/2 下午1:34
@Author  : dididididi
@Email   : 
@Software: PyCharm
"""

class Solution(object):
    def isNumber(self, s):
        """
        :type s: str
        :rtype: bool
        """
        # 说实话，不是很清楚此处的含义，但通过观看题解的时候发现他们说到了编译原理的问题
        # 后面可能会花一些时间来解决这个问题
        # 接下来，使用一个简单的方法来实现该问题
        # 其实这个方法真的是很好的，绕过了编译原理部分的冗杂内容
        try:
            float(s)
        except:
            return False
        return True

if __name__ == '__main__':
    sol = Solution()
    print(sol.isNumber("123"))