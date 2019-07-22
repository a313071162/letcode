#!/usr/bin/env python
#!/usr/bin/python
# -*- coding: UTF-8 -*-


"""
@File：letcode_17_电话号码的字母组合.py
@Data：2019/7/22
@param：
@return：
"""

# 递归调用
class Solution:
    def __init__(self):
        self.res = []
        self.number = {
            '2': 'abc',
            '3': 'def',
            '4': 'ghi',
            '5': 'jkl',
            '6': 'mno',
            '7': 'pqrs',
            '8': 'tuv',
            '9': 'wxyz'
        }
    def dataCombinations(self, digits, st, i):
        if i == len(digits):
            self.res.append(st)
            return
        for j in self.number[digits[i]]:
            # 此处不能让st加了j后再传值，这会影响到最初到st值
            self.dataCombinations(digits, st + j, i + 1)
    def letterCombinations(self, digits: str) -> list:
        d_len = len(digits)
        if d_len == 0:
            return self.res
        self.dataCombinations(digits, "", 0)
        return self.res


class Solutions:
    def __init__(self):
        self.res = []
        self.number = {
            '2': 'abc',
            '3': 'def',
            '4': 'ghi',
            '5': 'jkl',
            '6': 'mno',
            '7': 'pqrs',
            '8': 'tuv',
            '9': 'wxyz'
        }
    def backtrack(self, digits, st):
        if len(digits) == 0:
            self.res.append(st)
            return
        for value in self.number[digits[0]]:
            # 此处有个递归切片的小知识
            self.backtrack(digits[1:], st + value)
    def letterCombinations(self, digits: str) -> list:
        if digits:
            self.backtrack(digits, "")
            return self.res
        else:
            return self.res

