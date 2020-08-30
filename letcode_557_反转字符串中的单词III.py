# -*- encoding: utf-8 -*-


"""
@File    : letcode_557_反转字符串中的单词III.py
@Time    : 2020/8/30 下午3:22
@Author  : dididididi
@Email   : 
@Software: PyCharm
"""


class Solution(object):
    def reverseWords(self, s):
        """
        :type s: str
        :rtype: str
        """
        # 第一次感觉自己写的很棒，虽然题很简单，一行实现
        return " ".join(val[::-1] for val in s.split(' '))


class Solutions(object):
    def reverseWords(self, s):
        """
        :type s: str
        :rtype: str
        """
        s = s[::-1].split(' ')
        s.reverse()
        return " ".join(s)


if __name__ == '__main__':
    sol = Solutions()
    print(sol.reverseWords("Let's take LeetCode contest"))