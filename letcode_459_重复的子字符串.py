# -*- encoding: utf-8 -*-


"""
@File    : letcode_459_重复的子字符串.py
@Time    : 2020/8/24 上午11:01
@Author  : dididididi
@Email   : 
@Software: PyCharm
"""


class Solution(object):
    def repeatedSubstringPattern(self, s):
        """
        :type s: str
        :rtype: bool
        """
        # 自己没想到的方法，特别简单和实用，还是太菜了
        return (s + s)[1: len(s) * 2 - 1].find(s) != -1



if __name__ == '__main__':
    sol = Solution()
    print(sol.repeatedSubstringPattern("ababab"))