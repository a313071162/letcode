#!/usr/bin/env python
#!/usr/bin/python
# -*- coding: UTF-8 -*-


"""
@File：letcode_22_括号生成.py
@Data：2019/7/23
@param：
@return：
"""

"""
这道题有些难度，感觉题意还是好理解，但是想不到怎么用代码实现。
看了原理是使用回溯法，但是也不知道怎么回溯，这可能是自己的一个弱点
对递归和动态规划算法上有很大问题
"""
# 回溯法，此方法不是自己写的，是学习别人的代码来写的
class Solution:
    """
    递归法是思路最简单的一种方法
    """
    def __init__(self):
        self.res = []
    def backtrack(self, s, n, left, right):
        if len(s) == 2 * n:
            self.res.append(s)
        if left < n:
            self.backtrack(s + '(', n, left + 1, right)
        if right < left:
            self.backtrack(s + ')', n, left, right + 1)
    def generateParenthesis(self, n: int) -> list:
        if n == 1:
            return ["()"]
        self.backtrack('', n, 0, 0)

        return self.res

