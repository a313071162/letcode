# -*- encoding: utf-8 -*-


"""
@File    : letcode_344_ 反转字符串.py
@Time    : 2020/10/8 上午9:39
@Author  : dididididi
@Email   : 
@Software: PyCharm
"""


class Solution(object):
    """
    本来想偷懒，看来不成啦
    简单的使用了一下双指针，过了
    """
    def reverseString(self, s):
        """
        :type s: List[str]
        :rtype: None Do not return anything, modify s in-place instead.
        """
        p1, p2 = 0, len(s) - 1
        while p1 <= p2:
            s[p1], s[p2] = s[p2], s[p1]
            p1 += 1
            p2 -= 1

if __name__ == '__main__':
    sol = Solution()
    sol.reverseString(["h","e","l","l","o"])